#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler, HTTPError
import mako.lookup
import mako.template
from mako import exceptions
from os.path import join


TEMPLATE_PATH = [join('./', 'templates')]

MAKO_LOOK_UP = mako.lookup.TemplateLookup(
    directories=TEMPLATE_PATH,
    input_encoding='utf-8',
    output_encoding='utf-8',
    filesystem_checks=False,
    encoding_errors='replace',
    module_directory=join('./', '_templates'),
)


class BaseHandler(RequestHandler):
    def initialize(self, lookup=MAKO_LOOK_UP):
        '''Set template lookup object, Defalut is MAKO_LOOK_UP'''
        self._lookup = lookup

    def render_string(self, filename, **kwargs):
        '''Override render_string to use mako template.
        Like tornado render_string method, this method
        also pass request handler environment to template engine.
        '''
        try:
            template = self._lookup.get_template(filename)
            env_kwargs = dict(
                handler=self,
                request=self.request,
                current_user=self.current_user,
                locale=self.locale,
                _=self.locale.translate,
                static_url=self.static_url,
                xsrf_form_html=self.xsrf_form_html,
                reverse_url=self.application.reverse_url,
            )
            env_kwargs.update(kwargs)
            return template.render(**env_kwargs)
        except:
            # exception handler
            return exceptions.html_error_template().render()
            # pass

    def render(self, filename, **kwargs):
        self.finish(self.render_string(filename, **kwargs))

    def write_json(self, data_dict):
        """if data is dict, self.write default write it as json data."""
        self.write(data_dict)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            super(BaseHandler, self).write_error(status_code, **kwargs)


class PageNotFoundHandler(BaseHandler):
    def get(self):
        # then call write_error
        raise HTTPError(404)

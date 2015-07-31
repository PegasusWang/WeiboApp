知识细节:
*arg可以解包元组，而**arg则可以解包字典
leancloud用递归查询方式遍历* 所有*数据,递归注意要排序，否则有可能取到重复数据

to learn:
scrapy learn# don't use
通过代理
casperjs
用nodejs搭建博客http://witcheryne.iteye.com/blog/1169854

重新组织代码：
写一个weibo_types.py在weibo_app里导入
写一个爬虫基类,让以后的爬虫继承
把lencloud接口封装（包括上传和获取接口），直接给出类名就可以操作）
爬虫站点分类，+lenncloud, types，app里边只要给出类型和权重就好
画url表示爬虫-weiboapp-lencloud接口-类型接口之间的关系


todo：
#encoding=utf-8
import jieba

seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
print "Default Mode:", "/ ".join(seg_list) #默认模式
seg_list = jieba.cut("他来到了网易杭研大厦")
print ", ".join(seg_list)
jieba分词，提取图片名字评论提取tag，设置tag——list,写在上传
煎蛋爬虫jiandan_wuliao, jiandan_meizi
douban_meizi爬虫
duowan tuku图片爬虫


图片按月分类
电子书按月分类
月底分享

next：
搭建mxiong，学习bottle使用方法
教程从零搭建一个网站


域名：
搜索godaddy优惠券

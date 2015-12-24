# Footprint--:snail::mushroom:记录去过的足迹

#### 程序员的浪漫，我女朋友蘑菇喜欢旅游，于是我做了这个，记录2015一起去过的地方，祝她圣诞快乐

#### 如果觉得对你有帮助，麻烦去[她的微博](http://www.weibo.com/u/2814551062)评论一句圣诞快乐


```
├── README.md 说明文档
├── javascript 网页版本
│   └── index.html
└── python python版本
    ├── build.py 编译生成文件
    └── config.py 你需要修改的配置文件

```

### 写配置文件，生成去过的足迹，哄妹子必备

本文集中了我的前两篇文章[日志可视化](https://github.com/shengxinjing/my_blog/issues/2)和[配置文件生成cmdb](http://shengxinjing.cn/woniu-cmdb/)，最终做出来的，分为网页和python两个版本，喜欢的跪求star

### 网页版

1. [戳地址](http://mushdog.sinaapp.com/footprint.html)
2. 左边输入标题，副标题
3. 下面的输入框输入行程，每个输入框是一个行程，地点之间用空格间隔，可以点击添加行程按钮新增输入框
4. 点击右侧的查看效果，右侧的图就会变成你配置的效果
5. 新建一个html文件，点击导出代码，把弹出来的一坨代码粘进去，bingo
6. 去[蘑菇的微博](http://www.weibo.com/u/2814551062)评论一句圣诞快乐
7. 谢谢大家

![](http://7xjoq9.com1.z0.glb.clouddn.com/footprint01.png)
![](http://7xjoq9.com1.z0.glb.clouddn.com/footprint02.gif)

### python版本

* 下载本项目，进入到python目录下，有两个文件，config是你需要修改的2. 


```
config={
	'title':'去过的地方',
	'subtitle':'北京 昆明 西北 呼和浩特',
	'foot':[
		'北京 昆明 丽江 香格里拉 丽江 昆明 北京',
		'霍营地铁站 布达拉宫',
		'北京 北戴河 北京',
		'北京 兰州 敦煌 张掖 祁连 西宁 青海湖 茶卡盐湖 西宁 银川 呼和浩特 北京'
	]
}

```

* 修改上面这个配置里的title(标题),subtitle(副标题)和foot(行程)
* foot是一个数组，每个元素是一个行程，目的地(景点)之间用空格分开
* 执行 python build.py ,会生成一个footprint.html，大功告成，浏览器打开看效果吧
* 去[蘑菇的微博](http://www.weibo.com/u/2814551062)评论一句圣诞快乐
* 谢谢大家
![](http://7xjoq9.com1.z0.glb.clouddn.com/footprint03.gif)


### 彩色版本和定制区域

* 时间仓促，网页版还没加上
* config加一个color变量，就会把足迹线编程彩色，如下

```
config={
	'title':'去过的地方',
	'subtitle':'北京 昆明 西北 呼和浩特',
	'color':True,
	'foot':[
		'北京 昆明 丽江 香格里拉 丽江 昆明 北京',
		'霍营地铁站 布达拉宫',
		'北京 北戴河 北京',
		'北京 兰州 敦煌 张掖 祁连 西宁 青海湖 茶卡盐湖 西宁 银川 呼和浩特 北京'
	]
}
```

![](http://7xjoq9.com1.z0.glb.clouddn.com/footprint04.gif)


* 如果你只在北京内部玩，或者定制一个北京旅游计划，可以加一个region字段，如下

```
config={
	'title':'北京去过的地方',
	'subtitle':'走啊走',
	'color':True,
	'region':'北京',
	'foot':[
		'北京交通大学 霍营地铁站 古北水镇',
		'北京交通大学 八达岭 北京交通大学',
		'北京交通大学 妙峰山 潭柘寺'
		
	]
}
```


最后，麻烦大家去[蘑菇的微博](http://www.weibo.com/u/2814551062)评论一句圣诞快乐

![](http://7xjoq9.com1.z0.glb.clouddn.com/footprint05.gif)




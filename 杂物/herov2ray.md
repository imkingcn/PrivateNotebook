---
title: Hero+V2+CF
tags:
  - v2
  - 教程
  - Cloudflare
abbrlink: hero
categories: 教程
date: 2020-06-17 10:12:08
---
Heroku 是一个提供并支持多种编程语言的云平台即服务，提供免费的容器服务（美国、欧洲节点），可以用免费的容器来搭建一个V2+CF加速网络，提供一个日常下载浏览的合适网站

<!--more-->

## 注册Hero账户并配置容器

1. 在<https://dashboard.heroku.com/>注册一个Hero账户，有账号直接登录(注册不要用QQ邮箱，可能收不到验证码)
2. 点击[创建应用](https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2Fbclswl0827%2Fv2ray-heroku)来部署免费应用，名字随便，节点有美国和欧洲，其它默认即可,点击Deploy app
![](http://p.ananas.chaoxing.com/star3/origin/3aa04daff60d54ea1585bc451cb165ba.png)
3. 部署完成以后，点击 Settings 再点击 Reveal Config Vars 就可以看见 UUID了！记下自己的UUID等会还是用到：
![](http://p.ananas.chaoxing.com/star3/origin/b4f16c589d09af6f7d9147616a4efc9a.png)

## 配置Cloudflare反向代理加速

1. 登陆CloudFlare官网，然后点击 右侧的 Workers ：
![](http://p.ananas.chaoxing.com/star3/origin/b7ac9ca73f9ec4f1ecdd16e1c94ee2e1.png)
2. 在Hero的setting的Domains项后有个域名！`https://*****.herokuapp.com/`记下域名
![](http://p.ananas.chaoxing.com/star3/origin/17b1bb3de405940e04598f6a3998743f.png)
3. 创建Workers，添加下列代码，替换自己的域名
```
addEventListener(
  "fetch",event => {
     let url=new URL(event.request.url);
     url.hostname="项目名字.herokuapp.com";
     let request=new Request(url,event.request);
     event. respondWith(
       fetch(request)
     )
  }
)
```
![](http://p.ananas.chaoxing.com/star3/origin/83e2ed5c473132c866c3a4bf541eca12.png)

## Cloudflare自选IP

下载Clloudflare自选IP程序，按提示进行操作
[下载地址](https://koyang.lanzous.com/igiAqeg0rli)
找到自己当前设备网络最好的IP

## 配置V2客户端

因为没有导入配置链接，只能手动配置，按图片提示来配置，记得打开tls
![](http://p.ananas.chaoxing.com/star3/origin/a501252138cd455941308f9cde210bc5.png)
配置完毕启动即可

## 效果

移动200M宽带测速
![](http://p.ananas.chaoxing.com/star3/origin/09df91184ab2bb69a66a970023a4efbc.png)
看4K视频
![](http://p.ananas.chaoxing.com/star3/origin/4db58aebc166e4fd8e1198aa74b8965b.png)

## 后记
- Hero不能滥用有封号风险
- 本教程只适用加速前几期的加速下载各种配置文件如npm、git和浏览学习资料如Github，如果你用于其它需求，与本人一概无关，请自觉遵守中国的网络法律发展，严于律己。
- 速度取决于你的运营商和自选的IP，请合理选择IP，而且对免费的东西不要抱有太高的要求，加钱世界即可及。

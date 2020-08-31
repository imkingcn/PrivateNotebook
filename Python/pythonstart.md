---
title: 腾讯云函数托管python代码定时打卡
date: 2020-08-03 14:45:30
tags: [Python,教程]
abbrlink: pythonstart
categories: Python
cover: https://cdn.jsdelivr.net/gh/HandsomeKY/picture@latest/code.jpg
---
因为疫情，所以我们的生活又多了一项定时打卡的任务，为了拯救愉快的假期，所以我将运用python程序自动打开，并将这个python程序放置到腾讯云，利用云函数定时执行python程序，实行完全的托管
## 注册腾讯云账号
有腾讯云账号直接登录，没有则注册一个，然后打开腾讯云的[云函数](https://console.cloud.tencent.com/scf/)界面
![](https://gitee.com/koyangyang/pictures/raw/master/20200803145254.png)
## 创建云函数任务
1. 地区随便选择，最后选个中国境内的，地理位置较近的最好
![](https://gitee.com/koyangyang/pictures/raw/master/20200803145747.png)
2. 名称随便，运行环境一定要选`python3.6`，创建方式`空白模板`
![](https://gitee.com/koyangyang/pictures/raw/master/20200803145904.png)
3. **腾讯云函数不是直接将python程序代码直接复制上去，需要对程序的启动方式和主函数进行一定修改才可以执行，如有兴趣想了解请移步**[帮助文档](https://cloud.tencent.com/document/product/583/37509),输入下面已经修改好的代码，将注释部分修改自己的信息
```python
# -*- coding: utf8 -*-
import json
import requests
import time
def main_handler(event, context):
    url = "http://swxg.haust.edu.cn/xgh5/openData"
    data = {}
    data["command"] = "command"
    param = {
        "cmd":"yqsbFormSave",
        # 修改这中间的自己的信息
        "xh":"",
        "sbsj":"2020-02-04",
        "nl":"19",
        "lxfs":"",
        "jzdq":"",
        "jzdq_xxdz":"",
        # 修改自己信息
        "tw":"36.5",
        "sflx":"0",
        "jcbr":"0",
        "zyzz":"1,",
        "fbrq":"",
        "zyzzms":"",
        "bz":"",
        "bz1":"",
        "wcjtgj":"",
        "wcjtgjxq":"",
        "wcdq":"",
        "wcdqxxdz":"",
        "lkdate":"",
        "fhdate":"",
        "zszt":""
    }
    param["sbsj"] = time.strftime("%Y-%m-%d", time.localtime())
    data["param"] = json.dumps(param)
    req = requests.post(url, data=data).json()
    req["xh"] = param["xh"]
    print(json.dumps(req, ensure_ascii=False))
    # 有需要Sever酱推送请开启这一项
    # result = requests.get("https://sc.ftqq.com/{自己的key}?text=主人报平安打卡任务完成")
```
方框中修改自己的信息
![](https://gitee.com/koyangyang/pictures/raw/master/20200803150413.png)
## 添加定时任务
创建触发器
![](https://gitee.com/koyangyang/pictures/raw/master/20200803150539.png)
选择自定义触发周期
`0 0 7 * * * *`<br>
`代表的是秒 分 时，比如八点十分五十六秒就是 56 10 8 * * *`
![](https://gitee.com/koyangyang/pictures/raw/master/20200803150713.png)
## 关于Sever酱
在代码最后一行有个[Sever](http://sc.ftqq.com/3.version)，方便查看代码有没有运行，其实只要配置好了就不会不运行，也不会因为服务器问题导致宕机，除非腾讯倒闭了。
在腾讯云的日志查询可以查看运行情况
![](https://gitee.com/koyangyang/pictures/raw/master/20200803151429.png)
如果我们添加了`Sever酱`推送服务,可以每天执行完任务给我们发微信消息通知,将这段代码
```python
result = requests.get("https://sc.ftqq.com/{自己的key}.send?text=主人报平安打卡任务完成")
```
中的{}部分换成自己的`Sever酱`的key
![](https://cdn.jsdelivr.net/gh/HandsomeKY/picture@latest/sever.jpg
)
其实这个只是方便观察程序有没有执行，其实并不用担心，因为腾讯云作为第三大云服务器厂商还是值得信赖的，背靠大树乘凉。
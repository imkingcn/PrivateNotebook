# 好看视频的爬取
## 获取url
打开网页，打开开发者选项，找到`Network`,选择`XHR`，找到`Request URL`
![](https://gitee.com/koyangyang/pictures/raw/master/20200820111454.png)
## 增加反爬信息
在`requests(url,headers)`中的`headers`中加入`User-Agent`、`Referer`、`Cookie`
```python
headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
	"Referer": "https://haokan.baidu.com/"
}
```
## 分析数据
其中`title`等信息经过三层嵌套['data']->['response']->['videos']
![](https://gitee.com/koyangyang/pictures/raw/master/20200820112127.png)
此时在输出，就已经是`video`的字典内容了
![](https://gitee.com/koyangyang/pictures/raw/master/20200820112332.png)

## 具体代码
[传送门](https://github.com/koyangyang/PrivateNotebook/blob/master/Python/Hotvideo.py)
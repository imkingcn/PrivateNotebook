# Json文件提取

## 获取Json文件

- 演示地址:
- **url:https://www.tianqiapi.com/api/**

## 安装所需库

-  **requests：**

  ```python
  pip3 install requests
  ```

- **jsonpath：**

  ```python
  pip3 install jsonpath
  ```

## 创建requests对象

```python
url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

response = requests.get(url,headers=headers)
```

## 获取内容

```python
html=response.text
```

至于`.text`和`.content`区别还情看[text和content区别](#text和content区别)

## 数据转换

```python
data = json.loads(html)
```

## 利用Jsonpath提取数据

```python
cities = jsonpath.jsonpath(data,'$...name')
```

## 完整代码

```python
import requests
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

response = requests.get(url,headers=headers)
html = response.text

data = json.loads(html)

cities = jsonpath.jsonpath(data,'$...name')
print(cities)
```

结果

![](https://gitee.com/koyangyang/pictures/raw/master/20200818232250.png)

## text和content区别

content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串，大部分情况建议使用.text，因为显示的是汉字，但有时会显示乱码，这时需要用.content.decode('utf-8')，中文常用utf-8和GBK，GB2312等

resp.text返回的是Unicode型的数据。

resp.content返回的是bytes型也就是二进制的数据。

**想取文本，可以通过r.text**

**如果想取图片，文件，则可以通过r.content**

（resp.json()返回的是json格式数据）

## Json模块使用

- json.loads json字符串 转 Python数据类型
- json.dumps Python数据类型 转 json字符串
- json.load json文件 转 Python数据类型
- json.dump Python数据类型 转 json文件
  - ensure_ascii=False 实现让中文写入的时候保持为中文
  - indent=空格数 通过空格的数量进行缩紧

## 总结

- JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
- JSON相关的方法
  - json.loads json字符串 转 Python数据类型
  - json.dumps Python数据类型 转 json字符串
  - json.load json文件 转 Python数据类型
  - json.dump Python数据类型 转 json文件
- jsonpath 是一种语法规则快速从 JSON 数据中提取数据。
- jsonpath 基本语法
  - $ 根节点
  - . 下一个节点
  - .. 子孙节点
  - [] 筛选条件，可以编写下标
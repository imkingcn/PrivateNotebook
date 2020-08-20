import requests
import json

# 爬取链接
url="https://haokan.baidu.com/videoui/api/videorec?tab=yingshi&act=pcFeed&pd=pc&num=5&shuaxin_id=1597890478195"
# 表头
headers={
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
	"Referer": "https://haokan.baidu.com/"
}
# 获取请求，text返回文本信息
response=requests.get(url,headers=headers).text
# 将Json转换为python格式
result=json.loads(response)
# 提取信息
data=result['data']['response']['videos']
for vedio in data:
	mp4_name=vedio['title']
	mp4_url=vedio['play_url']
	# content用于获取二进制文件
	mp4=requests.get(mp4_url,headers=headers).content
	print('正在下载：'+mp4_name)
	with open('./视频/%s.mp4'%(mp4_name),'wb') as f:
		f.write(mp4)
		print(mp4_name+'下载完成\n')

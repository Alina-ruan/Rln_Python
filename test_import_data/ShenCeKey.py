import requests

class ShenCeKey:
    # get请求的封装：因为params课程会存在无值的情况，存放默认值None
     def do_put(self, url, headers, data):
         # 因为请求会默认返回一个响应，所以函数定义时需要return一下
         return requests.put(url=url,  headers=headers, json=data)


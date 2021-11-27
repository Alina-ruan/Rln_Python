import requests
import json

#创建表单
url = 'https://test-rest-form.kaikeba.com/admin/form/saveForm'
headers = {
    'authorization': 'bearer d4cec690-b3bc-4d38-b471-e99efb7ec4b5',
    'content-type': 'application/json'
}

data1 = {
    "name": "测试表单009878877",
    "use": 4,
    "businessLine": 1,
    "subject": 1,
    "templateId": 1839,
    "accountId": 1001,
    "accountName": "kkb1028",
    "note": ""
}

r = requests.post(url=url, headers=headers, data=json.dumps(data1))

#提取formId的值
formId1 = r.json()['data']['formId']

#发布表单
url = 'https://test-rest-form.kaikeba.com/admin/form/publish'
data2 = {
    "formId": formId1,
    "status": 1,
    "isLogin": 1,
    "condition": 3,
    "isPush": 1,
    "eventId": 1
}


r = requests.post(url=url, headers=headers, data=json.dumps(data2))
print(r.json())

requests.get()







import openpyxl
from ShenCeKey import ShenCeKey

url = 'https://sensors.kaikeba.com/api/v2/sdg/metadata/events'

def read_excel_file(filepath):
    # 加载文件
    excel = openpyxl.load_workbook(filepath)
    # 通过表格的名字来读取sheet
    sheet = excel['哈哈']

    # 读取每一行的文件作为请求参数
    for cell in sheet.values:
        data = {"event_define": {"tag": [], "cname": cell[1], "name": cell[0],
                                 "visible": 'true', "trigger_opportunity": cell[2],
                                 "platform": [{"name": "WEB", "uploaded": 'true'}], "snapshot_ids": [], "comment": ""},
                "properties": [
                    {"id": 483, "name": "staff_name", "cname": "员工姓名", "data_type": "STRING", "has_dict": 'true',
                     "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true', "comment": "",
                     "trigger_opportunity": "", "disable": 'true'},
                    {"id": 444, "name": "is_login", "cname": "is_login", "data_type": "BOOL", "has_dict": 'true',
                     "is_in_use": 'true', "uploaded": 'true', "is_common": 'true', "comment": "",
                     "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER", "OTHER"],
                     "trigger_opportunity": "登录时候调整设置"},
                    {"id": 466, "name": "sid", "cname": "员工ID", "data_type": "STRING", "has_dict": 'true',
                     "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true', "comment": "",
                     "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER"], "trigger_opportunity": "每次"},
                    {"id": 397, "name": "event_id", "cname": "event_id", "data_type": "STRING", "has_dict": 'true',
                     "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true', "comment": "",
                     "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER"], "trigger_opportunity": "每次"},
                    {"id": 361, "name": "device_type", "cname": "用户设备类型", "data_type": "STRING", "has_dict": 'true',
                     "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true', "comment": "",
                     "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER"], "trigger_opportunity": "每次"},
                    {"id": 240, "name": "uid", "cname": "uid", "data_type": "STRING", "has_dict": 'true',
                     "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true',
                     "comment": "开课吧统一的用户ID",
                     "platform": ["ANDROID", "IOS", "WEB", "MINI_APP"],
                     "trigger_opportunity": "登录时候调整设置,没有登录，不用填写uid字段"},
                    {"id": 134, "name": "system_type", "cname": "system_type", "data_type": "STRING",
                     "has_dict": 'true', "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true',
                     "comment": "用户端/管理端", "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER", "OTHER"],
                     "trigger_opportunity": "系统初始化"},
                    {"id": 114, "name": "sub_product_name", "cname": "sub_product_name", "data_type": "STRING",
                     "has_dict": 'true', "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true',
                     "comment": "", "platform": ["IOS", "ANDROID", "MINI_APP", "WEB", "SERVER", "OTHER"],
                     "trigger_opportunity": "系统初始化"},
                    {"id": 113, "name": "platform_type", "cname": "platform_type", "data_type": "STRING",
                     "has_dict": 'true', "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true',
                     "comment": "", "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER", "OTHER"],
                     "trigger_opportunity": "系统初始化"},
                    {"id": 30, "name": "product_name", "cname": "product_name", "data_type": "STRING",
                     "has_dict": 'true', "is_in_use": 'true', "unit": "", "uploaded": 'true', "is_common": 'true',
                     "comment": "", "platform": ["IOS", "ANDROID", "WEB", "MINI_APP", "SERVER", "OTHER"],
                     "trigger_opportunity": "前端初始化"}]}

        headers = {'Content-Type': 'application/json',
                   'cookie': 'gr_user_id=6fcbe656-ad1b-4369-abbc-b2e3970e1c27; kd_user_id=b764fd9d-c59e-402c-a426-2cea97297bd7; Hm_lvt_156e88c022bf41570bf96e74d090ced7=1636014919,1636707512; corgi-token-prod-data=bc9c36f5-073b-444a-8bdc-2389dfd96eb9; figui=9O4D3T1xPCy1AAA1; corgi-token-test-data=28b05250-3437-4171-9715-36945881af5b; test_figui=WqGZNOK6287AAAA1; sensorsdata-token=HCSJtN03BxKVXMNAPIYyetDsqOOYW67FIy8qlpVLxxQd8jjOMQMwu7acUOWa6kBD5Wub1WGQSJ27OfDXcz1KiXd0ePlzTnAdA7EXQ5JxgkfvftWTHmVbNBlmnLSbeeez; kd_5001f43b-938d-425d-a40d-4ffdd9d0fab5_log_id=e2LqoYjeoiXS5TWvZjy%3Ad30406b4-b56b-4e0f-95ac-2c54fff76365%3A51f2400d-aacd-499b-879b-fcba257da9ff; user=286d9b60757cb48c7c1dcc37ae3722fa39d96c6a3cd996e59347eadc1576635cf302dded2b34b47b19b339bb05a7261b837c090e176e4a8d06a92534ed2bee7f01162dc3f2f17a2876bb3954556815241bcf61e2c2c0ab98a18b44f17e7db1264a162cf0caabdedcb4602bd696104fef4838a3d8b5cf1f1dc50291ee4e3ebd6077ebb1dd9cd366ec375e4b84e29a28c103207cf161d3097a210822a37c03cb54a42ad4fdb914a4a79237cc3e75b99a583084f7ff3fe6dfcc42364ef8583ed86ec9c21d00442407182a961cd892337cdcd7955783fface55a38dbf06cc8c20ad9ce51914693d826730a32e703bbac1f6713b432583aaf8c9f315766846f2c49484420be3ae4b50d9bb9fc729390bbd927b1b2ee1f79e6eb3ce1bb1d9c470c6279fd6484c0c965cb54a15d59f777317def4cb76462a703675c537fc6dc963e05a4851bb48d5634ab6854a6df3f78257f1e58bd281cafd32c7051298faa2f68f065a59fa7454dab3cd3d0e5a6575b2d49a868d9f062f64013945ede5c1f2678b2b0fe50687a5d7d78a16277418b0ac4f031952d627f8b0fd189b2533f858147e468b386d2cce43ce4a995fb8e89ae69cfed2baa959c88146015b52bee0600e396afcad20f89ecf4b3b3d7c80911c74cd5b80b7d32022ac6d2357b2a99f1cd91d99c861489e7f162a9ff7435d43e99ceb94a79b0fb28a0493d20f0c3580cac7d54b4509773dbf0b7b52f8e82ffa73dd51c25e0b64da9cfa8b4a87264da7f3a51d07f753e7d9ad0b91d4b618c6e7158f53bc4666905a4a5f4f315065c2302fbdc5a212ceb6822b7573779af32a350af4c187e0fe5e9b9492692780059529dd16b46a774d9951ac5e2248e6032469c7a4f2999928967bfa84bacfad1bbd61f2b9f0d601d1289718a6a900dd9b3feb12e642ad6e1d393d011de869f14f182947807638bc31992f106e309a8f956689c79ba9f2f9a9fef882ff778e5b8decd9c1439b865510d665de82148c9a0980ac0b871ac92edcfdd74b1c8a9dc624058de9a0388cfdd8c388204e59bc62024a6b6e73af30b030cdef4d8b80d885408ee86c29626aab80370c72f65e9ade2e975748e4f6219b680bca9286444914b4ecb466141dced6121be46433db650de82e2fec2bf2c83e20596dab055dc4e9c14d51500b497228d6fd0a6432f6a3600802e4ba537f54d13e84043c73f160c5c37823a417879a006e4db5348b2d362b847c54fc0ddc1e1f52cb9e1fc2734748a0fc07f32f53800fbaa9a2958cfa61e51c3a79e5e01e4857e20308fb59d11e6c823ef3b81c8b8e24db4231928574fb79287609343575b83576c3890bb0672dc7d05414af6dd3886876b8d44b6b61165befaa0bf1beb45da; user_id=71487; access_token=7b3ea3ef8bd7178ec583a938081a814a7e5da70b8624f22044e60e81165081d3c1b5b53b0488da5e378bb1c6e85cba8c32b02c8aaa43f2060afe5b1c91b58d88; user_name=%E8%B5%B5%E4%B8%BD%E5%90%9B; user_photo_url=https%3A%2F%2Fkcn-img-prod.kaikeba.com%2Fuser%2Fheader%2Fguest.png; kd_10bc337c-8863-4a4e-a8f8-74e09ab6bbb3_kuickDeal_pageIndex=99; kd_10bc337c-8863-4a4e-a8f8-74e09ab6bbb3_log_id=87xZdxZIa2sux4nm6g8%3A3a840e60-0f7f-4c91-87b6-ce1c12890106%3Aundefined; kd_10bc337c-8863-4a4e-a8f8-74e09ab6bbb3_view_log_id=X7dgCiYGtxqmpU2e6iE; kd_4fc6e1e8-454d-4065-a6fd-68fee7a77b0d_log_id=hUUhCpVl7jJ3gHBswnC%3A982dc765-35b6-4adc-8b34-3af969394981%3Afb3475da-6f07-496c-afe3-12bf2f3fe0ed; kd_4fc6e1e8-454d-4065-a6fd-68fee7a77b0d_view_log_id=962kqrZlLzBjbfaVU22; kd_5d6526d7-3c9f-460b-b6cf-ba75397ce1ac_kuickDeal_pageIndex=6; kd_5d6526d7-3c9f-460b-b6cf-ba75397ce1ac_log_id=YIoftiTtoV1Nynvgt5i%3A35880672-91d7-4943-9d84-b5d080764137%3Aundefined; kd_5d6526d7-3c9f-460b-b6cf-ba75397ce1ac_view_log_id=9gzAeQEvXRGqXgZzKXQ; kd_4fc6e1e8-454d-4065-a6fd-68fee7a77b0d_kuickDeal_pageIndex=0; kd_4fc6e1e8-454d-4065-a6fd-68fee7a77b0d_kuickDeal_leaveTime=1637145785143; sbp_web=888acef53366613414bbc47fa9a1f6b1; sa_v2_web_route=9a223b694dd87bed26a2dfba3de9f116; sa_web_route=6538444517bf26a12b03d7f344c20cd7; route=fe309fb147b94bbeaf23e878f68556e3; sdg_web_route=1e5af9b0564f7deb7031b7406d394f82; test2_user_id=139752; test2_access_token=55374f2e4bd0df0481e834cf0e34b94a707c1cc5908978a28b5fb873d08fd52f929139ec2dc53d4836386c1b2f40991eed76428d8ea8991713d5985145b13700; test2_user_name=%E8%B5%B5%E4%B8%BD%E5%90%9B; test2_user_photo_url=https%3A%2F%2Fkcn-img-prod.kaikeba.com%2Fuser%2Fheader%2Fguest.png; kd_5001f43b-938d-425d-a40d-4ffdd9d0fab5_kuickDeal_leaveTime=1637159017374; kd_5001f43b-938d-425d-a40d-4ffdd9d0fab5_kuickDeal_pageIndex=2; kd_5001f43b-938d-425d-a40d-4ffdd9d0fab5_view_log_id=7XgdnU894TtqbCz9wIk; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100007826%22%2C%22first_id%22%3A%2217c79223e3965c-0b435a87d4bc818-123b6650-2073600-17c79223e3a8e0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217c79223e3965c-0b435a87d4bc818-123b6650-2073600-17c79223e3a8e0%22%7D'
                   }
        #初始化执行操作的对象
        sck = ShenCeKey()
        res = sck.do_put(url, headers, data)
        print(res.text)
        print(res.status_code)


if __name__ == '__main__':
    read_excel_file('/Users/rln/Documents/test_excel.xlsx')




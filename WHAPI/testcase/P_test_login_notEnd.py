import requests
import json
#用于字符串匹配
import re
from common.yaml_util import write_yaml, read_testcase
from common.csv_util import read_csv
import pytest


class TestRequest:    
    #读取yaml文件中的数据
    test_data = read_testcase("getToken.yaml")

    #使用yaml文件的方法
    @pytest.mark.parametrize("case", read_testcase("getToken.yaml"))
    #@pytest.mark.parametrize("args_name, test_data_name", csv_data, test_data)
    #登录
    def test_login(self, case):
        #print(args_name)
        #读取csv文件中的数据
        csv_data = read_csv("D:/Python/WHAPI/data/get_token_data.csv")
        
        data = csv_data[0]
        url = case["request"]["url"]
        method = case["request"]["method"]
        res = requests.request(method=method, url=url, json=data)
        #res = RequestUtil().send_request(method="post", url=url, datas=data)
        print(res.json())
        #获取token放到全局变量中
        #TestRequest.accessToken = res.json()['data']['accessToken']
        
        #将token写入yaml文件
        #write_yaml({"accessToken": res.json()['data']['accessToken']})
        
        #如果有多条用例，需要判断什么时候将accessToken写入yaml文件
        if "accessToken" in res.text:
            write_yaml({"accessToken": res.json()['data']['accessToken']})



   
#单元测试方法
if __name__ == '__main__':  
    TestRequest().test_login()  
   











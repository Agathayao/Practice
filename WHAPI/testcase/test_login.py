import requests
import json
#用于字符串匹配
import re
from common.yaml_util import write_yaml, clear_yaml, read_testcase
import pytest
import yaml


class TestRequest:    
    #使用yaml文件的方法
    @pytest.mark.parametrize("args_name", read_testcase("getToken.yaml"))
    #登录
    def test_login(self, args_name):
        #print(args_name)
        
        url = args_name["request"]["url"]
        data = args_name["request"]["data"]
        method = args_name["request"]["method"]
        res = requests.request(method=method, url=url, json=data)
        #res = RequestUtil().send_request(method="post", url=url, datas=data)
        print(res.json())
        #获取token放到全局变量中
        #TestRequest.accessToken = res.json()['data']['accessToken']
        
        #将token写入yaml文件
        #write_yaml({"accessToken": res.json()['data']['accessToken']})
        
        '''
        #清除yaml文件中的数据后再写入
        with open(r"D:/Python/WHAPI/extract.yaml", 'r', encoding='utf-8') as file:  
            current_data = yaml.safe_load(file)
        if current_data is not None and current_data != {}:  
            # 调用clear_yaml()方法清空文件  
            clear_yaml()  
            # 调用write_yaml()方法写入新数据  
            if "accessToken" in res.text:
                write_yaml({"accessToken": res.json()['data']['accessToken']})
        else:  
            # 如果文件为空或不存在数据，则直接写入新数据  
            write_yaml({"accessToken": res.json()['data']['accessToken']})
        '''
        
        #如果有多条用例，需要判断什么时候将accessToken写入yaml文件
        if "accessToken" in res.text:
            write_yaml({"accessToken": res.json()['data']['accessToken']})
        


   
#单元测试方法
if __name__ == '__main__':  
    TestRequest().test_login()  
   











import pytest
import requests
from common.yaml_util import read_yaml

class TestPlan:
    #获取计划列表
    
    def test_planList(self):
        url = "https://f.fkhwl.com/ml_nfs_api/transportPlan/pages"
        header = {
            #"Authorization": f'Bearer {TestRequest.accessToken}' 
            "Authorization": f'Bearer {read_yaml("accessToken")}'   
        }
        
        data = {
            "limit": 15,
            "page": 1
        }
        
        res = requests.request(method="post", url=url, headers= header, json=data)
        print(res.json())
    
   
        
#单元测试方法
if __name__ == '__main__': 
    TestPlan().test_planList()     
        
        
        
        
        
        
import pytest
import requests
from common.yaml_util import read_yaml, read_testcase, write_yaml, clear_yaml


class TestMaterial:
    @pytest.mark.parametrize("args_name", read_testcase("/testdata/material.yaml"))
    #新增物资
    def test_addMaterial(self, args_name):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'   
        }
    
        url = args_name["request"]["url"]
        method = args_name["request"]["method"]
        data = args_name["request"]["data"]
        
        res = requests.request(method=method, url=url, headers=header, json=data)
        print(res.json())
        #assert res.json()['success'] == True
        
        
    #查询物资
    def test_searchMaterial(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/material/pages"
        method = "post"
        data = {
            "limit": 15,
            "page": 1
        }    
        
        res = requests.request(method=method, url=url, headers=header, json=data)  
        print(res.json())
        assert res.json()['success'] == True
        
        clear_yaml("materialId")
        write_yaml({"materialId": res.json()['data']['records'][0]["id"]})
     
     
        
    #编辑物资    
    def test_editMaterial(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/material/saveOrUpdate"
        method = "post"
        data = {
            "name": "石英1",
            "code": "shiying",
            "id": f'{read_yaml("materialId")}' 
        }
        
        res = requests.request(method=method, url=url, headers=header, json=data)  
        print(res.json())
        assert res.json()['success'] == True
        
   
    #审核物资
    def test_auditMaterial(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/material/audit/1"
        method = "post"
        data = {
            "id": f'{read_yaml("materialId")}',
            "type": 1 
        }

        res = requests.request(method=method, url=url, headers=header, json=data)  
        print(res.json())
        assert res.json()['success'] == True
        
    
    #删除物资
    def test_deleteMaterial(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'   
        }
        
        materialId = f'{read_yaml("materialId")}'
        url = f"https://f.fkhwl.com/ml_nfs_api/material/delete/{materialId}"
        method = "post"
        data = {
            "id": f'{read_yaml("materialId")}'
        }

        res = requests.request(method=method, url=url, headers=header, json=data)  
        print(res.json())
        assert res.json()['success'] == True
    
        
#单元测试方法
if __name__ == '__main__': 
    TestMaterial().test_addMaterial()  
    TestMaterial().test_searchMaterial()
    TestMaterial().test_editMaterial() 
    TestMaterial().test_auditMaterial()
    TestMaterial().test_deleteMaterial()  
        
        
        
        
        
        
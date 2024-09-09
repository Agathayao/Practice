import pytest
import requests
from common.yaml_util import read_yaml, clear_yaml, write_yaml



class TestPlan:
    #新增计划
    def test_addPlan(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}',
            "Content-Type": "application/json;charset=UTF-8"   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/transportPlan/saveOrUpdate"
        method = "post"
        data = {
            "planName": "9月测试计划",
            "transportType": 1,
            "sendCompany": "四川天呈托运有限公司",
            "receiveCompany": "成都新川贸易有限公司",
            "sendAddrName": "西安世博园",
            "receiveAddrName": "武侯大道",
            "logisticsName": "成都快运有限公司",
            "corporateContractId": 27,
            "materialName": "连砂石",
            "materialNumber": 2000,
            "unitPrice": 150,
            "lessPrice": 20,
            "weighDifferenceMode": 1,
            "precisionStandard": 0,
            "perfectBillMode": [
                1,
                2
            ],
            "logisticsId": 41,
            "sendCompanyId": 37,
            "receiveCompanyId": 42,
            "materialId": 1096,
            "freightRule": {
                "precisionStandard": 0,
                "perfectBillMode": [
                    1,
                    2
                ],
                "deficientTonSet": [
                    {
                        "ladderSort": 1,
                        "minDifference": 0,
                        "maxDifference": 1,
                        "settleNetWeightMode": 2,
                        "deductWeighDifferenceMode": 0,
                        "penalty": 0,
                        "penaltyPrice": 0
                    },
                    {
                        "ladderSort": 2,
                        "minDifference": 1,
                        "maxDifference": 2,
                        "settleNetWeightMode": 2,
                        "deductWeighDifferenceMode": 2,
                        "allowWeighDifference": 1,
                        "penalty": 0,
                        "penaltyPrice": 0
                    },
                    {
                        "ladderSort": 3,
                        "minDifference": 2,
                        "maxDifference": 9999,
                        "settleNetWeightMode": 1,
                        "deductWeighDifferenceMode": 3,
                        "allowWeighDifference": 0.5,
                        "fixedWeighDifference": 0.5,
                        "penalty": 1,
                        "penaltyPrice": 3
                    }
                ],
                "increaseTonSet": [
                    {
                        "ladderSort": 1,
                        "minDifference": 0,
                        "maxDifference": 9999,
                        "settleNetWeightMode": 1,
                        "deductWeighDifferenceMode": 0,
                        "allowWeighDifference": 0,
                        "penalty": 0,
                        "penaltyPrice": 0
                    }
                ],
                "materialUnit": 1,
                "weighDifferenceMode": 1
            },
            "receiveAddrId": 31,
            "sendAddrId": 18,
            "materialUnit": 1
        }

        res = requests.request(method=method, url=url, headers=header, json=data)
        print(res.json())
        assert res.json()['success'] == True


    #查询计划列表
    def test_searchPlan(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}',
            "Content-Type": "application/json;charset=UTF-8"   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/transportPlan/pages"
        method = "post"
        data = {
            "limit": 15,
            "page": 1
        }

        res = requests.request(method=method, url=url, headers=header, json=data)
        print(res.json())
        assert res.json()['success'] == True
        
        clear_yaml("planId")
        write_yaml({"planId": res.json()['data']['records'][0]["id"]})
        
        
    #编辑计划
    def test_editPlan(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}',
            "Content-Type": "application/json;charset=UTF-8"   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/transportPlan/saveOrUpdate"
        method = "post"
        data = {
            "planName": "9月测试计划1",
            "transportType": 1,
            "sendCompany": "四川天呈托运有限公司",
            "receiveCompany": "成都新川贸易有限公司",
            "sendAddrName": "西安世博园",
            "receiveAddrName": "武侯大道",
            "logisticsName": "成都快运有限公司",
            "corporateContractId": 27,
            "materialName": "连砂石",
            "materialNumber": 2000,
            "unitPrice": 150,
            "lessPrice": 20,
            "weighDifferenceMode": 1,
            "precisionStandard": 0,
            "perfectBillMode": [
                1,
                2
            ],
            "logisticsId": 41,
            "sendCompanyId": 37,
            "receiveCompanyId": 42,
            "materialId": 1096,
            "freightRule": {
                "precisionStandard": 0,
                "perfectBillMode": [
                    1,
                    2
                ],
                "deficientTonSet": [
                    {
                        "ladderSort": 1,
                        "minDifference": 0,
                        "maxDifference": 1,
                        "settleNetWeightMode": 2,
                        "deductWeighDifferenceMode": 0,
                        "penalty": 0,
                        "penaltyPrice": 0
                    },
                    {
                        "ladderSort": 2,
                        "minDifference": 1,
                        "maxDifference": 2,
                        "settleNetWeightMode": 2,
                        "deductWeighDifferenceMode": 2,
                        "allowWeighDifference": 1,
                        "penalty": 0,
                        "penaltyPrice": 0
                    },
                    {
                        "ladderSort": 3,
                        "minDifference": 2,
                        "maxDifference": 9999,
                        "settleNetWeightMode": 1,
                        "deductWeighDifferenceMode": 3,
                        "allowWeighDifference": 0.5,
                        "fixedWeighDifference": 0.5,
                        "penalty": 1,
                        "penaltyPrice": 3
                    }
                ],
                "increaseTonSet": [
                    {
                        "ladderSort": 1,
                        "minDifference": 0,
                        "maxDifference": 9999,
                        "settleNetWeightMode": 1,
                        "deductWeighDifferenceMode": 0,
                        "allowWeighDifference": 0,
                        "penalty": 0,
                        "penaltyPrice": 0
                    }
                ],
                "materialUnit": 1,
                "weighDifferenceMode": 1
            },
            "receiveAddrId": 31,
            "sendAddrId": 18,
            "materialUnit": 1,
            "id": f'{read_yaml("planId")}' 
        }

        res = requests.request(method=method, url=url, headers=header, json=data)
        print(res.json())
        assert res.json()['success'] == True
    
    
    #计划详情
    def test_planInfo(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'
        }
        
        #f-strings：格式化字符串
        planId = f'{read_yaml("planId")}'
        url = f"https://f.fkhwl.com/ml_nfs_api/transportPlan/info/{planId}"
        method = "post"  
        data = {
            "id": f'{read_yaml("planId")}',
        }  

        res = requests.request(method=method, url=url, headers=header, json=data)
        print(res.json())
        assert res.json()['success'] == True
    
    
    #计划日志
    def test_planLog(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}',
            "Content-Type": "application/json;charset=UTF-8"   
        }
        
        url = "https://f.fkhwl.com/ml_nfs_api/operationLog/record/pages"
        method = "post"
        data = {
            "businessId": f'{read_yaml("planId")}',
            "operationType": 1
        }
    
        res = requests.request(method=method, url=url, headers=header,json=data)
        print(res.json())
        assert res.json()['success'] == True
       
        
    #删除计划
    def test_deletePlan(self):
        header = {
            "Authorization": f'Bearer {read_yaml("accessToken")}'  
        }
        
        planId = f'{read_yaml("planId")}'
        url = f"https://f.fkhwl.com/ml_nfs_api/transportPlan/delete/{planId}"
        method = "post"   
        data = {
            "id": f'{read_yaml("planId")}'
        }  
    
        res = requests.request(method=method, url=url, headers=header, json=data)
        print(res.json())
        assert res.json()['success'] == True



if __name__ == '__main__':
    TestPlan().test_addPlan()
    TestPlan().test_searchPlan()
    TestPlan().test_editPlan()
    TestPlan().test_planInfo()
    TestPlan().test_planLog()
    TestPlan().test_deletePlan()



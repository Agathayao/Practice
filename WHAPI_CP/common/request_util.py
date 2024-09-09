import requests
import json

#封装意味着这个方法能够适应所有请求
class RequestUtil:
    
    #全局变量、类变量，通过类名调用
    sess = requests.session()
    
    #**kwargs表示不定长参数
    def send_request(self, method, url, datas=None, **kwargs):
        #先转化成字符串，小写格式
        method = str(method).lower()
        res = None
        if  method == "get":
            res = RequestUtil.sess.request(method=method, url=url, params=datas, **kwargs)
        elif method == "post":
            #如果不为空且是字典类型才做转化
            if datas and isinstance(datas, dict):
                #json类型的先转化成字符串，再传值
                str_datas = json.dumps(datas)    
            res = RequestUtil.sess.request(method=method, url=url, data=str_datas, **kwargs)
        else:
            pass 
        return res      
            
        
        
        
        
        
        
    
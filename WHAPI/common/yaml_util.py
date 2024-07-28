import os
import yaml
import csv


#读取（f是文件对象）中间变量
def read_yaml(key):
    #getcwd()方法：返回当前工作目录的绝对路径，获取项目的根目录，r表示加载
    #with open(os.getcwd()+'/extract.yaml', mode='r', encoding='utf-8') as f:     #注：这段代码有问题，读不出来文件
    with open(r"D:/Python/WHAPI/extract.yaml", mode='r', encoding='utf-8') as f:
        #全局加载，safe_load():安全解析函数，解析yaml文件
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        #value = yaml.safe_load(stream=f)
        return value[key]

# result = read_yaml("./WHAPI/extract.yaml")
# print(result)

#写入
def write_yaml(data):
    #获取项目的根目录，a表示追加
    #with open(os.getcwd()+'/extract.yaml', mode='a', encoding='utf-8') as f:      #注：这段代码有问题，读不出来文件
    with open(r"D:/Python/WHAPI/extract.yaml", mode='a', encoding='utf-8') as f:
        #允许unicode的方式写入
        yaml.dump(data, stream=f, allow_unicode=True)


#清空
def clear_yaml():
    #获取项目的根目录，w表示写入
    #with open(os.getcwd()+'/extract.yaml', mode='w', encoding='utf-8') as f:
    with open(r"D:/Python/WHAPI/extract.yaml", mode='w', encoding='utf-8') as f:
        f.truncate()



#读取（f是文件对象）测试用例
def read_testcase(yaml_name):
    #getcwd()方法：返回当前工作目录的绝对路径，获取项目的根目录，r表示加载
    #with open(os.getcwd()+'/extract.yaml', mode='r', encoding='utf-8') as f:     #注：这段代码有问题，读不出来文件
    with open(r"D:/Python/WHAPI/testcase/" + yaml_name, mode='r', encoding='utf-8') as f:
        #全局加载，safe_load():安全解析函数，解析yaml文件
        value = yaml.safe_load(stream=f)
        return value
    
    
    

#检查文件是否为空
def check_and_update_yaml():  
    """  
    检查YAML文件中的数据是否不为空,如果不为空则先清空,然后写入新数据。  
      
    :param file_path: YAML文件的路径  
    :param new_data: 要写入的新数据，应为字典类型  
    """  
    # 尝试读取YAML文件内容  
    try:  
        with open(r"D:/Python/WHAPI/extract.yaml", 'r', encoding='utf-8') as file:  
            current_data = yaml.safe_load(file)  
            # 如果current_data不是None且不为空字典，则认为数据不为空  
            if current_data is not None and current_data != {}:  
                # 调用clear_yaml()方法清空文件  
                clear_yaml()  
                # 调用write_yaml()方法写入新数据  
                write_yaml()  
            else:  
                # 如果文件为空或不存在数据，则直接写入新数据  
                write_yaml()  
    except FileNotFoundError:  
        # 如果文件不存在，则直接写入新数据  
        write_yaml()  
    except yaml.YAMLError:  
        # 如果YAML文件格式错误，可以选择打印错误并退出，或者做其他处理  
        print(f"YAML文件格式错误,将尝试直接覆盖。")  
        write_yaml()   
 
 
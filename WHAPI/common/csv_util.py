import csv  
  

def read_csv(file_path):  
    """加载CSV文件并返回一个字典,键是用户名,值是一个包含其他数据的字典。"""  
    data = []  
    with open(file_path, mode='r', encoding='utf-8') as file:  
        csv_reader = csv.DictReader(file)  
        for row in csv_reader: 
            data.append(row)  
    return data
    
# file_path = ''  
# result = read_csv(file_path)    
# print(result)   
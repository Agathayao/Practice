#fixture：用于在部分用例之前或之后执行数据库操作
import pytest

from common.yaml_util import clear_yaml

@pytest.fixture(scope="function")
def exe_sql():
    print("用例之前执行")
    yield
    print("用例之后执行")

#在所有的接口请求之前执行    
@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml()  
    
    
    
import pytest
import os
import time

if __name__ == "__main__":
    pytest.main(['-vs', './WHAPI']) 
    time.sleep(3)      
    os.system('allure generate ./WHAPI/temp -o ./WHAPI/report --clean')     #清掉原有的报告重新生成一份新的报告


#coding=utf-8
import configparser

class ReadConfig:
    #定义一个读取配置文件的类
    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            #读取配置文件的绝对路径
            configpath = (r'C:\eclipse\workspace\UItest\config.ini')
        cf = configparser.ConfigParser() 
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)
        
    def get_user(self, param):
        #读取[section为UserInfo的参数]
        value = self.cf.get('登录信息', param)
        return value
    
if __name__ == '__main__':
    #运行class文件
    test = ReadConfig()
    #打印配置文件中键为user对应的值，只需修改参数（键）即可
    u = test.get_user('用户名')
    print(u)
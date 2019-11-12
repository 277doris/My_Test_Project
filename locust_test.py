# coding:utf-8
from locust import HttpLocust, TaskSet, task


class LoginTest(TaskSet):
    @task(1)  # 给task装饰器传一个参数，代表先访问首页
    def index(self):  # 首页
        self.client.get('/')
        # 发get请求

    @task(2)
    def login(self):  # 登录
        self.client.post('/user/login', {'username': 'master', 'password': '111111'})
        # 发送post请求，第一个是路径，第二个这个接口的入参，账号和密码


class User(HttpLocust):
    # 这个类继承了HttpLocust，代表每个并发里面的每个用户
    task_set = LoginTest        # 这个是每个用户都去干什么，指定了LoginTest这个类
    min_wait = 1000
    max_wait = 3000
    host = "http://192.168.1.114:18608"

'''
执行代码：
locust -f locust_test.py
'''
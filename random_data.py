from locust import HttpLocust, TaskSet, task
from random import randint


# web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    # 随机返回登录用户
    def login_user(self):
        users = {"user1": 123456, "user2": 123123, "user3": 111222}
        data = randint(1, 3)
        username = "user" + str(data)
        password = users[username]
        return username, password

    @task
    def login(self):
        username, password = UserBehavior.login_user()
        self.client.post("/user/login", {"username": username, "password": password})


class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
    host = "http://192.168.1.114:18608"
# 创建 login_user() 方法，定义登录字典 users , 通过randint 随机获取字典中的用户数据。
# 在 login() 登录任务中，调用 login_user() 方法实现 随机用户的登录。



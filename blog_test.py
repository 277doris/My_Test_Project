from locust import HttpLocust, TaskSet, task


# 定义用户行为的类：
class UserBehavior(TaskSet):

    @task(1)
    def baidu_index(self):
        self.client.get("/")


# WebsiteUser类用于设置性能测试。
class UserOne(HttpLocust):
    task_set = UserBehavior
    weight = 4
    min_wait = 3000
    max_wait = 6000


class UserTwo(HttpLocust):
    task_set = UserBehavior
    weight = 6
    stop_timeout = 5

# WebsiteUser类用于设置性能测试。
# task_set ：指向一个定义的用户行为类。
# min_wait ：执行事务之间用户等待时间的下界（单位：毫秒）。
# max_wait ：执行事务之间用户等待时间的上界（单位：毫秒）。


'''
在控制面板中，使用命令：
locust -f blog_test.py UserOne UserTwo --host=https://www.baidu.com 
-f 指定性能测试脚本文件。
--host 指定被测试应用的URL的地址，注意访问百度使用的HTTPS协议。
通过浏览器访问：http://localhost:8089（Locust启动网络监控器，默认为端口号为: 8089）
'''

'''
Number of users to simulate 设置模拟用户数。
# Hatch rate（users spawned/second） 每秒产生（启动）的虚拟用户数。
性能测试参数
Type： 请求的类型，例如GET/POST。
Name：请求的路径。这里为百度首页，即：https://www.baidu.com/
request：当前请求的数量。
fails：当前请求失败的数量。
Median：中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值。
Average：平均值，单位毫秒，所有请求的平均响应时间。
Min：请求的最小服务器响应时间，单位毫秒。
Max：请求的最大服务器响应时间，单位毫秒。
Content Size：单个请求的大小，单位字节。
reqs/sec：是每秒钟请求的个数。
'''

'''
通过 no-web 模式运行测试:
locust -f blog_test.py --host=https://www.baidu.com --no-web -c 10 -r 2 -t 1m
启动参数：

--no-web 表示不使用Web界面运行测试。
-c 设置虚拟用户数。
-r 设置每秒启动虚拟用户数。
-t 设置设置运行时间。
'''
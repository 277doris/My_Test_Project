# 由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，
# 直接选择一个比较流行的Web框架——Flask来使用。
# 用Flask编写Web App比WSGI接口简单（这不是废话么，要是比WSGI还复杂，用框架干嘛？），我们先用pip安装Flask：
# $ pip install flask
# 然后写一个app.py，处理3个URL，分别是：
# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果。
# 注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样：
from flask import Flask
from flask import request
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

# 实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。
# 除了Flask，常见的Python Web框架还有：
# Django：全能型Web框架；
# web.py：一个小巧的Web框架；
# Bottle：和Flask类似的Web框架；
# Tornado：Facebook的开源异步Web框架。
# 当然了，因为开发Python的Web框架也不是什么难事，我们后面也会讲到开发Web框架的内容。

#coding: utf8

# 从flask框架中导入Flask类
from flask import Flask,request

# 传入__name__初始化一个Flask实例
app = Flask(__name__)

# app.route装饰器映射URL和执行的函数。这个设置将根URL映射到了hello_world函数上
@app.route('/',methods=['GET','POST'])
def hello_world():
  return 'Hello World!'

@app.route('/register',methods=['POST'])
def shit():
      if request.method=='POST':
        username=request.form['name']
        print(username)
        return 'success'
      else:
         return 'failed'

@app.route('/login',methods=['POST'])
def login():
      username=request.form['name']
      print(username)
      return 'success'

if __name__ == '__main__':
# 运行本项目，host=0.0.0.0可以让其他电脑也能访问到该网站，port指定访问的端口。默认的host是127.0.0.1，port为5000
    app.run(host='192.168.137.1',port=9000)
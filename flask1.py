# -*- coding:utf-8 -*-
import flask
from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zdw20001209@localhost/lockDb'
app.config.from_pyfile("./settings.py")

db = SQLAlchemy(app)

def to_dict(self):
        return{c.name:getattr(self,c.name,None) for c in self.__table__.columns}

def jsonLoad():
        data=request.data
        j_data=json.loads(data)
        return j_data

class Admin(db.Model):
        __tablename__='admins'
        id=db.Column(db.Integer,primary_key=True)#主键
        adminName=db.Column(db.String(32),unique=True)
        password=db.Column(db.String(32))
        email = db.Column(db.String(32),unique=True)
        admins=db.relationship('History',backref="admin")#历史记录，关系引用
        #users = db.relationship('User',backref='role')
        # def __repr__(self):
        #         return'<Role:%s %s>' % (self.name ,self.id)

class Door(db.Model):
        __tablename__='doors'
        id=db.Column(db.Integer,primary_key=True)
        doorName=db.Column(db.String(32),unique=True)
        address=db.Column(db.String(32),unique=True)
        doors=db.relationship('History',backref="door")#历史记录，关系引用
        # def __repr__(self):
        #         return'<Role:%s %s %s %s>' % (self.name ,self.id,self.email,self.password)

class History(db.Model):
        __tablename__='historys'
        id=db.Column(db.Integer,primary_key=True)
        doorName=db.Column(db.String(32),db.ForeignKey('doors.doorName'))
        adminName=db.Column(db.String(32),db.ForeignKey('admins.adminName'))#外键
        right = db.Column(db.String(32))#可选，owner或者user
        charge = db.Column(db.String(32))
        
        def to_json(self):
                json_history={
                        "doorName":self.doorName,#门的名字
                        "adminName":self.adminName,
                        "right":self.right,
                        "charge":self.charge,
                        "address":self.door.address#门的蓝牙
                }
                return json_history
# door1=Door(doorName="10",address="127.0.0.1")
# db.session.add(door1)
# db.session.commit()
# admin1=Admin(adminName="zdw",password="123",email="121")
# db.session.add(admin1)
# db.session.commit()
# his1=Histoty(doorName="10",adminName="zdw",right="user")
# his2=Histoty(doorName="10",adminName="zdw",right="user")
# db.session.add_all([his1,his2])
# db.session.add(his1)
# db.session.commit()
@app.route('/')
def menu():
        return 'yes'

# #不能用
# @app.route('/login',methods=["POST"])
# def index():
#         print(request.form)
#         data=request.data
#         j_data=json.loads(data)
#         json_data=request.get_json()
#         print('request.data:',request.data)
#         #request.get_datac
#         # print('request.data.userName:',request.data.userName)
#         print('userName:',j_data['userName'])
#         print('json',json_data['userName'])
#         # print('get',request.data.get('userName'))
#         # print('values',request.values)
#         # print('get',request.form.get('userName'))
#         result_json = jsonify({"statusCode":0})
#         response=flask.make_response(result_json)
#         response.headers['Access-Control-Allow-Origin'] = '*'
#         response.headers['Access-Control-Allow-Methods'] = 'POST'
#         # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#         return response
#     return render_template('form.html')
#不能用
@app.route('/login/login',methods=["POST"])
def index2():
        if request.method == 'POST':
                print('post')
        print(request.form.get('userName'))
        return 0
#     return render_template('form.html')

#不能用
@app.route('/orders/<int:id>')
def getId(id):
        print (type(id))
        return 'id %s'%id

#不能用
@app.route('/form/222',methods=['GET','POST'])
def getForm():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('password2')
        if not all([username,password,password2]):
                print ('not enough')
        elif password!=password2:
                print ('no no no')
        else:
                print (username)
                return 'success'

#不能用
@app.route('/url',methods=['GET','POST'])
def putJson():
        t={
                'a':1,
                'b':2,
                'c':3
        }
        return jsonify(t)

# @app.route('/register',methods=['GET','POST'])
# def getJson():
#         getData=request.args
#         print(getData)
#         postData=request.form
#         print(postData)
#         username=request.form.get('name')
#         print(username)
#         return 'ok'

#注册路由
@app.route('/register',methods=['POST'])
def getAdmin():
        #接受post请求
        # j_data=jsonLoad()
        # print(j_data["name"])
        # adminName=j_data["name"]
        # password=j_data["password"]
        # email=j_data["email"]
        print('yes')
        adminName=request.form.get('name')
        password=request.form.get('password')
        email=request.form.get('email')
        print("get admin,pass,email:",adminName,password,email)
        if Admin.query.all():
                for user in Admin.query.all():
                        print("name:",user.adminName)
                        if adminName == user.adminName:
                                return 'samename'
                        elif email == user.email:
                                return 'sameemail'
        admin=Admin(adminName=adminName,password=password,email=email)
        db.session.add(admin)
        db.session.commit()
        return 'success'

#登录路由
@app.route('/login',methods=['POST'])
def checkAdmin():
        adminName=request.form.get('name')
        password=request.form.get('password')
        print("password",adminName,password)
        print("all admin",Admin.query.all())
        for user in Admin.query.all():
                if(adminName == user.adminName):
                        if(password == user.password):
                                return 'success'
                        else:
                                return 'wrongpass'
        return 'nouser'

#查询是否有这个门
@app.route('/hasdoor',methods=['POST'])
def checkDoor():
        doorName=request.form.get('name')
        address=request.form.get('address')
        print("get door name:",doorName)
        print("get address:",address)
        for door in Door.query.all():
                if(doorName == door.doorName):
                        return 'matchname'
                elif(address==door.address):
                        return 'matchaddress'
        return 'success'

#添加家庭门，用户作为管理员
@app.route('/addFdoor',methods=['POST'])
def addFdoor():
        # data=request.data
        # j_data=json.loads(data)
        # print(j_data["name"])
        # doorName=j_data["name"]
        # address=j_data["address"]
        # adminName=j_data["owner"]
        # print("get door:",doorName)
        doorName=request.form.get('name')#门的名字
        address=request.form.get('address')
        adminName=request.form.get('owner')#用户名字

        right="owner"
        print("all get:",doorName,adminName,address,right)
        door=Door(doorName=doorName,address=address)
        db.session.add(door)
        db.session.commit()
        history=History(doorName=doorName,adminName=adminName,right=right)
        db.session.add(history)
        db.session.commit()
        return 'success'

#添加公共门，用户作为管理员
@app.route('/addPdoor',methods=['POST'])
def addPdoor():
        # data=request.data#postman
        # j_data=json.loads(data)
        # print(j_data["name"])
        # doorName=j_data["name"]
        # address=j_data["address"]
        # adminName=j_data["owner"]
        # charge=j_data["money"]
        doorName=request.form.get('name')#product
        address=request.form.get('address')
        adminName=request.form.get('owner')
        charge=request.form.get('money')
        right="owner"
        print("all get:",doorName,adminName,address,right)
        door=Door(doorName=doorName,address=address)
        db.session.add(door)
        db.session.commit()
        history=History(doorName=doorName,adminName=adminName,right=right,charge=charge)
        db.session.add(history)
        db.session.commit()
        return 'success'

#查询一个用户可以开的所有门
@app.route('/adminDoor',methods=['POST'])
def searchAdminDoor():
        admin=request.form.get('name')#接受客户端的用户名
        # data=request.data#postman测试
        # j_data=json.loads(data)
        # admin=j_data["name"]
        historys=History.query.filter_by(adminName=admin).all()
        # history=history.to_dict()#转化为字典
        # history=history.__dict__
        # history=jsonify(history)
        dict1={}#json字典
        count=0#从0开始计数
        for history in historys:
                history=history.to_json()
                history=json.dumps(history)
                print(history)
                dict1[str(count)]=history
                count+=1
        print(dict1)
        dict1=jsonify(dict1)
        return dict1#返回一个json数组

#查询一个用户管理的所有门
@app.route('/adminOwnerDoor',methods=['POST'])
def searchAdminOwnerDoor():
        admin=request.form.get('name')
        # data=request.data#postman测试
        # j_data=json.loads(data)
        # admin=j_data["name"]
        historys=History.query.filter_by(adminName=admin).all()
        dict1={}
        count=0
        for history in historys:
                if(history.right=="owner"):#是否为管理者
                        history=history.to_json()
                        history=json.dumps(history)
                        dict1[str(count)]=history
                        count+=1
                        print(history)
        dict1=jsonify(dict1)
        return dict1#返回一个json数组

#添加用户为家庭门的使用者
@app.route('/addFDoorUser',methods=['POST'])
def addFDoorUser():
        # data=request.data#postman
        # j_data=json.loads(data)
        # address=j_data["address"]
        # owner=j_data["owner"]
        # member=j_data["member"]
        address=request.form.get("address")
        owner=request.form.get("owner")
        member=request.form.get("member")
        print("all get:",address,owner,member)
        door=Door.query.filter_by(address=address).first()
        user=Admin.query.filter_by(adminName=member).first()
        if(not user):
                return "nofound"
        if(not door):
                return "nofound"
        doorName=door.doorName
        print("doorname:",doorName)
        historys=History.query.filter_by(doorName=doorName).all()
        if(not historys):
                return "nofound"
        for history in historys:
                if(member==history.adminName):
                        return "already"
        historyNew=History(doorName=doorName,adminName=member,right="user")
        db.session.add(historyNew)
        db.session.commit()
        return "success"

@app.route('/deleteFDoorUser',methods=['POST'])
def deleteFDoorUser():
        return 'success'
   
@app.route('/isPDoor',methods=['POST'])
def isPDoor():
        # data=request.data#postman
        # j_data=json.loads(data)
        # address=j_data["address"]
        address=request.form.get("address")
        door=Door.query.filter_by(address=address).first()
        if(not door):
                return "nofound"
        doorName=door.doorName
        historys=History.query.filter_by(doorName=doorName)
        for history in historys:
                if(not history.charge):
                        return "family"
        return "public"

# @app.route('/addPDoorUser',methods=['POST'])
# def addDoorUser():
#         data=request.data#postman
#         j_data=json.loads(data)
#         doorName=j_data["doorName"]
#         adminName=j_data["adminname"]
#         doors=Door.query.filter_by(doorName=doorName).all()
app.debug=True
if __name__== '__main__':
        # db.drop_all()
        # db.create_all()
        # db.create_all()
        # app.run(host='192.168.137.58',port='5000')#局域网
        # app.run()#本地 
        app.run(host='192.168.137.1',port='9000')#局域网
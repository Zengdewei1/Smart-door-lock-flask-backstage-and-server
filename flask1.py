# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zdw20001209@localhost/lockDb'
app.config.from_pyfile("./settings.py")

db = SQLAlchemy(app)

def to_dict(self):
        return{c.name:getattr(self,c.name,None) for c in self.__table__.columns}

# def to_json():


class Admin(db.Model):
        __tablename__='admins'
        id=db.Column(db.Integer,primary_key=True)#主键
        adminName=db.Column(db.String(32),unique=True)
        password=db.Column(db.String(32))
        email = db.Column(db.String(32),unique=True)
        #users = db.relationship('User',backref='role')
        # def __repr__(self):
        #         return'<Role:%s %s>' % (self.name ,self.id)

class Door(db.Model):
        __tablename__='doors'
        id=db.Column(db.Integer,primary_key=True)
        doorName=db.Column(db.String(32),unique=True)
        address=db.Column(db.String(32),unique=True)
        # def __repr__(self):
        #         return'<Role:%s %s %s %s>' % (self.name ,self.id,self.email,self.password)

class History(db.Model):
        __tablename__='historys'
        id=db.Column(db.Integer,primary_key=True)
        doorName=db.Column(db.String(32),db.ForeignKey('doors.doorName'))
        adminName=db.Column(db.String(32),db.ForeignKey('admins.adminName'))#外键
        right = db.Column(db.String(32))
        charge = db.Column(db.String(32))
        def to_json(self):
                json_history={
                        'doorName':self.doorName,
                        'adminName':self.adminName,
                        'right':self.right,
                        'charge':self.charge,
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
def index():
        return 'yes'
#     return render_template('form.html')

@app.route('/orders/<int:id>')
def getId(id):
        print (type(id))
        return 'id %s'%id

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
@app.route('/register',methods=['POST'])
def getAdmin():
        adminName=request.form.get('name')
        password=request.form.get('password')
        email=request.form.get('email')
        print(adminName,password,email)
        print(Admin.query.all())
        for user in Admin.query.all():
                print('yes')
                print(user.adminName)
                if adminName == user.adminName:
                        return 'samename'
                elif email == user.email:
                        return 'sameemail'
        admin=Admin(adminName=adminName,password=password,email=email)
        db.session.add(admin)
        db.session.commit()
        return 'success'

@app.route('/login',methods=['POST'])
def checkAdmin():
        adminName=request.form.get('name')
        password=request.form.get('password')
        print(adminName,password)
        print(Admin.query.all())
        for user in Admin.query.all():
                if(adminName == user.adminName):
                        if(password == user.password):
                                return 'success'
                        else:
                                return 'wrongpass'
        return 'nouser'

@app.route('/hasdoor',methods=['POST'])
def checkDoor():
        doorName=request.form.get('name')
        address=request.form.get('address')
        print(doorName,address)
        # for door in Door.query.all():
        #         if(doorName == door.doorName):
        #                 return 'matchname'
        #         elif(address==door.address):
        #                 return 'matchaddress'
        return 'success'

@app.route('/addfdoor',methods=['POST'])
def addFdoor():
        doorName=request.form.get('name')
        address=request.form.get('address')
        adminName=request.form.get('owner')
        right='owner'
        print(doorName,adminName,address,right)
        # door=Door(doorName=doorName,address=address)
        # history=Histoty(doorName=doorName,adminName=adminName,right=right)
        # db.session.add(history)
        # db.session.add(door)
        # db.session.commit()
        return 'success'

@app.route('/addpdoor',methods=['POST'])
def addPdoor():
        doorName=request.form.get('name')
        address=request.form.get('address')
        adminName=request.form.get('owner')
        charge=request.form.get('money')
        right='owner'
        print(doorName,adminName,address,right)
        # door=Door(doorName=doorName,address=address)
        # history=Histoty(doorName=doorName,adminName=adminName,right=right,charge=charge)
        # db.session.add(history)
        # db.session.add(door)
        # db.session.commit()
        return 'success'

@app.route('/admindoor')
def searchAdminDoor():
        # admin=request.form.get('name')
        historys=History.query.filter_by(adminName="zdw").all()
        # history=history.to_dict()
        # history=history.__dict__
        # history=jsonify(history)
        list=[]
        for history in historys:
                history=history.to_json()
                print(history)
                history=jsonify(history)
                list.append(history)
                print(history.data)
        # list=jsonify(list)
        print(list[0].data)
        # print('yes')
        # return history
        return "admindoor"


if __name__== '__main__':
        # db.drop_all()
        db.create_all()
        # db.create_all()
        app.run(host='127.0.0.1')
        # app.run(host='192.168.137.1',port='9000')
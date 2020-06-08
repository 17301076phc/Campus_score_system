# coding:utf-8
from flask import Flask, render_template, request, Response
import dbfunction,dataHandle
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/activity', methods=['GET', 'POST'])
def getActivity():
    if request.method == 'GET':
        return dbfunction.getDB_Activity()
    if request.method == 'POST':
        recv_data = request.get_data()
        json_re = json.loads(recv_data)
        print(json_re['name'])
        print(json_re['sore'])
        print(json_re['descrip'])

@app.route('/transaction')
def getTransaction():
    return dataHandle.transactionHandle()

@app.route('/publish')
def getPublish():
    return dbfunction.getDB_Publish()

@app.route('/product')
def getProduct():
    return dbfunction.getDB_Product()

@app.route('/business')
def getBusiness():
    return dbfunction.getDB_Business()

@app.route('/user')
def getUser():
    return dbfunction.getDB_User()

@app.route('/admin')
def getAdmin():
    return dbfunction.getDB_Admin()

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        username = jsondata.get("username")
        password = jsondata.get("password")

        rightdata = {
            "code": 200,
            "message": 123,
            "data":
                {
                    "token": 1
                }
        }

        errordata = {
            "code": 404,
            "message": 123,
            "data":
                {
                    "token": 1
                }
        }
        if username == "admin" and password == "123456":
            return rightdata
        else:
            return errordata


@app.route('/user/info', methods=['GET', 'POST'])
def userinfor():
    if request.method == 'GET':
        data = {
            "code": 200,
            "message": 123,
            "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                     "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                     "name": "Super Admin"}
        }

        return data


# 积分申请表
@app.route('/score/applylist', methods=['GET', 'POST'])
def scoreapplist():
    if request.method == 'GET':
        db_data = dbfunction.getDB_ScoreApply()
        data = {
            "code": 200,
            "message": 1,
            "data": {
                "total": 30,
                "items": json.loads(db_data)
            }
        }

        return data

@app.route('/scoreapply/update', methods=['GET', 'POST'])
def scoreapplist_update():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        id = jsondata.get("itable_id")
        application_time = jsondata.get("application_time")
        finish_case = jsondata.get("finish_case")
        application_content = jsondata.get("application_content")
        application_material = jsondata.get("application_material")
        application_state = jsondata.get("application_state")
        note = jsondata.get("note")
        dbfunction.updateDB_ScoreApply(id, application_time, finish_case, application_content, application_material, application_state, note)

        data = {
            "code": 200,
            "message": "success update",
            "data": {}
        }

        return data

@app.route('/scoreapply/delete', methods=['GET', 'POST'])
def scoreapplist_delete():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        id = jsondata.get("itable_id")
        dbfunction.deleteDB_ScoreApply(id)

        data = {
            "code": 200,
            "message": "success delete",
            "data": {}
        }

        return data

@app.route('/scoreapply/add', methods=['GET', 'POST'])
def scoreapplist_add():
    if request.method == 'POST':
        data = request.get_data()
        jsondata = json.loads(data)
        user_id = jsondata.get("user_id")
        activity_id = jsondata.get("activity_id")
        print(activity_id)
        itable_id = jsondata.get("itable_id")
        application_time = jsondata.get("application_time")
        finish_case = jsondata.get("finish_case")
        print("finishcae="+finish_case)
        application_content = jsondata.get("application_content")
        application_material = jsondata.get("application_material")
        application_state = jsondata.get("application_state")
        note = jsondata.get("note")
        print(note)
        dbfunction.addDB_ScoreApply(user_id,activity_id,itable_id, application_time, finish_case, application_content, application_material,
                                       application_state, note)

        data = {
            "code": 200,
            "message": "success add",
            "data": {}
        }

        return data


@app.route('/test', methods=['GET', 'POST'])
def getUsers():
    if request.method == 'GET':
        db_data = dbfunction.getDB_ScoreApply()
        data = {
            "code": db_data
        }
        return data


@app.route('/image', methods=['GET', 'POST'])
def getImage():
    if request.method == 'GET':
        with open("image/image001.png", 'rb') as f:
            image = f.read()
        return Response(image, mimetype="image/jpeg")


if __name__ == '__main__':
    print('WebServer Start>>>>>>>>>')
    # app.run()
    app.run(host='0.0.0.0', port=5566)

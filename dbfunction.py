# coding:utf-8
import json
import MySQLdb
from collections import OrderedDict

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="flaskdb", port=3306, charset='utf8')

conn = db.cursor()


# 获得活动
def getDB_Activity():
    sql = "select * from activity"
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for activity in result:
        data = OrderedDict()
        data['activity_id'] = str(activity[0])
        data['activity_name'] = str(activity[1])
        data['activity_des'] = str(activity[2])
        data['activity_begintime'] = str(activity[3])
        data['activity_endtime'] = str(activity[4])
        data['sore'] = str(activity[5])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# 获得商品
def getDB_Product():
    sql = "select * from product"
    conn.execute(sql)
    result = conn.fetchall()
    #conn.close()
    jsondata = []
    for product in result:
        data = OrderedDict()
        data['p_id'] = str(product[0])
        data['admin_id'] = str(product[1])
        data['p_name'] = str(product[2])
        data['p_description'] = str(product[3])
        data['p_price'] = str(product[4])
        data['p_place'] = str(product[5])
        data['p_production_date'] = str(product[6])
        data['p_validity'] = str(product[7])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# 交易信息获取  transaction
def getDB_Transaction():
    sql = "select * from transaction "
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for transaction in result:
        data = OrderedDict()
        data['p_id'] = str(transaction[0])
        data['user_id'] = str(transaction[1])
        data['tr_id'] = str(transaction[2])
        data['tr_time'] = str(transaction[3])
        data['state'] = str(transaction[4])

        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# 积分申请表  integral_table
def getDB_ScoreApply():
    sql = "select * from integral_table "
    conn.execute(sql)
    result = conn.fetchall()
    #conn.close()
    jsondata = []
    for transaction in result:
        data = OrderedDict()
        data['user_id'] = str(transaction[0])
        data['activity_id'] = str(transaction[1])
        data['itable_id'] = str(transaction[2])
        data['application_time'] = str(transaction[3])
        data['finish_case'] = str(transaction[4])
        data['application_content'] = str(transaction[5])
        data['application_material'] = str(transaction[6])
        data['application_state'] = str(transaction[7])
        data['note'] = str(transaction[8])

        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# user
def getDB_User():
    sql = "select * from user"
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for user in result:
        data = OrderedDict()
        data['user_id'] = str(user[0])
        data['admin_id'] = str(user[1])
        data['user_name'] = str(user[2])
        data['user_password'] = str(user[3])
        data['user_major'] = str(user[4])
        data['user_class'] = str(user[5])
        data['sore'] = str(user[6])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas


# admin
def getDB_Admin():
    sql = "select * from admin"
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for admin in result:
        data = OrderedDict()
        data['admin_id'] = str(admin[0])
        data['admin_username'] = str(admin[1])
        data['admin_password'] = str(admin[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas

# business
def getDB_Business():
    sql = "select * from business"
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for bs in result:
        data = OrderedDict()
        data['bussiness_id'] = str(bs[0])
        data['admin_id'] = str(bs[1])
        data['bussiness_name'] = str(bs[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas

# publish
def getDB_Publish():
    sql = "select * from publish"
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for bs in result:
        data = OrderedDict()
        data['admin_id'] = str(bs[0])
        data['activity_id'] = str(bs[1])
        data['publish_time'] = str(bs[2])
        data['statement'] = str(bs[3])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas

# productowner_table
def getDB_ProductOwner():
    sql = "select * from productowner_table"
    conn.execute(sql)
    result = conn.fetchall()
   # conn.close()
    jsondata = []
    for bs in result:
        data = OrderedDict()
        data['p_id'] = str(bs[0])
        data['bussiness_id'] = str(bs[1])
        data['p_number'] = str(bs[2])
        jsondata.append(data)
        jsondatas = json.dumps(jsondata, ensure_ascii=False)
    return jsondatas
#conn.close()

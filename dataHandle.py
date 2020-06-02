# coding:utf-8
import json
import dbfunction
from collections import OrderedDict

cnn = dbfunction.conn
def transactionHandle():
    data = json.loads(dbfunction.getDB_Transaction())
    jsondata = []
    for jsdata in data:

        pid = jsdata["p_id"]
        uid = jsdata["user_id"]
        tr_id = jsdata["tr_id"]
        tr_time = jsdata["tr_time"]
        state = jsdata["state"]

        sqlp = "select p_name from product where p_id ="+pid
        cnn.execute(sqlp)
        resultp = cnn.fetchall()

        sqlu = "select user_name from user where user_id =" + uid
        cnn.execute(sqlu)
        resultu = cnn.fetchall()

        jdata = OrderedDict()
        jdata["p_name"] = resultp[0]
        jdata["user_name"] = resultu[0]
        jdata["tr_time"] = tr_time
        jdata["state"] = state
        jdata["sore"] = "20"
        jsondata.append(jdata)
    tr_data = json.dumps(jsondata,ensure_ascii=False)
    return tr_data


print(transactionHandle())
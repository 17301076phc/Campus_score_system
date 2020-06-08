# coding:utf-8
import json
import dbfunction
import decimal
from collections import OrderedDict


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


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

        sqlu = "select user_name from user where user_id =" + uid  #username
        cnn.execute(sqlu)
        resultu = cnn.fetchall()

        sqlsore = "select score from user where user_id =" + uid  #score
        cnn.execute(sqlsore)
        resultscore = cnn.fetchall()
        jdata = OrderedDict()
        jdata["p_name"] = str(resultp[0])
        jdata["user_name"] = str(resultu[0])
        jdata["tr_time"] = tr_time
        jdata["state"] = state
        jdata["score"] = str(resultscore[0])
        jsondata.append(jdata)
    tr_data = json.dumps(jsondata,ensure_ascii=False,cls=DecimalEncoder)
    return tr_data


#print(transactionHandle())
import pymysql
import requests

def Judgment():
    mysql = pymysql.connect(host="", user="school", password="", db="school", charset="utf8")
    con = mysql.cursor()
    sql = "SELECT * FROM main"
    con.execute(sql)
    data = con.fetchall()
    data = list(data)
    mysql.close()
    mima=data[0][2]
    url=data[0][0]
    version=data[0][1]
    content=data[0][3]
    info="软件最新版本为: "+url+"\n软件版本为: "+version+"\n软件内容为: "+content
    return info,mima


def Enquiries(key):  # 模糊查询
    text="'%{text}%'".format(text=key)
    mysql=pymysql.connect(host="",user="school",password="",db="school",charset="utf8")
    con=mysql.cursor()
    sql=r"SELECT * FROM students where name LIKE {text} or  xuehao LIKE {text} or sfz LIKE {text} or xibu LIKE {text} or zhuanye LIKE {text} or phone LIKE {text}".format(text=text)
    con.execute(sql)
    data=con.fetchall()
    data=list(data)
    mysql.close()
    return data

def url(key,num):
    mysql= pymysql.connect(host="",user="school",password="",db="school",charset="utf8")
    con = mysql.cursor()
    sql = "SELECT url FROM sgk where content='{chose}'".format(chose=key)
    con.execute(sql)
    urllist = con.fetchone()
    url = urllist[0]+num
    mysql.close()
    res=requests.get(url)
    res.encoding="utf-8"
    res=res.text
    res=dict(eval(res))
    if res["status"]==200 and key=="qq2sj":
        info="QQ为: "+res["qq"]+"\n手机号为: "+res["phone"]+"\n地址为: "+res["phonediqu"]
    elif res["status"]==200 and key=="sj2qq":
        info="QQ为: "+res["qq"]+"\n手机号为: "+res['']+"\n地址为: "+res["phonediqu"]
    elif res["status"]==200 and key=="qq2lol":
        info="QQ为: "+res["qq"]+"\nLOL昵称为: "+res["name"]+"\nLOL区服为: "+res["daqu"]
    elif res["status"]==200 and key=="lol2qq":
        info="QQ为: "+res["qq"]+"\nLOL昵称为: "+res["name"]+"\nLOL区服为: "+res["daqu"]
    elif res["status"]==200 and key=="wb2sj":
        info="微博id为: "+res["id"]+"\n手机号为: "+res["phone"]+"\n地址为: "+res["phonediqu"]+"\n微博地址为: "+"https://weibo.com/u/"+res["id"]
    elif res["status"]==200 and key=="sj2wb":
        info="微博id为: "+res["id"]+"\n手机号为: "+res["phone"]+"\n地址为: "+res["phonediqu"]+"\n微博地址为: "+"https://weibo.com/u/"+res["id"]
    elif res["status"]==200 and key=="qqlm":
        info="QQ为: "+res["qq"]+"\nQQ老密为: "+res["qqlm"]
    else:
        info="未查询到信息"
    return info


# test=Enquiries("贵露")
# test=Judgment()

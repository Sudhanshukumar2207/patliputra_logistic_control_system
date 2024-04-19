#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
t=con.cursor()
try:
    f=cgi.FieldStorage()
    d1=f.getvalue('t1')
    if (d1=='load'):
        d2=f.getvalue('t2')
        url="select distinct city from distributor_details where dipo_id='%s'"%(d2)
        t.execute(url)
        rs=t.fetchall()
        for i in rs:
            print("<option>"+i[0]+"</option>")
    else:    
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        # print(d1,d2,d3,d5,d6)
        if d5=='FTL':
            url1="select vtype,cname,lt,dipo_id from plvehicle where vtype='%s' and cname='%s' and lt='%s' and dipo_id='%s'"%(d1,d3,d5,d6)
        else:
            url1="select cname,lt,dipo_id from plvehicle where cname='%s' and lt='%s' and dipo_id='%s'"%(d3,d5,d6)
        t.execute(url1)
        res=t.fetchall()
        # print(res)
        if (res==[]):
            if d5=='FTL':
                d1=d1.upper()
            url='insert into plvehicle values(%s,%s,%s,%s,%s)'
            t.execute(url,(d1,d2,d3,d5,d6))
            con.commit()
            print('Successfully inserted')
        else:
            a=0
            print(a)
except Exception as e:
    print('Unsuccess',e)
#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
import re
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
f=cgi.FieldStorage()
try:
    a=f.getvalue('x')
    if(a=='inst'):
        dist_id=f.getvalue('t1').upper()
        dist_name=f.getvalue('t3').title()
        depot_name=f.getvalue('t2')
        cont_no=f.getvalue('t4')
        state1=f.getvalue('t6')
        addrs=f.getvalue('t7').title()
        city=f.getvalue('t8').title()
        landline_no=f.getvalue('t5')
        d9=f.getvalue('t9')
        d10=f.getvalue('t10').upper()
        d11=f.getvalue('t11')
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        a=1
        if dist_id!=d13:
            if len(dist_id)==5:
                if(re.findall("^DS[0-9][0-9][0-9]",dist_id)):
                    print("You can not enter distributor id as same pattern of auto generate!,,,",4)
                    a=0
        x.execute('select dist_id from distributor_details where dist_id="'+dist_id+'"')
        r=x.fetchall()
        if r!=[]:
            print("This Distributor ID allready Inserted, please click ok to generate new ID!,,,",2)
            a=0
        if a:
            x.execute("select gst_no from distributor_details where dipo_id='"+d9+"' and gst_no='"+d10+"'")
            res=x.fetchall()
            # print(res)
            if res==[]:
                url="insert into distributor_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                x.execute(url,(dist_id,dist_name,cont_no,depot_name,addrs,state1,city,landline_no,d9,d10,d11,d12))
                if(d13==dist_id):
                    a=int(dist_id[2:5])
                    url="update automatic1 set dist_id=%d"%(a)
                    x.execute(url)
                con.commit()
                print("Suceessfully Inserted!,,,",3)
            else:
                print("This GST no allready entered!,,,",4)
    elif(a=='auto'):
        x.execute("select dist_id from automatic1")
        rs=x.fetchall()
        rs=rs[0][0]
        rs=str(rs+1)
        if int(rs)<10:
            b='DS00'+rs
        elif int(rs)<100:
            b='DS0'+rs
        else:
            b='DS'+rs
        print(b)
    elif (a=='get'):
        d1=f.getvalue('t1')
        x.execute("select pri_name from dipo_details where dipo_id='"+d1+"'")
        rs=x.fetchall()
        print(rs[0][0])
except Exception as e:
    print("Unsuccesss",e)
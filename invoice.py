#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
t=con.cursor()
try:
    f=cgi.FieldStorage()
    d1=f.getvalue('t1')
    d2=f.getvalue('t2')
    url1='select pri_name,ope_name,distr,addr,gst from dipo_details where dipo_id="'+d1+'"'
    t.execute(url1)
    rs1=t.fetchall()
    url2='select dist_name,addrs,pin,gst_no from distributor_details where dist_id="'+d2+'"'
    t.execute(url2)
    rs2=t.fetchall()
    print(rs1[0][0],',',rs1[0][3],'</br> <b>GSTIN : </b>',rs1[0][4])
    print(',,,')
    print(rs1[0][1])
    print(',,,')
    print(rs1[0][2])
    print(',,,')
    print(rs2[0][0],',',rs2[0][1],rs2[0][2],',','</br> <b>GSTIN : </b> ',rs2[0][3])
except:
    print('Some thing is error')
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
    if (d1=='load'):
        t.execute("select dist_name,dist_id from distributor_details where dipo_id='"+d2+"'")
        res=t.fetchall()
        for i in res:
            print("<option>"+i[0]+'-'+i[1]+"</option>")
        print(',,,')
        t.execute("select trans_name,trans_id from transporter_details where dipo_id='"+d2+"'")
        res=t.fetchall()
        for i in res:
            print("<option>"+i[0]+'-'+i[1]+"</option>")
        print(',,,')
        t.execute("select distinct vtype from plvehicle where dipo_id='"+d2+"'")
        res=t.fetchall()
        for i in res:
            if (str(i[0]) !='None'):
                print("<option>"+str(i[0])+"</option>")
        print(',,,')
        t.execute("select lrno from plorder where tname is null and dipo_id='"+d2+"'")
        res=t.fetchall()
        for i in res:
            print("<option>"+str(i[0])+"</option>")
        t.execute
    elif (d1=='lr_gen'):
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d3=int(d3)
        d3=d3%100
        d3=str(d3)
        if (d4=='12' and d5=='31'):
            t.execute("select lrno from plorder order by lrno desc limit 1")
            lrno=t.fetchall()
            lrno=lrno[0][0]
            lrno=lrno.split('/')
            yy=lrno[2]
            if d3!=yy:
                t.execute('update dipo_details set auto=0')
                con.commit()
        t.execute("select auto from dipo_details where dipo_id='"+d2+"'")
        i=t.fetchall()
        i=i[0][0]
        i=str(i+1)
        x=0
        if int(i)<10:
            x='0000'+i
        elif int(i)<100:
            x='000'+i
        elif int(i)<1000:
            x='00'+i
        elif int(i)<10000:
            x='0'+i
        else:
            x=i
        lr=d2+'/'+d3+'/'+x
        print(lr)
    elif (d1=='cal'):
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getfirst('t4')
        d5=f.getvalue('t5')
        if d4=='FTL':
            url="select vprise from plvehicle where cname='%s' and vtype='%s' and lt='%s' and dipo_id='%s'"%(d2,d3,d4,d5)
        else:
            url="select vprise from plvehicle where cname='%s' and lt='%s' and dipo_id='%s'"%(d2,d4,d5)
        t.execute(url)
        res=t.fetchall()
        if res!=[]:
            print(res[0][0])
        else:
            a=0
            print(a)
    elif d1=='ds_id':
        d2=f.getvalue('t2')
        t.execute("select city,le_ex from distributor_details where dist_id='"+d2+"'")
        res=t.fetchall()
        print(res[0][0],',,,',res[0][1])
    elif d1=='preserve':
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=int(f.getvalue('t7'))
        t.execute("select lrno from plorder where lrno='"+d2+"'")
        rs=t.fetchall()
        if(rs==[]):
            url="insert into plorder (lrno,lrdate,dname,dtown,dipo_id) values('%s','%s','%s','%s','%s')"%(d2,d3,d4,d5,d6)
            t.execute(url)
            url1="update dipo_details set auto=%d where (dipo_id='%s')"%(d7,d6)
            t.execute(url1)
            con.commit()
            print('Successfuly preserve this LR No.!')
        else:
            print('This LR.No. allready present, please click ok to generate new LR!')
    elif d1=='preload':
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        t.execute("select lrdate,dname,dtown from plorder where lrno='"+d2+"' and dipo_id='"+d3+"'")
        rs=t.fetchall()
        a=rs[0][1].split('-')
        a=a[1]
        t.execute("select le_ex from distributor_details where dist_id='"+a+"' and dipo_id='"+d3+"'")
        res=t.fetchall()
        print((rs[0][0]),rs[0][1],rs[0][2],res[0][0],sep=',,')
    # elif d1=='chk1':
    #     d2=f.getvalue('t2')
    #     d3=f.getvalue('t3')
    #     t.execute("select lrno from plorder where lrno='"+d2+"' and dipo_id='"+d3+"'")
    #     res=t.fetchall()
    #     if res==[]:
    #         print(1)
    #     else:
    #         print(0)
    else:
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6').upper()
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        d9=f.getvalue('t9').upper()
        d10=f.getvalue('t10')
        d11=f.getvalue('t11')
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        d14=f.getvalue('t14')
        d15=f.getvalue('t15')
        d16=f.getvalue('t16')
        d17=f.getvalue('t17')
        d18=f.getvalue('t18')
        d19=f.getvalue('t19')
        d20=f.getvalue('t20')
        d21=f.getvalue('t21')
        pd=f.getvalue('pd')
        lr_no=f.getvalue('lr_no')
        d21=int(d21)
        d22=f.getvalue('t22')
        sta='NO'
        lr_pre=f.getvalue('lr_pre')
        if lr_pre=='no':
            t.execute("select lrno from plorder where lrno='"+d1+"'")
            rs=t.fetchall()
            if rs==[]:
                # if d1==lr_no:
                url='insert into plorder values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d22,pd,sta))
                if d1==lr_no:
                    url1="update dipo_details set auto=%d where (dipo_id='%s')"%(d21,d20)
                    t.execute(url1)
                print('Successfully inserted',',,,',5)
            else:
                print('This LR.No. allready present, please click ok to generate new LR!',',,,',2)
        else:
            url="update plorder set lrdate='%s',dname='%s',dtown='%s',tname='%s',vno='%s',vtype='%s',lt='%s',ino='%s',ivalue='%s',idate='%s',quantity='%s',weight='%s',freight='%s',le='%s',ta='%s',aa='%s',da='%s',m_ch='%s',pd='%s',status='%s' where lrno='%s'"%(d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d22,pd,sta,d1)
            t.execute(url)
            print('Successfully inserted',',,,',5)
        con.commit()
except Exception as e:
    print('Unsuccess',e)
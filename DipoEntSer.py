#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
f=cgi.FieldStorage()
def autogen(str2):
    d_id=int(str2)+1
    st=str(d_id)
    if(d_id!=1000):
        if(d_id<10):
            b="D00"+st
        elif(d_id<100):
            b="D0"+st
        elif(d_id<1000):
            b="D"+st
        print(str(d_id)+',,,')
        print(b+',,,')
    else:
        print(str(d_id)+',,,')
        print("More than 999 records not allowed!"+',,,')
d_id=0    
try:
    a=f.getvalue('x')
    if(a=='inst'):
        dp_id=f.getvalue('t1').strip()
        p_n=f.getvalue('t3').title()
        o_n=f.getvalue('t4')
        m_n=f.getvalue('t5').title()
        m_c=f.getvalue('t6')
        d_c=f.getvalue('t7')
        d_t=f.getvalue('t8')
        if(d_t==None):
            d_t=0
        stat=f.getvalue('t9')
        distr=f.getvalue('t10')
        addres=f.getvalue('t11').title()
        dd_id=int(f.getvalue('t12'))
        dcode=f.getvalue('t13').strip()
        cid=f.getvalue('t14')
        gst=f.getvalue('t15').upper()
        x.execute("select gst from dipo_details where gst='"+gst+"'")
        res=x.fetchall()
        if res==[]:
            url="select dipo_id from dipo_details where dipo_id='%s'"%(dp_id)
            x.execute(url)
            rs=x.fetchall()
            if rs==[]:
                url="insert into dipo_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                x.execute(url,(dp_id,p_n,o_n,m_n,m_c,d_c,d_t,stat,distr,addres,gst,0))
                if(dp_id==dcode):
                    url="update automatic1 set dipo_id=%s"
                    x.execute(url,(dd_id,))
                con.commit()
                print("Suceessfully Inserted!"+',,,')
                bb=0
                print(bb)
            else:
                print("Depot ID Already Present!")
        else:
            aa=5
            print(aa)
        
    elif(a=='cb1'):
        x.execute("select distinct pri_name from dipo_details")
        rs=x.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
        print(',,,')
        x.execute("select distinct distr from dipo_details")
        rs=x.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
    elif(a=='search'):
        cb1=f.getvalue('t1')
        cb2=f.getvalue('t2')
        # lst=[]
        url="select * from dipo_details where"
        if cb1!='dn':
            url=url+" pri_name='"+cb1+"'"
        if cb2!='dist' and cb1!='dn':
            url=url+" and distr='"+cb2+"'"
        if cb2!='dist' and cb1=='dn':
            url=url+" distr='"+cb2+"'"
        if cb2=='dist' and cb1=='dn':
            url="select * from dipo_details"
        # flag=False
        # if(cb1!='dn'):
        #     if flag:
        #         url=url+" and pri_name=%s"
        #     else:
        #         url=url+" pri_name=%s"
        #     flag=True
        #     lst.append(cb1)
        # if(cb2!='dist'):
        #     if flag:
        #         url=url+" and distr=%s"
        #     else:
        #         url=url+" distr=%s"
        #     flag=True
        #     lst.append(cb2)
        # if cb1==None and cb2==None:
        #     url="select * from dipo_details"
        #     flag=True
        # if flag:
        #     lst=tuple(lst)
            # x.execute(url,lst)
        # print(url)
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            print("""<table class="tab"><tr style="background-color:lightgrey;"><th>Dcode</th><th>Pri_name</th><th>Oper_name</th><th>Man_name</th><th>Man_cont</th><th>Depo_cont</th><th>Depo_tel</th><th>State</th><th>District</th><th>Address</th><th>GST No.</th><th id="th1" style="color:blue;">Tick Below</th></tr>""")
            for a in rs:
                print("<tr class='tab_r'><td class='tab_c'>"+a[0]+"  "+"</td><td class='tab_c z' contenteditable='true' id='p_n' onkeypress='keychk('#p_n','#span')'>"+str(a[1])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[2])+"  "+"</td><td class='tab_c z' contenteditable='true' id='m_n'>"+str(a[3])+"  "+"</td><td class='tab_c z' contenteditable='true' id='m_c'>"+str(a[4])+"  "+"</td><td class='tab_c z' contenteditable='true' id='d_c'>"+str(a[5])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[6])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[7])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[8])+"  "+"</td><td class='tab_c z' contenteditable='true' id='add'>"+str(a[9])+"  "+"</td><td class='tab_c z' contenteditable='true' id='add'>"+str(a[10])+"  "+"</td><td id='th1' class='tab_c'><input class='del_bt' type='radio' name='rad'></td></tr>""")
            print("""</table>""")
        else:
            a=0
            print(a)
    elif(a=='update'):
        q=f.getvalue('t1')
        w=f.getvalue('t2')
        e=f.getvalue('t3')
        r=f.getvalue('t4')
        t=f.getvalue('t5')
        y=f.getvalue('t6')
        u=f.getvalue('t7')
        i=f.getvalue('t8')
        o=f.getvalue('t9')
        p=f.getvalue('t10')
        gst=f.getvalue('t11')
        if(q==None):
            print("Please Select Any Row!")
        else:       
            url="update dipo_details set pri_name='"+w+"',ope_name='"+e+"',man_name='"+r+"',man_cont='"+t+"',dipo_cont='"+y+"',dipo_tel='"+u+"',state1='"+i+"',distr='"+o+"',addr='"+p+"',gst='"+gst+"' where dipo_id='"+q+"'"
            x.execute(url)
            con.commit()
            print("Successfully Updated!")
    elif(a=='delete'):
        dp=f.getvalue('t1')
        if(dp==None):
            print("Please Select Any Row!")
        else:
            url="delete from dipo_details where dipo_id='"+dp+"'"
            x.execute(url)
            con.commit()
            print("Successfully Deleted!")
    elif(a=='distadd'):
        dist=f.getvalue('t1')
        if(dist!='----------Select State----------'):
            url="select distr from state1 where stat='"+dist+"'"
            x.execute(url)
            rs=x.fetchall()
            rs=rs[0][0].split(',')
            for a in rs:
                print("<option>"+a+"</option>")
    else:
        x.execute("select dipo_id from automatic1")
        rs=x.fetchall()
        for a in rs:
            d_id=a[0]
        print(str(d_id)+',,,')
        autogen(d_id)
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        x.close()
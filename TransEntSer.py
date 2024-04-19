#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
f=cgi.FieldStorage()
def autogen(str2):
    t_id=int(str2)+1
    st=str(t_id)
    if(t_id!=1000):
        if(t_id<10):
            b="TR00"+st
        elif(t_id<100):
            b="TR0"+st
        elif(t_id<1000):
            b="TR"+st
        print(str(t_id)+',,,')
        print(b)
    else:
        print(str(t_id)+',,,')
        print('More than 999 records not allowed!')

try:
    a=f.getvalue('x')

    if(a=='inst'): #insert
        tid=f.getvalue('t1')
        tn=f.getvalue('t2').title()
        tc=f.getvalue('t3')
        tt=f.getvalue('t4')
        pn=f.getvalue('t5').title()
        adds=f.getvalue('t6').title()
        st=f.getvalue('t7')
        dist=f.getvalue('t8')
        bn=f.getvalue('t9')
        ahn=f.getvalue('t10')
        an=f.getvalue('t11')
        ifs=f.getvalue('t12')
        vn=f.getvalue('t13')
        tr_id=int(f.getvalue('t14'))
        dipo=f.getvalue('t15')
        x.execute("select trans_id from transporter_details where trans_id='"+tid+"'")
        rs=x.fetchall()
        if rs==[]:
            x.execute("select trans_name,prop_name from transporter_details where trans_name='"+tn+"' and prop_name='"+pn+"' and dipo_id='"+dipo+"'")
            res=x.fetchall()
            if res==[]:
                if bn!=None:
                    bn=bn.upper()
                    ahn=ahn.upper()
                    ifs=ifs.upper()
                v=(tid,tn,tc,tt,pn,adds,st,dist,bn,ahn,an,ifs,vn,dipo)
                url="insert into transporter_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                x.execute(url,v)
                url2="update automatic1 set trans_id=%s"
                x.execute(url2,(tr_id,))
                con.commit()
                print("Successfully Inserted!"+',,,')
                bb=0
                print(bb)
            else:
                aa=5
                print(aa)
        else:
             print(4)
        
        # autogen(tr_id)
    elif(a=='next'):
        tid=int(f.getvalue('t1'))
        autogen(tid)
    elif(a=='cb1'):
        d1=f.getvalue('t1')
        x.execute("select distinct trans_name from transporter_details where dipo_id='"+d1+"'")
        rs=x.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
        print(',,,')

        x.execute("select distinct distr from transporter_details where dipo_id='"+d1+"'")
        rs=x.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
        print(',,,')

        x.execute("select distinct state1 from transporter_details where dipo_id='"+d1+"'")
        rs=x.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
       
        print(',,,')
        x.execute("select distinct veh_ty from transporter_details where dipo_id='"+d1+"'")
        rs=x.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
            

    elif(a=='search'):
        cb1=f.getvalue('t1')
        cb2=f.getvalue('t2')
        cb3=f.getvalue('t3')
        cb4=f.getvalue('t4')
        d5=f.getvalue('t5')
        url="select * from transporter_details where "
        
        # flag=False
        if (cb1!=None): #for tn
                url=url+" trans_name='"+cb1+"'"
        if (cb2!=None and cb1!=None): # for dist
                url=url+" and distr='"+cb2+"'"
        if (cb2!=None and cb1==None):#for stat
                url=url+" distr='"+cb2+"'"
        if (cb3!=None and (cb2!=None or cb1!=None)):
                url=url+" and state1='"+cb3+"'"
        if (cb3!=None and cb2==None and cb1==None):
                url=url+" state1='"+cb3+"'"
        if (cb4!=None and (cb3!=None or cb2!=None or cb1!=None)):
                url=url+" and veh_ty='"+cb4+"'"
        if (cb4!=None and cb3==None and cb2==None and cb1==None):
                url=url+" veh_ty='"+cb4+"'"  
        # print(url) 
        url=url+" and dipo_id='"+d5+"'"   
        if (cb4==None and cb3==None and cb2==None and cb1==None):
            url="select * from transporter_details where dipo_id='"+d5+"'"
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            print("""<input type="button" value="Downlod" id="pr" class="b1"><input type="button" value="UPDATE" id="upt" class="b1"><input type="button" value="DELETE" id="del" class="b1"><div id="d_s"><table class="tab"><thead><tr><th class="tab_c">trans_id</th><th class="tab_c">trans_name</th><th class="tab_c">cont_no</th><th class="tab_c">land_no</th><th class="tab_c">prop_name</th><th class="tab_c">addrs</th><th class="tab_c">state1</th><th class="tab_c">distr</th><th class="tab_c">bnk_name</th><th class="tab_c">acchold_name</th><th class="tab_c">acc_no</th><th class="tab_c">ifsc</th><th class="tab_c">veh_ty</th><th id="th1" class="tab_c" style="color:blue;">Click This</th></tr></thead><tbody>""")
            for a in rs:
                print("<tr class='tab_r'><td class='tab_c z'>"+str(a[0])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[1])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[2])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[3])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[4])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[5])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[6])+"  "+"</td><td  contenteditable='true'class='tab_c z'>"+str(a[7])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[8])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[9])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[10])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[11])+"  "+"</td><td contenteditable='true' class='tab_c z'>"+str(a[12])+"  "+"</td><td id='th1'  class='tab_c'><input class='ch1' type='radio' name='rad'></td></tr>""")
            print("""</tbody></table></div>""")
        else:
            a=0
            print(a)
       

    elif a=='delete':
        cb1=f.getvalue('t1')
        if cb1==None :
            print("Please select any row!")
        else:
            url="delete from transporter_details where trans_id='"+cb1+"'; "
            x.execute(url) 
            con.commit()
            print("Successfully Deleted!")

    elif a=='update':
        cb1=f.getvalue('t1')
        cb2=f.getvalue('t2')
        cb3=f.getvalue('t3')
        cb4=f.getvalue('t4')
        cb5=f.getvalue('t5')
        cb6=f.getvalue('t6')
        cb7=f.getvalue('t7')
        cb8=f.getvalue('t8')
        cb9=f.getvalue('t9')
        cb10=f.getvalue('t10')
        cb11=f.getvalue('t11')
        cb12=f.getvalue('t12')
        cb13=f.getvalue('t13')
        v=(cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9,cb10,cb11,cb12,cb13,cb1)
        if cb1==None or  cb2==None or  cb3==None  or  cb4==None  or  cb5==None  or  cb6==None  or  cb7==None:
            print("Please select any row")
        else:
            v=(cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9,cb10,cb11,cb12,cb13,cb1)
            url="update transporter_details set trans_name=%s, cont_no=%s, land_no=%s, prop_name=%s, addrs=%s, state1=%s, distr=%s, bnk_name=%s, acchold_name=%s, acc_no=%s, ifsc=%s, veh_ty=%s where trans_id=%s"
            x.execute(url,v)
            con.commit()
            print("Successfully Updated!")

    elif(a=='distadd'):
        dist=f.getvalue('t1')
        if(dist!='----------Select State----------'):
            url="select distr from state1 where stat='"+dist+"'"
            print(url)
            x.execute(url)
            rs=x.fetchall()
            rs=rs[0][0].split(',')
            for a in rs:
               print("<option>"+a+"</option>")
    elif a=='load':
         d1=f.getvalue('t1')
         x.execute('select distinct vtype from plvehicle where dipo_id="'+d1+'"')
         rs=x.fetchall()
         for i in rs:
              if str(i[0]) !='None':
                   print('<option>'+i[0]+'</option>')
    else:
        x.execute("select trans_id from automatic1")
        rs=x.fetchall()
        for a in rs:
            t_id=a[0]
        autogen(t_id)

except Exception as ee:
    print('Unsuccess',ee)
finally:
    if con.is_connected:
        con.close()
        x.close()
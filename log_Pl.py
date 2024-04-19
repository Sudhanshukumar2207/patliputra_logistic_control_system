#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
f=cgi.FieldStorage()
try:
    t = f.getvalue('x')
    if t=='insert':
        u_id = f.getvalue('u_i')
        x.execute("select u_id from pl_sign where u_id=%s",(u_id,))
        res=x.fetchall()
        if(len(res)==0):
            # sts=f.getvalue('s')
            # r=f.getvalue('ro')
            x.execute("select u_id from pl_sign")
            rs1=x.fetchall()
            if(rs1==[]):
                r=0
                sts=1
            else:
                r=2
                sts=0
            u_name = f.getvalue('u_n')
            password = f.getvalue('pas')
            s_question = f.getvalue('s_qus')
            s_answer = f.getvalue('s_ans')
            d_id=''
            v=(sts,r,u_name,u_id,password,s_question,s_answer,d_id)
            a=x.execute("insert into pl_sign (satu,r_o_l_e,u_name,u_id,P_WORD,S_QUESTIONS,S_ANSWER,dipo_id) values(%s,%s,%s,%s,%s,%s,%s,%s)",v)
            con.commit()
            print("Successfully Inserted!")
        else:
            print("Userid already exist!")
    elif t=='search':
        x.execute("select u_id from pl_sign")
        res=x.fetchall()
        if len(res)==0:
            print("""<label class="A">WELCOME Super Admin!</label>,,,<label class="A_1">Now you can sign up</label>,,,1""")
        else:
            print(0)
    elif t=='dp_id':
        x.execute("select dipo_id,pri_name from dipo_details")
        res=x.fetchall()
        for a in res:
            print("<option>"+a[1]+"-"+a[0]+"</option>")
    elif t=='match':
        user_id=f.getvalue('u_id')
        pas=f.getvalue('p')
        x.execute("select u_name,satu,dipo_id from pl_sign where u_id=%s and BINARY p_word=%s",(user_id,pas))
        res=x.fetchall()
        if(res!=[]):
            if int(res[0][1])==0:
                print(3)
            else:
                print(res[0][0],res[0][2],user_id,pas,sep=',,,')
        else:
            print(4)
    elif t=='dash_chk':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        x.execute("select SATU,R_O_L_E from pl_sign where u_id=%s and BINARY p_word=%s",(d1,d2))
        r=x.fetchall()
        if(r==[]):
            print(0)
        else:
            print(r[0][0],r[0][1],sep=',,,')
    elif t=="show":
        x.execute("select u_id,u_name,r_o_l_e,satu from pl_sign where satu=0")
        res=x.fetchall()
        x.execute("select dipo_id,pri_name from dipo_details")
        dr=x.fetchall()
        print("""<div class="t_r" id="t_r">""")
        print("""<p class="t35">LOG IN TABLE STATUS</p>""")
        print("""<table class="table_1"><tr class="t36"><th>USER ID</th><th>USER NAME</th><th>ROLE</th><th>STATUS</th><th>DEPOT</th><th>UPDATE</th><th>DELETE</th></tr>""")
        if res!=[]:
            for r in res:
                print("<tr class='u'><td>"+r[0]+"   </td><td>"+r[1]+"   </td>")
                print("<td><select id='ro'><option value='1' selected>Admin</option><option value='2'>User</option></select></td>")
                print("<td><select id='a_i'><option value='0' selected>Inactive</option><option value='1'>Active</option></select></td>")
                print("<td id='d'><select id='dipo'><option id='op1' value='0' hidden>---Select any one---</option>")
                for a in dr:
                    print("<option>"+a[1]+"-"+a[0]+"</option>")
                print("</select></td>")
                print("<td><input type='checkbox' class='t41 up'></td><td><input type='checkbox' class='t41 dl'></td></tr>")
        else:
            print('<td colspan="6">Record Not Found</td>')
        print("</table>")
        print("""</div>""")    
    elif t=="up1":
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        d=f.getvalue('d')
        url="update pl_sign set SATU='"+str(b)+"', dipo_id='"+str(c)+"',R_O_L_E='"+str(d)+"' where U_ID='"+str(a)+"';"
        x.execute(url)
        con.commit()
        print("Records Successfilly Updated")
    elif t=="search_2":
        b=f.getvalue('b')
        c=f.getvalue('c')
        if(b):
            url="select u_name, u_id, dipo_id, satu from pl_sign where u_name=%s and satu='1'"
            x.execute(url,(b,))
            res=x.fetchall()
            print("""<div class="t_r2" id="t_r">""")
            print("""<table class='table_2 table_3'><tr class='t36'><th class="th_1">USER NAME</th><th class="th_1">USER ID</th><th class="th_1">DIPOT I'D</th><th class="th_1">STATUS</th><th class="th_1">Check</th></tr>""")
            if(res!=[]):
                for a in res:
                    print("<tr class='u2'><td>"+a[0]+"   </td><td>"+a[1]+"   </td><td class='single'>"+a[2]+"   </td>")
                    print("<td><select id='a_i'><option value='1' selected>Active</option><option value='0'>Inactive</option></select></td>")
                    print("<td><input type='checkbox' name='radio1' class='t41 r1'></td></tr>")
            else:
                print("<tr><td style='text-align: center;height:100px; font-size:25px;' colspan='5'>Records not found!</td></tr>")
            print("""</table>""")
            print("""</div>""")
        elif(c):
            url="select u_id, u_name, dipo_id, satu from pl_sign where u_id=%s and satu='1'"
            x.execute(url,(c,))
            res=x.fetchall()
            print("""<div class="t_r2" id="t_r">""")
            print("""<table class='table_2 table_3'><tr class='t36'><th>USER ID</th><th>USER NAME</th><th>DIPOT I'D</th><th>STATUS</th><th>Check</th></tr>""")
            if(res!=[]):
                for a in res:
                    print("<tr class='U2'><td>"+a[0]+"   </td><td>"+a[1]+"   </td><td class='single'>"+a[2]+"   </td>")
                    print("<td><select id='a_i'><option value='1' selected>Active</option><option value='0'>Inactive</option></select></td>")
                    print("<td><input type='checkbox' name='radio2' class='t41 r1'></td></tr>")
            else:
                print("<tr><td style='text-align: center;height:100px; font-size:25px;' colspan='5'>Records not found!</td></tr>")
            print("""</table>""")
            print("""</div>""")
    elif t=="search_3":
            url="select u_name, u_id, dipo_id, satu,R_O_L_E from pl_sign where SATU='1' and R_O_L_E='1' or R_O_L_E='2' order by s_n desc"
            x.execute(url)
            res=x.fetchall()
            print("""<div class="t_r2" id="t_r">""")
            print("""<table class='table_3'><tr class='t36'><th class="th_1">USER NAME</th><th class="th_1">USER ID</th><th class="th_1">DIPOT I'D</th><th class="th_1">STATUS</th><th class="th_1">ROLE</th></tr>""")
            if(res!=[]):
                for a in res:
                    print("<tr class='u2'><td>"+a[0]+"   </td><td>"+a[1]+"   </td><td>"+a[2]+"   </td><td>"+a[3]+"   </td><td>"+a[4]+"   </td>")
                    # print("<td><input type='checkbox' name='radio1' class='t41 r1'></td></tr>")
            else:
                print("<tr><td style='text-align: center;height:100px; font-size:25px;' colspan='5'>Records not found!</td></tr>")
            print("""</table>""")
            print("""</div>""")
    elif t=="up3":
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        d=f.getvalue('d')
        # print(a,b,c,d)
        if a=='Username':
            url="update pl_sign set satu='%s' where u_id='%s'"%(d,c)
        elif a=='UserID':
            url="update pl_sign set satu='%s' where u_id='%s'"%(d,b)
        # print(url)
        x.execute(url)
        con.commit()
        print("Successfully updated")
    elif t=='xyz':
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        e=int(f.getvalue('e'))
        x.execute("select P_WORD from pl_sign where U_ID='"+a+"' and S_QUESTIONS='"+b+"' and S_ANSWER='"+c+"' and SATU='1'")
        res=x.fetchall()
        if res==[]:
            if e==1:
                x.execute("update pl_sign set SATU='0' where U_ID='"+a+"'")
                con.commit()
            a=0
            print(a)
        else:
            a=1
            print(a)
    elif t=="f_p":
        a=f.getvalue('a')
        b=f.getvalue('b')
        c=f.getvalue('c')
        d=f.getvalue('d')
        url="update pl_sign set P_WORD='%s' where U_ID='%s' and S_QUESTIONS='%s' and S_ANSWER='%s'"%(d,a,b,c)
        x.execute(url)
        con.commit()
        print("Password Changed now you can login!")
    elif (t=='delete'):
        a=f.getvalue('a')
        x.execute("delete from pl_sign where U_ID='"+a+"'")
        con.commit()
        print('Successfully Deleted!')
except Exception as e:
    print("Data is not Inserted!",e)
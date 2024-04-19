#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
try:
    f=cgi.FieldStorage()
    d=f.getvalue('t')
    if (d=='search'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        url='select * from distributor_details where'
        if(d1!=None):
            url=url+" dist_id='"+d1+"'"
        if(d2!=None and d1!=None):
            url=url+" and dist_name='"+d2+"'"
        if(d2!=None and d1==None):
            url=url+" dist_name='"+d2+"'"
        if (d3!=None and (d1!=None or d2!=None)):
            url=url+" and city='"+d3+"'"
        if(d3!=None and d1==None and d2==None):
            url=url+" city='"+d3+"'"
        url=url+" and dipo_id='"+d4+"'"
        if(d3==None and d1==None and d2==None):
            url="select * from distributor_details where dipo_id='"+d4+"'"
        # print(url)
        x.execute(url)
        rs=x.fetchall()
        # print(rs)
        if(rs!=[]):
            print('<input type="button" value="Downlod" id="pr"><input type="button" value="Update" class="b1" id="t11"><input type="button" value="Delete" class="b2" id="t12">')
            print('<div id="d_s"><table id="t2" class="table_2"><thead><tr><th id="th" class="th">Dist_Id</th><th id="th" class="th">Dist_Name</th><th id="th" class="th">Depot_Name</th><th id="th" class="th">State</th><th id="th" class="th">City</th><th id="th" class="th">Addrs</th><th id="th" class="th">Cont_No.</th><th id="th" class="th">Landline_No</th><th id="th" class="th">GST No</th><th id="th" class="th">Labour Expense</th><th id="th" class="th">PIN Code</th><th id="th1" class="th">Check</th></tr></thead><tbody>')
            for a in rs:
                print('<tr><td class="td">'+a[0]+'   '+'</td><td contenteditable="true" id="e" class="td">'+a[1]+'   '+'</td><td class="td">'+str(a[3])+'   '+'</td><td contenteditable="true" id="e" class="td">'+a[5]+'   '+'</td><td contenteditable="true" id="e" class="td">'+a[6]+'   '+'</td><td contenteditable="true" id="e" class="td_a">'+a[4]+'   '+'</td><td contenteditable="true" id="e" class="td">'+str(a[2])+'   '+'</td><td contenteditable="true" id="e" class="td">'+str(a[7])+'   '+'</td><td contenteditable="true" id="e" class="td">'+str(a[9])+'   '+'</td><td contenteditable="true" id="e" class="td">'+str(a[10])+'   '+'</td><td contenteditable="true" id="e" class="td">'+str(a[11])+'   '+'</td><td class="td" id="th1"><input type="radio" name="z" id="ch1"></td></tr>')
            print('</tbody></table></div>')
        else:
            a=0
            print(a)
    elif d=='delete':
        a=f.getvalue('t1')   
        if a==None:
            print("Please select any row")
        else:
           x.execute("delete from distributor_details where dist_id='"+str(a)+"'")
           con.commit()
           print("Successfully deleted!")
    elif d=='update':
        a=f.getvalue('t1')  
        b=f.getvalue('t2') 
        d=f.getvalue('t4') 
        e=f.getvalue('t5') 
        g=f.getvalue('t6')
        h=f.getvalue('t7')
        i=f.getvalue('t8')  
        j=f.getvalue('t9')
        k=f.getvalue('t10')
        l=f.getvalue('t11') 
        if a==None or b==None :
            print("Please select any row")
        else:
           url="update distributor_details set cont_no='"+str(h)+"', addrs='"+str(g)+"', state1='"+str(d)+"', city='"+str(e)+"', landline_no='"+str(i)+"',gst_no='"+str(j)+"',dist_name='"+str(b)+"',le_ex='"+str(k)+"',pin='"+str(l)+"' where dist_id='"+str(a)+"'"
           x.execute(url)
           con.commit()
           print("Successfully Updated!")
    else:
        d1=f.getvalue('t2')
        x.execute("select dist_id,dist_name,city from distributor_details where dipo_id='"+d1+"' order by dist_id desc")
        res=x.fetchall()
        # a=set()
        b=set()
        c=set()
        for t in res:
            # a.add(t[0])
            b.add(t[1])
            c.add(t[2])
        for i in res:
            print("<option>"+i[0]+"</option>")
        print(',,,')
        for i in b:
            print("<option>"+i+"</option>")
        print(',,,')
        for i in c:
            print("<option>"+i+"</option>")

except:
    print("unsuccess")
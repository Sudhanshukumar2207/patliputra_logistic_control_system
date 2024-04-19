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
        url='select * from plvehicle where'
        if(d1!=None):
            url=url+" vtype='"+d1+"'"
        if(d2!=None and d1!=None):
            url=url+" and lt='"+d2+"'"
        if(d2!=None and d1==None):
            url=url+" lt='"+d2+"'"
        if (d3!=None and (d1!=None or d2!=None)):
            url=url+" and cname='"+d3+"'"
        if(d3!=None and d1==None and d2==None):
            url=url+" cname='"+d3+"'"
        url=url+" and dipo_id='"+d4+"'"
        if(d1==None and d2==None and d3==None):
            url="select * from plvehicle where dipo_id='"+d4+"'"
        # print(url)
        
        
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            print('<input type="button" value="Downlod" id="pr" class="b1"><input type="button" value="Update" class="b1" id="t11"><input type="button" value="Delete" class="b1" id="t12"><div id="d_s" class= "yesPrint"><table id="t2"><thead><tr><th id="th">Vehicle Type</th><th id="th">City Name</th><th id="th">Load Type</th><th id="th">Freight</th><th id="th1">Check</th></tr></thead><tbody>')
            for a in rs:
                print('<tr><td>'+str(a[0])+'   '+'</td><td>'+a[2]+'   '+'</td><td>'+a[3]+'   '+'</td><td contenteditable="true" id="e">'+str(a[1])+'   '+'</td><td id="th1"><input type="radio" name="a" id="ch1"></td></tr>')
            print('</tbody></table></div>')
        else:
            a=0
            print(a)
    elif d=='delete':
        a=f.getvalue('t1')  
        b=f.getvalue('t2') 
        c=f.getvalue('t3')
        d=f.getvalue('t4')   
        if a==None or b==None or c==None:
            print("Please select any row")
        else:
           if a=='None':
                x.execute("delete from plvehicle where cname='"+b+"' and lt='"+c+"' and dipo_id='"+d+"'")
           else:  
                x.execute("delete from plvehicle where vtype='"+a+"' and cname='"+b+"' and lt='"+c+"' and dipo_id='"+d+"'")
           con.commit()
           print("Successfully deleted!")
    elif d=='update':
        a=f.getvalue('t1')  
        b=f.getvalue('t2') 
        c=f.getvalue('t3') 
        d=f.getvalue('t4')   
        g=f.getvalue('t6')
        if a==None or b==None or c==None:
            print("Please select any row")
        else:
            if a=='None':
                url="update plvehicle set vprise='"+d+"' where cname='"+b+"' and lt='"+c+"' and dipo_id='"+g+"'"
            else:
                url="update plvehicle set vprise='"+d+"' where vtype='"+a+"' and cname='"+b+"' and lt='"+c+"' and dipo_id='"+g+"'"
            x.execute(url)
            con.commit()
            print("Successfully Updated!")
    else:
        d1=f.getvalue('t1')
        x.execute("select vtype,cname from plvehicle where dipo_id='"+d1+"'")
        res=x.fetchall()
        a=set();b=set()
        for t in res:
            a.add(t[0])
            b.add(t[1])
        for i in a:
            if str(i) !='None':
                print("<option>"+str(i)+"</option>")
        print(',,,')
        for i in b:
            print("<option>"+str(i)+"</option>")
except:
    print("unsuccess")
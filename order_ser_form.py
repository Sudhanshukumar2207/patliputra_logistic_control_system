#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
x=con.cursor()
try:
    f=cgi.FieldStorage()
    d=f.getvalue('t')
    if d=='search':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        url='select * from plorder where'
        if(d1!=None):
            url=url+" lrno='"+d1+"'"
        if(d2!=None and d1!=None):
            url=url+" and dname='"+d2+"'"
        if(d2!=None and d1==None):
            url=url+" dname='"+d2+"'"
        if (d3!=None and (d1!=None or d2!=None)):
            url=url+" and tname='"+d3+"'"
        if(d3!=None and d1==None and d2==None):
            url=url+" tname='"+d3+"'"
        if (d4!=None and (d1!=None or d2!=None or d3!=None)):
            url=url+" and dtown='"+d4+"'"
        if(d4!=None and d1==None and d2==None and d3==None):
            url=url+" dtown='"+d4+"'"
        if (d5!=None and (d1!=None or d2!=None or d3!=None or d4!=None)):
            url=url+" and lrdate between '"+d5+"' and '"+d6+"'"
        if(d5!=None and d1==None and d2==None and d3==None and d4==None):
            url=url+" lrdate between '"+d5+"' and '"+d6+"'"
        # print(url)
        url=url+" and dipo_id='"+d7+"'"
        x.execute(url)
        res=x.fetchall()
        if res!=[]:
            print('<input type="button" value="Downlod" id="b1" class="pr"><input type="button" value="Print Invoice" class="print" id="b1"><input type="button" value="Update" class="b1" id="b1"><input type="button" value="Delete" class="b2" id="b1"><div id="d_s"><table id="t2"><thead><tr><th id="th" class="th">LR NO.</th><th id="th3">LR Date</th><th id="th">Distributor Name</th><th id="th">Distributor Town</th><th id="th">Transporter Name</th><th id="th">Vehicle No.</th><th id="th2">Vehicle Type</th><th id="th2">Load Type</th><th id="th">Invoice no.</th><th id="th">Invoice Value</th><th id="th3">Invoice Date</th><th id="th2">Quantity</th><th id="th2">Weight</th><th id="th2">Freight</th><th id="th2">Labour Expense</th><th id="th2">Total Amount</th><th id="th2">Advance Amount</th><th id="th2">Dues Amount</th><th id="th2">Miscallaneous Charge</th><th id="th2">Product</th><th id="th2">Received</th><th id="th1">Check</th></tr></thead><tbody>')
            for a in res:
                print('<tr><td>'+str(a[0])+'   '+'</td><td>'+str(a[1])+'   '+'</td><td>'+str(a[2])+'   '+'</td><td>'+str(a[3])+'   '+'</td><td>'+str(a[4])+'   '+'</td><td>'+str(a[5])+'   '+'</td><td>'+str(a[6])+'   '+'</td><td>'+str(a[7])+'   '+'</td><td>'+str(a[8])+'   '+'</td><td>'+str(a[9])+'   '+'</td><td>'+str(a[10])+'   '+'</td><td>'+str(a[11])+'   '+'</td><td>'+str(a[12])+'   '+'</td><td>'+str(a[13])+'   '+'</td><td>'+str(a[14])+'   '+'</td><td>'+str(a[15])+'   '+'</td><td>'+str(a[16])+'   '+'</td><td>'+str(a[17])+'   '+'</td><td>'+str(a[19])+'   '+'</td><td>'+str(a[20])+'   '+'</td><td>'+str(a[21])+'   '+'</td><td id="th1"><input type="radio" name="a" id="ch1"></td></tr>')
            print('</tbody></table></div>')
        else:
            print(0)
    elif d=='delete':
        a=f.getvalue('t1')
        if a==None:
            print("Please select any row")
        else:
            x.execute("delete from plorder where lrno='"+a+"'")
            con.commit()
            print("Successfully deleted!")
    elif d=='update':
        d1=f.getvalue('t1')
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
        pd=f.getvalue('pd')
        sta=f.getvalue('sta')
        url="update plorder set lrdate='%s',dname='%s',dtown='%s',tname='%s',vno='%s',vtype='%s',lt='%s',ino='%s',ivalue='%s',idate='%s',quantity='%s',weight='%s',freight='%s',le='%s',ta='%s',aa='%s',da='%s',m_ch='%s',pd='%s',status='%s' where lrno='%s'"%(d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,pd,sta,d1)
        x.execute(url)
        con.commit()
        print('Update successfull!')
    else:
        d1=f.getvalue('t1')
        a=set()
        b=set()
        c=set()
        x.execute("select lrno,dname,tname,dtown from plorder where dipo_id='"+d1+"' order by lrno desc")
        res=x.fetchall()
        for i in res:
            a.add(i[1])
            b.add(i[2])
            c.add(i[3])
        for i in res:
            print("<option>"+i[0]+"</option>")
        print(',,,')
        for i in a:
            print("<option>"+i+"</option>")
        print(',,,')
        for i in b:
            print("<option>"+str(i)+"</option>")
        print(',,,')
        for i in c:
            print("<option>"+i+"</option>")
except:
    print("unsuccess")
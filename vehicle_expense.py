#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
t=con.cursor()
try:
    f=cgi.FieldStorage()
    d=f.getvalue('t')
    if d=='ent':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        Url='insert into veh_exp (veh_no,fuel_ty,fuel_qty,fuel_amt,toll_amt,misc_amt,tot_amt,exp_date) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        t.execute(Url,(d1,d2,d3,d4,d5,d6,d7,d8))
        con.commit()
        print('Successfilly Inserted!')
    elif d=='ent_drv':
        d1=f.getvalue('d1')
        d2=f.getvalue('d2')
        d3=f.getvalue('d3')
        d4=f.getvalue('d4')
        d5=f.getvalue('d5')
        Url='insert into drv_pay (veh_no,drv_nm,sal_mot,pay_amt,pay_date) values(%s,%s,%s,%s,%s)'
        t.execute(Url,(d1,d2,d3,d4,d5))
        con.commit()
        print('Successfilly Inserted!'+',,,'+'10')
    elif d=='ent_rep':
        d1=f.getvalue('d1')
        d2=f.getvalue('d2')
        d3=f.getvalue('d3')
        d4=f.getvalue('d4')
        Url='insert into veh_rep (veh_no,veh_part,rep_prc,rep_date) values(%s,%s,%s,%s)'
        t.execute(Url,(d1,d2,d3,d4))
        con.commit()
        print('Successfilly Inserted!'+',,,'+'10')
    elif d=='load':
        t.execute('select distinct veh_no from veh_exp')
        rs=t.fetchall()
        for i in rs:
            print('<option>'+i[0]+'</option>')
    elif d=='load_rep':
        t.execute('select distinct veh_no from veh_rep')
        rs=t.fetchall()
        for i in rs:
            print('<option>'+i[0]+'</option>')
    elif d=='load_drv':
        t.execute('select distinct veh_no from drv_pay')
        rs=t.fetchall()
        for i in rs:
            print('<option>'+i[0]+'</option>')
        print(',,,')
        t.execute('select distinct drv_nm from drv_pay')
        rs=t.fetchall()
        for i in rs:
            print('<option>'+i[0]+'</option>')
    elif d=='search':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        url='select * from veh_exp'
        if(d1!=None):
            url=url+" where veh_no='"+d1+"'"
        if(d1!=None and d2!=None):
            url=url+" and exp_date between '"+d2+"' and '"+d3+"'"
        if(d1==None and d2!=None):
            url=url+" where exp_date between '"+d2+"' and '"+d3+"'"
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            print('<br><div id="t21"><input type="button" value="Download" id="b3" class="b1"><input type="button" value="Update" id="b4" class="b1"><input type="button" value="Delete" id="b5" class="b1"></div><div id="t22"><br>')
            print('<table id="t2"><tr><th hidden>SN</th><th>Vehicle No.</th><th>Fuel Type</th><th>Fuel Qty(in ltr)</th><th>Fuel Amt.</th><th>Toll Amt.</th><th>Misc Amt.</th><th>Total</th><th>Exp Date</th><th id="th1">Check</th></tr>')
            for i in rs:
                print('<tr><td hidden>'+str(i[0])+'   '+'</td><td id="e" contenteditable="true">'+i[1]+'   '+'</td><td id="e" contenteditable="true">'+i[2]+'   '+'</td><td id="e" contenteditable="true">'+i[3]+'   '+'</td><td id="e" contenteditable="true">'+i[4]+'   '+'</td><td id="e" contenteditable="true">'+i[5]+'   '+'</td><td id="e" contenteditable="true">'+i[6]+'   '+'</td><td id="e" contenteditable="true">'+i[7]+'   '+'</td><td id="e" contenteditable="true">'+str(i[8])+'   '+'</td><td id="th1"><input type="radio" name="a" id="r"></td></tr>')
            print('</table></div>')
        else:
            print(0)
    elif d=='search_rep':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        url='select * from veh_rep' 
        if(d1!='dn' and d2!=None):
            url=url+" where veh_no='"+d1+"' and rep_date between '"+d2+"' and '"+d3+"'"
        elif(d1=='dn' and d2!=None):
            url=url+" where rep_date between '"+d2+"' and '"+d3+"'"
        elif(d1!='dn' and d2==None):
            url=url+" where veh_no='"+d1+"'"   
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            print('<br><div id="t21"><input type="button" value="Download" id="b3" class="b1"><input type="button" value="Update" id="b4" class="b1"><input type="button" value="Delete" id="b5" class="b1"></div><div id="t22"><br>')
            print('<table id="t2"><tr><th hidden>SN</th><th>Vehicle No.</th><th>Vehicle Part</th><th>Repairing Price</th><th>Repairing Date</th><th id="th1">Check</th></tr>')
            for i in rs:
                print('<tr><td hidden>'+str(i[0])+'   '+'</td><td id="e" contenteditable="true">'+i[1]+'   '+'</td><td id="e" contenteditable="true">'+i[2]+'   '+'</td><td id="e" contenteditable="true">'+i[3]+'   '+'</td><td id="e" contenteditable="true">'+str(i[4])+'   '+'</td><td id="th1"><input type="radio" name="a" id="r"></td></tr>')
            print('</table></div>')
            print(',,,')
        else:
            print("No Record Found!"+',,,'+'10')
    elif d=='search_drv':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        url='select * from drv_pay'
        if(d1!=None and d2!=None and d3!=None and d4!=None):
            url=url+" where veh_no='"+d1+"' and drv_nm='"+d2+"' and pay_date between '"+d3+"' and '"+d4+"'"
        elif(d1==None and d2==None and d3!=None and d4!=None):
            url=url+" where pay_date between '"+d3+"' and '"+d4+"'"
        elif(d1!=None and d2==None and d3!=None and d4!=None):
            url=url+" where veh_no='"+d1+"' and pay_date between '"+d3+"' and '"+d4+"'"
        elif(d1==None and d2!=None and d3!=None and d4!=None):
            url=url+" where drv_nm='"+d2+"' and pay_date between '"+d3+"' and '"+d4+"'"
        elif(d1!=None and d2!=None and d3==None and d4==None):
            url=url+" where veh_no='"+d1+"' and drv_nm='"+d2+"'"
        elif(d1!=None and d2==None and d3==None and d4==None):
            url=url+" where veh_no='"+d1+"'"
        elif(d1==None and d2!=None and d3==None and d4==None):
            url=url+" where drv_nm='"+d2+"'"   
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            print('<br><div id="t21"><input type="button" value="Download" id="b3" class="b1"><input type="button" value="Update" id="b4" class="b1"><input type="button" value="Delete" id="b5" class="b1"></div><div id="t22"><br>')
            print('<table id="t2"><tr><th hidden>SN</th><th>Vehicle No.</th><th>Driver Name</th><th>Salary Month</th><th>Payment Amount</th><th>Payment Date</th><th id="th1">Check</th></tr>')
            for i in rs:
                print('<tr><td>'+str(i[0])+'   '+'</td><td id="e" contenteditable="true">'+i[1]+'   '+'</td><td id="e" contenteditable="true">'+i[2]+'   '+'</td><td id="e" contenteditable="true">'+str(i[3])+'   '+'</td><td id="e" contenteditable="true">'+i[4]+'   '+'</td><td id="e" contenteditable="true">'+str(i[5])+'   '+'</td><td id="th1"><input type="radio" name="a" id="r"></td></tr>')
            print('</table></div>')
            print(',,,')
        else:
            print("No Record Found!"+',,,'+'10')
    elif d=='delete':
        d1=f.getvalue('t1')
        t.execute('delete from veh_exp where sn='+d1+'')
        con.commit()
        print('Successfully Deleted!')
    elif d=='delete_rep':
        d1=f.getvalue('t1')
        t.execute('delete from veh_rep where sn='+d1+'')
        con.commit()
        print('Successfully Deleted!')
    elif d=='delete_drv':
        d1=f.getvalue('t1')
        t.execute('delete from drv_pay where sn='+d1+'')
        con.commit()
        print('Successfully Deleted!')
    elif d=='update':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        d9=f.getvalue('t9')
        url="update veh_exp set veh_no='"+d2+"',fuel_ty='"+d3+"',fuel_qty='"+d4+"',fuel_amt='"+d5+"',toll_amt='"+d6+"',misc_amt='"+d7+"',tot_amt='"+d8+"',exp_date='"+d9+"' where sn="+d1+""
        t.execute(url)
        con.commit()
        print('Successfully Updated!')
    elif d=='update_rep':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        # print(d2)
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        url="update veh_rep set veh_no='"+d2+"',veh_part='"+d3+"',rep_prc='"+d4+"',rep_date='"+d5+"' where sn="+d1+""
        t.execute(url)
        con.commit()
        print('Successfully Updated!')
    elif d=='update_drv':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2').strip()
        d3=f.getvalue('t3').strip()
        d4=f.getvalue('t4').strip()
        d5=f.getvalue('t5').strip()
        d6=f.getvalue('t6').strip()
        url="update drv_pay set veh_no='"+d2+"',drv_nm='"+d3+"',sal_mot='"+d4+"',pay_amt='"+d5+"',pay_date='"+d6+"' where sn="+d1+""
        t.execute(url)
        con.commit()
        print('Successfully Updated!')
    elif d=='r_load':
        t.execute('select distinct veh_no from veh_exp union select distinct veh_no from veh_rep')
        rs=t.fetchall()
        for i in rs:
            print('<option>'+i[0]+'</option>')
    elif d=='report':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        url1="select sum(rep_prc) from veh_rep where veh_no='"+d1+"'"
        url2="select sum(fuel_amt),sum(toll_amt),sum(misc_amt) from veh_exp where veh_no='"+d1+"'"
        if d2!=None:
            url1=url1+" and rep_date between '"+d2+"' and '"+d3+"'"
            url2=url2+" and exp_date between '"+d2+"' and '"+d3+"'"
        # print(url1,'</br>',url2)
        t.execute(url1)
        r1=t.fetchall()
        if r1[0][0]==None:
            r1=0
        else:
            r1=r1[0][0]
        t.execute(url2)
        r2=t.fetchall()
        if r2[0][0]==None:
            a=0
            b=0
            c=0
        else:
            a=r2[0][0]
            b=r2[0][1]
            c=r2[0][2]
        d=r1+a+b+c
        print('<input type="button" value="Downlode" class="b1"><div id="t22"><table id="t2"><tr><th>Vehicle No.</th><th>Parts Exp</th><th>Fuel Exp</th><th>Toll Amt</th><th>Misc Amt</th><th>Total</th></tr>')
        print('<tr><td>'+d1+'</td><td>'+str(r1)+'</td><td>'+str(a)+'</td><td>'+str(b)+'</td><td>'+str(c)+'</td><td>'+str(d)+'</td></tr>')
        print('</table></div>')
except Exception as e:
    print('Unsuccess!',e)
finally:
    if con.is_connected:
        con.close()
        t.close()
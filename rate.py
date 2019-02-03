import urllib2
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import pymysql
import datetime as DT
#specify the url - I used yahoo

rate_page= "https://in.finance.yahoo.com/quote/INR=X/"

#Opening

page=urllib2.urlopen(rate_page)

#Parse

soup = BeautifulSoup(page, 'html.parser')


# Get the tag

tag= soup.find('span', attrs={'class':'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})

rate= tag.text
r=float(rate)
flag=0
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)

# Database Connection
try:
    db=pymysql.connect("localhost","root","mysql","rate")

    cursor=db.cursor()
    
    min_price="SELECT today FROM ratex WHERE today_rate=(select min(today_rate) from ratex)"

    cursor.execute(min_price)
   
    which_date=cursor.fetchall()

    for row in which_date:
        if row[0]==today:
            flag=1
    insert = "INSERT INTO ratex VALUES(%f,'%s')" % (r,today)

    cursor.execute(insert)

    delete= "DELETE FROM ratex WHERE today='%s'" % week_ago
    
    cursor.execute(delete)

    db.commit()

    db.close()
except:
    pass



#Notification
  

toaster = ToastNotifier()


if flag==1:
    toaster.show_toast("Rate Notification","Lowest Recorded Today. Rate is {}, Go to bank".format(rate))
    flag=0
else:
    toaster.show_toast("Rate Notification","Today's conversion rate is {}".format(rate))




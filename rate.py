import urllib2
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


#specify the url - I used yahoo

rate_page= "https://in.finance.yahoo.com/quote/INR=X/"

#Opening

page=urllib2.urlopen(rate_page)

#Parse

soup = BeautifulSoup(page, 'html.parser')


# Get the tag

tag= soup.find('span', attrs={'class':'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})

rate= tag.text


#Notification  

toaster = ToastNotifier()

toaster.show_toast("Rate Notification","Today's conversion rate is {}".format(rate))





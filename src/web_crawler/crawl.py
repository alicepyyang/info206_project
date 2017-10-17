import json
from bs4 import BeautifulSoup
import time 
import cPickle
from TorCtl import TorCtl
import urllib2


# library to fake the user agent docstring
from fake_useragent import UserAgent
ua = UserAgent()


# A function to request an html page from a server.
# If request is denied, it switches the IP, masks the the user agent 
# and sends the request again.
def request(url):
    def _set_urlproxy():
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
    _set_urlproxy()

    user_agent = ua.random 
    headers={'User-Agent':user_agent}
    request=urllib2.Request(url, None, headers)
    return urllib2.urlopen(request).read()
 
# Function to close the connection with the current IP and launch a new session.
def _renew_connection():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9052, passphrase="your_password")
    conn.send_signal("NEWNYM")
    conn.close()
 
data = {}
oldIP = "0.0.0.0"
newIP = "0.0.0.0"


# Check if the IP switch was succesful by pinging a random server
def renew_connection():
    global oldIP
    global newIP
    if oldIP == "0.0.0.0":
        _renew_connection()
        oldIP = request("http://icanhazip.com/")
    else:
	oldIP = request("http://icanhazip.com/")
	_renew_connection()
	newIP = request("http://icanhazip.com/")
    while oldIP == newIP:
    	newIP = request("http://icanhazip.com/")
    print request("http://icanhazip.com/")


# This function is a beautifulSoup wrapper to get recipes from a html page.
def explore_level_4(link):
	html = request(link)
	soup = BeautifulSoup(html, "lxml")
        ingredients = []	
	recipe = []
	for u in soup.findAll('li', {'class':'checkList__line'}):
		for s in u.findAll('span',{'class':'recipe-ingred_txt added'}):
			ingredients.append(s.getText())
        for u in soup.findAll('ol', {'class': 'list-numbers recipe-directions__list'}):
		for s in u.findAll('span', {'class':'recipe-directions__list--item'}):
			recipe.append(s.getText())
        data[link] = {'ing' : ingredients, 'recipe': recipe}

    # If enough data has been crawled, save it to disk.
	if(len(data.keys()) % 100 == 0):
		f = open('data.pkl','w')
		cPickle.dump(data, f)
		f.close()

# This function is a beautifulSoup wrapper to get from cuisines to recipes for a html page.
def explore_level_3(link):
	html = request(link)
	soup = BeautifulSoup(html, "lxml")
	link_list = []
	for u in soup.findAll('section',{'class' : 'grid salvattore-grid grid-fixed'}):
		for v in u.findAll('a', href=True):
			link_list.append("http://allrecipes.com/" + v['href'])
	link_list = list(set(link_list))
	for i in link_list:
		try:
			explore_level_4(i)
		except Exception as e:
			print(e)
			print(i)
			time.sleep(20);
			renew_connection()


# This function is a beautifulSoup wrapper to get from categories to cuisines for a html page.
def explore_level_2(link):
	html = request(link)
	soup = BeautifulSoup(html, "lxml")
	link_list = []
	for u in soup.findAll('div',{'class' : 'grid slider desktop-view'}):
		for v in u.findAll('a', href=True):
			link_list.append("http://allrecipes.com/" + v['href'])
	link_list = list(set(link_list))
	for i in link_list:
		try:
			explore_level_3(i)
		except Exception as e:
			print(e)
			print(i)
			time.sleep(20);
			renew_connection()

# This function is a beautifulSoup wrapper to get from the main listing to categories for a html page.
def explore_level_1(link):
	html = request(link)
	soup = BeautifulSoup(html, "lxml")
	link_list = []
	for u in soup.findAll('div',{'class' : 'hub-daughters__container'}):
		for v in u.findAll('a', href=True):
			link_list.append("http://allrecipes.com/" + v['href'])
	link_list = list(set(link_list))
	for i in link_list:
		try:
			explore_level_2(i)
		except Exception as e:
 			print(e)
			print(i)
			time.sleep(20);
			renew_connection()



# This function is a beautifulSoup wrapper to get from the home page to the listings for a html page.
def explore_main_link(link):
	html = request(link)
	soup = BeautifulSoup(html, "lxml")
	link_list = []
	for u in soup.findAll('div',{'class' : 'grid ng-hide'}):
		for v in u.findAll('a', href=True):
			link_list.append("http://allrecipes.com/" + v['href'])
	link_list = list(set(link_list))
	for i in link_list:
		try:
			explore_level_1(i)
		except Exception as e:
			print(e)
			print(i)
			time.sleep(20);
			renew_connection()


proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
explore_main_link("http://allrecipes.com/recipes/")




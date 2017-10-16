import json
from bs4 import BeautifulSoup
import time 
import cPickle
from TorCtl import TorCtl
import urllib2
 
#import socks
#import socket
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
#__originalSocket = socket.socket

from fake_useragent import UserAgent
ua = UserAgent()

 
def request(url):
    def _set_urlproxy():
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
    _set_urlproxy()

    user_agent = ua.random # 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent}
    request=urllib2.Request(url, None, headers)
    return urllib2.urlopen(request).read()
 
def _renew_connection():
    #socket.socket = __originalSocket
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9052, passphrase="your_password")
    conn.send_signal("NEWNYM")
    conn.close()
    #socket.socket = socks.socksocket
 
data = {}
oldIP = "0.0.0.0"
newIP = "0.0.0.0"


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
	if(len(data.keys()) % 100 == 0):
		f = open('data.pkl','w')
		cPickle.dump(data, f)
		f.close()

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




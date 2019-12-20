import requests
import os
from bs4 import BeautifulSoup
import bs4
global header
import time

header = {'User-Agent': 'Mozilla/5.0'}

def get_ip_soup(url):
    try:
        r=requests.get(url,timeout=20,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,"html.parser")
        #print(soup)
        return soup
    except:
        print("申请错误")

ips = []
def get_list_text(soup):
    trs=soup.find("tbody").children
    for tr in trs:
        if isinstance(tr, bs4.element.Tag):
            tds=tr("td")
            http=tds[3].string
            ip=tds[0].string
            port=tds[1].string
            true_ip=http+"://"+ip+":"+port
            ips.append(true_ip)
    return ips

def deal_with_url2(soup,url):
    index=soup.find("div",{"id":"listnav"})
    lis=index("li")
    page=lis[-2].string
    print(page)

def writeFile(dir_url,ips):
    #print(ips)
    if not os.path.exists(dir_url):
        os.mkdir(dir_url)
    path=dir_url+"\\ip_list.txt"

    with open(path,"w") as f:
        for item in ips:
            f.write(item)
            f.write("\n")

def add_page(url,num):
    url_=url+"inha/"+str(num)+"/"
    return url_

if __name__ == '__main__':
    urls=["http://www.goubanjia.com/","http://www.ip181.com/","https://www.kuaidaili.com/free/","http://www.xicidaili.com/"]
    dir_url="D:\\IP_LIST"
    #ip_soup=get_ip_soup(urls[2])
   # pages=deal_with_url2(ip_soup,urls[2])#所有页数，这里只提取前五十页
    for page in range(1,51):
        time.sleep(1)
        url_ =add_page(urls[2],page)
        print(url_)
        ip_soup = get_ip_soup(url_)
        ips=get_list_text(ip_soup)

    print("共"+len(ips)+"个")
    writeFile(dir_url,ips)
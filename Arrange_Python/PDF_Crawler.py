import requests
from htmldom import htmldom

dom = htmldom.HtmlDom("http:").createDom()
a = dom.find('a')

def pdfcraw(a):
    for link in a:
        if link.attr('href').find("pdf") > 1:
            res = requests.get("http:" + str(link.attr('href')), stream=True)
            bina = res.raw.read()
            path = "D://"+str(link.attr('href'))
            with open(path, 'wb') as f:
                f.write(bina)



if __name__=="__main__":
    pdfcraw(a)

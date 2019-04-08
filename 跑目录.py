#encoding:utf-8
import requests
import optparse
from threading import Thread

def send(url):
    statusCode = requests.get(url).status_code
    if statusCode != 404:
        print url

def main():
    parse = optparse.OptionParser('usage -u <url> -d <dictionary>')
    parse.add_option('-u',dest='url',type='string')
    parse.add_option('-d',dest='dname',type='string')
    (options,args) = parse.parse_args()
    if (options.url == None) | (options.dname == None):
        print parse.usage
        exit(0)
    else:
        url = options.url
        dname = options.dname

    lines = open(dname)
    for line in lines.readlines():
        line = line.strip()
        connurl = url+line
        t = Thread(send(connurl))
        t.start()

if __name__ == '__main__':
    main()
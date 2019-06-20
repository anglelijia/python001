import urllib.request
url = 'http://www.baidu.com'
if proxy_handle = {
    'http':'http://183.51.190.51:33913',
    'http':'http://119.191.79.46:80'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
request = urllib.request.Request(url,headers=headers)
response = opener.open(url)
print( response.read().decode('utf8'))
else：
    print('%s 错误'%url)



import urllib.request
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com'
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
for item in cookie:
print(item.name,item.value)
filename = 'tom.txt'
cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('tom.txt')
print(cookie)
##############################################
try:
    a = 100
    b = 100
    a + b
except Exception as o:
    print(o)
else:
    print('lalalala')


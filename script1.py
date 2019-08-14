import requests
from multiprocessing.dummy import Pool
import time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

url = 'http://www.sharathreddy.in/'

def req_split(r):
    start = time.time()
    req_proxy = RequestProxy()
    #print("Initialization took: {0} sec".format((time.time() - start)))
    #print("Size: {0}".format(len(req_proxy.get_proxy_list())))
    #print("ALL = {0} ".format(list(map(lambda x: x.get_address(), req_proxy.get_proxy_list()))))
    request = req_proxy.generate_proxied_request(url)
    if request is not None:
        print("\t Response: ip={0}".format(u''.join(request.text).encode('utf-8')))
        print("-> Going to sleep..")



    #requests.head is much faster than requests.get if your intention is only to get the status code
    #req = requests.get(url+str(r),headers={"teamname":"Cyber0ps"})
    #print(req.status_code) 

    #if req.status_code == 200:
     #   temp = r 
      #  print(r)#return the url string if the server report OK
    ##   temp = 0
    #return temp

data = range(0,5000)

with Pool(150) as p:
    pm = p.imap_unordered(req_split,data)
    pm = [i for i in pm if i]

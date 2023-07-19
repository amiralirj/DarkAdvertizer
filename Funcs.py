from random import choice
from asyncio import sleep
import requests



async def proxy_getter():
    resp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&anonymity=elite&ssl=all')
    #print(resp.text)
    r=str(resp.text).split('\n')
    host_url = 'https://www.example.org'
    for i in r:
        try:
            proxy=i.split(':')
            proxies={'ip':'{}'.format(proxy[0]),'port':'{}'.format(proxy[1])}      
            headers=None
            response = requests.get(host_url, headers=headers, proxies=proxies,timeout=12)
            #print(f'proxy Working {i}')
            with open('proxy.txt', 'a+') as f:
                f.write(f'{i[0:-1]}\n')
        except :
            pass
        
    await sleep(200)
    await proxy_getter()


def get_proxy():
    proxy_list=[]
    with open('proxy.txt','r') as f:
        for i in f:
            proxy_list.append(i)
    rnd=choice(proxy_list[-3:-1])
    proxy=rnd.split(':')
    proxies={'ip':'{}'.format(proxy[0]),'port':'{}'.format(proxy[1])} 
    try:
        response = requests.get('https://www.example.org', headers=None, proxies=proxies,timeout=5)  
    except:
        for i in range(10):
            #print('proxy not found ! wait ...')
            rnd=choice(proxy_list)
            proxy=rnd.split(':')
            proxies={'ip':'{}'.format(proxy[0]),'port':'{}'.format(proxy[1])}   
            try:
                response = requests.get('https://www.example.org', headers=None, proxies=proxies,timeout=5)  
                break
            except:pass       
    p=(str(rnd)).split(':')
    return  {'ip':p[0],'port':int(p[1])}



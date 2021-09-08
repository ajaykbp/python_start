import datetime
import requests


def reqMethods():
    res = requests.get('http://httpbin.org/xml')
    print(res.status_code)
    print(res.text)
    print(res.url)

    # get request
    args = {'key1': 1, 'key2': 2}
    res = requests.post('http://httpbin.org/get', params=args)
    print(res.status_code)
    print(res.text)

    # post request
    args = {'key1': 1, 'key2': 2}
    res = requests.post('http://httpbin.org/post', data=args)
    print(res.encoding)
    print(res.headers)
    res.json()

    # Auth
    user = 'theuser'
    passwd = 'thepasswd'
    res = requests.get('https://httpbin.org/basic-auth/theuser/thepass',auth=(user, passwd))
    print(res.status_code)

    #Digest Auth
    from requests.auth import HTTPDigestAuth
    user = 'theuser'
    passwd = 'thepasswd'
    res = requests.get('https://httpbin.org/digest-auth/auth/theuser/thepass', auth=HTTPDigestAuth(user, passwd))
    print(res.status_code)

    #timeout
    res = requests.post('https://httpbin.org/delay/0.5', timeout=1.0)



def main():
    print('main')
    reqMethods()

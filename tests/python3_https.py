# python3 https_client_long.py
import urllib.request
import urllib.error
import time

while True:
    try:
        response = urllib.request.urlopen('https://www.baidu.com')
        print('response headers: "%s"' % response.info())
        print('response body (100 chars): "%s"' % response.read().decode()[:100])
    except urllib.error.HTTPError as e:
        print('http error code: ', e.code)
    except urllib.error.URLError as e:
        print("can't connect, reason: ", e.reason)

    time.sleep(5)  # 5초마다 반복 요청

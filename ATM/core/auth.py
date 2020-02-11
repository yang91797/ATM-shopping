import json
import hashlib
import os,sys

from ATM.conf import settings
from ATM.libs import common
root_login = {'name': None, 'login': False}    # 记录用户是否登陆
user_login = {'name': None, 'login': False}
root_list = [['alex', '1234'], ['egon', '1234'], ['antony', 'qwer']]


def login(args1):
    def login1(func):
        def wrapper(*args, **kwargs):
            if args1 == 'root':
                if root_login['name'] and root_login['login']:
                    res = func(*args, **kwargs)
                    return

                else:
                    while True:
                        username = input('请输入用户名：').strip()
                        pwd = input('请输入密码：').strip()

                        for item in root_list:
                            if item[0] == username and item[1] == pwd:
                                print('登录成功！')
                                root_login['name'] = username
                                root_login['login'] = True
                                res = func(*args, **kwargs)
                                return

            else:
                if user_login['name'] and user_login['login']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    lock_path = settings.lock_path
                    information_path = settings.information_path
                    while True:
                        username = input('请输入用户名：').strip()
                        pwd = input('请输入密码：').strip()
                        password = common.hs(pwd)           # 哈希模块
                        res1 = common.open_file(lock_path, md='r')
                        res2 = common.open_file(information_path, md='r')
                        for i in res2:
                            if i[1].strip() == username and i[2].strip() == password:
                                for items in res1:
                                    if i[0].strip() == items[0].strip():
                                        print('该账户已冻结')
                                        return
                                else:
                                    user_login['name'] = username
                                    user_login['login'] = True
                                    print('登陆成功！')
                                    func(*args, **kwargs)
                                    return
                        else:
                            print('账户或密码错误！')
        return wrapper

    return login1

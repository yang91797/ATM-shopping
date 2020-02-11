import os
from ATM.core import auth
from ATM.conf import settings
from ATM.libs import common
from ATM.core.loggers import logger

user_path = settings.information_path           # 用户信息路径
lock_path = settings.lock_path                  # 冻结用户路径
log_path = os.path.join(settings.log_path, 'root.log')          # 日志记录路径


@auth.login('root')
def root_user():
    flag = True
    while True:
        print('''
        1. 添加账户
        2. 冻结账户
        3. 用户额度
        4. 查看日志
        5. 退出
        ''')

        choice = input('请选择相关功能：').strip()
        if choice == '1':
            user_name = input('请输入用户名：').strip()
            password1 = input('请输入密码：').strip()
            password2 = input('请再次输入密码：').strip()
            if password1 == password2:
                password = common.hs(password2)

                res = common.open_file(user_path, md='r')          # 调用打开文件的模块
                last_id = 0
                for i in res:
                    last_id = i[0]

                new_id = int(last_id)+1
                common.write_in(user_path, str(new_id), user_name, password, md='a')    # 调用写入文件模块

                account_path = os.path.join(settings.accounts_path, '%s.json') % str(new_id)  # 账户额度路径
                common.write_in(account_path, '0', md='w')
                logger(auth.root_login['name'], log_path,).debug('添加账户:%s' % user_name)             # 调用日志模块
                print('已添加账户：', user_name)

            else:
                print('两次密码不一致！')

        elif choice == '2':
            user_id = []
            res = common.open_file(user_path, db='r', md='r')
            for i in res:
                print('ID:', i[0], 'name:', i[1])
                user_id.append(i[0])
            lock_id = input('请输入冻结账户的ID:').strip()
            if lock_id in user_id:
                with open(lock_path, mode='r', encoding='utf-8') as f:
                    data = f.read()
                if lock_id in data:         # 检验账户是否已冻结
                    print('该账户已冻结！')
                else:
                    common.write_in(lock_path, lock_id, md='a')
                    print('已冻结该账户！')

                logger(auth.root_login['name'], log_path,).debug('冻结账户:%s' % lock_id)

            else:
                print('不存在该账户')

        elif choice == '3':
            print('''
            1. 查看额度
            2. 增加额度 
            ''')
            option = input('请输入：').strip()
            if option == '1':
                res = common.open_file(user_path, md='r')
                for i in res:
                    path = os.path.join(settings.accounts_path, '%s.json') % i[0]
                    result = common.open_file(path, md='r')
                    for item in result:
                        print('ID:', i[0], 'name:', i[1], '余额:', item[0])
                logger(auth.root_login['name'], log_path,).debug('查看用户额度')

            elif option == '2':
                name_money = input('请输入要增加额度的用户ID:').strip()
                res = common.open_file(user_path, md='r')
                for i in res:
                    path = os.path.join(settings.accounts_path, '%s.json') % i[0]
                    if name_money == i[0]:
                        money = input('请输入金额：').strip()
                        if money.isdigit():
                            with open(path, mode='r', encoding='utf-8') as f:
                                user_m = f.read()
                            money = float(money) + float(user_m)
                            common.write_in(path, str(money), md='w')
                            logger(auth.root_login['name'], log_path).debug('增加ID为:%s的额度  增加金额：%s' % (name_money, money))
                            print('已成功增加额度')
                            flag = False
                if flag:
                    logger(auth.root_login['name'], log_path, ).warning('增加用户额度ID不存在')
                    print('ID不存在')

            else:
                print('请输入正确选项')

        elif choice == '4':
            print('''
            1. 查看管理员日志
            2. 查看普通用户日志
            ''')
            choice4 = input('请输入:').strip()
            if choice4 == '1':
                look_log = log_path
                logger(auth.root_login['name'], log_path).debug('查看root日志')

            if choice4 == '2':
                res = common.open_file(user_path, md='r')
                for i in res:
                    print('用户ID:', i[0], 'name:', i[1])
                user_id1 = input('请输入要查看用户的ID:').strip()
                look_log = os.path.join(settings.log_path, '%s.log') % user_id1  # 日志路径
                logger(auth.root_login['name'], log_path).debug('查看 %s 日志' % user_id1)
            try:
                with open(look_log, mode='r', encoding='gbk') as f:
                    for line in f:
                        print(line)
            except FileNotFoundError:
                print('该用户还没有日志记录')

        elif choice == '5':
            return

        else:
            print('请重新选择')


import os

from ATM.core import auth
from ATM.core import transaction
from shopping_mall.shopping import shop_module
from ATM.libs import common
from ATM.conf import settings


@auth.login('user')
def user_main():
    user_name = auth.user_login['name']
    res = common.open_file(settings.information_path, md='r')
    for i in res:
        if i[1] == user_name:
            user_id = i[0]

    while True:
        print('''
        1. 购物
        2. 提现
        3. 转账
        4. 还款
        5. 查看日志
        6. 退出
        ''')

        choice = input('请选择：').strip()

        if choice == '1':
            shop_module(user_id)

        elif choice == '2':
            transaction.withdrawal(user_id)

        elif choice == '3':
            transaction.transfer(user_id)

        elif choice == '4':
            transaction.repayment(user_id)

        elif choice == '5':
            log_path = os.path.join(settings.log_path, '%s.log') % user_id  # 日志路径
            try:
                with open(log_path, mode='r', encoding='gbk') as f:
                    for line in f:
                        print(line)
            except FileNotFoundError:
                print('你还没有日志记录噢')

        elif choice == '6':
            return

        else:
            print('无此选项')
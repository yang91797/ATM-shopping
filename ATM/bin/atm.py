import os, sys
import manage
from ATM.core.main import user_main
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
# print(sys.path)


def start():
    while True:
        print('''
        1. 普通用户
        2. 管理员
        3. 退出
        ''')

        choice = input('请输入对应的选项：').strip()
        if choice == '1':
            user_main()
        if choice == '2':
            manage.root_user()

        if choice == '3':
            return


start()

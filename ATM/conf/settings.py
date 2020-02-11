import os, sys

accounts_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'accounts')
information_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db',
                                'user_information.txt')
lock_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'lock_user.txt')
goods_history_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'goods_history')

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')

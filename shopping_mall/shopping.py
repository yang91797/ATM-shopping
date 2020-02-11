import os
import json
from ATM.conf import settings
from ATM.libs import common
from ATM.core.loggers import logger


def shop_module(user_id):

    gh_path = os.path.join(settings.goods_history_path, '%s.json') % user_id
    account_path = os.path.join(settings.accounts_path, '%s.json') % user_id
    log_path = os.path.join(settings.log_path, '%s.log') % user_id
    with open(account_path, mode='r', encoding='utf-8') as f:           # 读取余额
        money = f.read().strip()
    goods = [
                {"name": "电脑", "price": 1999},
                {"name": "鼠标", "price": 10},
                {"name": "游艇", "price": 200000},
                {"name": "美女", "price": 998},

    ]

    goods_dic = {}                          # 购物车
    goods_history = {}
    print('当前余额：\033[1;33;1m', money, '\033[0m')
    try:
        with open(gh_path, mode='r', encoding='utf-8') as f:
            goods_history = json.loads(f.read().strip())

        if goods_history:  # 打印历史消费记录
            consume = 0
            print('\033[1;32;1m历史购物信息\033[0m')
            for key in goods_history:
                consume += int(goods_history[key][0]) * int(goods_history[key][1])
                print('商品名称：\033[1;32;1m', key, '\033[0m数量：\033[1;32;1m', goods_history[key][1], '\033[0m')
            print('总消费:', consume)
    except FileNotFoundError:
        print('你还没有消费记录噢')

    while True:

        print('''
    按b结束购买
---------------------
编号      商品      价格
            ''')
        for item in goods:
            print('%s      %s         %s' %(goods.index(item), item['name'], item['price']))
        print('''
---------------------
            ''')

        choice = input('请输入购买商品的编号》'.strip())

        good_id = [choice for item in goods if choice.isdigit() and goods.index(item) == int(choice)]   # 检查是否存在该商品
        if good_id:
            choice = int(choice)

            if goods[choice]['name'] in goods_dic:
                goods_dic[goods[choice]['name']][1] += 1
            else:
                goods_dic[goods[choice]['name']] = [goods[choice]['price'], 1]

            if goods[choice]['name'] in goods_history:          # 历史购物车加入数据
                goods_history[goods[choice]['name']][1] += 1
            else:
                goods_history[goods[choice]['name']] = [goods[choice]['price'], 1]

            print('已购买商品：%s' % goods[choice]['name'])

        elif choice == 'b':  # 购买结束

            if goods_dic:
                money_sum = 0

                print('\033[1;32;1m已购买商品\033[0m')
                for key in goods_dic:
                    money_sum += int(goods_dic[key][0]) * int(goods_dic[key][1])
                    money = str(float(money) - money_sum)
                    print('商品名称：\033[1;32;1m', key, '\033[0m数量：\033[1;32;1m', goods_dic[key][1], '\033[0m')

                print('''
                      \033[1;32;1m消费总金额：%s\033[0m
                      \033[1;35;1m余额：%s\033[0m
                      ''' % (money_sum, money))
                common.write_in(gh_path, json.dumps(goods_history), md='w')
                common.write_in(account_path, money, md='w')
                print(goods_dic)
                logger(user_id, log_path).debug(goods_dic)
                if float(money) < 0:
                    print('\033[31;1m已透支，请尽快还款\033[0m')
                return
            else:
                print('未购买任何商品噢')
                return

        else:
            print('请重新选择')

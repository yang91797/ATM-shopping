import os

from ATM.conf import settings
from ATM.libs import common
from ATM.core.loggers import logger


def withdrawal(user_id):
    '''取款'''

    account_path = os.path.join(settings.accounts_path, '%s.json') % user_id  # 账户路径
    with open(account_path, mode='r', encoding='utf-8') as f:           # 读取余额
        money = f.read().strip()
    print('\033[32;1m账户余额：\033[0m', '\033[35;1m', money, '\033[0m')
    wd_money = input('请输入提现金额：').strip()
    if wd_money.isdigit():
        money = str(float(money)-float(wd_money)-float(wd_money)*0.05)            # 提现手续费5%
        common.write_in(account_path, money, md='w')
        log_path = os.path.join(settings.log_path, '%s.log') % user_id
        logger(user_id, log_path).debug('取款: %s  余额：%s' % (wd_money, money))      # 写入日志
        print('已取款：', wd_money, '手续费:', int(wd_money)*0.05, '\n', '余额：', money)


def repayment(user_id):
    '''还款'''
    log_path = os.path.join(settings.log_path, '%s.log') % user_id      # 日志路径
    account_path = os.path.join(settings.accounts_path, '%s.json') % user_id        # 账户路径
    with open(account_path, mode='r', encoding='utf-8') as f:           # 读取余额
        money = f.read().strip()
    if float(money) < 0:
        print('应还金额：', money)
        repay = input('请输入还款金额：').strip()
        if repay.isdigit():
            money = str(float(money)+float(repay))
            common.write_in(account_path, money, md='w')
            logger(user_id, log_path).debug('还款：%s  余额：%s' % (repay, money))
            print('已还款：', repay)
    else:
        print('你还没有要还的款项噢')


def transfer(user_id):
    '''转账'''

    other_id_list = []
    log_path = os.path.join(settings.log_path, '%s.log') % user_id  # 日志路径
    account_path = os.path.join(settings.accounts_path, '%s.json') % user_id  # 账户路径
    with open(account_path, mode='r', encoding='utf-8') as f:           # 读取余额
        money = f.read().strip()

    print('账户余额:', money)
    res = common.open_file(settings.information_path, md='r')

    for i in res:
        if i[0] != user_id:
            print('ID', i[0], 'name:', i[1])
            other_id_list.append(i[0])
    other_id = input('请输入转账用户的ID:').strip()

    if other_id in other_id_list:
        tra_money = input('请输入转账金额：').strip()

        if tra_money.isdigit():
            money = str(float(money)-float(tra_money))
            other_path = os.path.join(settings.accounts_path, '%s.json') % other_id  # 转账路径
            other_log = os.path.join(settings.log_path, '%s.log') % other_id

            with open(other_path, mode='r', encoding='utf-8') as f:
                other_money = f.read().strip()
            other_money = str(float(other_money)+float(tra_money))
            common.write_in(account_path, money, md='w')
            common.write_in(other_path, other_money, md='w')
            logger(user_id, log_path).debug(('转账：%s 对方ID:%s' % (tra_money, other_id)))
            logger(other_id, other_log).debug(('收到 %s 转账 %s' % (user_id, tra_money)))
            print('转账成功', '余额：', money)






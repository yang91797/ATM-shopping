## 模拟实现ATM + 购物商城程序
### 功能实现：
1. 用户额度 1500或自定义
2. 实现购物商城，买东西加入 购物车，调用信用卡功能进行结账
3. 可以提现，手续费5%
4. 支持多账户登录
5. 支持账户间转账（用户A转账给用户B，A账户减钱、B账户加钱）
6. 记录每月日常消费流水
7. 提供还款功能
8. ATM记录操作日志（使用logging模块记录日志）
9. 提供管理功能，包括添加账户、用户额度，冻结账户等
10. 用户认证使用用装饰器


### 相关功能目录
启动程序：ATM/bin/atm.py

管理员相关程序：ATM/bin/manage.py

配置文件：ATM/conf/settings.py

普通用户逻辑程序：ATM/core/main.py

认证模块：ATM/core/auth.py

日志模块：ATM/core/loggers.py

与账户相关的模块：ATM/core/transaction.py

账户数据：ATM/db/accounts

购物历史:ATM/db/goods_history

冻结账户：ATM/db/lock_user.txt

用户信息：ATM/db/user_information.txt

自定义模块：ATM/libs/common.py

购物车程序：shopping_mall/shopping.py

### 初始数据
用户名以及密码

管理员：['alex', '1234'], ['egon', '1234'], ['antony', 'qwer']

普通用户：['alex', '1234'], ['egon', 'qwer'], ['antony', '1234'],['esmail','1234'],['Draven','asdf']


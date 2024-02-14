# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116
A: `python -m venv .venv`
[From official docs](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

## Q: python-dotenv 如何使用？ #119
兩種情況

### 情況 1：已經使用 flask 框架

A：完全不需要做任何事，只要有 .env 檔 flask 就會自動讀取環境變數

[Source code](https://github.com/pallets/flask/blob/0c0b31a789f8bfeadcbcf49d1fb38a00624b3065/src/flask/cli.py#L632-L649)

### 情況 2：專案沒有任何套件用到 python-dotenv

#### Step 1: 安裝 python-dotenv
```bash
pip install python-dotenv
```

#### Step 2: 建立一個 .env 檔

例如：
.env
```
DOMAIN=example.com
```

#### Step 3: 匯入 load_dotenv、os 並使用
```python
import os
from dotenv import load_dotenv

load_dotenv()  # load enviroment variables from .env (從 .env 載入環境變數)

print(os.getenv('DOMAIN'))  # print example.com
# use os.getenv('variable_name') to access value (透過 os.getenv('變數名稱') 取得環境變數的值)
```


## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123
### Step 1: 安裝 PyMySQL
```bash
pip install PyMySQL
```

### Step 2: 修改 config

> Note：若沒有建立資料庫，請先建立資料庫

原先的 config
```python
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
```
按照下列格式修改：

`"mysql+pymysql://<MySQL 使用者名稱>:<使用者密碼>@localhost:3306/<資料庫名稱>"`

> 注意使用者名稱和密碼以及資料庫名稱是否正確，否則會錯誤或拒絕連接

變成
```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/db"
```

到這裡已經能夠連接 MySQL 了

直接 flask run，若順利執行就是成功

### 進一步：同步資料庫

在有建立 migration 的情況下

可以直接 flask db upgrade

成功的話會看到下列訊息

```
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
```

> P.S. 中途可能會出現訊息說缺少某些套件，就補安裝就好了

例如我在 flask db upgrade 的時候遇到下列訊息

```
ERROR [flask_migrate] Error: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods
```

就直接 `pip install cryptography`，解決！

[Reference](https://medium.com/seaniap/python-web-flask-flask-sqlalchemy%E6%93%8D%E4%BD%9Cmysql%E8%B3%87%E6%96%99%E5%BA%AB-2a799acdec4c)

> 後記：還有看到有人用 `mysql-connector-python`，有空可以玩玩看差別

例如：[Connect MySQL to sqlAlchemy In python](https://ankushkunwar7777.medium.com/connect-mysql-to-sqlalchemy-in-python-b94c34568818)

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129
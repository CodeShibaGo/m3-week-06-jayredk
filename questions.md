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

### Step 1: 安裝 Flask-Migrate
```bash
pip install Flask-Migrate
```

### Step 2: 在 flask 中使用 Flask-Migrate
> Note: 請先建立好 Model 以及連線資料庫的設定

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

### Step 3: 創建 migration repository
```bash
flask db init
```

### Step 4: 建立 migration 版本
```bash
flask db migrate -m "輸入版本訊息"
```

### Step 5: 套用最新的 migration 版本
```bash
flask db upgrade
```


### 常用指令
- `flask db init`: 創建 migration repository
- `flask db migrate -m <message>`: 建立新的 migration 版本
- `flask db history`: 查看所有 migration 版本
- `flask db current`: 查看目前 migration 版本
- `flask db upgrade`: 升級至最新版本
- `flask db upgrade <revision>`: 升級至特定版本
- `flask db downgrade <revision>`: 退回特定版本
- `flask db –help`: 查詢相關指令


> 後記: 其實概念跟 git 差不多

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125
> Note: 這裡假設 SQLAlchemy 已經連接資料庫並設定完畢

那麼你會有
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
```

準備好就開始了

### Step 1: 從 sqlalchemy 匯入 text
```python
#...

from sqlalchemy import text
```

### Step 2: 使用 Raw SQL 進行 Query
```python
def get_user():
    query = text('SELECT * FROM User') # 這裡可以代入需要的 Raw SQL 語句
    res = db.session.execute(query).fetchall()  # 會 return CursorResult object，要用 fetchall 轉換所有資料

    for item in res:
        print(item)  # 印出每個 row
```
Reference:
- [basic-usage - sqlalchemy docs](https://docs.sqlalchemy.org/en/20/core/connections.html#basic-usage)
- [Query the data - Flask-SQLAlchemy docs](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#query-the-data)
- ChatGPT（問了大概 3 次才正確）

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129
# Questions

## Q: 使用 `virtualenv` 建立虛擬環境 #116
A: `python -m venv .venv`
[From official docs](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

## Q: python-dotenv 如何使用？ #119
兩種情況

情況 1：已經使用 flask 框架

A：完全不需要做任何事，只要有 .env 檔 flask 就會自動讀取環境變數

[Source code](https://github.com/pallets/flask/blob/0c0b31a789f8bfeadcbcf49d1fb38a00624b3065/src/flask/cli.py#L632-L649)

情況 2：專案沒有任何套件用到 python-dotenv

Step 1: 安裝 python-dotenv
```bash
pip install python-dotenv
```

Step 2: 建立一個 .env 檔

例如：
.env
```
DOMAIN=example.com
```

Step 3: 匯入 load_dotenv、os 並使用
```python
import os
from dotenv import load_dotenv

load_dotenv()  # load enviroment variables from .env (從 .env 載入環境變數)

print(os.getenv('DOMAIN'))  # print example.com
# use os.getenv('variable_name') to access value (透過 os.getenv('變數名稱') 取得環境變數的值)
```


## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129
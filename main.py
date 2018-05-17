import requests
from time import gmtime, strftime, sleep
import sqlite3
from datetime import datetime

db = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cur = db.cursor()
# Создание таблицы
cur.execute("""DROP TABLE IF EXISTS time""")
cur.execute("""CREATE TABLE time (time text)""")
db.commit()
cur.close()

_list = []
counter = 0

while True:
    if counter < 100:
        sleep(30)
        try:
            r = requests.get('https://pos-stg01.shtrih-cloud.ru')
            if r.status_code == 200:
                pass
            else:
                _list.append(tuple(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                counter = counter + 1
                print(counter)
        except:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S'), # создаем кортеж из одного элемента
            _list.append(tuple(now))
            counter = counter + 1
            print(counter)
    else:
        db = sqlite3.connect("mydatabase.db")
        cur = db.cursor()
        cur.executemany("""INSERT INTO time VALUES(?)""", _list)
        db.commit()
        cur.close()
        counter = 0

'''
while counter < 9:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    _list.append(tuple(now))
    counter = counter + 1

print(_list)
db = sqlite3.connect("mydatabase.db")
cur = db.cursor()
cur.executemany("""INSERT INTO time VALUES(?)""", _list)
db.commit()
cur.close()
'''

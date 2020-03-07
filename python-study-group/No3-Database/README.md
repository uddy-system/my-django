# 初期設定
## docker-compose起動
```
$ git clone https://github.com/grant-hope/python-study-group.git
$ cd python-study-group/No3-Database/
$ docker-compose up -d
```

## 実行用テーブル準備
1. docker-compose内MySQLにログイン
    ```
    $ docker-compose exec db bash
    # mysql -u root -p
    Enter password: password
    ```
1. 実行用テーブル作成
    ```
    mysql> create database python_test;
    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | python_test        |
    | sys                |
    +--------------------+
    5 rows in set (0.02 sec)
    ```
1. docker-compose内MySQLからログアウト
    ```
    mysql> exit
    # exit
    ```

# 実行確認
```
$ python mysql_test.py
insert into python_test_table(id, dttm) values(1, "2020-01-14 22:19:38.360598")
insert into python_test_table(id, dttm) values(1, "2020-01-14 22:19:38.360598")
(0, '2020-01-14 22:19:38.360598')
(1, '2020-01-14 22:19:38.360598')
```

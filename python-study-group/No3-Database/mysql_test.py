import mysql.connector
from datetime import datetime

# DB接続設定
conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='password',
    database='python_test',
)
conn.ping(reconnect=True)
cur = conn.cursor(buffered=True)
print('Auto commit mode: %s' % str(conn.autocommit))

try:
    table_name = 'python_test_table'

    # テスト用テーブル作成（既に有る場合何もしない）
    cur.execute(
        '''
        create table if not exists {table} (
            id int,
            dttm text
        )
        '''.format(table=table_name)
    )

    # 現在のデータ数を取得
    cur.execute('select * from %s' % table_name)
    row_num = len(cur.fetchall())

    now = datetime.now()

    # 「id=0」のデータのdttmを実行時刻にする
    if row_num == 0:
        sql = 'insert into {table}(id, dttm) values(0, "{dttm}")'.format(table=table_name, dttm=str(now))
        row_num = 1
    else:
        sql = 'update {table} set dttm="{dttm}" where id=0'.format(table=table_name, dttm=str(now))
    print(sql)
    cur.execute(sql)

    # 新規データ追加
    sql = 'insert into {table}(id, dttm) values({id}, "{dttm}")'.format(table=table_name, id=row_num, dttm=str(now))
    print(sql)
    cur.execute(sql)

    # 全データを取得して表示
    cur.execute('select * from %s' % table_name)
    for row in cur.fetchall():
        print(row)

    # 変更をDBに反映
    conn.commit()

except Exception as e:
    conn.rollback()
    raise e

finally:
    cur.close()
    conn.close()


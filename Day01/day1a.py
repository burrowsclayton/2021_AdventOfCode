
import pandas as pd
import sqlite3 as sqlite

'''
(1) Read and index depths using a convenient CSV reader
(2) Write CSV to sqlite
(3) Query sqlite table for answer
'''

stmnt = """
select
    sum(  
        case 
           when d1.depth < d2.depth then 1
           else 0
           end
        ) bool_sum
from day1a d1
left join day1a d2 on d1.idx = (d2.idx - 1)
"""

df = pd.read_csv('input_day1a.txt', names=['depth'])

df['idx'] = list(range(len(df)))

with sqlite.connect('proj.db') as con:
    cur = con.cursor()

    df.to_sql('day1a', con, if_exists='replace')

    answer = cur.execute(stmnt).fetchall()

print(answer[0][0])

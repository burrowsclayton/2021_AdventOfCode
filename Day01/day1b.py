
import sqlite3 as sqlite

'''
(1) Create a convenient view to easily access each rows sliding window
(2) Modify the query from `day1a.py` to query the sliding window view
(3) Display the answer
'''

with sqlite.connect('proj.db') as con:

    cur = con.cursor()

    cur.execute('drop view if exists day1b_3_sliding_window')

    cur.execute('''
create view day1b_3_sliding_window as
select
      d1.idx
    , d1.depth as depth1
    , d2.depth as depth2
    , d3.depth as depth3
    , d1.depth + d2.depth + d3.depth as depth_sum
from day1a d1
left join day1a d2 on d1.idx = (d2.idx - 1)
left join day1a d3 on d1.idx = (d3.idx - 2)
    ''')

    con.commit()

    rows = cur.execute('''
select
    sum(  
        case 
           when d1.depth_sum < d2.depth_sum then 1
           else 0
           end
        ) bool_sum
from day1b_3_sliding_window d1
left join day1b_3_sliding_window d2 on d1.idx = (d2.idx - 1)
    ''').fetchall()

print(rows)

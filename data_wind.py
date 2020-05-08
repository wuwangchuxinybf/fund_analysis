
# import WindPy  as wp
# import pandas as pd
#
# data = wp.w.wsd("110011.OF", "nav,NAV_adjfactor,NAV_acc,peer_fund_return_rank_per", "2020-03-21", "2020-04-19", "fundType=1")
# data_df = pd.DataFrame()



import psycopg2
import pandas as pd
import numpy as np
con = psycopg2.connect(database="highdb", user="postgres", password="pg@123", host="10.21.26.101", port="5432")
sql = "select id_stock,date_trade,time_trade,val_open,val_high,val_low,val_close,amt_amount,amt_volumn " \
      "FROM public.stock_fifteenminute_history_2020 where time_trade='10:00' and date_trade='2020-04-14'"
print(sql)
data = pd.read_sql(sql, con)

sql2 = "select id_stock,date_trade,time_trade,val_bp1,val_bv1,val_sp1,val_sv1 " \
      "FROM public.stock_tick_2020_0428 LIMIT 100" #where time_trade='10:00'
print(sql2)
data2 = pd.read_sql(sql2, con)

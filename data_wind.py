
import WindPy  as wp
import pandas as pd

data = wp.w.wsd("110011.OF", "nav,NAV_adjfactor,NAV_acc,peer_fund_return_rank_per", "2020-03-21", "2020-04-19", "fundType=1")
data_df = pd.DataFrame()

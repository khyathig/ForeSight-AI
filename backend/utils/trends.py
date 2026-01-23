from pytrends.request import TrendReq

def get_trend_score(keyword):
    pytrends = TrendReq()
    pytrends.build_payload([keyword], geo="IN")
    data = pytrends.interest_over_time()
    if data.empty:
        return 0
    return int(data[keyword].iloc[-1])

import pyupbit
from comm import dbconn
import schedule
import time


def getsignal(coinn):
    candle = pyupbit.get_ohlcv(coinn, interval="minute1", count=60)
    opens = candle["open"]
    closes = candle["close"]
    highs = candle["high"]
    lows = candle["low"]
    rate = (max(highs)-min(lows))/min(closes)*100
    closess = closes.tolist()
    ratess = []
    for i in range(len(closess)-1):
        diff = closes.iloc[i+1]-closes.iloc[i]
        rates = round(diff/closes.iloc[i]*100,3)
        ratess.append(float(rates))
    ratv = round(rate,3)
    maxv = max(ratess)
    minv = min(ratess)
    sumv = round(sum(ratess),2)
    sigv = round(sum(ratess),2)/max(ratess)
    dbconn.insertSignal(coinn,ratv,maxv,minv,sumv,sigv,1)


def getSignals():
    coins = pyupbit.get_tickers(fiat="KRW")
    try:
        for coin in coins:
            getsignal(coin)
            time.sleep(0.1)
    except Exception as e:
        print("시그널 취득 에러 : ",e)
    finally:
        print("코인 트렌드 취득 완료")


schedule.every(1).minutes.do(getSignals)


while True:
    schedule.run_pending()
    time.sleep(5)
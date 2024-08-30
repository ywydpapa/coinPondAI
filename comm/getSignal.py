import pyupbit
import dbconn
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
    rate30 = ratess[29:]
    rate15 = ratess[44:]
    rate10 = ratess[49:]
    rate5 = ratess[54:]
    ratv = round(rate,3)
    maxv = max(ratess)
    minv = min(ratess)
    sumv = round(sum(ratess),2)
    sigv60 = round(sum(ratess),2)/max(ratess)
    sigv30 = round(sum(rate30), 2) / max(rate30)
    sigv15 = round(sum(rate15), 2) / max(rate15)
    sigv10 = round(sum(rate10), 2) / max(rate10)
    sigv5 = round(sum(rate5), 2) / max(rate5)
    dbconn.insertSignal(coinn,ratv,maxv,minv,sumv,sigv60,sigv30, sigv15, sigv10, sigv5,60)


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
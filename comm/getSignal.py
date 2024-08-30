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
    rate60 = []
    for i in range(len(closess)-1):
        diff = closes.iloc[i+1]-closes.iloc[i]
        rates = round(diff/closes.iloc[i]*100,3)
        rate60.append(float(rates))
    rate30 = rate60[29:]
    rate15 = rate60[44:]
    rate10 = rate60[49:]
    rate5 = rate60[54:]
    ratv = round(rate,3)
    maxv = max(rate60)
    minv = min(rate60)
    sumv = round(sum(rate60),2)
    mx60 = max(rate60)
    mx30 = max(rate30)
    mx15 = max(rate15)
    mx10 = max(rate10)
    mx5 = max(rate5)
    if mx60 != 0.0:
        sigv60 = round(sum(rate60),2)/max(rate60)
    else:
        sigv60 = 0.0001
    if mx30 != 0.0:
        sigv30 = round(sum(rate30), 2)/max(rate30)
    else:
        sigv30 = 0.0001
    if mx15 != 0.0:
        sigv15 = round(sum(rate15), 2)/max(rate15)
    else:
        sigv15 = 0.0001
    if mx10 != 0.0:
        sigv10 = round(sum(rate10), 2)/max(rate10)
    else:
        sigv10 = 0.0001
    if mx5 != 0.0:
        sigv5 = round(sum(rate5), 2)/max(rate5)
    else:
        sigv5 = 0.0001
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
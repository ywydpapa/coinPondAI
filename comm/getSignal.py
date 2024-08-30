import pyupbit
import dbconn
import schedule
import time


def getsignal(coinn):
    candle = pyupbit.get_ohlcv(coinn, interval="minute1", count=240)
    opens = candle["open"]
    closes = candle["close"]
    highs = candle["high"]
    lows = candle["low"]
    rate240 = round((max(highs) - min(lows)) / min(closes) * 100,3)
    opens180 = candle["open"][60:]
    closes180 = candle["close"][60:]
    highs180 = candle["high"][60:]
    lows180 = candle["low"][60:]
    rate180 = round((max(highs180) - min(lows180)) / min(closes180) * 100,3)
    opens120 = candle["open"][120:]
    closes120 = candle["close"][120:]
    highs120 = candle["high"][120:]
    lows120 = candle["low"][120:]
    rate120 = round((max(highs120) - min(lows120)) / min(closes120) * 100,3)
    opens60 = candle["open"][180:]
    closes60 = candle["close"][180:]
    highs60 = candle["high"][180:]
    lows60 = candle["low"][180:]
    rate60 = (max(highs60)-min(lows60))/min(closes60)*100
    closez60 = closes60.tolist()
    ratez = []
    for i in range(len(closez60)-1):
        diff = closez60[i+1]-closez60[i]
        rates = round(diff/closez60[i]*100,3)
        ratez.append(float(rates))
    rate30 = ratez[29:]
    rate15 = ratez[44:]
    rate10 = ratez[49:]
    rate5 = ratez[54:]
    ratv = round(rate60,3)
    maxv = max(ratez)
    minv = min(ratez)
    sumv = round(sum(ratez),2)
    mx60 = max(ratez)
    mx30 = max(rate30)
    mx15 = max(rate15)
    mx10 = max(rate10)
    mx5 = max(rate5)
    if mx60 != 0.0:
        sigv60 = round(sum(ratez),2)/max(ratez)
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
    dbconn.insertSignal(coinn,rate240,rate180,rate120,ratv,maxv,minv,sumv,sigv60,sigv30, sigv15, sigv10, sigv5,60)


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
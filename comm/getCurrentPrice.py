import time
from datetime import datetime
import requests
import asyncio
import dbconn
import schedule


def get_tickers():  #거래종목 취득
    url = 'https://api.upbit.com/v1/market/all?isDetails=true'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    tickers = response.json()
    return tickers


def get_crp(coinn): # 현재가 조회
    url = "https://api.upbit.com/v1/ticker?markets="+coinn
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def insertCprice():
    try:
        tickers = get_tickers()
        coinns = list()
        for coinn in tickers:
            if coinn["market"][:3] == "KRW":
                coinns.append(coinn["market"])
        coinlst = ','.join(coinns)
        actPr = get_crp(coinlst)
        for actP in actPr:
            dbconn.insertCRP(actP)
    except Exception as e:
        print("현재가 15분 취득 에러 : ",e)
    finally:
        now = datetime.now()
        print("Insert Current Prices at ", now.strftime("%Y-%m-%d %H:%M:%S"))


def insertCprice5():
    try:
        tickers = get_tickers()
        coinns = list()
        for coinn in tickers:
            if coinn["market"][:3] == "KRW":
                coinns.append(coinn["market"])
        coinlst = ','.join(coinns)
        actPr = get_crp(coinlst)
        for actP in actPr:
            dbconn.insertCRP5(actP)
    except Exception as e:
        print("현재가 5분 취득 에러 : ",e)
    finally:
        now = datetime.now()
        print("Insert Current Prices at ", now.strftime("%Y-%m-%d %H:%M:%S"))


def insertCprice30():
    try:
        tickers = get_tickers()
        coinns = list()
        for coinn in tickers:
            if coinn["market"][:3] == "KRW":
                coinns.append(coinn["market"])
        coinlst = ','.join(coinns)
        actPr = get_crp(coinlst)
        for actP in actPr:
            dbconn.insertCRP30(actP)
    except Exception as e:
        print("현재가 30분 취득 에러 : ",e)
    finally:
        now = datetime.now()
        print("Insert Current Prices at ", now.strftime("%Y-%m-%d %H:%M:%S"))

schedule.every(5).minutes.do(insertCprice5)
schedule.every(15).minutes.do(insertCprice)
schedule.every(30).minutes.do(insertCprice30)

while True:
    schedule.run_pending()
    time.sleep(5)
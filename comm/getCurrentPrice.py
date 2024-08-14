import time
import requests
import asyncio
from comm import dbconn

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
        print("현재가 취득 에러 : ",e)
    finally:
        return "OK"


insertCprice()


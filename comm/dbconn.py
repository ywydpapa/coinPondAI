import os
import pyupbit
import pymysql
import dotenv


dotenv.load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWD')
dbase = os.getenv('DB_NAME')


def insertCRP15(crp):
    try:
        db01 = pymysql.connect(host=host, user=user, password=password, db=dbase, charset='utf8')
        cursor01 = db01.cursor()
        d01 = crp["market"]
        d02 = crp["trade_date"]
        d03 = crp["trade_time"]
        d04 = crp["trade_date_kst"]
        d05 = crp["trade_time_kst"]
        d06 = crp["trade_timestamp"]
        d07 = crp["opening_price"]
        d08 = crp["high_price"]
        d09 = crp["low_price"]
        d10 = crp["trade_price"]
        d11 = crp["prev_closing_price"]
        d12 = crp["change"]
        d13 = crp["change_price"]
        d14 = crp["change_rate"]
        d15 = crp["signed_change_price"]
        d16 = crp["signed_change_rate"]
        d17 = crp["trade_volume"]
        d18 = crp["acc_trade_price"]
        d19 = crp["acc_trade_price_24h"]
        d20 = crp["acc_trade_volume"]
        d21 = crp["acc_trade_volume_24h"]
        d22 = crp["highest_52_week_price"]
        d23 = crp["highest_52_week_date"]
        d24 = crp["lowest_52_week_price"]
        d25 = crp["lowest_52_week_date"]
        d26 = crp["timestamp"]
        sql = ("INSERT INTO activePrice15 (market,trade_date,trade_time,trade_date_kst,trade_time_kst,trade_timestamp,opening_price,high_price,low_price,trade_price,prev_closing_price,changeP,change_price,change_rate,signed_change_price,signed_change_rate,trade_volume,acc_trade_price,acc_trade_price_24h,acc_trade_volume,acc_trade_volume_24h,highest_52_week_price,highest_52_week_date,lowest_52_week_price,lowest_52_week_date,timestamp) "
           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor01.execute(sql,(d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26))
        db01.commit()
        db01.close()
    except Exception as e:
        print("현재가 인서트 에러", e)


def insertCRP5(crp):
    try:
        db02 = pymysql.connect(host=host, user=user, password=password, db=dbase, charset='utf8')
        cursor02 = db02.cursor()
        d01 = crp["market"]
        d02 = crp["trade_date"]
        d03 = crp["trade_time"]
        d04 = crp["trade_date_kst"]
        d05 = crp["trade_time_kst"]
        d06 = crp["trade_timestamp"]
        d07 = crp["opening_price"]
        d08 = crp["high_price"]
        d09 = crp["low_price"]
        d10 = crp["trade_price"]
        d11 = crp["prev_closing_price"]
        d12 = crp["change"]
        d13 = crp["change_price"]
        d14 = crp["change_rate"]
        d15 = crp["signed_change_price"]
        d16 = crp["signed_change_rate"]
        d17 = crp["trade_volume"]
        d18 = crp["acc_trade_price"]
        d19 = crp["acc_trade_price_24h"]
        d20 = crp["acc_trade_volume"]
        d21 = crp["acc_trade_volume_24h"]
        d22 = crp["highest_52_week_price"]
        d23 = crp["highest_52_week_date"]
        d24 = crp["lowest_52_week_price"]
        d25 = crp["lowest_52_week_date"]
        d26 = crp["timestamp"]
        sql = ("INSERT INTO activePrice5 (market,trade_date,trade_time,trade_date_kst,trade_time_kst,trade_timestamp,opening_price,high_price,low_price,trade_price,prev_closing_price,changeP,change_price,change_rate,signed_change_price,signed_change_rate,trade_volume,acc_trade_price,acc_trade_price_24h,acc_trade_volume,acc_trade_volume_24h,highest_52_week_price,highest_52_week_date,lowest_52_week_price,lowest_52_week_date,timestamp) "
           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor02.execute(sql,(d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26))
        db02.commit()
        db02.close()
    except Exception as e:
        print("현재가 5분 인서트 에러", e)


def insertCRP30(crp):
    try:
        db03 = pymysql.connect(host=host, user=user, password=password, db=dbase, charset='utf8')
        cursor03 = db03.cursor()
        d01 = crp["market"]
        d02 = crp["trade_date"]
        d03 = crp["trade_time"]
        d04 = crp["trade_date_kst"]
        d05 = crp["trade_time_kst"]
        d06 = crp["trade_timestamp"]
        d07 = crp["opening_price"]
        d08 = crp["high_price"]
        d09 = crp["low_price"]
        d10 = crp["trade_price"]
        d11 = crp["prev_closing_price"]
        d12 = crp["change"]
        d13 = crp["change_price"]
        d14 = crp["change_rate"]
        d15 = crp["signed_change_price"]
        d16 = crp["signed_change_rate"]
        d17 = crp["trade_volume"]
        d18 = crp["acc_trade_price"]
        d19 = crp["acc_trade_price_24h"]
        d20 = crp["acc_trade_volume"]
        d21 = crp["acc_trade_volume_24h"]
        d22 = crp["highest_52_week_price"]
        d23 = crp["highest_52_week_date"]
        d24 = crp["lowest_52_week_price"]
        d25 = crp["lowest_52_week_date"]
        d26 = crp["timestamp"]
        sql = ("INSERT INTO activePrice30 (market,trade_date,trade_time,trade_date_kst,trade_time_kst,trade_timestamp,opening_price,high_price,low_price,trade_price,prev_closing_price,changeP,change_price,change_rate,signed_change_price,signed_change_rate,trade_volume,acc_trade_price,acc_trade_price_24h,acc_trade_volume,acc_trade_volume_24h,highest_52_week_price,highest_52_week_date,lowest_52_week_price,lowest_52_week_date,timestamp) "
           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor03.execute(sql,(d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26))
        db03.commit()
        db03.close()
    except Exception as e:
        print("현재가 인서트 에러", e)
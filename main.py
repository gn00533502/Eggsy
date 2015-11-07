#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

# 設定初始變數
supermarket = {
    '電子': ["ipad", "iphone", "顯示器", "筆記型電腦", "鍵盤"],
    "食品": ["麵包", "餅乾", "蛋糕", "牛肉", "魚", "蔬菜"],
    "日用品": ["餐巾紙", "收納箱", "咖啡杯", "雨傘"],
    "酒類": ["啤酒", "白酒", "伏特加"]
}

situation = True #促銷資訊
situation2 = True #購買產品
situation3 = True #折抵資訊

if __name__ == '__main__':

    while situation == True:
        str_ask = raw_input('請輸入折扣資訊,若輸入完成直接鍵入空格進入購買選項(格式為 日期|折扣|產品品類 ex: 2013.11.11|0.7|電子 ):').split('|')

        try:
            if str_ask[0] == ' ':
                print ("\n")
                situation = False
                total = 0

                while situation2 == True:
                    print "目前總金額為 %10.2f" % total
                    item = raw_input("請輸入購買項目(格式為 數量*品名:單價[小數兩位] ex: 1*ipad:2399.00 ):")
                    if item == " ":
                        situation2 = False #進入下一階段
                        print ("\n")
                    else:
                        try:
                            z = 0
                            a1 = item.split('*')
                            number = int(a1[0])
                            a2 = a1[1].split(':')
                            thing = a2[0]
                            price = round(float(a2[1]), 2)

                            for i in supermarket:
                                if thing in supermarket[i]:
                                    z += 1
                                    if isinstance(supermarket[i][-1], float) == True:
                                        total = total + round(price * supermarket[i][-1] * number, 2)
                                    else:
                                        total = total + round(price * number, 2)
                            if z == 0:
                                print "該商品並不在清單內! 請重新輸入"
                        except:
                            print "輸入格式不對！請重新輸入購買資訊"

                while situation3 == True:
                    try:
                        close_date = datetime.strptime(raw_input("請輸入結算日期 ex: 2015.11.11 ):"), "%Y.%m.%d")
                        end_ask = raw_input('請輸入優惠資訊，若無請輸入一格空白即可 (格式為 日期 到達金額 折抵金額 ex:2016.3.2 1000 200:').split(' ')

                        if len(end_ask) < 3: #無折抵
                            print '總金額為 %10.2f ' %total
                            situation3 = False
                        elif len(end_ask) == 3: #有折抵
                            end_date = datetime.strptime(end_ask[0], "%Y.%m.%d")
                            if end_ask[1].isdigit() == True and end_ask[2].isdigit() == True:
                                if total > int(end_ask[1]) and end_date > close_date:
                                    print "優惠卷還可以使用喔！"
                                    total = total - int(end_ask[2])
                                    print '總金額為 %10.2f ' %total
                                    situation3 = False
                                else:
                                    print '總金額為 %10.2f ' %total
                                    situation3 = False

                    except:
                        print "您輸入的格式不正確，請重新輸入結算日期以及優惠資訊"


            # 確認產品有在選單裡面，第二位為浮點數
            elif str_ask[2] in supermarket and isinstance(float(str_ask[1]), float) == True:
                datefirst = datetime.strptime(str_ask[0], "%Y.%m.%d")
                supermarket[str_ask[2]].append(float(str_ask[1]))
                print "促銷資訊: %s 類產品於 %s 開始折價 %3.2f 喔！ " % (str_ask[2],str_ask[0],float(str_ask[1]))
            else:
                print "您輸入的格式不正確，請重新輸入購買選項資訊"

        except:
            print "您輸入的格式不正確，請重新輸入折扣資訊"

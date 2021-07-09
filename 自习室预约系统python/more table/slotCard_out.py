import json
import sys
sys.path.append("...")
import datetime
import argparse
from InfOperate import refreshTime


# Python slotCard_out.py -i="XXXXXXXXXXX"


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='slot card to in')
    parser.add_argument("-i", "--student-id", dest="id")
    args = parser.parse_args()
    studentId=args.id

    with open("./config/orderList.json","r") as f1:
        orderList=json.load(f1)
        orderList=json.loads(orderList)
        f1.close()

    studentIds=orderList[1]
    try:
        Pos=studentIds.index(studentId)
        nowDate=datetime.datetime.now()
        nowDateStr=nowDate.strftime('%Y-%m-%d %H:%M:%S')
        if len(orderList[2][Pos])==4:
            print("[out]===============================")
            print("暂离时间："+nowDateStr)
            print("校园卡号："+orderList[1][Pos])
            print("座次："+orderList[0][Pos])
            print(" ")
            refreshTime(orderList[0][Pos])
    except:
        print("[out error]=========================")
        print("请更换卡片再次尝试")
        print(" ")


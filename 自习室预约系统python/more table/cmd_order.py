import json
import sys

sys.path.append("...")
import datetime
import argparse
from InfOperate import order, timeoutDetection, occupySeat, alreadyOreder

'''
TEST CODE:
--------------------------------
see Map:
Python cmd_order.py
--------------------------------
order seat: 
Python cmd_order.py -i="XXXXXXXXXXX" -n="xxx" -s="A1"

-h   --help         show the help message and exit
-i   --student-id   student id
-n   --student-name student name
-s   --seatPos      seat id  
'''


def mapDisp():
    with open("./config/occupied.json", "r") as f1:
        occupied = json.load(f1)
        occupied = json.loads(occupied)
        f1.close()
    with open("./config/seatInf.json", "r") as f2:
        seatInf = json.load(f2)
        f2.close()
    print("[seat]============================")
    print("可预约座位：")
    print(" ")
    letterList = seatInf["tableId"]
    tempStr1 = ""
    for i in range(0, len(letterList)):
        tempStr2 = ""
        for j in range(0, seatInf["chairNum"][i]):
            tempStr1 = letterList[i] + str(j + 1)
            if occupied[tempStr1]:
                tempStr2 = tempStr2 + " ▇ "
            else:
                tempStr2 = tempStr2 + " " + tempStr1
        print(tempStr2)
    print(" ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inf submit')
    parser.add_argument("-i", "--student-id", dest="Stid", default='seeMap', help='student id')
    parser.add_argument("-n", "--student-name", dest="Stname", default='seeMap', help='student name')
    parser.add_argument("-s", "--seatPos", dest="Sid", default='seeMap', help='seat id')
    args = parser.parse_args()
    studentId = args.Stid
    studentName = args.Stname
    seatId = args.Sid

    timeoutDetection()
    if args.Stid == 'seeMap':
        mapDisp()
    else:
        with open("./config/orderList.json", "r") as f1:
            orderList = json.load(f1)
            orderList = json.loads(orderList)
            f1.close()

        seatIds = orderList[0]
        try:
            Pos = seatIds.index(seatId)
            with open("./config/occupied.json", "r") as f2:
                occupied = json.load(f2)
                occupied = json.loads(occupied)
                f2.close()
            if occupied[seatId]:
                print("[book error]========================")
                print("座位已被占，请选择其他位置申请")
                print(" ")
            elif alreadyOreder(studentId):
                print("[book error]========================")
                print("请勿重复预约")
                print(" ")
            else:
                nowDate = datetime.datetime.now()
                nowDateStr = nowDate.strftime('%Y-%m-%d %H:%M:%S')
                occupySeat(seatId)
                order(studentId, nowDateStr, seatId)
                print("[book]===========================================")
                print(nowDateStr)
                print("姓名：" + studentName)
                print("学号：" + studentId)
                print("座次：" + seatId)
                print("预约成功！")
                print("-------------------------------------------------")
                print("注意事项：")
                print("1、预约成功后请在30分钟内到达，否则预约信息将失效。")
                print("2、进入自习室前请刷校园卡核验信息。")
                print("3、如要暂离请cmd运行如下代码：")
                print("   Python cmd_leave.py -i='XXXXXXXXXXX' -t='temp'")
                print("4、离开、取消预约请cmd运行如下代码：")
                print("   Python cmd_leave.py -i='XXXXXXXXXXX' -t='free'")


        except:
            print("[book error]========================")
            print("座位编号格式不正确")
            print(" ")

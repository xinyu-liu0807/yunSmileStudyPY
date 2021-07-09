import json
import sys
sys.path.append("...")
import argparse
from InfOperate import timeoutDetection,setString


# Python slotCard_in.py -i="XXXXXXXXXXX"


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='slot card to in')
    parser.add_argument("-i", "--student-id", dest="id")
    args = parser.parse_args()
    studentId=args.id
    timeoutDetection()
    
    with open("./config/orderList.json","r") as f1:
        orderList=json.load(f1)
        orderList=json.loads(orderList)
        f1.close()

    studentIds=orderList[1]
    try:
        Pos=studentIds.index(studentId)
        print("[in]================================")
        print("预约时间："+orderList[2][Pos])
        print("校园卡号："+orderList[1][Pos])
        print("座次："+orderList[0][Pos])
        print(" ")
        setString(orderList[0][Pos],"arrive")
    except:
        print("[in error]==========================")
        print("非本校校园卡或已超时")
        print(" ")

    
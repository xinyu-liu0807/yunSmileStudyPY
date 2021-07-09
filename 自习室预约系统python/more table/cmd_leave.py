import json
import sys
sys.path.append("...")
import argparse
from InfOperate import setString,freeSeat

'''
TEST CODE:
----------------------------------------------
leave for temp
Python cmd_leave.py -i="XXXXXXXXXXX" -t="temp"
----------------------------------------------
leave
Python cmd_leave.py -i="XXXXXXXXXXX" -t="free"  
[or]
Python cmd_leave.py -i="XXXXXXXXXXX" 

-h   --help         show the help message and exit
-i   --student-id   student id
-t   --leave-type   temp/free 
'''

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='leave')
    parser.add_argument("-i", "--student-id", dest="id")
    parser.add_argument("-t", "--leave-type",default='free', dest="type",help='temp/free')
    args = parser.parse_args()
    studentId=args.id
    leaveType=args.type

    with open("./config/orderList.json","r") as f1:
        orderList=json.load(f1)
        orderList=json.loads(orderList)
        f1.close()
    studentIds=orderList[1]
    try:
        Pos=studentIds.index(studentId)
        seatId=orderList[0][Pos]
        if leaveType=="temp":
            setString(seatId,"temp")
            print("[out]===============================")
            print("已进行暂离申请")
            print(" ")
        else:
            freeSeat(seatId)
            print("[out]===============================")
            print("已释放位置")
            print(" ")
    except:
        print("[out error]=========================")
        print("可能输入了错误的校园卡号")
        print(" ")

    
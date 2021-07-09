import json
import sys
import datetime

sys.path.append("...")


def occupySeat(seatId):
    # path=sys.argv[0]
    # path=path[0:path.rfind("/")]
    with open("./config/occupied.json", "r") as f1:
        occupied = json.load(f1)
        occupied = json.loads(occupied)
        occupied[seatId] = True
        f1.close()
    with open("./config/occupied.json", "w") as f2:
        jsonType = json.dumps(occupied)
        json.dump(jsonType, f2)
        f2.close()


def freeSeat(seatId):
    # path=sys.argv[0]
    # path=path[0:path.rfind("/")]
    with open("./config/occupied.json", "r") as f1:
        occupied = json.load(f1)
        occupied = json.loads(occupied)
        occupied[seatId] = False
        f1.close()
    with open("./config/occupied.json", "w") as f2:
        jsonType = json.dumps(occupied)
        json.dump(jsonType, f2)
        f2.close()

    with open("./config/orderList.json", "r") as f3:
        orderList = json.load(f3)
        orderList = json.loads(orderList)
        f3.close()
    seatIds = orderList[0]
    changePos = seatIds.index(seatId)
    orderList[1][changePos] = ""
    orderList[2][changePos] = ""

    with open("./config/orderList.json", "w") as f4:
        jsonType = json.dumps(orderList)
        json.dump(jsonType, f4)
        f4.close()


def clearOccupied():
    with open("./config/seatInf.json", "r") as f1:
        seatInf = json.load(f1)
        f1.close()
    occupied = dict()
    for i in range(0, len(seatInf["tableId"])):
        for j in range(0, int(seatInf["chairNum"][i])):
            occupied[seatInf["tableId"][i] + str(j + 1)] = False

    with open("./config/occupied.json", "w") as f2:
        jsonType = json.dumps(occupied)
        json.dump(jsonType, f2)
        f2.close()


def clearOrderList():
    # path=sys.argv[0]
    # path=path[0:path.rfind("/")]
    seatId = []
    studentId = []
    orderTime = []
    with open("./config/seatInf.json", "r") as f1:
        seatInf = json.load(f1)
        f1.close()
    occupied = dict()
    for i in range(0, len(seatInf["tableId"])):
        for j in range(0, int(seatInf["chairNum"][i])):
            seatId.append(seatInf["tableId"][i] + str(j + 1))
            studentId.append("")
            orderTime.append("")

    orderList = []
    orderList.append(seatId)
    orderList.append(studentId)
    orderList.append(orderTime)

    with open("./config/orderList.json", "w") as f:
        jsonType = json.dumps(orderList)
        json.dump(jsonType, f)


def order(studentId, timeStr, seatId):
    # path=sys.argv[0]
    # path=path[0:path.rfind("/")]
    with open("./config/orderList.json", "r") as f1:
        orderList = json.load(f1)
        orderList = json.loads(orderList)
        f1.close()
    seatIds = orderList[0]
    changePos = seatIds.index(seatId)
    orderList[1][changePos] = studentId
    orderList[2][changePos] = timeStr

    with open("./config/orderList.json", "w") as f2:
        jsonType = json.dumps(orderList)
        json.dump(jsonType, f2)
        f2.close()


def timeoutDetection():
    with open("./config/orderList.json", "r") as f1:
        orderList = json.load(f1)
        orderList = json.loads(orderList)
        f1.close()

    nowDate = datetime.datetime.now()
    timeList = orderList[2]
    for i in range(0, len(timeList)):
        lastTimeStr = timeList[i]
        if len(lastTimeStr) > 7:
            lastTime = datetime.datetime.strptime(lastTimeStr, '%Y-%m-%d %H:%M:%S')
            diffTime = nowDate - lastTime
            if diffTime.seconds > 30 * 60:
                orderList[1][i] = ""
                orderList[2][i] = ""
                freeSeat(orderList[0][i])

    with open("./config/orderList.json", "w") as f2:
        jsonType = json.dumps(orderList)
        json.dump(jsonType, f2)
        f2.close()


def refreshTime(seatId):
    nowDate = datetime.datetime.now()
    nowDateStr = nowDate.strftime('%Y-%m-%d %H:%M:%S')
    with open("./config/orderList.json", "r") as f1:
        orderList = json.load(f1)
        orderList = json.loads(orderList)
        f1.close()
    seatIds = orderList[0]
    changePos = seatIds.index(seatId)
    orderList[2][changePos] = nowDateStr
    with open("./config/orderList.json", "w") as f2:
        jsonType = json.dumps(orderList)
        json.dump(jsonType, f2)
        f2.close()


def setString(seatId, string):
    with open("./config/orderList.json", "r") as f1:
        orderList = json.load(f1)
        orderList = json.loads(orderList)
        f1.close()
    seatIds = orderList[0]
    changePos = seatIds.index(seatId)
    orderList[2][changePos] = string
    with open("./config/orderList.json", "w") as f2:
        jsonType = json.dumps(orderList)
        json.dump(jsonType, f2)
        f2.close()


def alreadyOreder(studentId):
    with open("./config/orderList.json", "r") as f1:
        orderList = json.load(f1)
        orderList = json.loads(orderList)
        f1.close()

    try:
        studentIds = orderList[1]
        Pos = studentIds.index(studentId)
        return True
    except:
        return False
# clearOccupied()
# clearOrderList()

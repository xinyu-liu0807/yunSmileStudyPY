# Python 程序--座位预约系统

## 1 程序说明

该程序用以模拟自习座位预约及刷卡出入，其中预约界面使QT(pyside2)制作，使用命令行代码模拟刷卡过程，可将程序放至流程托管平台。以下是各个类和函数的说明：

- orderSystem.py 预约界面
- orderDataDisplay.py 预约结果界面
- InfOperate.py 数据交互函数集合
- slotCard_in.py 刷卡模拟(入)
- slotCard_out.py 刷卡模拟(出)
- cmd_closure.py 命令行每日清空数据
- cmd_order.py 命令行预约
- cmd_leave.py 命令行申请暂离或离开

## 2 交互函数说明

以下为伪代码

- **occupySeat(seatId)**
  - occupied.json内字典key：seatId 对应value：Flase->True
- **freeSeat(seatId)**
  - occupied.json内字典key：seatId 对应value：Flase->True
  - orderList.json中pos=seatIds.index(seatId),orderList[1][pos]="",orderList[2][pos]=""
- **clearOrderList()**
  - orderList.json中orderList[1][:]="",orderList[2][:]=""
- **order(studentId,timeStr,seatId)**
  - orderList.json中pos=seatIds.index(seatId)位置数据填充
- **timeoutDetection()**
  - 超时数据清除
- **refreshTime(seatId)**
  - orderList.json中pos=seatIds.index(seatId)位置时间刷新
- **setString(seatId,string)**  
  - orderList.json中pos=seatIds.index(seatId)位置时间字符串更改(arrive/temp)
- **alreadyOreder**
  - 检测座位是否已经被占

## 3 Python packages

Python 环境中需要安装下列 python 包：

1. PySide2
2. datetime
3. json
4. argparse

详细需求：

- **orderSystem** : PySide2,datetime,json,orderDataDisplay,InfOperate
- **orderDataDisplay** : PySide2, InfOperate
- **InfOperate** : datetime,json
- **slotCard_in** : argparse,json,InfOperate
- **slotCard_out** : argparse,datetime,json,InfOperate
- **cmd_closure** : InfOperate
- **cmd_order** : argparse,datetime,json,InfOperate
- **cmd_leave** : argparse,json,InfOperate

## 4 命令行参数

**slotCard_in(以下两种均可):**

- Python slotCard_in.py -i="XXXXXXXXXXX"
- Python slotCard_in.py --student-id="XXXXXXXXXXX"

**slotCard_out(以下两种均可):**

- Python slotCard_out.py -i="XXXXXXXXXXX"
- Python slotCard_out.py --student-id="XXXXXXXXXXX"

**cmd_closure:**

- Python cmd_closure.py

**cmd_order:**

``` python25
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
```

**cmd_leave:**

``` python
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
```

## 5 命令行输出

### 5.1 cmd_order

```cmd
> Python cmd_order.py
[seat]============================
可预约座位：

 ▇ A2 A3 A4 A5 A6
 B1 B2 B3 B4 B5 B6
 C1 C2 C3 C4 C5 C6
 D1 D2 D3 D4 D5 D6
 E1 E2 E3 E4 E5 E6
 F1 F2 F3 F4 F5 F6

> Python cmd_order.py -i="18160000000" -n="xxx" -s="A1"
[book error]========================
座位已被占，请选择其他位置申请

> Python cmd_order.py -i="18160000000" -n="xxx" -s="A100"
[book error]========================
座位编号格式不正确

> Python cmd_order.py -i="18160000000" -n="xxx" -s="A2"
[book]===========================================
2021-05-31 18:04:35
姓名：xxx
学号：18160000000
座次：A2
预约成功！
-------------------------------------------------
注意事项：
1、预约成功后请在30分钟内到达，否则预约信息将失效。
2、进入自习室前请刷校园卡核验信息。
3、如要暂离请cmd运行如下代码：
   Python cmd_leave.py -i='XXXXXXXXXXX' -t='temp'
4、离开、取消预约请cmd运行如下代码：
   Python cmd_leave.py -i='XXXXXXXXXXX' -t='free'

> Python cmd_order.py -i="18160000000" -n="xxx" -s="A3"
[book error]========================
请勿重复预约
```

### 5.2 slotCard_in

```cmd
> Python slotCard_in.py -i="1816000XXXX"
[in error]==========================
非本校校园卡或已超时

> Python slotCard_in.py -i="18160000000"
[in]================================
预约时间：2021-05-31 18:04:35
校园卡号：18160000000
座次：A2

```

### 5.3 cmd_leave

```cmd
> Python cmd_leave.py -i="1816000XXXX" -t="temp"
[out error]=========================
可能输入了错误的校园卡号

> Python cmd_leave.py -i="18160000000" -t="temp"
[out]===============================
已进行暂离申请

> Python cmd_leave.py -i="18160000000" -t="free"
[out]===============================
已释放位置

```

### 5.4 slotCard_out

```cmd
> Python slotCard_out.py -i="18160000000"
[out]===============================
暂离时间：2021-05-31 18:23:09
校园卡号：18160000000
座次：A1

> Python slotCard_out.py -i="1816000XXXX"
[out error]=========================
请更换卡片再次尝试

```

## 6 config 配置

### 6.1 seatInf.json

``` json
{
    "tableNum": 6,
    "tablePos": [
        [0.02,0.15],
        [0.35,0.15],
        [0.68,0.15],
        [0.02,0.65],
        [0.35,0.65],
        [0.68,0.65]
    ],
    "tableSize": [
        [0.25,0.2],
        [0.25,0.2],
        [0.25,0.2],
        [0.25,0.2],
        [0.25,0.2],
        [0.25,0.2]
    ],
    "tableType": [
        0,1,2,0,0,0
    ],
    "tableSS": [
        "QLabel{background: rgb(245,245,245);color:rgb(92,92,92);border-radius:50px;border: 3px solid rgb(142,142,142)}",
        "QLabel{background: rgb(245,245,245);color:rgb(92,92,92);border: 3px solid rgb(142,142,142)}",
        "QLabel{background: rgb(221,217,195);color:rgb(92,92,92);border: 3px solid rgb(142,142,142)}"
    ],
    "tableId": [
        "A","B","C","D","E","F"
    ],
    "chairNum": [
        6,6,6,6,6,6
    ],
    "chairPos": [
        [
            [0.04,-0.08],
            [0.105,-0.08],
            [0.17,-0.08],
            [0.04,0.21],
            [0.105,0.21],
            [0.17,0.21]
        ],
        [
            [0.04,-0.08],
            [0.105,-0.08],
            [0.17,-0.08],
            [0.04,0.21],
            [0.105,0.21],
            [0.17,0.21]
        ],[
            [0.04,-0.08],
            [0.105,-0.08],
            [0.17,-0.08],
            [0.04,0.21],
            [0.105,0.21],
            [0.17,0.21]
        ],[
            [0.04,-0.08],
            [0.105,-0.08],
            [0.17,-0.08],
            [0.04,0.21],
            [0.105,0.21],
            [0.17,0.21]
        ],[
            [0.04,-0.08],
            [0.105,-0.08],
            [0.17,-0.08],
            [0.04,0.21],
            [0.105,0.21],
            [0.17,0.21]
        ],[
            [0.04,-0.08],
            [0.105,-0.08],
            [0.17,-0.08],
            [0.04,0.21],
            [0.105,0.21],
            [0.17,0.21]
        ]
    ],
    "chairSize": [
        0.032,0.07
    ],
    "chairSS_W": "background: rgb(242,242,242);border-radius:15px;border: 3px solid rgb(74,69,42)",
    "chairSS_K": "background: rgb(64,64,64);border-radius:15px;border: 3px solid rgb(74,69,42)",
    "chairSS_R": "background: rgb(149,55,43);border-radius:15px;border: 3px solid rgb(74,69,42)",
    "mapSize": [
        2,2
    ]
}
```

### 6.2 occupied.json

``` json
"{
    \"A1\": true, 
    \"A2\": true, 
    \"A3\": true,
    ... ...
}"
```

### 6.3 orderList.json

``` json
"[[\"A1\", \"A2\", \"A3\", \"A4\", \"A5\", \"A6\", \"B1\", \"B2\",... ...],
[\"1816000XXXX\", \"1816000XXXX\",\"1816000XXXX\",... ...],
[\"2021-05-30 21:48:15\",\"2021-05-30 17:25:15\",... ...]]"
```

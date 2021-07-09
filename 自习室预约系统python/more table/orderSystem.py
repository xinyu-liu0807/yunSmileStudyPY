from PySide2.QtWidgets import QApplication, QWidget,QScrollArea
from PySide2.QtWidgets import QLabel,QPushButton,QLineEdit
from PySide2.QtGui import QIcon,QFont
from PySide2.QtCore import Qt
import sys
sys.path.append("...")
import json
import datetime
from orderDataDisplay import orderDisplay
from InfOperate import occupySeat,order,timeoutDetection,alreadyOreder


class Window_main(QWidget):
    def __init__(self,Width=700,Height=840):
        super().__init__() 
        self.setWindowTitle("book seat online")
        timeoutDetection()

        self.Width=Width
        self.Height=Height
        self.selectedId=""
        self.selectedBtn=[]
        self.icoPath="./gallery/icon.ico"

        # 字体标签
        title_qf=QFont()
        title_qf.setPointSize(11)
        title_qf.setBold(True)
        title_qf.setFamily("Cambria")
        main_qf=QFont()
        main_qf.setPointSize(27)
        main_qf.setBold(True)
        main_qf.setFamily("Cambria")
        Inf_qf=QFont()
        Inf_qf.setPointSize(10)
        Inf_qf.setBold(True)
        Inf_qf.setFamily("Cambria")
        table_qf=QFont()
        table_qf.setPointSize(16)
        table_qf.setBold(True)
        table_qf.setFamily("Cambria")
        # ---
        self.QF_part_title=title_qf         # 框标题字体标签
        self.QF_main_title=main_qf          # 主标题字体标签
        self.QF_state_explain=Inf_qf        # 状态标签解释文本字体标签
        self.QF_Inf_title=title_qf          # 信息标题字体标签
        self.QF_Inf_text=Inf_qf             # 信息文本字体标签
        self.QF_table_name=table_qf         # 桌子编号信息标签

        # 样式表
        self.SS_part_frame="QLabel{background: rgb(245,245,245);color:rgb(92,92,92);border-radius:8px;border: 2.5px solid rgb(122,122,122)}"
        self.SS_part_title="QLabel{background: rgb(245,245,245);color:rgb(92,92,92)}"
        self.SS_main_title="QLabel{background: rgb(245,245,245);color:rgb(92,92,92);border-radius:50px;border: 3px solid rgb(142,142,142)}"
        self.SS_state_frame="QLabel{background: rgb(245,245,245);border-radius:5px;border: 3px solid rgb(172,172,172)}"
        self.SS_W="QLabel{background: rgb(242,242,242);border-radius:9px;border: 3px solid rgb(74,69,42)}"
        self.SS_K="QLabel{background: rgb(64,64,64);border-radius:9px;border: 3px solid rgb(74,69,42)}"
        self.SS_R="QLabel{background: rgb(149,55,43);border-radius:9px;border: 3px solid rgb(74,69,42)}"
        self.SS_state_explain="QLabel{background: rgb(214,219,233);color:rgb(92,92,92)}"
        self.SS_Inf_title="QLabel{background: rgb(230,230,230);color:rgb(82,82,82);border-radius:8px}"
        self.SS_text_Line="QLineEdit{border-radius:3px;background: rgb(205,205,205);color:rgb(82,82,82)}"
        self.SS_book_btn="color:rgb(255,255,255);background: rgb(79,148,204)"

        # path=sys.argv[0]
        # path=path[0:path.rfind("/")]
        f=open("./config/seatInf.json","r")
        seatInf=json.load(f)
        f=open("./config/occupied.json","r")
        seatOccupied=json.load(f)
        self.seatInf=seatInf
        self.seatOccupied=json.loads(seatOccupied)

        self.setSize()
        self.setIcon()
        self.partition()
        self.setStateExp()
        self.setInfBox()
        self.setMap()
        self.setBookBtn()    
    # ================================================================================================
    # 回调函数部分：
    def selectedPos(self):# 座位选择回调
        btn=self.sender()
        tempSelectedId=btn.property("chairId")
        if not self.seatOccupied[tempSelectedId]:
            if len(self.selectedId)==0:
                self.selectedId=tempSelectedId
                self.selectedBtn=btn
                btn.setStyleSheet(self.seatInf["chairSS_R"])
                self.selectedBox.setText(" 当前选择:  "+tempSelectedId)
            else:
                self.selectedBtn.setStyleSheet(self.seatInf["chairSS_W"])
                self.selectedBtn=btn
                btn.setStyleSheet(self.seatInf["chairSS_R"])
                self.selectedId=tempSelectedId
                self.selectedBox.setText(" 当前选择:  "+tempSelectedId)

    def bookSeat(self):
        if not len(self.selectedId)==0:
            if alreadyOreder(self.InfBox_Id.text()):
                print("================================")
                print("请勿重复预约")
                print(" ")
            else:
                nowDate=datetime.datetime.now()
                nowDateStr=nowDate.strftime('%Y-%m-%d %H:%M:%S')
                print("================================")
                print(nowDateStr)
                print("姓名："+self.InfBox_Name.text())
                print("学号："+self.InfBox_Id.text())
                print("座次："+self.selectedId)
                print(" ")
                # myapp.exit()
                # app = QApplication.instance()
                # if app is None: 
                #     app = QApplication(sys.argv)
                self.window_disp= orderDisplay(self.InfBox_Name.text(),
                            self.InfBox_Id.text(),
                            nowDateStr,
                            self.selectedId,700,840)
                self.window_disp.show()
                self.close()

                occupySeat(self.selectedId)
                order(self.InfBox_Id.text(),nowDateStr,self.selectedId)

            
            


    # ================================================================================================
    # 框架构造函数部分：
    def setSize(self):# 调整框架大小
        self.setGeometry(80,80,self.Width,self.Height)
        self.setMaximumSize(self.Width,self.Height)
        self.setMinimumSize(self.Width,self.Height)

    def setIcon(self):# 设置图标
        appIcon=QIcon(self.icoPath)
        self.setWindowIcon(appIcon)

    def setStateExp(self):# 绘制状态解释框
        Width=self.Width
        Height=self.Height
        self.part0=QLabel(self)
        self.part0.setGeometry(0.66*Width,0.045*Height,
                               0.28*Width,0.14*Height)
        self.part0.setStyleSheet(self.SS_state_frame)

        # ---Color Bar--------------------------------------------------------------------
        self.CB1=QLabel(self)
        self.CB1.setGeometry(0.68*Width,0.06*Height,0.05*Width,0.03*Height)
        self.CB1.setStyleSheet(self.SS_W) 
        self.CB2=QLabel(self)
        self.CB2.setGeometry(0.68*Width,(0.06+0.04)*Height,0.05*Width,0.03*Height)
        self.CB2.setStyleSheet(self.SS_K) 
        self.CB3=QLabel(self)
        self.CB3.setGeometry(0.68*Width,(0.06+0.08)*Height,0.05*Width,0.03*Height)
        self.CB3.setStyleSheet(self.SS_R) 

        # ---Color Bar 解释文本-------------------------------------------------------------
        self.plaintext1=QLabel(self)
        self.plaintext1.setGeometry(0.76*Width,(0.059)*Height,0.15*Width,0.032*Height)
        self.plaintext1.setStyleSheet(self.SS_state_explain)
        self.plaintext1.setText(" 可选择")
        self.plaintext1.setFont(self.QF_state_explain)
        self.plaintext2=QLabel(self)
        self.plaintext2.setGeometry(0.76*Width,(0.059+0.04)*Height,0.15*Width,0.032*Height)
        self.plaintext2.setStyleSheet(self.SS_state_explain)
        self.plaintext2.setText(" 已被选")
        self.plaintext2.setFont(self.QF_state_explain)
        self.plaintext3=QLabel(self)
        self.plaintext3.setGeometry(0.76*Width,(0.059+0.08)*Height,0.15*Width,0.032*Height)
        self.plaintext3.setStyleSheet(self.SS_state_explain)
        self.plaintext3.setText(" 当前选择")
        self.plaintext3.setFont(self.QF_state_explain)

    def setInfBox(self):
        Width=self.Width
        Height=self.Height
        # ---信息标题------------------------------------------
        self.InfTitle_Name=QLabel(self)
        self.InfTitle_Name.setGeometry(0.09*Width,0.28*Height,
                                       0.16*Width,0.05*Height)
        self.InfTitle_Name.setStyleSheet(self.SS_Inf_title)
        self.InfTitle_Name.setText("   姓名：")
        self.InfTitle_Name.setFont(self.QF_Inf_title)
        # ---
        self.InfTitle_Id=QLabel(self)
        self.InfTitle_Id.setGeometry(0.09*Width,0.36*Height,
                                     0.16*Width,0.05*Height)
        self.InfTitle_Id.setStyleSheet(self.SS_Inf_title)
        self.InfTitle_Id.setText("   学号：")
        self.InfTitle_Id.setFont(self.QF_Inf_title)

        # ---信息文本框------------------------------------------
        self.InfBox_Name=QLineEdit(self) 
        self.InfBox_Name.setText("示例：李华") 
        self.InfBox_Name.move(0.3*Width,0.281*Height)  
        self.InfBox_Name.resize(0.6*Width,0.048*Height)
        self.InfBox_Name.setFont(self.QF_Inf_text)
        self.InfBox_Name.setStyleSheet(self.SS_text_Line)
        #self.InfBox_Name.textChanged.connect(self.colorCheckFunc)

        self.InfBox_Id=QLineEdit(self) 
        self.InfBox_Id.setText("示例：XXXXXXXXXXX") 
        self.InfBox_Id.move(0.3*Width,0.361*Height)  
        self.InfBox_Id.resize(0.6*Width,0.048*Height)
        self.InfBox_Id.setFont(self.QF_Inf_text)
        self.InfBox_Id.setStyleSheet(self.SS_text_Line)
        #self.InfBox_ID.textChanged.connect(self.colorCheckFunc)

    def partition(self):# 绘制框线分布
        Width=self.Width
        Height=self.Height
        # ---标题框---------------------------------------------------
        self.part0=QLabel(self)
        self.part0.setGeometry(0.05*Width,0.045*Height,
                               0.52*Width,0.14*Height)
        self.part0.setStyleSheet(self.SS_main_title)
        self.part0.setAlignment(Qt.AlignCenter)
        self.part0.setText(" 自习室预约")
        self.part0.setFont(self.QF_main_title)
        # self.part0title=QLabel(self)
        # self.part0title.setGeometry(0.098*Width,0.06*Height,
        #                             0.43*Width,0.11*Height)
        # self.part0title.setStyleSheet(self.SS_part_title)
        # self.part0title.setText(" 自习室预约")
        # self.part0title.setFont(self.QF_main_title)
        
        # ---信息填写框-----------------------------------------------
        self.part1=QLabel(self)
        self.part1.setGeometry(0.04*Width,0.23*Height,
                               0.92*Width,0.24*Height)
        self.part1.setStyleSheet(self.SS_part_frame)
        self.part1title=QLabel(self)
        self.part1title.setGeometry(0.08*Width,0.21*Height,
                                    0.15*Width,0.04*Height)
        self.part1title.setStyleSheet(self.SS_part_title)
        self.part1title.setText(" 信息填写")
        self.part1title.setFont(self.QF_part_title)
    
        # ---座位选择框------------------------------------------------
        self.part2=QLabel(self)
        self.part2.setGeometry(0.04*Width,0.53*Height,
                               0.92*Width,0.355*Height)
        self.part2.setStyleSheet(self.SS_part_frame)
        self.part1title=QLabel(self)
        self.part1title.setGeometry(0.08*Width,0.51*Height,
                                    0.15*Width,0.04*Height)
        self.part1title.setStyleSheet(self.SS_part_title)
        self.part1title.setText(" 座位选择")
        self.part1title.setFont(self.QF_part_title)
        # ================================================================================================
        # 可滑动区域部分：
    def setMap(self):
        Width=self.Width
        Height=self.Height
        self.map=QScrollArea(self)
        self.map.setGeometry(0.05*Width,0.545*Height,
                             0.9*Width,0.325*Height)
        self.drawMap()
        self.map.setWidget(self.mapContent)


    def drawMap(self):# 绘制座位地图
        self.mapContent=QWidget(self)   
        boxWidth=0.9*self.Width
        boxHeight=0.325*self.Height
        
        seatInf=self.seatInf
        seatOccupied=self.seatOccupied
        

        mapWidth=boxWidth*seatInf["mapSize"][0]
        mapHeight=boxHeight*seatInf["mapSize"][1]
        tableSize=seatInf["tableSize"]
        tablePos=seatInf["tablePos"]
        chairSize=seatInf["chairSize"]
        chairPos=seatInf["chairPos"]

        self.mapContent.setGeometry(0,0,mapWidth,mapHeight) 
        self.mapContent.setMaximumSize(mapWidth,mapHeight)
        self.mapContent.setMinimumSize(mapWidth,mapHeight)
        
        for i in range(0,seatInf["tableNum"]):
            table=QLabel(self.mapContent)
            table.setGeometry(tablePos[i][0]*mapWidth,tablePos[i][1]*mapHeight,
                              tableSize[i][0]*mapWidth,tableSize[i][1]*mapHeight)
            table.setText(seatInf["tableId"][i])
            table.setFont(self.QF_table_name)
            table.setAlignment(Qt.AlignCenter)
            table.setStyleSheet(seatInf["tableSS"][seatInf["tableType"][i]])
            for j in range(0,seatInf["chairNum"][i]):
                chairBnt=QPushButton(self.mapContent)
                chairBnt.setGeometry((tablePos[i][0]+chairPos[i][j][0])*mapWidth,
                                     (tablePos[i][1]+chairPos[i][j][1])*mapHeight,
                                     chairSize[0]*mapWidth,
                                     chairSize[1]*mapHeight)

                chairId=seatInf["tableId"][i]+str(j+1)
                if seatOccupied[chairId]:
                    chairBnt.setStyleSheet(seatInf["chairSS_K"])
                else:
                    chairBnt.setStyleSheet(seatInf["chairSS_W"])

                chairBnt.setProperty("chairId",chairId)
                chairBnt.clicked.connect(self.selectedPos)

    def setBookBtn(self):
        Width=self.Width
        Height=self.Height
        self.selectedBox=QLabel(self)
        self.selectedBox.setGeometry(0.54*Width,(0.92)*Height,0.22*Width,0.05*Height)
        self.selectedBox.setStyleSheet(self.SS_state_explain)
        self.selectedBox.setText(" 当前选择:")
        self.selectedBox.setFont(self.QF_Inf_title)
        
        self.bookBtn=QPushButton(self)
        self.bookBtn.setGeometry(0.79*Width,(0.92)*Height,0.16*Width,0.05*Height)
        self.bookBtn.setStyleSheet(self.SS_book_btn)
        self.bookBtn.setText("预约")
        self.bookBtn.setFont(self.QF_Inf_title)
        self.bookBtn.clicked.connect(self.bookSeat)
# ===========================================================================================
# 函数调用：
myapp = QApplication(sys.argv)
window_main = Window_main(700,840)
window_main.show()
sys.exit(myapp.exec_())




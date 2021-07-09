from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtWidgets import QLabel,QPushButton
from PySide2.QtGui import QIcon,QFont,QPixmap
from PySide2.QtCore import Qt
import sys
sys.path.append("...")
import datetime
from InfOperate import freeSeat,setString

class Window_disp(QWidget):
    def __init__(self,studentName,studentId,bookTime,seatId,Width=700,Height=840):
        super().__init__() 
        self.setWindowTitle("order successfully")
        

        self.studentName=studentName
        self.studentId=studentId
        self.bookTime=bookTime
        self.seatId=seatId
        self.Width=Width
        self.Height=Height

        # path=sys.argv[0]
        # path=path[0:path.rfind("/")]
        self.orderSuccTitlePath="./gallery/order_succ_title.png"
        self.icoPath="./gallery/icon.ico"

        # 字体标签
        title_qf=QFont()
        title_qf.setPointSize(11)
        title_qf.setBold(True)
        title_qf.setFamily("Cambria")
        Inf_qf=QFont()
        Inf_qf.setPointSize(10)
        Inf_qf.setBold(True)
        Inf_qf.setFamily("Cambria")
        matters_qf=QFont()
        matters_qf.setPointSize(10.5)
        matters_qf.setBold(True)
        matters_qf.setFamily("Cambria")
        # ---
        self.QF_part_title=title_qf         # 框标题字体标签
        self.QF_Inf_title=title_qf          # 信息标题字体标签
        self.QF_Inf_text=Inf_qf             # 信息文本字体标签
        self.QF_matters=matters_qf          # 注意事项字体标签

        # 样式表
        self.SS_part_frame="QLabel{background: rgb(245,245,245);color:rgb(92,92,92);border-radius:8px;border: 2.5px solid rgb(122,122,122)}"
        self.SS_part_title="QLabel{background: rgb(245,245,245);color:rgb(92,92,92)}"
        self.SS_Inf_title="QLabel{background: rgb(230,230,230);color:rgb(82,82,82);border-radius:8px}"
        self.SS_text_Line="QLabel{border-radius:3px;background: rgb(205,205,205);color:rgb(82,82,82)}"
        self.SS_book_btn="color:rgb(255,255,255);background: rgb(79,148,204)"

        self.setSize()
        self.setIcon()
        self.setTitle()
        self.partition()
        self.InfDisplay()
        self.mattersDisplay()
        self.setBtn()
    # ================================================================================================
    # 回调函数部分：
    def tempLeave(self):
        if self.tleaveBtn.text()=="暂离":
            setString(self.seatId,"temp")
            nowDate=datetime.datetime.now()
            nowDateStr=nowDate.strftime('%Y-%m-%d %H:%M:%S')
            self.InfBox_Time.setText(nowDateStr) 
            self.tleaveBtn.setText("暂离中")

    def leave(self):
        freeSeat(self.seatId)
        self.close()



    # ================================================================================================
    # 框架构造函数部分：
    def setSize(self):# 调整框架大小
        self.setGeometry(80,80,self.Width,self.Height)
        self.setMaximumSize(self.Width,self.Height)
        self.setMinimumSize(self.Width,self.Height)

    def setIcon(self):# 设置图标
        appIcon=QIcon(self.icoPath)
        self.setWindowIcon(appIcon)

    def setTitle(self):
        Width=self.Width
        Height=self.Height
        self.Imgbox=QLabel(self)
        self.Imgbox.setGeometry(0.24*Width,0.02*Height,
                                0.52*Width,0.18*Height)
        self.Imgpic=QPixmap(self.orderSuccTitlePath)
        self.Imgpic=self.Imgpic.scaled(0.52*Width,0.18*Height)
        self.Imgbox.setPixmap(self.Imgpic)

    def partition(self):# 绘制框线分布
        Width=self.Width
        Height=self.Height
        # ---信息展示框-----------------------------------------------
        self.part1=QLabel(self)
        self.part1.setGeometry(0.04*Width,0.23*Height,
                               0.92*Width,0.40*Height)
        self.part1.setStyleSheet(self.SS_part_frame)
        self.part1title=QLabel(self)
        self.part1title.setGeometry(0.08*Width,0.21*Height,
                                    0.15*Width,0.04*Height)
        self.part1title.setStyleSheet(self.SS_part_title)
        self.part1title.setText(" 个人信息 ")
        self.part1title.setFont(self.QF_part_title)
        # ---注意事项框-----------------------------------------------
        self.part2=QLabel(self)
        self.part2.setGeometry(0.04*Width,0.67*Height,
                               0.92*Width,0.22*Height)
        self.part2.setStyleSheet(self.SS_part_frame)
        self.part2title=QLabel(self)
        self.part2title.setGeometry(0.08*Width,0.65*Height,
                                    0.15*Width,0.04*Height)
        self.part2title.setStyleSheet(self.SS_part_title)
        self.part2title.setText(" 注意事项")
        self.part2title.setFont(self.QF_part_title)

    def InfDisplay(self):
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
        # ---
        self.InfTitle_Time=QLabel(self)
        self.InfTitle_Time.setGeometry(0.09*Width,0.44*Height,
                                     0.16*Width,0.05*Height)
        self.InfTitle_Time.setStyleSheet(self.SS_Inf_title)
        self.InfTitle_Time.setText("   时间：")
        self.InfTitle_Time.setFont(self.QF_Inf_title)
        # ---
        self.InfTitle_Seat=QLabel(self)
        self.InfTitle_Seat.setGeometry(0.09*Width,0.52*Height,
                                     0.16*Width,0.05*Height)
        self.InfTitle_Seat.setStyleSheet(self.SS_Inf_title)
        self.InfTitle_Seat.setText("   座次：")
        self.InfTitle_Seat.setFont(self.QF_Inf_title)

        # ---信息文本框------------------------------------------
        self.InfBox_Name=QLabel(self) 
        self.InfBox_Name.setText(self.studentName) 
        self.InfBox_Name.move(0.3*Width,0.281*Height)  
        self.InfBox_Name.resize(0.6*Width,0.048*Height)
        self.InfBox_Name.setFont(self.QF_Inf_text)
        self.InfBox_Name.setStyleSheet(self.SS_text_Line)
        self.InfBox_Name.setAlignment(Qt.AlignCenter)
        # ---
        self.InfBox_Id=QLabel(self) 
        self.InfBox_Id.setText(self.studentId) 
        self.InfBox_Id.move(0.3*Width,0.361*Height)  
        self.InfBox_Id.resize(0.6*Width,0.048*Height)
        self.InfBox_Id.setFont(self.QF_Inf_text)
        self.InfBox_Id.setStyleSheet(self.SS_text_Line)
        self.InfBox_Id.setAlignment(Qt.AlignCenter)
        # ---
        self.InfBox_Time=QLabel(self) 
        self.InfBox_Time.setText(self.bookTime) 
        self.InfBox_Time.move(0.3*Width,0.441*Height)  
        self.InfBox_Time.resize(0.6*Width,0.048*Height)
        self.InfBox_Time.setFont(self.QF_Inf_text)
        self.InfBox_Time.setStyleSheet(self.SS_text_Line)
        self.InfBox_Time.setAlignment(Qt.AlignCenter)
        # ---
        self.InfBox_Seat=QLabel(self) 
        self.InfBox_Seat.setText(self.seatId) 
        self.InfBox_Seat.move(0.3*Width,0.521*Height)  
        self.InfBox_Seat.resize(0.6*Width,0.048*Height)
        self.InfBox_Seat.setFont(self.QF_Inf_text)
        self.InfBox_Seat.setStyleSheet(self.SS_text_Line)
        self.InfBox_Seat.setAlignment(Qt.AlignCenter)

    def mattersDisplay(self):
        Width=self.Width
        Height=self.Height
        self.m1=QLabel(self) 
        self.m1.setText("1、预约成功后请在30分钟内到达，否则预约信息将失效。") 
        self.m1.setGeometry(0.06*Width,0.71*Height,
                            0.87*Width,0.03*Height)
        self.m1.setStyleSheet("QLabel{color:rgb(82,82,82)}")
        self.m1.setFont(self.QF_matters)

        self.m2=QLabel(self) 
        self.m2.setText("2、进入自习室前请刷校园卡核验信息。") 
        self.m2.setGeometry(0.06*Width,0.75*Height,
                            0.87*Width,0.03*Height)
        self.m2.setStyleSheet("QLabel{color:rgb(82,82,82)}")
        self.m2.setFont(self.QF_matters)

        self.m3=QLabel(self) 
        self.m3.setText("3、如要离开请点击下方“暂离”按钮，否则将释放座位信息。") 
        self.m3.setGeometry(0.06*Width,0.79*Height,
                            0.87*Width,0.03*Height)
        self.m3.setStyleSheet("QLabel{color:rgb(82,82,82)}")
        self.m3.setFont(self.QF_matters)

        self.m4=QLabel(self) 
        self.m4.setText("4、离开、取消预约请点击下方“离开\取消”按钮。") 
        self.m4.setGeometry(0.06*Width,0.83*Height,
                            0.87*Width,0.03*Height)
        self.m4.setStyleSheet("QLabel{color:rgb(82,82,82)}")
        self.m4.setFont(self.QF_matters)

    def setBtn(self):
        Width=self.Width
        Height=self.Height
        self.tleaveBtn=QPushButton(self)
        self.tleaveBtn.setGeometry(0.18*Width,(0.92)*Height,0.2*Width,0.05*Height)
        self.tleaveBtn.setStyleSheet(self.SS_book_btn)
        self.tleaveBtn.setText("暂离")
        self.tleaveBtn.setFont(self.QF_Inf_title)
        self.tleaveBtn.clicked.connect(self.tempLeave)

        Width=self.Width
        Height=self.Height
        self.leaveBtn=QPushButton(self)
        self.leaveBtn.setGeometry((1-0.2-0.18)*Width,(0.92)*Height,0.2*Width,0.05*Height)
        self.leaveBtn.setStyleSheet(self.SS_book_btn)
        self.leaveBtn.setText("离开\取消")
        self.leaveBtn.setFont(self.QF_Inf_title)
        self.leaveBtn.clicked.connect(self.leave)

# ===========================================================================================
# 函数调用：
# myapp = QApplication(sys.argv)
# window_disp = Window_disp("李华","1816000XXXX","2021-05-30 17:04:24","A1",700,840)
# window_disp.show()
# myapp.exec_()


def orderDisplay(studentName,studentId,bookTime,seatId,Width=700,Height=840):
    window_disp = Window_disp(studentName,studentId,bookTime,seatId,Width,Height)
    return window_disp


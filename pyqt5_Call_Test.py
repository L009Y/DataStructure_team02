path = "C:\\Users\\admin\\Desktop\\파이썬\\ui_module\\"
import copy
from data_structure.Queue.queue_plus import *
from information import *
from reservation import *
from table import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 초기 UI 파일 로드
        loadUi(path + 'movie_selection_fixed2.ui', self)
        
        # 스크롤 기능
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.groupBox)
        self.setCentralWidget(scroll_area)
        
        # 버튼 클릭 이벤트 연결 함수 호출
        self.Event_Connect()


# ==============================================================================================
# ==============================================================================================
    # 영화, 관, 시간 선택 함수
    def Movie_Button(self):
        sender = self.sender()
        groupbox = sender.parent()
        time = sender.text()
        movie = Select_Movie.get(groupbox.objectName())
        jangre = Select_Jangre.get(movie)
        
        if isinstance(groupbox, QGroupBox):
            button_y = sender.geometry().y()            # 클릭한 버튼의 y 좌표
            label_theaters = groupbox.findChildren(QLabel)      # 클릭한 버튼의 부모 box
            theater = ""
            for label in label_theaters:
                label_theater_y = label.geometry().y()  # 부모box의 라벨들 중 y 좌표
                distance = abs(button_y - label_theater_y)      # y좌표의 거리 차에 따라 관 결정
                if distance <= 60:                              # Because, 같은 부모box라서 관 분리가 안됨
                    theater = label.text()
                    break

        if movie and theater:
            movie_click_button(movie, jangre, theater, time)    # 1. 영화 이름, 장르, 관, 시간 넣기
            self.change_window()
            self.paint_recommend_seat(jangre, theater)
            self.Exist_Seat(movie, jangre, theater, time)
        
        else:
            print("error")
            
    # ==========================================================================================
    # 좌석 선택 함수
    def Seat_Button(self):
        sender = self.sender()
        name = sender.objectName()
        seat_click_button(name)
        
        self.Full_recommend_seat(temp_Movie.Movie_num, temp_Movie.Jangre, temp_Movie.theater, temp_Movie.time)
        
        self.open_login()
        
    # ==========================================================================================
    # 고객 정보 입력 함수
    def User_Info_Button(self):
        name = self.dialog1.name.text()
        phone = self.dialog1.phone.text()
        passwd = self.dialog1.passwd.text()
        if name == "":
            self.dialog1.close()
        else:
            user_info_click_button(name, phone, passwd)

        global Book_yes_or_no
        if Book_yes_or_no == "예":
            str_movie = repr(temp_Movie.Movie_num)
            name_str = str_movie + ", " + temp_Movie.theater + ", " + temp_Movie.time + ", " + \
            temp_Movie.Seat_name + ", " + temp_Movie.Client_name
            
            if int(str_movie) == 1:
                Book_class1.enqueue(name_str)
            elif int(str_movie) == 2:
                Book_class2.enqueue(name_str)
            elif int(str_movie) == 3:
                Book_class3.enqueue(name_str)
            elif int(str_movie) == 4:
                Book_class4.enqueue(name_str)
            elif int(str_movie) == 5:
                Book_class5.enqueue(name_str)
                
            Book_yes_or_no == "아니오"
            
        # 임시 class 초기화
        temp_Movie.reset()
        
        self.change_window_reverse()
    
# ==============================================================================================
# ==============================================================================================
    # 좌석 gui를 열 때, 추천 자리를 색칠하도록 하는 함수
    def paint_recommend_seat(self, jangre, theater):
        recommend_Seats = recommend_Seat_table.get((jangre, theater))
        for recommend_Seat in recommend_Seats:
            target_button = self.findChild(QPushButton, recommend_Seat)
            if target_button:
                target_button.setStyleSheet(recommend_Seat_Color[jangre])

    # ==========================================================================================
    # 좌석 gui를 열 때, 이미 예매된 좌석의 경우 클릭이 안되도록 비활성화하는 함수
    def Exist_Seat(self, movie, jangre, theater, time):
        movie -= 1
        recommend_Seats = recommend_Seat_table.get((jangre, theater))
        linkedLists = [Suzume, Exorcist, Lala_Land, John_Wick_4, Guardians_of_the_Galaxy3]
        soldOut_Seats = []

        if (linkedLists[movie].head == None):
            return False
            
        for i in range(linkedLists[movie].count_nodes()):
            node = linkedLists[movie].get(i)

            if (node.time == time and node.theater == theater):
                seatInfo = {
                    "seatName": node.Seat_name,
                    "seatTheater": node.theater,
                    "seatTime": node.time
                }
                soldOut_Seats.append(seatInfo)
            
        for soldOut_Seat in soldOut_Seats:
            target_button = self.findChild(QPushButton, soldOut_Seat['seatName'])
            if target_button:
                target_button.setEnabled(False)
            for recommend_Seat in recommend_Seats:
                temp_recommend_seat = self.findChild(QPushButton, recommend_Seat)
                if target_button == temp_recommend_seat:
                    target_button.setStyleSheet("background-color: rgb(188, 188, 188);" + recommend_Seat_Color[jangre])
                    break
                target_button.setStyleSheet("background-color: rgb(188, 188, 188);")
   
    # ==========================================================================================
    # 예약할 것 인지 질문
    def Full_recommend_seat(self, movie, jangre, theater, time):
        recommend_seats = recommend_Seat_table.get((jangre, theater))
        
        global count_recommend_seat
        count_recommend_seat = len(recommend_seats)
        
        global count_node
        count_node = 0

        movie -= 1
        linkedLists = [Suzume, Exorcist, Lala_Land, John_Wick_4, Guardians_of_the_Galaxy3]

        if (linkedLists[movie].head == None):
            return False
            
        for i in range(linkedLists[movie].count_nodes()):
            node = linkedLists[movie].get(i)
            if (node.time == time and node.theater == theater):
                count_node += 1
                if count_recommend_seat == count_node:
                    break
                
        if count_recommend_seat == count_node:
            self.dialog2 = QDialog(self)
            loadUi(path + 'book_seat.ui', self.dialog2)
            self.dialog2.button_yes.clicked.connect(self.yes_or_no)
            self.dialog2.button_no.clicked.connect(self.yes_or_no)
            self.dialog2.exec_()
            
    # ==========================================================================================    
    # 예, 아니오 버튼 클릭 시, 예약 여부 창 닫기
    def yes_or_no(self):
        sender = self.dialog2.sender()
        
        # 예약 여부 클래스 변수
        global Book_yes_or_no
        Book_yes_or_no = sender.text()
        
        self.dialog2.close()
    
# ==============================================================================================
# ==============================================================================================
    # 구글처럼 창 변경 - 관에 따라 ui 창 변경
    def change_window(self):
        # 기존 위젯 삭제
        self.centralWidget().setParent(None)
        
        # 관에 따른 새로운 UI 파일 로드
        t = temp_Movie.theater
        t = t[0]
        if t == '1':
            loadUi(path + 'Theater_1.ui', self)
            self.Event_Connect_1()
        elif t == '2':
            loadUi(path + 'Theater_2.ui', self)
            self.Event_Connect_2()
        elif t == '3':
            loadUi(path + 'Theater_3.ui', self)
            self.Event_Connect_3()
        elif t == '4':
            loadUi(path + 'Theater_4.ui', self)
            self.Event_Connect_4()
        elif t == '5':
            loadUi(path + 'Theater_5.ui', self)
            self.Event_Connect_5()
            
        self.Back.clicked.connect(self.Back_widget)
            
    # ==========================================================================================
    # 다시 제일 처음 창으로 변경
    def change_window_reverse(self):
        # 새 창 닫기
        self.dialog1.close()
        
        # 기존 위젯 삭제
        self.centralWidget().setParent(None)
        
        # 새로운 UI 파일 로드
        loadUi(path + 'movie_selection_fixed2.ui', self)
        
        # 스크롤 기능
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.groupBox)
        self.setCentralWidget(scroll_area)
        
        # 이벤트 연결 함수
        self.Event_Connect()

    # ==========================================================================================
    # naver처럼 새로운 창 열기
    # 고객 정보 입력 창 열기
    def open_login(self):
        self.dialog1 = QDialog(self)
        loadUi(path + 'login_fixed1.ui', self.dialog1)
        self.dialog1.user_button.clicked.connect(self.User_Info_Button)
        self.dialog1.exec_()    
        
    # ==========================================================================================
    # 뒤로가기 함수
    def Back_widget(self):
        # 기존 위젯 삭제
        self.centralWidget().setParent(None)
        
        # 새로운 UI 파일 로드
        loadUi(path + 'movie_selection_fixed2.ui', self)
        
        # 스크롤 기능
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.groupBox)
        self.setCentralWidget(scroll_area)
        
        # 이벤트 연결 함수
        self.Event_Connect()
        
    # ==========================================================================================
    # 노드 관리 gui 열기
    def Manage_Node(self):
        # 기존 위젯 삭제
        self.centralWidget().setParent(None)
        
        # 새로운 UI 파일 로드
        loadUi(path + 'Admin.ui', self)
        self.Back.clicked.connect(self.Back_widget)
        self.Check.clicked.connect(self.delete_node)
        
        linkedLists = [Suzume, Exorcist, Lala_Land, John_Wick_4, Guardians_of_the_Galaxy3]
        for linkedList in linkedLists:
            if linkedList.head == None:
                continue
            
            for k in range(linkedList.count_nodes()):
                node = linkedList.get(k)
                str_info = repr(node.Movie_num) + ", " + node.theater + ", " + node.time + ", " + node.Seat_name + ", " + node.Client_name
                self.show_node.append(str_info)
        
    # ==========================================================================================
    # 노드의 고객 이름 정보 입력 받는 함수
    def delete_node(self):
        Input_name = self.delete_name.text()
        linkedLists = [Suzume, Exorcist, Lala_Land, John_Wick_4, Guardians_of_the_Galaxy3]
        linkedQueues = [Book_class1, Book_class2, Book_class3, Book_class4, Book_class5]
        
        for i in range(5):
            if linkedLists[i].head == None:
                continue

            for k in range(linkedLists[i].count_nodes()):
                node = linkedLists[i].get(k)
                str_node = repr(node.Movie_num) + ", " + node.theater + ", " + node.time + ", " + node.Seat_name + ", " + node.Client_name
                if Input_name == str_node:
                    pre_data = linkedQueues[i].peek()
                    
                    if linkedQueues[i].head != None and pre_data[0:12] == str_node[0:12]:
                        temp_node = copy.deepcopy(node)
                        temp_node.Client_name = pre_data[18:]
                        linkedLists[i].append(temp_node)
                        # 코드 보류
                        linkedQueues[i].dequeue()
                    
                    linkedLists[i].delete(node)

        self.show_node.clear()
        self.show_node.append('다시 나갔다 들어오세요.')
        
        # --------------------------------------------------------------------------------------
        # 노드 삭제 후, 예약
        

# ==============================================================================================
# ==============================================================================================
    # 이벤트 연결 함수 : 위젯 양이 많아 외관 상 밑으로 보냄.
    # 영화 선택 Gui에서, 각 버튼에 이벤트를 연결하는 함수
    def Event_Connect(self):
        time_buttons = [
            self.Time1, self.Time2, self.Time3, self.Time4, self.Time5, self.Time6,     \
            self.Time7, self.Time8, self.Time9, self.Time10, self.Time11, self.Time12 ]
        
        for button in time_buttons:
            button.clicked.connect(self.Movie_Button)
        self.Admin.clicked.connect(self.Manage_Node)

    # 1관 Gui를 열었을 때, 각 버튼에 이벤트를 연결하는 함수
    def Event_Connect_1(self):
        seat_button1 = [
            self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8,             \
            self.A9, self.A10, self.A11, self.A12, self.A15, self.A16,                          \
            self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8,             \
            self.B9, self.B10, self.B11, self.B12, self.B13, self.B14, self.B15, self.B16,      \
            self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8,             \
            self.C9, self.C10, self.C11, self.C12, self.C13, self.C14, self.C15, self.C16,      \
            self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8,             \
            self.D9, self.D10, self.D11, self.D12, self.D13, self.D14, self.D15, self.D16,      \
            self.E3, self.E4, self.E5, self.E6, self.E7,                            \
            self.E8, self.E9, self.E10, self.E11, self.E12, self.E13, self.E14,     \
            self.F3, self.F4, self.F5, self.F6, self.F7,                            \
            self.F8, self.F9, self.F10, self.F11, self.F12, self.F13, self.F14,     \
            self.G3, self.G4, self.G5, self.G6, self.G7,                            \
            self.G8, self.G9, self.G10, self.G11, self.G12, self.G13, self.G14,     \
            self.H3, self.H4, self.H5, self.H6, self.H7,                            \
            self.H8, self.H9, self.H10, self.H11, self.H12, self.H13, self.H14,     \
            self.I3, self.I4, self.I5, self.I6, self.I7,                            \
            self.I8, self.I9, self.I10, self.I11, self.I12, self.I13, self.I14,     \
            self.J3, self.J4, self.J5, self.J6, self.J7,                            \
            self.J8, self.J9, self.J10, self.J11, self.J12, self.J13, self.J14 ]
    
        for seat in seat_button1:
            seat.clicked.connect(self.Seat_Button)
        
    # ==========================================================================================
    # 2관 Gui를 열었을 때, 각 버튼에 이벤트를 연결하는 함수
    def Event_Connect_2(self):
        seat_button2 = [
            self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9, self.A10, self.A11, self.A12,              \
            self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, self.B9, self.B10, self.B11, self.B12, self.B13,    \
            self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8, self.C9, self.C10, self.C11, self.C12, self.C13,    \
            self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8, self.D9, self.D10, self.D11, self.D12, self.D13,    \
            self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9, self.E10, self.E11, self.E12, self.E13,    \
            self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8, self.F9, self.F10, self.F11, self.F12, self.F13,    \
            self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9, self.G10, self.G11, self.G12, self.G13,    \
            self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8, self.H9, self.H10, self.H11, self.H12, self.H13,    \
            self.I1, self.I2, self.I3, self.I4, self.I5, self.I6, self.I7, self.I8, self.I9, self.I10, self.I11, self.I12, self.I13 ]
        
        for seat in seat_button2:
            seat.clicked.connect(self.Seat_Button)
            
    # ==========================================================================================
    # 3관 Gui를 열었을 때, 각 버튼에 이벤트를 연결하는 함수
    def Event_Connect_3(self):
        seat_button3 = [
            self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9,    \
            self.A10, self.A11, self.A12, self.A13, self.A16, self.A17,                         \
            self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, self.B9,    \
            self.B10, self.B11, self.B12, self.B13, self.B14, self.B15, self.B16, self.B17,     \
            self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8, self.C9,    \
            self.C10, self.C11, self.C12, self.C13, self.C14, self.C15, self.C16, self.C17,     \
            self.D3, self.D4, self.D5, self.D6, self.D7, self.D8, self.D9,                      \
            self.D10, self.D11, self.D12, self.D13, self.D14, self.D15, self.D16,               \
            self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9,                      \
            self.E10, self.E11, self.E12, self.E13, self.E14, self.E15, self.E16,               \
            self.F3, self.F4, self.F5, self.F6, self.F7, self.F8, self.F9,                      \
            self.F10, self.F11, self.F12, self.F13, self.F14, self.F15, self.F16,               \
            self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9,                      \
            self.G10, self.G11, self.G12, self.G13, self.G14, self.G15, self.G16 ]
        
        for seat in seat_button3:
            seat.clicked.connect(self.Seat_Button)

    # ==========================================================================================
    # 4관 Gui를 열었을 때, 각 버튼에 이벤트를 연결하는 함수
    def Event_Connect_4(self):
        seat_button4 = [
            self.A1, self.A2, self.A3, self.A6, self.A7, self.A8, self.A9, self.A10, self.A11, self.A12, self.A13,  \
            self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8,     \
            self.B9, self.B10, self.B11, self.B12, self.B13, self.B14,                  \
            self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8,     \
            self.C9, self.C10, self.C11, self.C12, self.C13, self.C14, self.C15,        \
            self.D1, self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8,     \
            self.D9, self.D10, self.D11, self.D12, self.D13, self.D14, self.D15,        \
            self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8,     \
            self.E9, self.E10, self.E11, self.E12, self.E13, self.E14, self.E15,        \
                
            self.F4, self.F5, self.F6, self.F7, self.F8, self.F9, self.F10, self.F11, self.F12, self.F13, self.F14, \
            self.G4, self.G5, self.G6, self.G7, self.G8, self.G9, self.G10, self.G11, self.G12, self.G13,           \
            self.H4, self.H5, self.H6, self.H7, self.H8, self.H9, self.H10, self.H11, self.H12, self.H13, self.H14, \
            self.I4, self.I5, self.I6, self.I7, self.I8, self.I9, self.I10, self.I11, self.I12, self.I13, self.I14, \
            self.J4, self.J5, self.J6, self.J7, self.J8, self.J9, self.J10, self.J11, self.J12, self.J13, self.J14, \
            
            self.K1, self.K2, self.K4, self.K5, self.K6, self.K7, self.K8,          \
            self.K9, self.K10, self.K11, self.K12, self.K13, self.K14, self.K15,    \
            self.L1, self.L2, self.L4, self.L5, self.L6, self.L7, self.L8,          \
            self.L9, self.L10, self.L11, self.L12, self.L13, self.L14, self.L15,    \
            self.M1, self.M2,self.M4, self.M5, self.M6, self.M7, self.M8,           \
            self.M9, self.M10, self.M11, self.M12, self.M13, self.M14,              \
            self.N1, self.N2,self.N4, self.N5, self.N6, self.N7, self.N8,           \
            self.N9, self.N10, self.N11, self.N12, self.N13, self.N14,              \
            self.O1, self.O2,self.O4, self.O5, self.O6, self.O7, self.O8,           \
            self.O9, self.O10, self.O11, self.O12, self.O13, self.O14,              \
            self.P1, self.P2,self.P4, self.P5, self.P6, self.P7, self.P8,           \
            self.P9, self.P10, self.P11, self.P12, self.P13, self.P14,              \
            self.Q1, self.Q2,self.Q4, self.Q5, self.Q6, self.Q7, self.Q8,           \
            self.Q9, self.Q10, self.Q11, self.Q12, self.Q13, self.Q14 ]
        
        for seat in seat_button4:
            seat.clicked.connect(self.Seat_Button)

    # ==========================================================================================
    # 5관 Gui를 열었을 때, 각 버튼에 이벤트를 연결하는 함수
    def Event_Connect_5(self):
        seat_button5 = [
            self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9, self.A10, self.A11, self.A12,  \
            self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, \
            self.B9, self.B10, self.B11, self.B12, self.B13, self.B14,              \
            self.C1, self.C2, self.C3, self.C4, self.C5, self.C6, self.C7, self.C8, \
            self.C9, self.C10, self.C11, self.C12, self.C13, self.C14,              \
            self.D2, self.D3, self.D4, self.D5, self.D6, self.D7, self.D8,  \
            self.D9, self.D10, self.D11, self.D12, self.D13, self.D14,      \
            self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8,  \
            self.E9, self.E10, self.E11, self.E12, self.E13, self.E14,      \
            self.F1, self.F2, self.F3, self.F4, self.F5, self.F6, self.F7, self.F8, self.F9, self.F10, self.F11,    \
            self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9, self.G10, self.G11,    \
            self.H1, self.H2, self.H3, self.H4, self.H5, self.H6, self.H7, self.H8, self.H9, self.H10, self.H11,    \
            self.I1, self.I2, self.I3, self.I4, self.I5, self.I6, self.I7, self.I8, self.I9, self.I10, self.I11,    \
            self.J1, self.J2, self.J3, self.J4, self.J5, self.J6, self.J7, self.J8, self.J9, self.J10, self.J11,    \
            self.K1, self.K2, self.K3, self.K4, self.K5, self.K6, self.K7,  \
            self.K8, self.K9, self.K10, self.K11, self.K13, self.K14,       \
            self.L1, self.L2, self.L3, self.L4, self.L5, self.L6, self.L7,  \
            self.L8, self.L9, self.L10, self.L11, self.L13, self.L14,       \
            self.M1, self.M2, self.M3, self.M4, self.M5, self.M6, self.M7,  \
            self.M8, self.M9, self.M10, self.M11, self.M13, self.M14,       \
            self.N1, self.N2, self.N3, self.N4, self.N5, self.N6, self.N7,  \
            self.N8, self.N9, self.N10, self.N11, self.N13, self.N14 ]
        
        for seat in seat_button5:
            seat.clicked.connect(self.Seat_Button)
            
# ==============================================================================================
# ==============================================================================================

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
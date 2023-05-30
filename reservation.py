from data_structure.Linked_List import *
from data_structure.Linked_Queue import *
from information import *
import copy

Book_class1 = List_Queue()  # 스즈메
Book_class2 = List_Queue()  # 엑소시스트
Book_class3 = List_Queue()  # 라라랜드
Book_class4 = List_Queue()  # 존 윅 4
Book_class5 = List_Queue()  # 가오갤3
Book_yes_or_no = "아니오"
count_node = 0
count_recommend_seat = 0
                            
Suzume = linked_list()       # 외국자막
Exorcist = linked_list()     # 공포
Lala_Land = linked_list()    # 음악
John_Wick_4 = linked_list()  # 액션
Guardians_of_the_Galaxy3 = linked_list()     # sf

# 임시 Movie class
temp_Movie = Movie()

# 영화 선택 button을 click 시, temp_Movie에 영화, 장르, 관, 시간 정보 저장
def movie_click_button(movie, jangre, theater, time):
    temp_Movie.Movie_num = movie
    temp_Movie.Jangre = jangre
    temp_Movie.theater = theater
    temp_Movie.time = time

# 좌석 선택 button을 click 시, 좌석 정보 저장
def seat_click_button(seat):
    temp_Movie.Seat_name = seat
    
# 고객 정보 입력 button을 click 시, 마지막 정보까지 채우고, 영화 이름에 맞게 노드 추가 및 임시 class 리셋
def user_info_click_button(name, number, passwd):
    temp_Movie.Client_name = name
    temp_Movie.Client_number = number
    temp_Movie.passwd = passwd
    copy_Movie = copy.deepcopy(temp_Movie)      # 깊은 복사
    temp_name = temp_Movie.Movie_num
    
    # 임시 class를 실제 영화에 따른 노드로 추가
    if temp_name == 1:
        Suzume.append(copy_Movie)
    elif temp_name == 2:
        Exorcist.append(copy_Movie)
    elif temp_name == 3:
        Lala_Land.append(copy_Movie)
    elif temp_name == 4:
        John_Wick_4.append(copy_Movie)
    elif temp_name == 5:
        Guardians_of_the_Galaxy3.append(copy_Movie)
    else:
        print("영화 없음!")
from data_structure.LinkedList.Linked_List import *
from information import *
                            
Suzume = LinkedList()       #외국 자막
Exorcist = LinkedList()     #공포
Lala_Land = LinkedList()    #음악 영화
John_Wick_4 = LinkedList()  #액션
Guardians_of_the_Galaxy3 = LinkedList()     #영상미 sf

#임시 Movie class
temp_Movie = Movie()

#영화 선택 button을 click 시, temp_Movie에 영화, 장르, 관, 시간 정보 저장
def movie_click_button(movie, jangre, theater, time):
    temp_Movie.set_Movie(movie, jangre, theater, time)

#좌석 GUI를 보여주기 전, 장르과 관에 따른 추천 자리를 저장 및 좌석 GUI 색칠
def show_recommend_seat():
    temp_jangre = temp_Movie.get_Jangre()
    temp_theater = temp_Movie.get_Theater()
    temp_re_seat = recommend_Seat_table.get((temp_jangre, temp_theater))
    temp_Movie.set_recommend_Seat(temp_re_seat)

#좌석 선택 button을 click 시, 좌석 정보 저장
def seat_click_button(seat):
    temp_Movie.set_Seat(seat)
    
#고객 정보 입력 button을 click 시, 
def User_Info_click_button(name, number, unique, passwd):
    temp_Movie.set_User_Info(name, number, unique, passwd)
    temp_name = temp_Movie.get_M_name()
    #임시 class를 실제 영화에 따른 노드로 추가
    if temp_name == 'Suzume':
        Suzume.append(temp_Movie)
    elif temp_name == 'Exorcist':
        Exorcist.append(temp_Movie)
    elif temp_name == 'Lala_Land':
        Lala_Land.append(temp_Movie)
    elif temp_name == 'John_Wick_4':
        John_Wick_4.append(temp_Movie)
    elif temp_name == 'Guardians_of_the_Galaxy3':
        Guardians_of_the_Galaxy3.append(temp_Movie)
    else:
        print("영화 없음!")
    
    #임시 class 초기화
    temp_Movie.reset()
    
    
movie_click_button("d", "c", "a", "h")
seat_click_button("4444")
temp_Movie.set_User_Info("bbbb", "ddddd", "ddada")
temp_Movie.display()

temp_re_seat = recommend_Seat_table.get(("공포", "2관"))
print(temp_re_seat)
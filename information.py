class Client:
    def __init__(self, name, number, unique, passwd):
        self.Client_name = name
        self.Client_number = number
        self.Client_unique = unique       # 0 : 없음, 1 : 장애인, 2 : 국가 유공자
        self.passwd = passwd

class Seat(Client):
    def __init__(self, name, re_seat):
        super().__init__("", "", 0, "")
        self.Seat_name = name
        self.recommend_Seat = re_seat

class Movie(Seat):
    def __init__(self):
        super().__init__("", "")
        self.Movie_name = ""
        self.Jangre = ""
        self.theater = ""
        self.time = ""
        
    def get_M_name(self):
        return self.Movie_name
    
    def get_Jangre(self):
        return self.Jangre
    
    def get_Theater(self):
        return self.theater
    
    def get_Seat(self):
        return self.Seat_name
    
    def set_Movie(self, movie, jangre, theater, time):
        self.Movie_name = movie
        self.Jangre = jangre
        self.theater = theater
        self.time = time

    def set_Seat(self, seat):
        self.Seat_name = seat
        
    def set_recommend_Seat(self, re_seat):
        self.recommend_Seat = re_seat
        
    def set_User_Info(self, name, number, unique):
        self.Client_name = name
        self.Client_number = number
        self.Client_unique = unique
        
    def display(self):
        print(self.Movie_name)
        print(self.Jangre)
        print(self.theater)
        print(self.time)
        print(self.Seat_name)
        print(self.recommend_Seat)
        print(self.Client_name)
        
        
#Suzume                         외국 자막
#Exorcist                       공포
#Lala_Land                      음악 영화
#John_Wick_4                    액션
#Guardians_of_the_Galaxy3       영상미 sf

recommend_Seat_table = {
    ("외국자막", "1관"): "",
    ("외국자막", "2관"): "",
    ("외국자막", "3관"): "",
    ("외국자막", "4관"): "",
    ("외국자막", "5관"): "",
    ("공포", "1관"): "",
    ("공포", "2관"): "ㅇㅇㅇㅇ",
    ("공포", "3관"): "",
    ("공포", "4관"): "",
    ("공포", "5관"): "",
    ("음악", "1관"): "",
    ("음악", "2관"): "",
    ("음악", "3관"): "",
    ("음악", "4관"): "",
    ("음악", "5관"): "",
    ("액션", "1관"): "",
    ("액션", "2관"): "",
    ("액션", "3관"): "",
    ("액션", "4관"): "",
    ("액션", "5관"): "",
    ("sf", "1관"): "",
    ("sf", "2관"): "",
    ("sf", "3관"): "",
    ("sf", "4관"): "",
    ("sf", "5관"): "",
}
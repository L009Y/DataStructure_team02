# -------------------------------
# Movie
# 영화 미정 : -1 (초기값)
# Suzume : 1
# Exorcist : 2
# Lala_Land : 3
# John_Wick_4 : 4
# Guardians_of_the_Galaxy3 : 5
# -------------------------------
# Jangre
# Suzume : 외국자막
# Exorcist : 공포
# Lala_Land : 음악
# John_Wick_4 : 액션
# Guardians_of_the_Galaxy3 : sf
# -------------------------------

class Movie:
    def __init__(self):
        self.Movie_num = -1
        self.Jangre = ""
        self.theater = ""
        self.time = ""
        # ------------------------
        self.Seat_name = ""
        # ------------------------
        self.Client_name = ""
        self.Client_number = ""
        self.passwd = ""
        
    def display(self):
        print(self.Movie_num)
        print(self.Jangre)
        print(self.theater)
        print(self.time)
        print(self.Seat_name)
        print(self.Client_name)
        
    def reset(self):
        self.Movie_num = -1
        self.Jangre = ""
        self.theater = ""
        self.time = ""
        self.Seat_name = ""
        self.Client_name = ""
        self.Client_number = ""
        self.passwd = ""

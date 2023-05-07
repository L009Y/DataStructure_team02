import hashlib

def signUp():
    username = input("사용할 아이디를 입력하세요. : ")
    password = input("사용할 비밀번호를 입력하세요. : ")
    passwordCheck = input("사용할 비밀번호를 한번 더 입력하세요. : ")
    name = input("사용할 이름을 입력하세요. : ")
    
    with open("username.txt",'r') as k:
        usernamesLine = k.read()
        usernames = usernamesLine.strip().split()
    
    if username in usernames:
        print("중복된 아이디가 있습니다.")
        signUp()          
    
    elif(password != passwordCheck):
        print("비밀번호가 틀립니다.")
        signUp()
    
    else:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
    
        with open("members.txt","a") as f:
            f.write(f"{username} {password_hash} {name}\n")
        with open("username.txt","a") as t:
            t.write(f"{username} ")
        
        print("회원가입 완료")
def login():
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    with open("members.txt","r") as f:
        members = f.readlines()
    
    for member in members:
        member = member.strip().split()
        if member[0] == username and member[1] == password_hash:
            print("로그인 완료")
            return #영화 선택하는 화면으로
    
    print("아이디 혹은 비밀번호가 일치하지 않습니다.")
    login()    
        
        
        
login()
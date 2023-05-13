from bplustree import BPlusTree

# B+tree 인스턴스 생성
bptree = BPlusTree(5)

# 예매 정보 추가
bptree[100] = {'movie_title': 'Avengers: Endgame', 'seat': 'A5'}
bptree[200] = {'movie_title': 'Joker', 'seat': 'B3'}
bptree[300] = {'movie_title': 'Frozen II', 'seat': 'C2'}

# 예매 정보 조회
print(bptree[100])  # {'movie_title': 'Avengers: Endgame', 'seat': 'A5'}
print(bptree[200])  # {'movie_title': 'Joker', 'seat': 'B3'}
print(bptree[300])  # {'movie_title': 'Frozen II', 'seat': 'C2'}

# 예매 정보 삭제
del bptree[200]

# 예매 정보 업데이트
bptree[100] = {'movie_title': 'Avengers: Infinity War', 'seat': 'A5'}

# B+tree 순회
for key, value in bptree.items():
    print(key, value)

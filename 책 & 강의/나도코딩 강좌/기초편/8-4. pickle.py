import pickle
# 쓰기, pickle은 binary type을 지정해야함, 인코딩 설정은 불필요
profile_file = open("profile.pickle", "wb") 
profile = {"이름": "김대희", "나이": 23, "취미":["게임", "야구", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

# 읽기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

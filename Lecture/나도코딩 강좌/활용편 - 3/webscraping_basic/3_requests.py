import requests


# res = requests.get("http://naver.com")
# print("응답코드:", res.status_code) # 200이면 정상
# # 403: 페이지에 접근할 권한이 없음

# if res.status_code == requests.codes.ok: # 200
#     print("정상입니다")
# else:
#     print("에러가 발생하였습니다 [에러코드:", res.status_code,']')



# res.raise_for_status() # 오류가 발생했을 때, 프로그램을 바로 종료 시킴
# 결국 아래 두 문장은 항상 쌍으로 사용
res = requests.get("http://google.com")
res.raise_for_status()
print(len(res.text))

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text) # 파일로 만듦
from travel import *
# import all을 하더라도 공개범위에 속하지 않는 것들은 import 안됨
# 패키지 내 __init__에서 __all__을 통해 베트남 파일을 지정
tripto = vietnam.vietnampackage()
tripto.detail()



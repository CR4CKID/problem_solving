import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv # as 뒤에 mv를 붙이면, mv를 통해 모듈 호출 가능
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # from import를 통해 바로 사용 가능
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price_soldier, price_morning # 특정 함수만 import 가능

from theater_module import price_soldier as pc
pc(5)
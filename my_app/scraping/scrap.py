import requests
from bs4 import BeautifulSoup

BASE_URL = "https://auto.naver.com/car" # 네이버 자동차 홈에서 자동차 리스트를 볼 수 있는 사이트의 base

LIST_URL = f"{BASE_URL}/mainList.nhn" # 리스트 페이지 URL
DOMESTIC_URL = f"{BASE_URL}/mainList.nhn?importYn=N" #&page=2
IMPORT_URL = f"{BASE_URL}/mainList.nhn?importYn=Y"

def get_page(page_url):
    """
    get_page 함수는 페이지 URL 을 받아 해당 페이지를 가져오고 파싱한 두 결과들을 라턴하는 함수
    """
    page = requests.get(LIST_URL) # soup: BeautifulSoup 으로 파싱한 객체
    soup = BeautifulSoup(page.content,'html.parser') # page: requests 을 통해 받은 페이지 (requests 에서 사용하는 response 객체

    return soup, page

# def get_list(origin, page=None):
#     # origin 은 국산차와 수입차를 구분하기 위함으로, 국산 = N, 수입 = Y
#     ORIGIN_URL = f"{BASE_URL}/mainList.nhn?importYn={origin}"

#     soup, page = get_page(ORIGIN_URL)

#     return 

# "https://auto.naver.com/car/carKindType.nhn?carKndCd=3&importYn=N&page=1"
s, p = get_page(LIST_URL)
a = s.find('span',{"class" : "cont"})
# for n in a:
#     print(n.get_text())
# b = a.find(class_ = "box")
# c = b.text

print(a.text)
# print(page.text)


# """
# "https://auto.naver.com/car/mainList.nhn"
# "https://auto.naver.com/car/mainList.nhn?importYn=N" # 국내차 
# "https://auto.naver.com/car/mainList.nhn?importYn=Y" # 수입차

# class = "model_ct"
# """
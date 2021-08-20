##README

#Home-cooked meals recommendation

Objective
집 냉장고에 있는 재료로 만들 수 있는 집밥 목록을 추천해주는 프로그램

Instructions
[Random_main.py]
1. pip install openpyxl
2. RandomMenu class의 init : excel_path 변수 내 local경로 수정 (엑셀 저장 경로)

[집밥리스트.xlsx]
1. 엑셀 Random_List sheet에는 집밥 및 재료를 keep update
2. 엑셀 Have sheet에는 냉장고 재료들 keep update

개발환경
Python 3.6

Enhancement Plan
Excel에 데이터 maintain이 아닌 집밥 사이트를 크롤링해서 더 많은 집밥 리스트를 받을 수 있도록 개선 예정.
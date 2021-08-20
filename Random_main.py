from openpyxl import load_workbook


class RandomMenu:
    def __init__(self):
        """엑셀에 작성된 집밥리스트와 냉장고 재료 데이터를 읽어서 리스트화 함"""
        print("self __init__")
        excel_path=('D:\Dev_Application\Python36_work\MealRandom\집밥리스트.xlsx')
        load_excel=load_workbook(excel_path,data_only=True)
        self.print_randomlist=load_excel['Random_List'] #랜덤 dish 리스트
        self.print_havelist=load_excel['Have'] #냉장고 재료 리스트

    def __del__(self):
        print("self __del__")

    def get_menu_list(self,seltype):   
        """냉장고 있는재료와 필요한 재료 간에 비교하여 하나라도 있으면 추천 메뉴로 출력"""
        all_have_list=[] #냉장고 재료 엑셀 전체 읽기 : all_have_list[N][1]
        have_list=set() #냉장고 재료 프로그램 맵핑 값 : set화
        all_random_list=[]
        sel_item_list=[]
        
        for row in self.print_havelist: #냉장고에 있는 재료를 리스트화
            row_value=[]
            for cell in row:
                row_value.append(cell.value) #각 행의 값을 리스트화
            all_have_list.append(row_value) #저장한 행을 열 (*N)만큼 append
            
        for i in all_have_list:
            have_list.add(i[1])

        for row in self.print_randomlist: #랜덤음식목록 리스트화
            row_value=[]
            for cell in row:
                row_value.append(cell.value) #각 행의 값을 리스트화
            all_random_list.append(row_value) #저장한 행을 열 (*N)만큼 append

        for i in all_random_list:
            if i[1]==seltype:
                dish=i[0] #해당 요리이름
                items=i[2] #해당 메뉴 요리에 필요한 재료
                
                if items==None:
                    sel_item_list=['없음']
                    items='필요한 재료없음'
                else:
                    items=items.replace(' ','')
                    sel_item_list=items.split(',') #랜덤 dish에 필요한 재료를 리스트화함.
                    
                temp_dish='' #dish가 변경되면 줄바꿈, 등 식별하는 역할.
                
                for j in sel_item_list: #선택된 dish의 재료 읽기
                    if (j in have_list) or (j == '없음'): #dish를 만들 수 있는 재료가 냉장고에 있는지?
                        if temp_dish!=dish:
                           print('\n') 
                           print('추천 요리 -> '+dish+':'+items+' / 냉장고에 있는 재료 : '+j,end="")
                           
                        else :
                            print(', '+j,end="")
                        temp_dish=dish
        print('\n')
                            
    
        
if __name__=='__main__':
    print("Choose one : Side, Soup, Special, Noddle ")
    seltype=input()
    print("selected value is : {}".format(seltype))
    a=RandomMenu()
    a.get_menu_list(seltype)



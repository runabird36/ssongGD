


'''
Step 01. Make outer func + 파라미터로 꾸밈을 당하는 함수 받앙오고
Step 02. Make inner func (꾸밈을 받는 함수의 한가운데를 꾸밀수는 없다)
Step 03. return inner func
'''

def postfix_decorator(func):
    def aa():
        func()
        print("Created by SongTaiYeong")
    return aa


'''
Step 04. 꾸밀 함수 위에, @ outer func
'''
@ postfix_decorator
def print_first():
    print(111111)


@ postfix_decorator
def print_second():
    print(2222222)





print_first()
print_second()

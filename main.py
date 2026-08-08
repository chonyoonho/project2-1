# main.py

def start_program():
    print("--- 환영합니다! 파이썬 프롬프트 프로그램입니다 ---")
    
    while True:
        # 사용자로부터 입력을 받습니다.
        user_input = input("명령어를 입력하세요 (종료하려면 'exit' 입력): ")
        
        if user_input.lower() == 'exit':
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print(f"입력하신 내용은 '{user_input}'이군요!")

if __name__ == "__main__":
    start_program()
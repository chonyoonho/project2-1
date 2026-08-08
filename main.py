import json
import os

# 파일 경로 설정
DATA_FILE = 'prompts.json'

# 1. 기본 데이터 (파일이 없을 경우 사용)
default_prompts = [
    {"title": "블로그 포스팅 생성", "content": "주제에 맞는 블로그 글을 서론, 본론, 결론으로 써줘.", "category": "텍스트 생성", "favorite": True},
    {"title": "실사 이미지 생성", "content": "8k resolution, photorealistic, cinematic lighting...", "category": "이미지 생성", "favorite": False},
    {"title": "파이썬 튜터 페르소나", "content": "너는 친절한 파이썬 학습 도우미 AI야.", "category": "페르소나", "favorite": True}
]

# 2. 데이터 불러오기 함수
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return default_prompts

# 3. 데이터 저장하기 함수
def save_data(prompts):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        # indent=4는 보기 좋게 들여쓰기를 해줍니다.
        # ensure_ascii=False는 한글이 깨지지 않게 해줍니다.
        json.dump(prompts, f, ensure_ascii=False, indent=4)

# 전역 변수로 프롬프트 리스트 관리
prompts = load_data()

def show_menu():
    print("\n" + "="*30)
    print("   프롬프트 관리 프로그램 (JSON)")
    print("="*30)
    print("1. 새 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 모아보기")
    print("0. 종료")
    print("="*30)

def add_prompt():
    print("\n[새 프롬프트 추가]")
    title = input("제목: ").strip()
    content = input("내용: ").strip()
    category = input("카테고리: ").strip()
    
    if title and content and category:
        prompts.append({
            "title": title, "content": content, 
            "category": category, "favorite": False
        })
        save_data(prompts) # 데이터 변경 시 저장
        print("✅ 파일에 저장되었습니다!")
    else:
        print("⚠️ 모든 항목을 입력해야 합니다.")

def show_list(target_list=None, title="전체 목록"):
    display_list = target_list if target_list is not None else prompts
    print(f"\n[{title}]")
    if not display_list:
        print("데이터가 없습니다.")
        return
    for i, p in enumerate(display_list):
        fav = "⭐" if p['favorite'] else "  "
        print(f"{i+1}. [{p['category']}] {p['title']} {fav}")

def toggle_favorite():
    show_list()
    try:
        idx = int(input("\n즐겨찾기 등록/해제할 번호: ")) - 1
        prompts[idx]['favorite'] = not prompts[idx]['favorite']
        save_data(prompts) # 데이터 변경 시 저장
        print(f"✅ 상태가 변경되었습니다.")
    except:
        print("⚠️ 잘못된 번호입니다.")

# ... (나머지 search_prompt, view_detail 등은 이전과 동일) ...

def main():
    global prompts
    while True:
        show_menu()
        choice = input("메뉴 선택: ")
        if choice == '1': add_prompt()
        elif choice == '2': show_list()
        elif choice == '6': toggle_favorite()
        # ... 나머지 조건문 ...
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
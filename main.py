import json
import os

# 파일 경로 설정
DATA_FILE = 'prompts.json'

# 1. 데이터 불러오기 (파일이 없으면 빈 리스트 반환)
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

# 2. 데이터 저장하기
def save_data(prompts):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

# 전역 변수로 프롬프트 리스트 관리
prompts = load_data()

def show_menu():
    print("\n" + "="*40)
    print("   🚀 AI 프롬프트 관리 매니저")
    print("="*40)
    print("1. 새 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 상세 내용 보기 (번호 선택)")
    print("4. 프롬프트 검색 (제목/내용)")
    print("5. 카테고리별 모아보기")
    print("6. 즐겨찾기 등록/해제")
    print("7. 즐겨찾기 목록만 보기")
    print("0. 프로그램 종료")
    print("="*40)

# [기능 1] 새 프롬프트 추가
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
        save_data(prompts)
        print("✅ 성공적으로 저장되었습니다!")
    else:
        print("⚠️ 모든 항목을 입력해야 합니다.")

# [기능 2] 목록 출력 (재사용 가능하게 설계)
def show_list(target_list=None, title="전체 목록"):
    display_list = target_list if target_list is not None else prompts
    print(f"\n--- {title} ({len(display_list)}개) ---")
    if not display_list:
        print("표시할 데이터가 없습니다.")
        return False
    for i, p in enumerate(display_list):
        fav = "⭐" if p.get('favorite') else "  "
        print(f"{i+1}. [{p['category']}] {p['title']} {fav}")
    return True

# [기능 3] 상세 보기
def view_detail():
    if not show_list(): return
    try:
        idx = int(input("\n상세히 볼 번호 (취소: 0): ")) - 1
        if idx == -1: return
        if 0 <= idx < len(prompts):
            p = prompts[idx]
            print("\n" + "-"*50)
            print(f"제목: {p['title']} ({p['category']})")
            print("-"*50)
            print(f"{p['content']}")
            print("-"*50)
            input("\n엔터를 누르면 메뉴로 돌아갑니다...")
        else:
            print("⚠️ 없는 번호입니다.")
    except ValueError:
        print("⚠️ 숫자만 입력해주세요.")

# [기능 4] 검색
def search_prompt():
    keyword = input("\n검색할 키워드를 입력하세요: ").lower()
    results = [p for p in prompts if keyword in p['title'].lower() or keyword in p['content'].lower()]
    show_list(results, f"'{keyword}' 검색 결과")

# [기능 5] 카테고리별 조회
def view_by_category():
    categories = list(set([p['category'] for p in prompts]))
    if not categories:
        print("\n데이터가 없습니다.")
        return
    
    print("\n[카테고리 목록]:", ", ".join(categories))
    target = input("조회할 카테고리 입력: ").strip()
    results = [p for p in prompts if p['category'] == target]
    show_list(results, f"카테고리: {target}")

# [기능 6] 즐겨찾기 토글
def toggle_favorite():
    if not show_list(): return
    try:
        idx = int(input("\n즐겨찾기 등록/해제할 번호: ")) - 1
        if 0 <= idx < len(prompts):
            prompts[idx]['favorite'] = not prompts[idx]['favorite']
            save_data(prompts)
            status = "등록" if prompts[idx]['favorite'] else "해제"
            print(f"✅ '{prompts[idx]['title']}' 항목이 즐겨찾기 {status}되었습니다.")
        else:
            print("⚠️ 없는 번호입니다.")
    except ValueError:
        print("⚠️ 숫자만 입력해주세요.")

# [메인 루프]
def main():
    while True:
        show_menu()
        choice = input("원하는 기능의 번호를 입력하세요: ")
        
        if choice == '1': add_prompt()
        elif choice == '2': show_list()
        elif choice == '3': view_detail()
        elif choice == '4': search_prompt()
        elif choice == '5': view_by_category()
        elif choice == '6': toggle_favorite()
        elif choice == '7':
            favs = [p for p in prompts if p.get('favorite')]
            show_list(favs, "즐겨찾기 목록")
        elif choice == '0':
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("⚠️ 잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
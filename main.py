class Quiz:
    """개별 퀴즈 하나를 표현하는 클래스 (붕어빵 틀)"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용 (글자, str)
        self.choices = choices    # 선택지 4개 묶음 (리스트, list)
        self.answer = answer      # 정답 번호 1~4 (숫자, int)

    def display(self, quiz_num):
        """퀴즈 문제와 선택지 4개를 화면에 출력하는 메서드"""
        print("\n----------------------------------------")
        print(f"[문제 {quiz_num}]")
        print(f"{self.question}\n")
        # 컴퓨터는 숫자를 0부터 세기 때문에(0, 1, 2, 3), 화면에는 +1을 해서 1~4번으로 보여줍니다.
        for i in range(4):
            print(f"{i + 1}. {self.choices[i]}")
        print()

    def check_answer(self, user_answer):
        """사용자가 입력한 번호가 정답과 같은지 확인하는 메서드 (맞으면 True, 틀리면 False 반환)"""
        return self.answer == user_answer


def get_valid_number(prompt, min_val, max_val):
    """사용자로부터 min_val ~ max_val 사이의 안전한 숫자를 입력받는 함수"""
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력해 주세요.")
            continue

        try:
            number = int(user_input)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
            continue

        if min_val <= number <= max_val:
            return number
        else:
            print(f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")


def display_menu():
    """메인 메뉴 화면을 출력하는 함수"""
    print("\n========================================")
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")


def main():
    """게임의 전체 흐름을 조절하는 메인 함수"""
    while True:
        display_menu()
        choice = get_valid_number("선택: ", 1, 5)

        if choice == 1:
            print("\n📝 [퀴즈 풀기] 기능은 곧 추가될 예정입니다!")
        elif choice == 2:
            print("\n📌 [퀴즈 추가] 기능은 곧 추가될 예정입니다!")
        elif choice == 3:
            print("\n📋 [퀴즈 목록] 기능은 곧 추가될 예정입니다!")
        elif choice == 4:
            print("\n🏆 [점수 확인] 기능은 곧 추가될 예정입니다!")
        elif choice == 5:
            print("\n👋 퀴즈 게임을 종료합니다. 다음에 또 만나요!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\n👋 프로그램을 안전하게 종료합니다.")
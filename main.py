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
        for i in range(4):
            print(f"{i + 1}. {self.choices[i]}")
        print()

    def check_answer(self, user_answer):
        """사용자가 입력한 번호가 정답과 같은지 확인하는 메서드"""
        return self.answer == user_answer


def get_default_quizzes():
    """기본으로 제공되는 회계/경제 상식 퀴즈 5개(Quiz 인스턴스 리스트)를 반환하는 함수"""
    return [
        Quiz(
            "재무상태표의 기본이 되는 '회계 등식'으로 올바른 것은?",
            ["자산 = 부채 - 자본", "자산 = 부채 + 자본", "자산 = 수익 - 비용", "자본 = 자산 + 부채"],
            2
        ),
        Quiz(
            "일정 기간 동안 기업의 경영성과(수익과 비용)를 나타내는 재무제표는?",
            ["재무상태표", "자본변동표", "포괄손익계산서", "현금흐름표"],
            3
        ),
        Quiz(
            "생산량이 증감하더라도 총원가가 일정하게 유지되는 원가(예: 공장 임차료)는?",
            ["변동원가", "기회원가", "매몰원가", "고정원가"],
            4
        ),
        Quiz(
            "현재 대한민국의 일반 부가가치세(VAT) 세율은 몇 %인가?",
            ["5%", "10%", "15%", "20%"],
            2
        ),
        Quiz(
            "재무제표가 회계기준에 따라 적정하게 작성되었을 때 외부감사인이 표명하는 최상의 감사의견은?",
            ["적정의견", "한정의견", "부적정의견", "의견거절"],
            1
        )
    ]


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


def play_quiz(quizzes):
    """저장된 퀴즈를 순서대로 출제하고 채점 결과를 보여주는 함수"""
    # 1. 만약 등록된 퀴즈가 하나도 없을 때의 예외 처리
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
        return

    total_count = len(quizzes)
    correct_count = 0

    print(f"\n📝 퀴즈를 시작합니다! (총 {total_count}문제)")

    # 2. for 반복문으로 문제를 1번부터 끝까지 순서대로 출제
    for i in range(total_count):
        quiz = quizzes[i]
        quiz.display(i + 1)

        # 1~4 사이의 안전한 정답 번호 입력받기
        user_answer = get_valid_number("정답 입력 (1-4): ", 1, 4)

        # 정답 확인 후 맞았으면 맞힌 개수(correct_count)에 1 더하기
        if quiz.check_answer(user_answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            print(f"❌ 오답입니다! (정답: {quiz.answer}번)")

    # 3. 모든 문제를 다 풀면 100점 만점 기준으로 점수 계산 및 출력
    score = int((correct_count / total_count) * 100)
    print("\n========================================")
    print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")
    print("========================================")


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
    quizzes = get_default_quizzes()

    while True:
        display_menu()
        choice = get_valid_number("선택: ", 1, 5)

        if choice == 1:
            play_quiz(quizzes)
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
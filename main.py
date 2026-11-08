import json


class Quiz:
    """개별 퀴즈 하나를 표현하는 클래스 (문제 카드 붕어빵 틀)"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용 (str)
        self.choices = choices    # 선택지 4개 리스트 (list)
        self.answer = answer      # 정답 번호 1~4 (int)

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

    def to_dict(self):
        """JSON 파일에 저장할 수 있도록 붕어빵을 딕셔너리(서랍장) 형태로 바꾸는 메서드"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }


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


def get_non_empty_text(prompt):
    """빈칸(그냥 Enter)이 아닌 글자를 안전하게 입력받는 함수"""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("⚠️ 내용이 비어 있습니다. 다시 입력해 주세요.")


class QuizGame:
    """게임 전체를 관리하는 진행자 로봇 클래스"""

    def __init__(self, file_path="state.json"):
        """로봇이 켜질 때 수첩 파일 경로를 기억하고 저장된 데이터를 불러옵니다."""
        self.file_path = file_path
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def get_default_quizzes(self):
        """기본으로 제공되는 회계/경제 상식 퀴즈 5개를 반환하는 메서드"""
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

    def load_state(self):
        """state.json 수첩 파일에서 퀴즈 목록과 최고 점수를 불러오는 메서드"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # 저장된 딕셔너리 데이터를 다시 Quiz 붕어빵(인스턴스)으로 복원합니다.
            loaded_quizzes = []
            for item in data["quizzes"]:
                quiz = Quiz(item["question"], item["choices"], int(item["answer"]))
                loaded_quizzes.append(quiz)

            self.quizzes = loaded_quizzes
            self.best_score = data.get("best_score", None)

            score_text = f"{self.best_score}점" if self.best_score is not None else "기록 없음"
            print(f"\n📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수: {score_text})")

        except FileNotFoundError:
            # 처음 실행해서 아직 state.json 파일이 없을 때는 기본 퀴즈 5개를 사용합니다.
            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.save_state()
        except Exception:
            # 파일이 손상되었거나 형식이 깨졌을 때는 안내 후 기본 데이터로 복구합니다.
            print("\n⚠️ 데이터 파일(state.json)이 손상되어 기본 퀴즈 데이터로 복구합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        """현재 퀴즈 목록과 최고 점수를 state.json 수첩 파일에 저장하는 메서드"""
        try:
            # 1. 모든 Quiz 붕어빵을 to_dict()로 포장해서 리스트에 담습니다.
            quiz_dicts = []
            for quiz in self.quizzes:
                quiz_dicts.append(quiz.to_dict())

            # 2. 과제에서 요구한 스키마(quizzes, best_score) 형태로 묶습니다.
            data = {
                "quizzes": quiz_dicts,
                "best_score": self.best_score
            }

            # 3. UTF-8 인코딩으로 state.json 파일에 깔끔하게 기록합니다.
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"\n⚠️ 데이터를 파일에 저장하는 중 오류가 발생했습니다: {e}")

    def display_menu(self):
        """메인 메뉴 화면을 출력하는 메서드"""
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def play_quiz(self):
        """주머니(self.quizzes)에 있는 문제를 출제하고 최고 점수를 갱신하는 메서드"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
            return

        total_count = len(self.quizzes)
        correct_count = 0

        print(f"\n📝 퀴즈를 시작합니다! (총 {total_count}문제)")

        for i in range(total_count):
            quiz = self.quizzes[i]
            quiz.display(i + 1)

            user_answer = get_valid_number("정답 입력 (1-4): ", 1, 4)

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답입니다! (정답: {quiz.answer}번)")

        score = int((correct_count / total_count) * 100)
        print("\n========================================")
        print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            # 최고 점수가 갱신되면 즉시 state.json 수첩에 자동 저장합니다!
            self.save_state()

        print("========================================")

    def add_quiz(self):
        """새 퀴즈를 입력받아 추가하고 파일에 즉시 저장하는 메서드"""
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = get_non_empty_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice_text = get_non_empty_text(f"선택지 {i}: ")
            choices.append(choice_text)

        answer = get_valid_number("정답 번호 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        # 새 문제가 추가되면 즉시 state.json 수첩에 자동 저장합니다!
        self.save_state()
        print("\n✅ 퀴즈가 추가되고 파일에 저장되었습니다!")

    def show_quiz_list(self):
        """저장된 모든 퀴즈 목록을 출력하는 메서드"""
        if not self.quizzes:
            print("\n⚠️ 현재 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("----------------------------------------")
        for i in range(len(self.quizzes)):
            print(f"[{i + 1}] {self.quizzes[i].question}")
        print("----------------------------------------")

    def show_best_score(self):
        """기록된 최고 점수를 출력하는 메서드"""
        if self.best_score is None:
            print("\n⚠️ 아직 퀴즈를 풀지 않아 기록된 최고 점수가 없습니다.")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점")

    def run(self):
        """게임의 전체 흐름을 실행하는 시작 버튼 메서드"""
        while True:
            self.display_menu()
            choice = get_valid_number("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                self.save_state()
                print("\n👋 데이터를 안전하게 저장하고 퀴즈 게임을 종료합니다!")
                break


if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        # 도중에 Ctrl+C로 강제 종료하더라도 그전까지의 데이터를 수첩에 저장하고 꺼집니다.
        game.save_state()
        print("\n\n👋 입력이 중단되어 현재 데이터를 저장하고 안전하게 종료합니다.")
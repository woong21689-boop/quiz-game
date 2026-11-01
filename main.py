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
      print(
          f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요."
      )
      continue

    if min_val <= number <= max_val:
      return number
    else:
      print(
          f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요."
      )


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
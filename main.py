def get_valid_number(prompt, min_val, max_val):
	"""사용자로부터 min_val ~ max_val 사이의 안전한 숫자를 입력받는 함수"""
	while True:
		# 1. 입력받고 앞뒤 공백 제거 (.strip())
		user_input = input(prompt).strip()

		# 2. 빈 입력(그냥 Enter) 처리
		if not user_input:
			print("⚠️ 입력이 비어 있습니다. 숫자를 입력해 주세요.")
			continue

		# 3. 숫자로 변환 시도 (abc 등 글자 입력 시 에러 방지 에어백)
		try:
			number = int(user_input)
		except ValueError:
			print(
					f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요."
			)
			continue

		# 4. 허용 범위(min_val ~ max_val) 안의 숫자인지 확인
		if min_val <= number <= max_val:
			return number
		else:
			print(
					f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요."
			)


# 프로그램 실행 시작점 (3단계에서 메뉴 화면으로 바뀔 예정입니다)
if __name__ == "__main__":
	try:
		choice = get_valid_number("선택 (1-5): ", 1, 5)
		print(f"✅ 정상 입력 완료! 선택한 번호: {choice}")
	except (KeyboardInterrupt, EOFError):
		print("\n\n👋 프로그램을 안전하게 종료합니다.")

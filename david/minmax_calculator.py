# ----------------------------------------------------------------------------------------------------
# 작성목적 : 반달곰 커피 최소값/최대값 계산 프로그램 구현
# 작성일 : 2025-07-21

# 변경사항 내역 (날짜 | 변경목적 | 변경내용 | 작성자 순으로 기입)
# 2025-07-21 | 최초 구현 | min(), max() 함수 사용 없이 최소값/최대값 계산 구현 | zookeeper
# ----------------------------------------------------------------------------------------------------

def find_min_max(numbers):
    """
    숫자 리스트에서 최소값과 최대값을 찾는 함수
    Python 내장 함수 min(), max() 사용 금지
    
    Args:
        numbers (list): 숫자들의 리스트
    
    Returns:
        tuple: (최소값, 최대값)
    """
    if not numbers:
        return None, None
    
    # 첫 번째 값으로 초기화
    minimum = numbers[0]
    maximum = numbers[0]
    
    # 모든 숫자를 순회하면서 최소값, 최대값 업데이트
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    
    return minimum, maximum

def parse_input(input_string):
    """
    입력 문자열을 숫자 리스트로 변환하는 함수
    
    Args:
        input_string (str): 공백으로 구분된 숫자 문자열
    
    Returns:
        list: 변환된 숫자 리스트 또는 None (오류 시)
    """
    try:
        # 공백으로 분리하고 각각을 float로 변환
        number_strings = input_string.strip().split()
        
        if not number_strings:
            return None
        
        numbers = []
        for num_str in number_strings:
            numbers.append(float(num_str))
        
        return numbers
        
    except ValueError:
        return None

def main():
    """
    메인 함수 - 프로그램의 주 실행 로직
    """
    print("=== 반달곰 커피 최소값/최대값 계산기 ===")
    print("숫자들을 공백으로 구분하여 입력하세요 (예: 3 9 1 4 2)")
    
    # 사용자 입력 받기
    user_input = input("숫자들을 입력하세요: ")
    
    # 입력값 파싱
    numbers = parse_input(user_input)
    
    # 예외 처리
    if numbers is None:
        print("Invalid input.")
        return
    
    # 최소값, 최대값 계산
    minimum, maximum = find_min_max(numbers)
    
    # 결과 출력
    print(f"Min: {minimum}, Max: {maximum}")

if __name__ == "__main__":
    main() 
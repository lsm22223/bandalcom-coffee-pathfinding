# ----------------------------------------------------------------------------------------------------
# 작성목적 : 반복문을 사용한 제곱 계산 프로그램 구현
# 작성일 : 2025-07-21

# 변경사항 내역 (날짜 | 변경목적 | 변경내용 | 작성자 순으로 기입)
# 2025-07-21 | 최초 구현 | 사용자 입력을 받아 반복문으로 제곱 계산하는 프로그램 작성 | zookeeper
# ----------------------------------------------------------------------------------------------------

def calculate_power(base, exponent):
    """
    반복문을 사용하여 제곱 계산하는 함수
    
    Args:
        base (float): 밑수
        exponent (int): 지수
    
    Returns:
        float: 제곱 계산 결과
    """
    result = 1.0
    
    # 양수 지수인 경우
    if exponent > 0:
        for i in range(exponent):
            result *= base
    # 음수 지수인 경우 (1/base를 양수 지수만큼 곱함)
    elif exponent < 0:
        for i in range(-exponent):
            result *= base
        result = 1.0 / result
    # 지수가 0인 경우 결과는 1
    else:
        result = 1.0
    
    return result

def get_number_input():
    """
    사용자로부터 숫자 입력을 받는 함수
    
    Returns:
        float: 변환된 숫자 또는 None (오류 시)
    """
    try:
        number_str = input("Enter number: ")
        return float(number_str)
    except ValueError:
        print("Invalid number input.")
        return None

def get_exponent_input():
    """
    사용자로부터 지수 입력을 받는 함수
    
    Returns:
        int: 변환된 지수 또는 None (오류 시)
    """
    try:
        exponent_str = input("Enter exponent: ")
        return int(exponent_str)
    except ValueError:
        print("Invalid exponent input.")
        return None

def main():
    """
    메인 함수 - 프로그램의 주 실행 로직
    """
    # 숫자 입력 받기
    base = get_number_input()
    if base is None:
        return
    
    # 지수 입력 받기
    exponent = get_exponent_input()
    if exponent is None:
        return
    
    # 제곱 계산 실행
    result = calculate_power(base, exponent)
    
    # 결과 출력 (정수인 경우 .0 제거)
    if result == int(result):
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main() 
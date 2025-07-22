# ----------------------------------------------------------------------------------------------------
# 작성목적 : 반달곰 커피 고객 대응용 계산기 프로그램 구현
# 작성일 : 2025-07-21

# 변경사항 내역 (날짜 | 변경목적 | 변경내용 | 작성자 순으로 기입)
# 2025-07-21 | 최초 구현 | 기본 계산기 기능 및 문자열 수식 입력 방식 구현 | zookeeper
# ----------------------------------------------------------------------------------------------------

def add(a, b):
    """
    덧셈 연산 함수
    
    Args:
        a (float): 첫 번째 숫자
        b (float): 두 번째 숫자
    
    Returns:
        float: a + b의 결과
    """
    return a + b

def subtract(a, b):
    """
    뺄셈 연산 함수 (a - b)
    
    Args:
        a (float): 첫 번째 숫자 (피감수)
        b (float): 두 번째 숫자 (감수)
    
    Returns:
        float: a - b의 결과
    """
    return a - b

def multiply(a, b):
    """
    곱셈 연산 함수
    
    Args:
        a (float): 첫 번째 숫자
        b (float): 두 번째 숫자
    
    Returns:
        float: a * b의 결과
    """
    return a * b

def divide(a, b):
    """
    나눗셈 연산 함수 (a / b)
    
    Args:
        a (float): 첫 번째 숫자 (피제수)
        b (float): 두 번째 숫자 (제수)
    
    Returns:
        float: a / b의 결과
        str: 0으로 나누는 경우 에러 메시지
    """
    if b == 0:
        return "Error: Division by zero."
    return a / b

def get_number_input(prompt):
    """
    사용자로부터 숫자 입력을 받는 함수
    
    Args:
        prompt (str): 입력 프롬프트 메시지
    
    Returns:
        float: 변환된 숫자
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number input.")
        return None

def get_operator_input():
    """
    사용자로부터 연산자 입력을 받는 함수
    
    Returns:
        str: 연산자 (+, -, *, /)
    """
    return input("Enter operator (+, -, *, /): ").strip()

def calculate_basic():
    """
    기본 계산기 기능 - 숫자 2개와 연산자를 개별적으로 입력받아 계산
    """
    print("\n=== 기본 계산기 ===")
    
    # 첫 번째 숫자 입력
    num1 = get_number_input("Enter first number: ")
    if num1 is None:
        return
    
    # 두 번째 숫자 입력
    num2 = get_number_input("Enter second number: ")
    if num2 is None:
        return
    
    # 연산자 입력
    operator = get_operator_input()
    
    # 연산 실행
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator.")
        return
    
    print(f"Result: {result}")

def parse_expression(expression):
    """
    문자열 수식을 파싱하는 함수
    
    Args:
        expression (str): "숫자 연산자 숫자" 형태의 수식
    
    Returns:
        tuple: (첫번째숫자, 연산자, 두번째숫자) 또는 None (파싱 실패시)
    """
    try:
        # 공백으로 분리
        parts = expression.strip().split()
        
        if len(parts) != 3:
            return None
        
        # 숫자 변환
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        # 연산자 유효성 검사
        if operator not in ['+', '-', '*', '/']:
            return None
        
        return num1, operator, num2
        
    except (ValueError, IndexError):
        return None

def calculate_expression():
    """
    문자열 수식 입력 방식 계산기 기능
    """
    print("\n=== 수식 입력 계산기 ===")
    
    expression = input("Enter expression (예: 2 + 3): ")
    
    # 수식 파싱
    parsed = parse_expression(expression)
    if parsed is None:
        print("Invalid expression format. Please use: number operator number")
        return
    
    num1, operator, num2 = parsed
    
    # 연산 실행
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
        if isinstance(result, str):  # 에러 메시지인 경우
            print(result)
            return
    
    print(f"Result: {result}")

def main():
    """
    메인 함수 - 계산기 프로그램의 주 실행 로직
    """
    print("=== 반달곰 커피 계산기 ===")
    print("1. 기본 계산기 (개별 입력)")
    print("2. 수식 계산기 (한 줄 입력)")
    print("3. 종료")
    
    while True:
        choice = input("\n메뉴를 선택하세요 (1-3): ").strip()
        
        if choice == '1':
            calculate_basic()
        elif choice == '2':
            calculate_expression()
        elif choice == '3':
            print("계산기를 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1-3 중에서 선택해주세요.")

if __name__ == "__main__":
    main() 
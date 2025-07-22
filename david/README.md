# 문제3 - 반달곰 커피 고객 대응 시스템

## 개요
반달곰 커피 매장의 고객 대응 효율성을 높이기 위한 음성 출력 웹 애플리케이션과 계산기 프로그램입니다.

## 📁 포함된 파일들
- `app.py` - 음성 출력 웹 애플리케이션
- `calculator.py` - 계산기 프로그램 (기본 + 수식 입력)
- `README.md` - 이 문서

## 🚀 실행 방법

### 1. 음성 출력 웹 애플리케이션 (app.py)

#### VS Code에서 실행
1. VS Code에서 `david/app.py` 파일 열기
2. `Ctrl + F5` (Run Without Debugging) 또는 `F5` (Start Debugging) 실행
3. 웹브라우저에서 접속:
   - `http://localhost:8080` - 한국어 음성 출력
   - `http://localhost:8080?lang=en` - 영어 음성 출력

#### 특징
- **gTTS (Google Text-to-Speech)** 사용
- **언어 설정 가능**: `?lang=ko` (한국어), `?lang=en` (영어)
- **즉시 재생**: 페이지 로딩 없이 바로 음성 파일 재생
- **환경변수 지원**: `DEFAULT_LANG` 환경변수로 기본 언어 설정

### 2. 계산기 프로그램 (calculator.py)

#### VS Code에서 실행
1. VS Code에서 `david/calculator.py` 파일 열기
2. `Ctrl + F5` 또는 `F5`로 실행
3. 메뉴 선택하여 사용

#### 기능
##### 📌 기본 계산기 (메뉴 1)
```
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +
Result: 15.0
```

##### 📌 수식 입력 계산기 (메뉴 2)
```
Enter expression (예: 2 + 3): 10 / 5
Result: 2.0
```

#### 구현된 연산 함수들
| 함수명 | 기능 | 예시 |
|--------|------|------|
| `add(a, b)` | 덧셈 | 5 + 3 = 8 |
| `subtract(a, b)` | 뺄셈 (a - b) | 5 - 3 = 2 |
| `multiply(a, b)` | 곱셈 | 5 * 3 = 15 |
| `divide(a, b)` | 나눗셈 (a / b) | 6 / 3 = 2 |

#### 예외 처리
- **0으로 나누기**: "Error: Division by zero."
- **잘못된 연산자**: "Invalid operator."
- **잘못된 숫자**: "Invalid number input."
- **잘못된 수식 형식**: "Invalid expression format."

## 🔧 보너스 과제

### Python 가상환경 (venv) 구성

#### 1. 가상환경 생성
```bash
# Windows
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate

# 가상환경 비활성화
deactivate
```

#### 2. 패키지 설치 (가상환경 내에서)
```bash
pip install flask
pip install gTTS
```

#### 3. requirements.txt 생성
```bash
pip freeze > requirements.txt
```

#### 4. 다른 환경에서 복원
```bash
pip install -r requirements.txt
```

### 가상환경 사용의 장점
- **의존성 격리**: 프로젝트별 독립적인 패키지 관리
- **버전 충돌 방지**: 서로 다른 버전의 패키지 사용 가능
- **깔끔한 환경**: 시스템 Python에 영향 없음
- **배포 용이성**: requirements.txt로 환경 재현 가능

## 🧪 테스트 시나리오

### app.py 테스트
1. **기본 접속**: `http://localhost:8080` → "Hello, DevOps" 한국어 음성
2. **언어 변경**: `http://localhost:8080?lang=en` → 영어 음성
3. **브라우저 재생**: MP3 파일이 자동으로 재생되는지 확인

### calculator.py 테스트
1. **기본 계산**: 10 + 5 = 15
2. **나눗셈**: 12 / 4 = 3
3. **0으로 나누기**: 5 / 0 → 에러 메시지
4. **수식 입력**: "2 + 3" → 5.0
5. **잘못된 형식**: "2+" → 에러 메시지

## 📋 개발 환경 요구사항

### 필수 패키지
```
Flask>=2.0.0
gTTS>=2.5.0
```

### 개발 도구
- **Visual Studio Code** (필수)
- **Python 3.8+** (필수)
- **웹브라우저** (Chrome, Firefox 등)

### 제약사항
- ✅ VS Code에서만 실행
- ✅ 터미널 명령어 사용 금지
- ✅ `flask run` 명령어 사용 금지

## 🎯 프로젝트 목표 달성도

### ✅ 완료된 기능
- [x] 음성 출력 웹 애플리케이션 구현
- [x] gTTS 패키지 사용
- [x] 기본 계산기 4가지 연산 구현
- [x] 예외 처리 완료
- [x] 문자열 수식 입력 방식 추가
- [x] 가상환경 구성 가이드 작성

### 🚀 확장 가능성
- 더 많은 언어 지원
- 복잡한 수식 계산 (괄호, 연산자 우선순위)
- 웹 인터페이스 계산기
- 음성 인식 기능 추가

---
*작성일: 2025년 7월 21일*  
*작성자: zookeeper*  
*프로젝트: 반달곰 커피 고객 대응 시스템* 
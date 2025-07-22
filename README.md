# 반달곰 커피 개발 프로젝트

## 📋 프로젝트 개요
반달곰 커피 매장의 디지털 전환을 위한 종합 개발 프로젝트입니다. Python을 기반으로 한 웹 애플리케이션, 계산기 프로그램, 그리고 체계적인 개발 환경 구축을 포함합니다.

## 📁 프로젝트 구조

```
personal_bandalgom/
├── README.md                    # 이 파일
├── david/                       # 문제3-4: 음성 출력 & Git 환경
│   ├── app.py                   # Flask 음성 출력 웹앱
│   ├── calculator.py            # 기본+수식 계산기
│   ├── minmax_calculator.py     # 최소값/최대값 계산기
│   ├── git_directory.md         # Git 버전 관리 가이드
│   └── README.md               # david 폴더 문서
├── 문제1/                       # Python 환경 구축
│   ├── my_solution.py           # Hello 함수 구현
│   └── python_webframework.md   # 웹프레임워크 비교
└── 문제2/                       # Flask 웹 환경 테스트
    ├── app.py                   # Flask 웹 애플리케이션
    ├── power_calculator.py      # 제곱 계산 프로그램
    └── flask_development_guide.md # Flask 개발 가이드
```

## 🚀 주요 기능

### 1. 웹 애플리케이션
- **Flask 기반 웹서버**: "Hello, DevOps!" 출력
- **음성 출력 기능**: gTTS를 활용한 한국어/영어 음성 변환
- **다국어 지원**: URL 파라미터로 언어 설정

### 2. 계산기 시스템
- **기본 계산기**: 사칙연산 (+, -, *, /)
- **수식 입력 계산기**: "2 + 3" 형태의 한 줄 입력
- **제곱 계산기**: 반복문으로 직접 구현 (** 연산자 사용 금지)
- **최소값/최대값 계산기**: 내장 함수 없이 직접 구현

### 3. 개발 환경 및 문서
- **Git 버전 관리**: 설정부터 활용까지 완전 가이드
- **Python 웹프레임워크 비교**: Flask, Django, FastAPI
- **Flask 개발 환경**: 디버깅, 호스트 설정, 포트 관리

## 🛠️ 기술 스택

### Backend
- **Python 3.8+**
- **Flask**: 웹 애플리케이션 프레임워크
- **gTTS**: Google Text-to-Speech

### Development Tools
- **Git**: 버전 관리
- **Visual Studio Code**: 개발 환경
- **Windows Terminal**: 터미널 환경

### 라이브러리
```bash
Flask>=2.0.0
gTTS>=2.5.0
```

## 📖 사용 방법

### 환경 설정
```bash
# Git 클론
git clone https://github.com/lsm22223/personal_bandalgom.git
cd personal_bandalgom

# 필요한 패키지 설치
pip install flask gtts
```

### 실행 방법

#### 1. Flask 웹 애플리케이션
```bash
# 기본 웹서버 (문제2)
cd 문제2
python app.py
# 접속: http://localhost:8080

# 음성 출력 웹앱 (david)
cd david  
python app.py
# 접속: http://localhost:8080 (한국어)
# 접속: http://localhost:8080?lang=en (영어)
```

#### 2. 계산기 프로그램들
```bash
cd david

# 기본+수식 계산기
python calculator.py

# 최소값/최대값 계산기  
python minmax_calculator.py
# 입력 예시: 3 9 1 4 2
# 출력: Min: 1.0, Max: 9.0
```

#### 3. 제곱 계산기
```bash
cd 문제2
python power_calculator.py
# 입력 예시: 3, 4
# 출력: Result: 81
```

## 🎯 핵심 구현 특징

### 1. 알고리즘 직접 구현
- **제곱 계산**: `**` 연산자 대신 반복문 사용
- **최소값/최대값**: `min()`, `max()` 함수 대신 직접 구현
- **예외 처리**: 잘못된 입력에 대한 안전한 처리

### 2. 웹 개발 베스트 프랙티스
- **호스트 설정**: 0.0.0.0 vs 127.0.0.1 차이점 이해
- **포트 관리**: 충돌 해결 방안 제시  
- **디버깅 모드**: Run vs Debug 차이점 설명

### 3. 버전 관리 시스템
- **Git 설정**: 전역 설정부터 저장소 초기화까지
- **3가지 VCS 비교**: Git, SVN, Mercurial
- **.git 디렉토리**: 구조와 역할 상세 설명

## 📚 학습 포인트

### Python 개발
- 함수 정의와 예외 처리
- 파일 I/O와 CSV 처리
- 웹 프레임워크 활용

### 웹 개발
- Flask 기본 구조 이해
- HTTP 요청/응답 처리
- 멀티미디어 콘텐츠 제공

### 개발 도구
- Git을 활용한 버전 관리
- VS Code 개발 환경 최적화
- 터미널 기반 개발 워크플로우

## 🔗 관련 저장소
- **길찾기 알고리즘**: [bandalcom-coffee-pathfinding](https://github.com/lsm22223/bandalcom-coffee-pathfinding)

## 👤 개발 정보
- **개발자**: zookeeper
- **개발 기간**: 2025.07.21
- **목적**: 반달곰 커피 디지털 전환 프로젝트

---
*"개발은 설치가 반이다" - 선배들의 격언* 
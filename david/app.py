# ----------------------------------------------------------------------------------------------------
# 작성목적 : 반달곰 커피 음성 출력 웹 애플리케이션 구현
# 작성일 : 2025-07-21

# 변경사항 내역 (날짜 | 변경목적 | 변경내용 | 작성자 순으로 기입)
# 2025-07-21 | 최초 구현 | gTTS를 사용한 음성 출력 Flask 애플리케이션 구현 | zookeeper
# ----------------------------------------------------------------------------------------------------

from flask import Flask, request, Response
import os
from io import BytesIO
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():
    """
    루트 경로에서 음성을 출력하는 함수
    
    Query Parameters:
        lang (str): 언어 설정 (기본값: 'ko')
    
    Returns:
        Response: MP3 형식의 음성 파일 응답
    """
    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)  # 포트 80은 관리자 권한 필요하므로 8080 사용 
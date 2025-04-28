import streamlit as st
import requests
import difflib

# FastAPI 서버 주소
FASTAPI_URL = "http://localhost:8000"

def generate_ai_video() :
    st.subheader("결과 영상 보기")
    st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")


st.title("AI 영상 프롬프트 생성기")

# 세션 상태 초기화
if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""

if "edited_prompt" not in st.session_state:
    st.session_state.edited_prompt = ""

if "last_diff" not in st.session_state:
    st.session_state.last_diff = []

if "diff_before" not in st.session_state:
    st.session_state.diff_before = ""

if "diff_after" not in st.session_state:
    st.session_state.diff_after = ""

# 자연어 입력창
user_input = st.text_area("자연어로 설명을 입력하세요", height=150)

# 프롬프트 생성 버튼
if st.button("프롬프트 생성하기"):
    if user_input.strip():
        response = requests.post(f"{FASTAPI_URL}/generate-prompt", json={"user_input": user_input})
        if response.status_code == 200:
            st.session_state.generated_prompt = response.json()["prompt"]
            st.session_state.edited_prompt = st.session_state.generated_prompt
            st.session_state.last_diff = []
            st.success("생성된 프롬프트를 수정하세요:")
        else:
            st.error("프롬프트 생성 실패")

# 수정 가능한 프롬프트 영역
if st.session_state.generated_prompt:
    st.session_state.edited_prompt = st.text_area(
        "프롬프트 수정하기",
        value=st.session_state.edited_prompt,
        height=250,
        key="edited_prompt_area"
    )

    # 수정 완료 및 Diff 저장 버튼
    if st.button("수정 완료 및 저장하기"):
        diff_payload = {
            "before": st.session_state.generated_prompt,
            "after": st.session_state.edited_prompt
        }
        diff_response = requests.post(f"{FASTAPI_URL}/save-diff", json=diff_payload)
        if diff_response.status_code == 200:
            diff_result = diff_response.json()["diff"]
            st.session_state.last_diff = diff_result
            st.session_state.diff_before = diff_payload["before"]   # 수정 전 저장
            st.session_state.diff_after = diff_payload["after"]     # 수정 후 저장
            st.success("수정 기록 저장 완료! Diff 결과를 확인하세요.")
            st.session_state.generated_prompt = ""
            st.session_state.edited_prompt = ""
        else:
            st.error("수정 기록 저장 실패")

# 단어 단위 Diff 하이라이트 렌더링 함수
def render_diff_text(before: str, after: str) -> str:
    before_words = before.split()
    after_words = after.split()
    matcher = difflib.SequenceMatcher(None, before_words, after_words)
    result = ""

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            result += " " + " ".join(after_words[j1:j2])
        elif tag == "insert":
            result += " " + "".join(f"<span style='background-color:#cce5ff;'>{word}</span>" for word in after_words[j1:j2])
        elif tag == "delete":
            result += " " + "".join(f"<span style='background-color:#f8d7da;text-decoration:line-through;'>{word}</span>" for word in before_words[i1:i2])
        elif tag == "replace":
            result += " " + "".join(f"<span style='background-color:#f8d7da;text-decoration:line-through;'>{word}</span>" for word in before_words[i1:i2])
            result += " " + "".join(f"<span style='background-color:#cce5ff;'>{word}</span>" for word in after_words[j1:j2])

    return result.strip()

# Diff 결과 표시
if st.session_state.diff_before and st.session_state.diff_after:
    st.subheader("수정 차이(Diff) 결과")

    diff_html = render_diff_text(st.session_state.diff_before, st.session_state.diff_after)
    st.markdown(diff_html, unsafe_allow_html=True)
    generate_ai_video()

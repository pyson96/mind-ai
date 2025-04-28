import random

def generate_prompt(user_input: str) -> str:
    camera_shots = ["TRACKING", "CLOSE UP", "FPV"]
    movements = ["DYNAMIC MOTION", "SLOW MOTION", "EXPLODES"]
    lighting_styles = ["CINEMATIC", "MOODY", "LENS FLARE"]

    camera, movement, lighting = retrieve_similar_prompt(camera_shots, movements, lighting_styles)

    return (
        f"Scene: '{user_input}'. "
        f"Camera Style: {camera}. "
        f"Movement: {movement}. "
        f"Lighting: {lighting}."
    )

# 유저가 입력한 자연어를 이전에 요청한 입력과 비교하여 유사한 프롬프트를 생성하는 함수 
def retrieve_similar_prompt(camera_shots: list, movements: list, lighting_styles: list):
    """
    카메라, 무브먼트, 조명 스타일 중 하나씩 랜덤 선택하는 함수
    """
    camera = random.choice(camera_shots)
    movement = random.choice(movements)
    lighting = random.choice(lighting_styles)
    return camera, movement, lighting
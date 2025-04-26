import random

def generate_prompt(user_input: str) -> str:
    camera_shots = ["TRACKING", "CLOSE UP", "FPV"]
    movements = ["DYNAMIC MOTION", "SLOW MOTION", "EXPLODES"]
    lighting_styles = ["CINEMATIC", "MOODY", "LENS FLARE"]

    camera = random.choice(camera_shots)
    movement = random.choice(movements)
    lighting = random.choice(lighting_styles)

    return (
        f"Scene: '{user_input}'. "
        f"Camera Style: {camera}. "
        f"Movement: {movement}. "
        f"Lighting: {lighting}."
    )

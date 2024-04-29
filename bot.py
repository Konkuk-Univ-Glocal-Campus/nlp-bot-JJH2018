import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["흥미로운 이야기네요. 더 이야기해주세요",
                    "알겠어요. 더 말씀해주시죠",
                    "왜 그렇게 말씀하시죠?",
                    "요새 날씨가 이상하지 않나요?",
                    "화제를 바꾸죠.",
                    "어제 밤에 있던 경기 보셨나요?"]

print("안녕하세요. 저는 단순 챗봇 마빈이라고 합니다.")
print("당신이 이 대화를 끝내고 싶다면 '잘가'라고 말씀해주세요.")
print("답변을 입력한 후 '엔터'를 누르세요.")
print("오늘은 어땠습니까?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였어요! 다음에 봐요!")

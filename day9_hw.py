import turtle as t
t.shape("turtle")
t.pensize(3) # 거북이가 칠하는 선 굵기가 3으로!
t.bgcolor("skyblue") #바탕을 스카이블루색으로 설정
t.fillcolor("yellow") # 도형 내부를 노란색으로 칠한다
t.color("red") # 거북이 색상을 빨간색으로 변경!
angle = 45
angle = 45 # 거북이가 왼쪽으로 회전할 각도를 45도로 지정
t.speed(0) # 거북이 속도를 가장 빠르게 지정
for x in range(320): # x값을 0에서 319번까지 320번 실행 : 은 한칸밑으로표시
    t.forward(x) # x만큼 앞으로 이동 320번
    t.left(angle) #거북이가 왼쪽으로 45도 회전

	
 # 끝 거미줄 같은 모형이 나옴! 

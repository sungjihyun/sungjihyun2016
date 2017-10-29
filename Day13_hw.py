import turtle as t
t.shape("turtle")
t.bgcolor("blue") #배경 파란색으로 변경 
t.pensize("3") # 펜사이즈 굵게 변경
t.goto(-250,250) #goto<< 선택된 좌표로 이동한다.
t.goto(-250,250)
t.fd(500)
t.lt(45)
t.rt(90)
t.rt(45)
t.fd(500)
t.lt(90)
t.rt(180)
t.fd(500)
t.rt(180)
t.lt(90)
t.fd(500)
t.goto(250,50)
t.goto(0,-250)
t.goto(-250,250)
t.goto(-250,250)
for x in range(200): #모서리 쪽으로 200번 반복해서 삼각형 만들기!
    t.goto(250,50)
    t.goto(0,-250)
    t.goto(-250,250)
t.seth(a) # 교수님 제가 실력이 안되서 솔직히 반사각 등을 잘 못구하겠습니다..
          # 공부 더 열심히 해서 다음번에는 과제 열심히 할 수 있도록 하겠습니다.

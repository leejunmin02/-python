import turtle as t 

t.shape("turtle")
t.pensize(20) //펜굵기

t.circle(100) //크기100의 원그리기

t.up()          //펜올리기
t.forward(240)  //240만큼 앞으로 이동하기
t.down()        //팬내리기
t.pencolor('red')//펜색깔 빨간색으로 설정
t.circle(100)    // 크기100의 원그리기

t.up()         //펜올리기
t.backward(480) //480만큼 뒤로 이동하기
t.down()          //펜내리기
t.pencolor('blue')//펜색깔 파란색으로 설정
t.circle(100)   //크기 100의 원그리기

t.up()      //펜올리기
t.right(90)  // 90도 회전
t.forward(120) // 앞으로 120만큼 이동
t.right(270)  // 270도 회전
t.forward(120)  //앞으로 120만큼 이동
t.down()  // 펜내리기
t.pencolor('yellow')  //펜색깔 노란색으로 설정
t.circle(100)  // 크기 100의 원그리기

t.up()  //펜올리기
t.forward(240) //앞으로 240만큼 이동
t.down()  // 펜내리기
t.pencolor('green') //펜색깔 초록색으로 설정
t.circle(100) //원그리기

t.done()

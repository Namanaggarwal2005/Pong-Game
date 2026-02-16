from turtle import Screen,Turtle
import paddle,ball,time,scoreboard

SPEED = 0.09

screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

paddle1 = paddle.Paddle(380)
paddle2 = paddle.Paddle(-390)

score = scoreboard.Scoreboard()
play_ball = ball.Ball()

screen.listen()
screen.onkeypress(key="Up",fun=paddle1.move_up)
screen.onkeypress(key="Down",fun=paddle1.move_down)
screen.onkeypress(key="w",fun=paddle2.move_up)
screen.onkeypress(key="s",fun=paddle2.move_down)

game_is_on = True
while game_is_on:
    time.sleep(SPEED)
    screen.update()
    play_ball.move()
    # Wall Collision
    if play_ball.ycor() >275 or play_ball.ycor()<-275 :
        play_ball.bounce_up()
    
    # Paddle Collision
    if play_ball.distance(paddle1)<50 and play_ball.xcor()>350 or play_ball.distance(paddle2)<50 and play_ball.xcor()<-360  :
        play_ball.bounce_paddle()
    
    # Missing the hit
    if play_ball.xcor()>390:
        screen.tracer(0)
        play_ball.goto(0,0)
        play_ball.bounce_paddle()
        screen.update()
        score.update_lscore() 
        SPEED /= 1.1
    
    if play_ball.xcor()<-400:
        screen.tracer(0)
        play_ball.goto(0,0)
        play_ball.bounce_paddle()
        screen.update()
        score.update_rscore()
        SPEED /= 1.1


screen.exitonclick()
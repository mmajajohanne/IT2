import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480)) # window size
pygame.display.set_caption("Simple pong") # window title

# this is a rect that contains the ball
# at the beginning it is set in the center of the screen
ball_rect = pygame.Rect((312, 232), (16, 16))
# speed of the ball (x, y)
ball_speed = [4, 4]

# this contains your paddle
# vertically centered on the left side
paddle_rect = pygame.Rect((30, 200), (8, 80))

# 1 point if you hit the ball
# -5 point if you miss the ball
score = 0

# load the font for displaying the score
font = pygame.font.Font(None, 30)

# mainloop
while True:
    # event handler
    for event in pygame.event.get():
        # quit event => close the game
        if event.type == pygame.QUIT:
            exit(0)
        # control the paddle with the mouse
        elif event.type == pygame.MOUSEMOTION:
            paddle_rect.centery = event.pos[1]
            # correct paddle position if it's going out of window
            if paddle_rect.top < 0:
                paddle_rect.top = 0
            elif paddle_rect.bottom >= 480:
                paddle_rect.bottom = 480

# this test if up or down keys are pressed
    # if yes move the paddle
    if pygame.key.get_pressed()[pygame.K_UP] and paddle_rect.top > 0:
        paddle_rect.top -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN] and paddle_rect.bottom < 480:
        paddle_rect.top += 5

    # update ball position
    # this move the ball
    ball_rect.left += ball_speed[0]
    ball_rect.top += ball_speed[1]

    # these two if block control if the ball is going out on the screen
    # if it's going it reverse speed to simulate a bounce
    if ball_rect.top <= 0 or ball_rect.bottom >= 480:
        ball_speed[1] = -ball_speed[1]

    if ball_rect.right >= 640:
        ball_speed[0] = -ball_speed[0]
    # this control if the ball touched the left side
    elif ball_rect.left <= 0:
        score -= 5
        # reset the ball to the center
        ball_rect = pygame.Rect((312, 232), (16, 16))
    # clear screen
    screen.fill((255, 255, 255))

    # draw the ball, the paddle and the score
    pygame.draw.rect(screen, (0, 0, 0), paddle_rect) # paddle
    pygame.draw.circle(screen, (0, 0, 0), ball_rect.center, ball_rect.width/2) # ball
    score_text = font.render(str(score), True, (0, 0, 0))
    screen.blit(score_text, (320-font.size(str(score))[0]/2, 5)) # score

    # update screen and wait 20 milliseconds
    pygame.display.flip()
    pygame.time.delay(20)

    # test if the ball is hit by the paddle
    # if yes reverse speed and add a point
    if paddle_rect.colliderect(ball_rect):
        ball_speed[0] = -ball_speed[0]
        score += 1

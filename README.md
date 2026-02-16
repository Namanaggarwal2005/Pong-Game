# Pong-Game
A classic Pong game built in Python using the TURTLE GRAPHICS LIBRARY . This project was created as part of Angela Yu’s 100 Days of Code: The Complete Python Pro Bootcamp.
1. Ball Module :
   - Inheritance:
         The Ball class extends Turtle, so it gains all the drawing and movement capabilities of the turtle graphics library.
  - Initialization (__init__):
        - Starts at the center (0,0).
        - Sets the ball’s color to white and shape to a circle.
        - Defines movement increments del_x and del_y (the change in x and y per frame).
  - Movement (move):
        - Calculates the new position by adding del_x and del_y to the current coordinates.
        - Uses penup() to prevent drawing lines while moving.
        - Moves the ball to the new position.
- Bounce Mechanics:
        - bounce_up(): Reverses the vertical direction by flipping the sign of del_y.
        - bounce_paddle(): Reverses the horizontal direction by flipping the sign of del_x.

2. Paddle Module :
   - Initialization (__init__):
        - Creates a paddle as a white rectangle (square stretched vertically).
        - Uses penup() to prevent drawing lines.
        - Sets speed to 0 (fastest rendering).
        - Positions the paddle at the given location (x‑coordinate) and centered vertically (y=0).
- Movement Methods:
        - move_up(): Increases the paddle’s y‑coordinate by 20 pixels.
        - move_down(): Decreases the paddle’s y‑coordinate by 20 pixels.
        - Both methods use goto() to update the paddle’s position smoothly.

3. ScoreBoard Module :
   - Initialization (__init__):
        - Sets the scoreboard color to white.
        - Hides the turtle cursor (hideturtle()) so only text is visible.
        - Initializes left and right player scores (l_score, r_score) to zero.
        - Calls write_score() to display the initial score.
  - Score Updating:
        - update_lscore(): Increases the left player’s score by 1 and refreshes the display.
        - update_rscore(): Increases the right player’s score by 1 and refreshes the display.
  - Writing Scores (write_score):
        - Clears the previous score display.
        - Positions the turtle at (-100, 200) to show the left score.
        - Positions the turtle at (100, 200) to show the right score.
        - Uses a large Arial font for visibility.

4. Main :
   - Screen Setup:
        - Creates an 800×600 black background window titled PONG.
        - tracer(0) disables auto‑refresh so updates happen manually for smoother animation.
- Game Objects:
        - Two paddles (paddle1, paddle2) positioned on opposite sides.
        - A Ball object that moves across the screen.
        - A Scoreboard to track points.
- Controls:
        - Right paddle: Up and Down arrow keys.
        - Left paddle: W and S keys.
- Game Loop:
        - Runs continuously while game_is_on is True.
        - Moves the ball each frame and checks for collisions.
- Collision Detection:
        - Wall Collision: Ball bounces vertically when hitting top/bottom edges.
        - Paddle Collision: Ball bounces horizontally when hitting a paddle.
        - Missed Hit: If the ball passes a paddle, the opponent scores a point, the ball resets to center, and speed slightly increases.




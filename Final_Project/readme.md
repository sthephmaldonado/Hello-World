Simple pong game with a robot background using Processing and Java. Every time the ball doesn't 
touch the movable bar the game ends and resets. 

My first idea was creating a character with a bouncing ball. After some research, and finishing it, 
I decided to make it as a pong game, since I already had the bouncing ball, I just had to add a movable bar, 
that when the ball hits it it goes to the other side.  

Description of the process:
 
First part of the program
Void setup: Define the initial properties of the program, such as screen size and background color.

Float: allows us to add and subtract with two decimals.  
Defining 5 variables
 2 variables on the X and Y axes with a value of 0
 2 more variables for the speed of the ball.  Random speed between 2-5
1 for the movable bar 

Void reset: so every time the player loses the game rests. (it didn't actually worked)

Drawing static shapes, the robot:
To make an ellipse: The first two numbers are the numbers of the circle circumference, the third point is the width
and the last is the height.
Stroke: sets the color to draw lines around the shape 
To draw squares, the quad function is used. The first two numbers are the upper left corner,
the next two are the lower left corner, the next two are the lower right corner and the last two are the upper right.

To remove edges of the figures we have to do is write the nostroke function and leave the parentheses empty.

For the ball to bounce
To give orders that the ball does not pass from the lower side X and bounces at the end of the screen on the Y axis. 
||: logic OR
Else, is so that the ball bounces constantly and does not touch the X axis if it does not fall back to the Axis y.

Variable for the conditions of the ball by the X and Y axes

In the end I put the color and draw the ball and make it ellipse type

Pong game:
I decided to add a pong game and use the robot as a background of the game. 
I tried using a simple pong game code https://gist.github.com/dc74089/4094da7928839063ae06 .
I start having troubles, the ball first wouldn't even touch the movable bar it will just keep bouncing constantly. 
After moving the code around the ball will actually touch the movable bar, but it will not return the ball.
I couldn't make the game reset when the ball doesn't touch the movable bar, it will constantly keep bouncing. 

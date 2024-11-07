Woobu Autonomous Drone

Woobu Autonomous Drone is a flying machine project. The code is completed. The code allows a flying machine to autonomously fly itself, autonomously hover, autonomously balance itself, and autonomously lands itself. A hardware fix and a different type of energy are needed though. 

This project uses Raspberry Pi Pico plus MPU6050 as main hardware, and (Micro)Python, HTML and Javascript as the main programming languages.

As of May 2024, the status of the drone is that it can read (using Kalman Filter and PID) X, Y angles faster than a blink of an eye and display (using AJAX, HTML, Javascript, ujson, utemplate) these X, Y values on your smartphone. On your smartphone, these buttons are provided: Auto Takeoff, Forward, Left, Right, Backward, Hover, Down, On, and Off.

The code purposely disabled the Forward, Left, Right, Backward buttons. All other buttons are enabled. Microdot framework, Javascript are used for the buttons control. When one working button is clicked, all other working buttons' opacity is changed to 50%.

As shown in the videos (https://www.youtube.com/watch?v=ECWFBZKwFYE and https://www.youtube.com/watch?v=JJ19gocz3pc), the current set-up has hardware issues and as mentioned a different type of energy is needed. These issues are the reason that I won't be sharing all of the hardware set-up. However, I am sharing all the code as the code is working. The code itself shows connections between Raspberry Pi Pico and MPU6050, and Raspberry Pi Pico and 4 Motors. A jpg file is also provided on how the code is organized. Put the index.html file inside templates folder and put the control.js file inside the static folder.

Future Milestones for Woobu Autonomous Drone Project:
- MPU6050's gyroscope and accelerometer shall be used to measure altitude and distance indoor and outdoor
- MPU6050 shall not only be used in autonomous drone setups but also in other flying machine setups

Support my work via Bitcoin donation: 
3PBQZaxNh1U5pmKQ3zSboVfSedTJ5jYdBs

or

bc1p63fyummqja06a3gyvw6r4khw8puw02p7fxd5wyysmgnmsm47cz0sa363pj

# bad-video-calculator
I doubt you've ever been this bored!™
This script provides a way to calculate what a video needs to be sped up by at certain intervals in a video to have a desired length. It sounds way more complicated that it actually is.

## Example
Lets say you have the following video: "[All Star by Smashmouth but it gets 15% faster everytime he says 'the'](https://www.youtube.com/watch?v=rLz1gBKk-t8)". This script allows you to find what percentage speed you should increase it so it has an exact length, for example 1:09. I know. It's literally the most useless thing in the universe.

For simplicity's sake, we're going to simplify it down so it's easier to understand. Let's use All Star again, but we're going to assume it's 1 minute long, and has speed up points at timestamp 0:15, timestamp 0:35, timestamp 0:40 and timestamp 0:58.

Once you run the program, it will prompt you to enter the current length of the video:
`What is the current length of the video? (Use a timestamp): 1:00`

It will then ask you for the desired length of the video, which is 0:30.
`What is the desired length of the video? (Use a timestamp): 0:30`

Now it will prompt you to enter the points in the video that need to be sped up. For us, this is 0:15, 0:35, 0:40 and 0:58.

    What is a point in the video that speeds up (1)? (timestamp or 'exit' to quit): 0:15
    What is a point in the video that speeds up (2)? (timestamp or 'exit' to quit): 0:35
    What is a point in the video that speeds up (3)? (timestamp or 'exit' to quit): 0:40
    What is a point in the video that speeds up (3)? (timestamp or 'exit' to quit): 0:58
    What is a point in the video that speeds up (4)? (timestamp or 'exit' to quit): exit

Finally, it will compute the answer.
`You need to multiply it by 0.53, or 53.38% to get a length of 30.0 seconds.`

## How
### In-Short
How you didn't ask? Well the maths behind it is actually pretty cool. In short, it uses *this* massive iterative formula (I hope):
<center>![Courtesy of https://ollybritton.com/katex/](https://i.imgur.com/then2Tj.png)</center>
(It's just [newton's method](https://en.m.wikipedia.org/wiki/Newton%27s_method) in disguise). Where:

- *p* is the set of all points that need to be sped up, plus the ending.
- *p_k* is the *k*-th point in the list.
- *z* is the desired length of the video.

### In-Long / Derivation
Every video timeline can be visualised as a one-dimensional line, with each point in the line representing the number of seconds into the video.

    0---------------------------------------z
    
Therefore, every point in the video that speeds up can be represented as a point on the line.
    
    0---------------------------------------z
        1       3               7   8       
        
We can come up with an expression for the length of a particular section, using the variable *c* as the multiplier. 

    0-1 = normal speed
    1-3 = normal speed * c
    3-7 = normal speed * c * c, or c²
    7-8 = normal speed * c * c * c, or c³
    8-z (which is ten in this example) = normal speed * c * c * c * c, or c⁴
    
Furthermore, we then could say that the length of the video is equal to the sum of these speeds:

    ( z - 8 ) * c⁴  +  (8 - 7) * c³  +  (7 - 3) * c²  + (3 - 1) * c  +  (1 - 0)
    
To write this in summation notation, I did this:
![](https://imgur.com/SPX5EfD.png)

The great thing that we can do now is reduce it down to a polynomial, by evaluating it:

    2c⁴ + c³ + 4c² + 2c + 1 = 10 (Using the previous example)

Now we just need to solve for c, so that it equals 10 when we evaluate it. The first thing we can do is subtract 10 (or *z*) from the answer so it equals zero:

    2c⁴ + c³ + 4c² + 2c + (1 - 10) = 0, so
    2c⁴ + c³ + 4c² + 2c - 9 = 0
    
To solve the polynomial, I decided to use [newton's method](https://en.m.wikipedia.org/wiki/Newton%27s_method), as I had already coded it in another project (hence the maths.py). Newton's method is an iterative formula for finding the root of any polynomial (with real roots). It looks like this:

![](https://imgur.com/KQhJdPp.png)

All we need to do is subsitute **f(x)** for the summation, and use **d/dx** instead of **f'(x)**. This gives us:

![](https://i.imgur.com/then2Tj.png)

Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> 
=========== RESTART: C:/Users/asus/Desktop/PythonIITM/02-Loops.py ===========
10
Hello
11
Hello
12
Hello
13
Hello
14
Hello
15
Hello
16
Hello
17
Hello
18
Hello
19
Hello
20
Hello
21
Hello
22
Hello
23
Hello
24
Hello
Bye
>>> for i in range(6):
	print('*' * i)

	

*
**
***
****
*****
>>> for i in reversed(range(6)):
	print('*' * i)

	
*****
****
***
**
*

>>> for i in range(6):
	print(' ' * (6-i) + '*' * (2*i+1))

	
      *
     ***
    *****
   *******
  *********
 ***********
>>> list_1 = [12,'Hello',10.5,True,'Bye']
>>> list_1[0]
12
>>> list_1[-1]
'Bye'
>>> 10.5 in list_1
True
>>> list_2 = [12,11,34,56,23,1,7,87,39]
>>> sorted(list_2)
[1, 7, 11, 12, 23, 34, 39, 56, 87]
>>> sorted(list_2, reverse = True)
[87, 56, 39, 34, 23, 12, 11, 7, 1]
>>> import turtle
>>> turtle.Pen()
<turtle.Turtle object at 0x0000020C2D6E3D68>
>>> turtle.forward(100)
>>> turtle.left()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    turtle.left()
TypeError: left() missing 1 required positional argument: 'angle'
>>> turtle.left(45)
>>> turtle.forward(100)
>>> turtle.reset()
>>> for i in range(40):
	turtle.forward(10*i)
	turtle.left(12*i)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 3, in <module>
    turtle.left(12*i)
  File "<string>", line 8, in left
  File "C:\Python36\lib\turtle.py", line 1699, in left
    self._rotate(angle)
  File "C:\Python36\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Python36\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 562, in _update
    self.cv.update()
  File "C:\Python36\lib\tkinter\__init__.py", line 1171, in update
    self.tk.call('update')
KeyboardInterrupt
>>> turtle.reset()
>>> for i in range(40):
	turtle.forward(5*i)
	turtle.left(45)

	
>>> turtle.reset()
>>> for i in range(40):
	turtle.circle(5*i)
	turtle.left(45)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    turtle.circle(5*i)
  File "<string>", line 8, in circle
  File "C:\Python36\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Python36\lib\turtle.py", line 3179, in _goto
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(40):
	turtle.circle(5*i)
	turtle.left(45)

	
>>> 

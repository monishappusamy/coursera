# "Stopwatch: The Game"
# @author Monish Kumar Appusamy

import simplegui

# define global variables
counter = 0 # the global seconds counter
x = 0 # the counter to count the successful hits
y = 0 # the counter to count the no. of stops

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """ transforms an input time (integer) into a string with m:ss.d format """
    a = t  // 600
    b = ( ( t / 10 ) % 60 ) // 10
    c = ( ( t / 10 ) % 60 ) % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# helper function to process hits & stops
def game():
    global x, y
    if ( timer.is_running() ):
        if ((counter % 10) == 0):
            x += 1
        y += 1

# helper function to reset call to reset all variables         
def reset():
    global counter, x, y
    counter = 0
    x = 0
    y = 0
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    game()
    timer.stop()
    
def reset_handler():
    reset()
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter +=1    
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), (80, 100), 22, 'White')
    score = str(x) + "/" + str(y)
    canvas.draw_text(score, (100, 70), 22, 'White')
    
# create frame
frame = simplegui.create_frame('stopwatch', 200, 200)

# register event handlers
frame.add_button("start", start_handler)
frame.add_button("stop", stop_handler)
frame.add_button("reset", reset_handler)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

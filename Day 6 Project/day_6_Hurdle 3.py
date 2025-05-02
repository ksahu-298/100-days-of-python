def turn_right():
    for right in range (0,3):
        turn_left()
        
def goal():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True :
    
    if wall_in_front() == True:
        goal()
    else :
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

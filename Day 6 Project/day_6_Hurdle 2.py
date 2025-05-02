def turn_right():
    for right in range (0,3):
        turn_left()
def goal():
    for complete in range (0,6):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
goal()

while at_goal() != True :
    goal()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

import turtle

# dictionary that will store all your production rules
DICT_OF_RULES = {}  


def create_pen(initial_angle):
    '''
    Receives initial orientation / direction given as an draw_angle (ex - 90).
    Returns a turtle object that will be your pen.
    '''
    # Create your pen
    pen = turtle.Turtle() 
    # Adjust your pen's width
    pen.pensize(1)
    # Adjust your pen's color
    pen.pencolor('green')
    # Adjust how fast you want to draw (fastest = 0)
    pen.speed(0)
    # Specify a title for your window
    pen.screen.title('L-System')
    # Specify initial direction you want to draw in
    pen.setheading(initial_angle) 

    return pen


def production_rule(sequence):
    '''
    Given a predecessor string
    Check if that string is in the dictionary of production rules
    Return the corresponding successor string, 
    Else return what you received
    '''
    # if predecessor string is in the dictionary
    if sequence in DICT_OF_RULES:
        # return the new successor string
        return DICT_OF_RULES[sequence]
    # else if it is not present, just return 
    # the predecessor string mapped to itself
    return sequence


def apply_production_rules(axiom, iterations):
    '''
    Given an initial string / axiom and amount of iterations
    Apply all the production rules to that list of symbols
    Return a new list of symbols
    '''
    # turn axiom string into a list of substrings
    # in our case, each of these substrings are 
    # an element of our list and each starts out
    # being a single character like F, +, -, etc
    list_of_substrings = [axiom]
    # for each iteration
    for _ in range(iterations):
        # start from the last substring in your list of substrings
        current_substring = list_of_substrings[-1]
        # for each character in that current substring, apply the production rule to it
        new_axiom = [production_rule(char) for char in current_substring]
        # add the new string to the list of substrings
        list_of_substrings.append(''.join(new_axiom))
    return list_of_substrings


def draw_L_system(our_pen, DICT_OF_RULES, segment_length, angle):
    # initialize your stack to push and pop your current L-system states 
    stack = []

    # for each symbol in your given string
    for command in DICT_OF_RULES:
        # begin drawing
        our_pen.pendown()

        # R = recursive string-rewriting where symbols on the right side of 
        # the recursive formulas are substituted by corresponding 
        # strings on the left side.  Used to build nodes. 
        # L = recursive string-rewriting where symbols on the left side of 
        # the recursive formulas are substituted by corresponding 
        # strings on the right side.  Used to build nodes. 
        # (see pgs. 15-16 of Algorithmic Botany Textbook)
        if command in ['F', 'R', 'L']:
            # draw one line segment length forward
            our_pen.forward(segment_length)
        elif command == 'f':
            # lift pen up / stop drawing
            our_pen.penup()  
            our_pen.forward(segment_length)
        elif command == "+":
            # turn right
            our_pen.right(angle)
        elif command == "-":
            # turn left
            our_pen.left(angle)
        elif command == "[":
            # push string / state to the memory stack
            stack.append((our_pen.position(), our_pen.heading()))
        elif command == "]":
            # lift pen up / stop drawing
            our_pen.penup()
            # pop string / state off the memory stack
            position, heading = stack.pop()
            our_pen.goto(position)
            our_pen.setheading(heading)


def main():

    # Asks user to input their starting Axiom
    axiom = input('Enter starting axiom (w): ')

    # Keep asking user to input their Production rules
    # minimum amount is 1 rule
    production_rule_num = 1 
    while True:
        production_rule = input(f'Enter production rule #{production_rule_num} (Input 0 if no more rules): ')
        
        # Check if there are no more production rules to be entered
        if production_rule == '0':
            break

        # Set key= initial symbol(s) to be replaced  
        # and set value= new symbol(s) you like to replace it with
        key, value = production_rule.split('->')

        # Represents our dictionary of rules
        DICT_OF_RULES[key] = value

        # For aesthetic purposes to help guide the future user input
        production_rule_num += 1

    # Asks user to input their number of iterations to apply their Production Rules   
    iterations = int(input('Enter number of iterations n: '))

    # Asks user to input the desired segment length that is created by Turtle 
    segment_length = int(input('Enter segment length: '))

    # Asks user to input Turtle's initial angle to start drawing towards
    # Angle starts at 3 o'clock and moves in the counterclockwise direction
    initial_angle = float(input('Enter initial angle: '))

    # Asks user to input Turtle's draw_angle to use each time when turning right '+' or left '-'
    draw_angle = float(input('Enter drawing angle: '))

    # Create the whole L-System by applying all the rules the starting axiom
    list_of_entire_L_system = apply_production_rules(axiom, iterations)  # axiom (initial string), nth iterations

    # Initialize Turtle object
    recursive_pen = create_pen(initial_angle)
    # Initialize the background paper or window you'll be drawing on
    window = turtle.Screen()  # create graphics window
    # Set the color of that background
    window.bgcolor('black')
    # Set the size of that background
    window.screensize(1000, 1000)

    # Turn the list representing the entire L-system
    # into an actual geometric drawing
    draw_L_system(recursive_pen, list_of_entire_L_system[-1], segment_length, draw_angle)  # draw list_of_entire_L_system

    # Ensures that the window that you are drawing in 
    # doesn't immediately close after execution
    window.exitonclick()

# Calling main function
if __name__ == "__main__":
    main()
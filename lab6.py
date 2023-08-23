import random

class cpre_lab6:
# author - Noah Cantrell, nbc@iastate.edu

    white_ball_drawings = []

    while True:
        for x in range(10):
            my_Seed = random.randrange(1, 100)
            white_Ball = random.randrange(1, 69)
            red_Ball = random.randrange(1, 26)
            
            for y in range(5):
                while True:
                    if not str(white_Ball) in white_ball_drawings:
                        white_ball_drawings.append(str(white_Ball))
                        break
                    else:
                        white_Ball = random.randrange(1, 69)

            red_Ball = random.randrange(1, 26)

            print("Week " + str(x+1) + ": White balls - " + str(" ".join(white_ball_drawings)) + " | red ball - " + str(red_Ball))

            white_ball_drawings = []
            red_Ball = 0;
        break
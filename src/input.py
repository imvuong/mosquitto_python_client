#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
Test inputs
"""

import tty
import sys
import select
import termios
import random, time

def show_menu():
    print("Instruction")
    print("")
    print("a s d f g h")
    print("z x c v b n")

def main():
    show_menu()
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    x = 0
    # while x != chr(27): # ESC
    #     x=sys.stdin.read(1)[0]
    #     # print("You pressed", x)
    #     if x == '.':
    #         break
    #     else:
    #         print("You pressed", x)

    # termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)  

    orders = 0
    operations = 0

    UP = "\x1B[9A"  #printing \x1B[2A (ESC [ 2 A) moves the cursor up 2 times, adjust the number as needed
    CLR = "\x1B[0K"
    print("\n\n\n\n\n\n\n\n\n")  # set up blank lines so cursor moves work

    while x != chr(27): # ESC
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            x=sys.stdin.read(1)[0]
            # x=sys.stdin.readline()
            print("You pressed", x)
            if x == '.':
                break
        
        # cmd = """Waist speed: %d%%   position: %d%%\n
        #     Shoulder speed: %d%%   position: %d%%\r""" % (
        #     waist_speed, waist_motor.position,
        #     shoulder_speed, shoulder_control1.position
            # )

        # sys.stdout.write(cmd)
        # sys.stdout.write("Waist speed: %d%%   position: %d%%"
        #                  "Shoulder speed: %d%%   position: %d%%\r" 
        #                 % (10, 20,
        #                  10, 30) )
        # sys.stdout.flush()


        orders += random.randrange(1, 3)
        operations += random.randrange(2, 10)

        print(f"{UP}\t\tSpeed\tRotation{CLR}\n", end="")
        print(f"Waist:\t\t{orders:03d}\t{orders}{CLR}\n", end="")
        print(f"Shoulder:\t{operations}\t{orders}{CLR}\n", end="")
        print(f"Elbow:\t\t{operations}\t{orders}{CLR}\n", end="")
        print(f"Roll:\t\t{operations}\t{orders}{CLR}\n", end="")
        print(f"Pitch:\t\t{operations}\t{orders}{CLR}\n", end="")
        print(f"Spin:\t\t{operations}\t{orders}{CLR}\n", end="")
        print(f"Grabber:\t{operations}\t{orders}{CLR}\n")

        # print(f"{UP}Waist: {orders}{CLR}\nShoulder: {operations}{CLR}\nElbow: {operations}{CLR}\nRoll: {operations}{CLR}\nPitch: {operations}{CLR}\nSpin: {operations}{CLR}\nGrabber: {operations}{CLR}\n")

        time.sleep(random.uniform(0.5, 2))

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)  


main()
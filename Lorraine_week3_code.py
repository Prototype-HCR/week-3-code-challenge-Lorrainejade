# Write your code here :-)
import time
import neopixel
import board
import digitalio


# make a neopixel object for 10 pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
pixels.brightness = 0.1

# declare some inputs for button a and b
button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.DOWN)

# declare some color constants
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
Color_list = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

# Define variables for bottons
cnt1 = 0
cnt2 = 0
B_Befor = button_B.value
B_Current = None
A_Befor = button_A.value
A_Current = None
Press_Duration = None
long_press = None
Brightness = 0.5
i = 0

while True:
    time.sleep(0.2)
    # gather input values
    button_a_read = button_A.value
    button_b_read = button_B.value

    # Count nembers pressed
    if A_Befor != button_a_read:
        A_Befor = button_a_read

        if button_a_read:
            click_time = time.monotonic()
        else:
            Press_Duration = time.monotonic() - click_time
            if Press_Duration <= 0.5:
                long_press = False
                print("ShortA press")
                cnt1 += 1
                print(cnt1)
            else:
                long_press = True
                print("LongA press")
                print(cnt1)
    # count B
    if B_Befor != button_b_read:
        B_Befor = button_b_read

        if button_b_read:
            click_time = time.monotonic()
        else:
            Press_Duration = time.monotonic() - click_time
            if Press_Duration <= 0.5:
                long_press = False
                print("ShortB press")
                cnt2 += 1
                print(cnt2)
            else:
                long_press = True
                print("LongB press")
                print(cnt2)
            i = cnt2 % len(Color_list)
            print(i)
    #  turn Light on

    if cnt1 % 2 == 1:
        color = YELLOW
        if button_a_read:
            Brightness -= 0.05
        print(Brightness)
        pixels.show()
    elif i != 0:
        color = Color_list[i]
        if button_b_read:
            Brightness += 0.05
        print(Brightness)
        pixels.show()
    else:
        color = OFF
        Brightness = 0.5
    pixels.fill(color)
    pixels.brightness = Brightness
    pixels.show()

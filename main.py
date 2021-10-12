def compass_heading():
    if input.temperature() > 0 and input.temperature() < 10:
        basic.show_number(10)
    if input.temperature() > 10 and input.temperature() < 20:
        basic.show_number(20)
    if input.temperature() > 20 and input.temperature() < 30:
        basic.show_number(30)
    if input.temperature() > 30 and input.temperature() < 40:
        basic.show_number(40)
    if input.temperature() > 40 and input.temperature() < 50:
        basic.show_number(50)
    if input.temperature() > 50 and input.temperature() < 60:
        basic.show_number(60)
    if input.temperature() > 60 and input.temperature() < 70:
        basic.show_number(70)
    if input.temperature() > 70 and input.temperature() < 80:
        basic.show_number(80)
    if input.temperature() > 80 and input.temperature() < 90:
        basic.show_number(90)
    if input.temperature() > 90 and input.temperature() < 100:
        basic.show_number(100)
    if input.temperature() > 100 and input.temperature() < 110:
        basic.show_number(110)
    if input.temperature() > 110 and input.temperature() < 120:
        basic.show_number(120)
    if input.temperature() > 120 and input.temperature() < 130:
        basic.show_number(130)
    if input.temperature() > 130 and input.temperature() < 140:
        basic.show_number(140)
    if input.temperature() > 140 and input.temperature() < 150:
        basic.show_number(150)
    if input.temperature() > 150 and input.temperature() < 160:
        basic.show_number(160)
    if input.temperature() > 160 and input.temperature() < 170:
        basic.show_number(170)
    if input.temperature() > 170 and input.temperature() < 180:
        basic.show_number(180)
    if input.temperature() > 180 and input.temperature() < 190:
        basic.show_number(190)
    if input.temperature() > 190 and input.temperature() < 200:
        basic.show_number(200)
    if input.temperature() > 200 and input.temperature() < 210:
        basic.show_number(210)
    if input.temperature() > 210 and input.temperature() < 220:
        basic.show_number(220)
    if input.temperature() > 220 and input.temperature() < 230:
        basic.show_number(230)
    if input.temperature() > 230 and input.temperature() < 240:
        basic.show_number(240)
    if input.temperature() > 240 and input.temperature() < 250:
        basic.show_number(250)
    if input.temperature() > 250 and input.temperature() < 260:
        basic.show_number(260)
    if input.temperature() > 260 and input.temperature() < 270:
        basic.show_number(270)
    if input.temperature() > 270 and input.temperature() < 280:
        basic.show_number(280)
    if input.temperature() > 280 and input.temperature() < 290:
        basic.show_number(290)
    if input.temperature() > 290 and input.temperature() < 300:
        basic.show_number(300)
    if input.temperature() > 300 and input.temperature() < 310:
        basic.show_number(310)
    if input.temperature() <= 310 and input.temperature() < 320:
        basic.show_number(320)
    if input.temperature() > 320 and input.temperature() < 330:
        basic.show_number(330)
    if input.temperature() > 330 and input.temperature() < 340:
        basic.show_number(340)
    if input.temperature() > 340 and input.temperature() < 350:
        basic.show_number(350)
    if input.temperature() > 350 and input.temperature() < 360:
        basic.show_number(360)

def on_button_pressed_a():
    read_temp()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    compass_heading()
input.on_button_pressed(Button.B, on_button_pressed_b)

def read_temp():
    if input.temperature() == -15:
        basic.show_number(-15)
    if input.temperature() == -14:
        basic.show_number(-14)
    if input.temperature() == -13:
        basic.show_number(-13)
    if input.temperature() == -12:
        basic.show_number(-12)
    if input.temperature() == -11:
        basic.show_number(-11)
    if input.temperature() == -10:
        basic.show_number(-10)
    if input.temperature() == -9:
        basic.show_number(-9)
    if input.temperature() == -8:
        basic.show_number(-8)
    if input.temperature() == -7:
        basic.show_number(-7)
    if input.temperature() == -6:
        basic.show_number(-6)
    if input.temperature() == -5:
        basic.show_number(-5)
    if input.temperature() == -4:
        basic.show_number(-4)
    if input.temperature() == -3:
        basic.show_number(-3)
    if input.temperature() == -2:
        basic.show_number(-2)
    if input.temperature() == -1:
        basic.show_number(-1)
    if input.temperature() == 0:
        basic.show_number(0)
    if input.temperature() == 1:
        basic.show_number(1)
    if input.temperature() == 2:
        basic.show_number(2)
    if input.temperature() == 3:
        basic.show_number(3)
    if input.temperature() == 4:
        basic.show_number(4)
    if input.temperature() == 5:
        basic.show_number(5)
    if input.temperature() == 6:
        basic.show_number(6)
    if input.temperature() == 7:
        basic.show_number(7)
    if input.temperature() == 8:
        basic.show_number(8)
    if input.temperature() == 9:
        basic.show_number(9)
    if input.temperature() == 10:
        basic.show_number(11)
    if input.temperature() == 12:
        basic.show_number(12)
    if input.temperature() == 13:
        basic.show_number(13)
    if input.temperature() == 14:
        basic.show_number(14)
    if input.temperature() == 15:
        basic.show_number(15)
    if input.temperature() == 16:
        basic.show_number(16)
    if input.temperature() == 17:
        basic.show_number(17)
    if input.temperature() == 18:
        basic.show_number(18)
    if input.temperature() == 19:
        basic.show_number(19)
    if input.temperature() == 20:
        basic.show_number(20)
    if input.temperature() == 21:
        basic.show_number(21)
    if input.temperature() == 22:
        basic.show_number(22)
    if input.temperature() == 23:
        basic.show_number(23)
    if input.temperature() == 24:
        basic.show_number(24)
    if input.temperature() == 25:
        basic.show_number(25)
    if input.temperature() == 26:
        basic.show_number(26)
    if input.temperature() == 27:
        basic.show_number(27)
    if input.temperature() == 28:
        basic.show_number(28)
    if input.temperature() == 29:
        basic.show_number(29)
    if input.temperature() == 30:
        basic.show_number(30)

def on_forever():
    if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.clear_screen()
        basic.pause(60000)
    else:
        if input.light_level() > 150:
            basic.show_leds("""
                # . # . #
                                . # # # .
                                # # # # #
                                . # # # .
                                # . # . #
            """)
        if input.light_level() < 150:
            basic.show_leds("""
                . # # # #
                                # # # . .
                                # # . . .
                                # # # . .
                                . # # # #
            """)
basic.forever(on_forever)

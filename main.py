def on_logo_pressed():
    basic.show_number(Factor_2 * Factor_1)
    basic.pause(200)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global Factor_1, Factor_2
    Factor_1 = randint(0, 10)
    Factor_2 = randint(0, 10)
    basic.show_number(Factor_1)
    basic.pause(200)
    basic.show_string("X")
    basic.pause(200)
    basic.show_number(Factor_2)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

Factor_1 = 0
Factor_2 = 0
basic.show_string("Tablas de multiplicar")
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)

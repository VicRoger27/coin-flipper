def on_button_pressed_a():
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SQUARE)
    if Math.random_boolean():
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)
    basic.pause(5000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
    if Math.random_boolean():
        basic.show_icon(IconNames.SMALL_DIAMOND)
    else:
        basic.show_icon(IconNames.DIAMOND)
    basic.pause(5000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        # . # . #
                . # # # .
                # # . # #
                . # # # .
                # . # . #
    """)
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)

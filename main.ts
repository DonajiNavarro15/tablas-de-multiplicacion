input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(Factor_2 * Factor_1)
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    Factor_1 = randint(0, 10)
    Factor_2 = randint(0, 10)
    basic.showNumber(Factor_1)
    basic.pause(200)
    basic.showString("X")
    basic.pause(200)
    basic.showNumber(Factor_2)
    basic.pause(200)
    basic.clearScreen()
})
let Factor_1 = 0
let Factor_2 = 0
basic.showString("Tablas de multiplicar")
basic.clearScreen()
basic.forever(function () {
	
})

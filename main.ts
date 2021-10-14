let sos = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.compassHeading())
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    sos = -1
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A) && input.buttonIsPressed(Button.B)) {
        sos = 1
        while (sos >= 0) {
            for (let index = 0; index < 3; index++) {
                pins.digitalWritePin(DigitalPin.P0, 1)
                basic.pause(500)
                pins.digitalWritePin(DigitalPin.P0, 0)
                basic.pause(500)
            }
            for (let index = 0; index < 3; index++) {
                pins.digitalWritePin(DigitalPin.P0, 1)
                basic.pause(1000)
                pins.digitalWritePin(DigitalPin.P0, 0)
                basic.pause(1000)
            }
            for (let index = 0; index < 3; index++) {
                pins.digitalWritePin(DigitalPin.P0, 1)
                basic.pause(500)
                pins.digitalWritePin(DigitalPin.P0, 0)
                basic.pause(500)
            }
            basic.pause(2000)
        }
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
        basic.clearScreen()
        basic.pause(2000)
    } else {
        if (input.lightLevel() > 150) {
            basic.showLeds(`
                # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
                `)
        }
        if (input.lightLevel() < 150) {
            basic.showLeds(`
                . # # # #
                # # # . .
                # # . . .
                # # # . .
                . # # # #
                `)
        }
    }
})

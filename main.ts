radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        a = -1
        OmniBit.RGB_Program().showColor(neopixel.colors(NeoPixelColors.Red))
        OmniBit.RGB_Program().show()
    } else if (receivedNumber == 2) {
        OmniBit.RGB_Program().showColor(neopixel.colors(NeoPixelColors.Green))
        OmniBit.RGB_Program().show()
    } else if (receivedNumber == 3) {
        OmniBit.RGB_Program().showColor(neopixel.colors(NeoPixelColors.Blue))
        OmniBit.RGB_Program().show()
    } else if (receivedNumber == 4) {
        a = 1
        OmniBit.RGB_Program().showColor(neopixel.colors(NeoPixelColors.Yellow))
        OmniBit.RGB_Program().show()
    } else {
        a = 0
        OmniBit.RGB_Program().clear()
        OmniBit.RGB_Program().show()
    }
})
radio.onReceivedString(function (receivedString) {
    saveString = receivedString
})
let y = 0
let x = 0
let flag2 = 0
let flag1 = 0
let saveString = ""
let a = 0
OmniBit.MotorStopAll()
OmniBit.RGB_Program().clear()
OmniBit.RGB_Program().show()
basic.showIcon(IconNames.Happy)
radio.setGroup(1)
radio.setTransmitPower(7)
basic.forever(function () {
    flag1 = parseFloat(saveString.charAt(1))
    flag2 = parseFloat(saveString.charAt(2))
    x = parseFloat(saveString.substr(4, flag1))
    y = parseFloat(saveString.substr(4 + flag1, flag2))
    OmniBit.Handle(x, y, a)
})

## RESISTANCE IS HIDDEN
Unlike an LED, a push-button switch doesn’t need a currentlimiting resistor. It does still need a resistor, though: it needs
what is known as a pull-up or pull-down resistor, depending
on how your circuit works. Without a pull-up or pull-down
resistor, an input is known as floating – which means it has a
‘noisy’ signal which can trigger even when you’re not pushing
the button.
So where’s the resistor in this circuit? Hidden in your Pico.
Just like it has an on-board LED, your Pico includes an on-board
programmable resistor connected to each GPIO pin. These can
be set in MicroPython to pull-down resistors or pull-up resistors
as required by your circuit.
What’s the difference? A pull-down resistor connects the
pin to ground, meaning when the push-button isn’t pressed,
the input will be 0. A pull-up resistor connects the pin to 3V3,
meaning when the push-button isn’t pressed, the input will be 1.
All the circuits in this book use the programmable resistors
in the pull-down mode.
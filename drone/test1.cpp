#include <unistd.h>
#include <iostream>
#include <iomanip>
#include <grove.hpp>
//#include "usr/include/upm/grove.hpp"


/*
 * On board LED blink C++ example
 *
 * Demonstrate how to blink the on board LED, writing a digital value to an
 * output pin using the MRAA library.
 * No external hardware is needed.
 *
 * - digital out: on board LED
 *
 * Additional linker flags: none
 */

int main()
{
// Create the temperature sensor object using AIO pin 0
    upm::GroveTemp* temp = new upm::GroveTemp(0);
    std::cout << temp->name() << std::endl;

    // Read the temperature ten times, printing both the Celsius and
    // equivalent Fahrenheit temperature, waiting one second between readings
    for (int i=0; i < 10; i++) {
        int celsius = temp->value();
        int fahrenheit = (int) (celsius * 9.0/5.0 + 32.0);
        printf("%d degrees Celsius, or %d degrees Fahrenheitn", celsius, fahrenheit);
        sleep(1);
    }

    // Delete the temperature sensor object
    delete temp;

    return 0;
}


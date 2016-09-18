#ifndef
#define DRONE_API

#include <unistd.h>
#include <iostream>
#include <iomanip>
#include <grove.hpp>
#include <signal.h>
#include <mma7660.hpp>
#include <jhd1313m1.hpp>
#include <mraa.hpp>
#include <groveled.hpp>


namespace libdrone{

	class cargo_io{
		public:
			cargo_io();
			~cargo_io();

		private:
			//Accelerometer
			upm::MMA7660 * accel = NULL;
			//LCD
			upm::Jhd1313m1 * lcd = NULL;
			//Temp
			upm::GroveTemp * temp = NULL;
			//headlight
			mraa::Pwm * pwm = NULL;
			//LEDs
			upm::GroveLed * red_led = NULL
			upm::GroveLed * green_led = NULL
			upm::GroveLed * blue_led = NULL

			

	
	};
}

#endif

#ifndef DRONE_API
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
			
			void getAcceleration(float * x, float * y, float * z);
			int getTempF();
			int getTempC();

			void switchHeadLight(float level = 0.5f);

			void switchLed(int in);
			void switchRedLed();
			void switchGreenLed();

		private:
			//Accelerometer
			upm::MMA7660 * accel = NULL;
			//LCD
			upm::Jhd1313m1 * lcd = NULL;
			//Temp
			upm::GroveTemp * temp = NULL;
			//headlight
			mraa::Pwm * headlight = NULL;
			bool headlight_on = false;
			//LEDs
			upm::GroveLed * red_led = NULL;
			bool red_led_on = false;
			upm::GroveLed * green_led = NULL;
			bool green_led_on = false;

	
	};
}

#endif

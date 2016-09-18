#include "drone.h"

using namespace std;

namespace libdrone{
	cargo_io::cargo_io(){
		//Do nothing now...
	}

	cargo_io::~cargo_io(){
		if(accel!=NULL)
			delete accel;
		if(lcd!=NULL)
			delete lcd;
		if(temp!=NULL)
			delete temp;
		if(headlight!=NULL)
			delete headlight;
		if(red_led!=NULL)
			delete red_led;
		if(green_led!=NULL)
			delete green_led;
	}


	void cargo_io::getAcceleration(float * x, float *y , float *z){
		//Create accel object if does not exist
		if(accel == NULL){
			accel = new upm::MMA7660(MMA7660_I2C_BUS, MMA7660_DEFAULT_I2C_ADDR);
			accel->setModeStandby();
			accel->setSampleRate(upm::MMA7660::AUTOSLEEP_64);
			accel->setModeActive();
		}

		accel->getAcceleration(x,y,z);

	}


	int cargo_io::getTempF(){
		int celsius = getTempC();
		int fahrenheit = (int) (celsius * 9.0/5.0 + 32.0);
		return fahrenheit;

	}

	int cargo_io::getTempC(){

		//create temp object if not already exist
		if(temp == NULL){
			temp = new upm::GroveTemp(0);
		}

		return temp->value();
	}

	void cargo_io::switchHeadLight(float level){
		if(headlight == NULL){
			headlight = new mraa::Pwm(3);
		}

		if(level == 0.2f || level == 0.4f)
			headlight->enable(true);


		headlight->write(level);

	}

	void cargo_io::switchRedLed(){
		if(red_led == NULL){
			red_led = new upm::GroveLed(4);
		}

		if(!red_led_on){
			red_led->on();
			red_led_on = true;
		}
		else{
			red_led->off();
			red_led_on = false;
		}


	}
	void cargo_io::switchGreenLed(){
		if(green_led == NULL){
			green_led = new upm::GroveLed(8);
		}

		if(!green_led_on){
			green_led->on();
			cout << "diplaying green now"<<endl;
			green_led_on = true;
		}
		else{
			green_led->off();
			green_led_on = false;
		}


	}


	void cargo_io::switchLed(int in){
		if(in>1 || in<0)
			return;
		if(in==0)
			switchRedLed();
		else 
			switchGreenLed();

	}



}



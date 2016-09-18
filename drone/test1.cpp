#include <unistd.h>
#include <iostream>
#include <iomanip>
#include <grove.hpp>
#include <signal.h>
#include <mma7660.hpp>
#include <jhd1313m1.hpp>

using namespace std;

int shouldRun = true;

void sig_handler(int signo){
if(signo==SIGINT)
	shouldRun= false;
}

int main()
{
    signal(SIGINT, sig_handler);

    upm::MMA7660 *accel = new upm::MMA7660(MMA7660_I2C_BUS, MMA7660_DEFAULT_I2C_ADDR);
    upm::Jhd1313m1 *lcd = new upm::Jhd1313m1(0, 0x3E, 0x62);
    lcd->setCursor(0,0);
    lcd->write("Hello World");
    lcd->setCursor(1,2);
    lcd->write("Hello World");
    sleep(5);
 

    accel->setModeStandby();
    accel->setSampleRate(upm::MMA7660::AUTOSLEEP_64);
    accel->setModeActive();


// Create the temperature sensor object using AIO pin 0
    upm::GroveTemp* temp = new upm::GroveTemp(0);
    std::cout << temp->name() << std::endl;

    // Read the temperature ten times, printing both the Celsius and
    // equivalent Fahrenheit temperature, waiting one second between readings
    while (shouldRun){
        int celsius = temp->value();
        int fahrenheit = (int) (celsius * 9.0/5.0 + 32.0);
        printf("%d degrees Celsius, or %d degrees Fahrenheitn\n", celsius, fahrenheit);
	float a,b,c;
	accel->getAcceleration(&a,&b,&c);
	cout << "Acceleration: x=" <<a<< "\ty="<<b<<"\tz="<<c<<endl;
	sleep(1);
    }
    // Delete the temperature sensor object
    delete lcd;
    delete temp;
    delete accel;

    return 0;
}


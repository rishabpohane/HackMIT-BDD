#include "drone.h"
#include <string>
#include <fstream>
#include <iostream>

int main(){
	libdrone::cargo_io ci;

	ci.lcdSetCursor(0,0);
	ci.lcdWrite("Helloo");
	ci.lcdSetColor(255,0,0);
	sleep(4);
	ci.lcdSetColor(0,255,0);
	sleep(4);
	ci.lcdSetColor(0,0,255);
	sleep(4);

	return 1;
}

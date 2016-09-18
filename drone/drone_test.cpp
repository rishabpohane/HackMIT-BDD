#include "drone.h"
#include <string>
#include <fstream>
#include <iostream>


using namespace std;


int shouldRun = true;

void sig_handler(int signo){
if(signo==SIGINT)
	shouldRun= false;
}

int main(){
	system("python detectFace.py & ");
	sleep(4);

	libdrone::cargo_io ci;
	float x,y,z;
	int temp;

	ci.lcdSetCursor(0,0);
	ci.lcdWrite("No data");
	ci.lcdSetColor(255,0,0);

	bool correct_face_detected  = false;
	ci.switchRedLed();

	while(shouldRun){

		ifstream myfile("f_status.txt", ifstream::in);
		//myfile.open("f_status.txt", ios::out);
		if(myfile.is_open()){
			string line1;
			string line2;
			getline(myfile,line1);
			getline(myfile,line2);
			int status = atoi(line1.c_str());
			if(status == 1){
				shouldRun = false;
				correct_face_detected = true;
			}
			ci.lcdSetCursor(0,0);
			ci.lcdWrite("               ");
			ci.lcdSetCursor(0,0);
			ci.lcdWrite(line2);
		}
		ci.getAcceleration(&x,&y,&z);
		temp = ci.getTempC();

		system(("curl -X POST -d '{\"xa\":\""+to_string(x)+"\",\"ya\":\""+to_string(y)+"\",\"za\":\""+to_string(z)+"\",\"temp\":\""+to_string(temp)+"\", \"face\":\""+to_string(correct_face_detected)+"\"}' } https://hackmit-bdd.firebaseio.com/flight-1.json &>/dev/null").c_str());
		if(correct_face_detected){
			ci.switchGreenLed();
			ci.switchRedLed();
			ci.switchHeadLight();
			ci.lcdSetColor(0,255,0);
		}

		sleep(1);
	}

	sleep(10);
	


}
//.#curl -X POST -d '{example:pls}' https://hackmit-bdd.firebaseio.com/flight-1.json

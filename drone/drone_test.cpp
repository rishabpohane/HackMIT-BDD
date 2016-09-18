#include "drone.h"
#include <string>


using namespace std;


int shouldRun = true;

void sig_handler(int signo){
if(signo==SIGINT)
	shouldRun= false;
}

int main(){
	libdrone::cargo_io ci;

	float x,y,z;
	int temp;

	bool correct_face_detected  = false;
	ci.switchRedLed();

	while(shouldRun){
		ci.getAcceleration(&x,&y,&z);
		temp = ci.getTempC();

		system(("curl -X POST -d '{\"xa\":\""+to_string(x)+"\",\"ya\":\""+to_string(y)+"\",\"za\":\""+to_string(z)+"\",\"temp\":\""+to_string(temp)+"\"}' } https://hackmit-bdd.firebaseio.com/flight-1.json").c_str());

		if(correct_face_detected){
			ci.switchGreenLed();
			ci.switchRedLed();
			ci.switchHeadLight();
		}

		sleep(1);

	}
	


}
//.#curl -X POST -d '{example:pls}' https://hackmit-bdd.firebaseio.com/flight-1.json

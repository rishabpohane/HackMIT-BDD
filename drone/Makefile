INCLUDE = -I/usr/include/upm
LIBS = -lupm-grove -lupm-mma7660 -lupm-i2clcd -std=c++11 -lmraa -g


test_sensor : drone.o drone_test.o
	g++ $? $(INCLUDE) $(LIBS) -o $@

red_led : drone.o red_led.o
	g++ $? $(INCLUDE) $(LIBS) -o $@

green_led : drone.o green_led.o
	g++ $? $(INCLUDE) $(LIBS) -o $@

lcd : drone.o lcd.o
	g++ $? $(INCLUDE) $(LIBS) -o $@


green_led.o : green_led.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@

red_led.o : red_led.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@

lcd.o : lcd.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@

drone.o : drone.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@

drone_test.o : drone_test.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@


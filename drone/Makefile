INCLUDE = -I/usr/include/upm
LIBS = -lupm-grove -lupm-mma7660 -lupm-i2clcd -std=c++11 -lmraa -g


test_sensor : drone.o drone_test.o
	g++ $? $(INCLUDE) $(LIBS) -o $@

drone.o : drone.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@
drone_test.o : drone_test.cpp
	g++ $? -c $(INCLUDE) $(LIBS) -o $@


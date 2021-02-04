CPP = g++
CPPFLAGS = -Wall -std=c++11 -MD -Wno-class-conversion -g -fpic
LD = g++
#LD_DIR = "-L/usr/local/include"
LIBS = $(addprefix -l, pthread dl amqpcpp uv)
LDFLAGS =  -Wall -shared
SHARED_LIB = libuv_example.so
TARGET = libuv_example
INCLUDES = $(addprefix -I, ../include /home/ryan/3p/libuv/include)
CPP_FILES = libuv.cpp
SHARED_OBJECTS = libuv_test.o

#${TARGET}: ${SHARED_LIB}
#	${LD} ${LDFLAGS} ${LIBS} $^ -o $@

#${SHARED_LIB} : ${SHARED_OBJECTS}
#	${LD} ${LDFLAGS} -o $@ $^

${TARGET} : ${CPP_FILES}
	echo $@
	echo $^
	${CPP} ${CPPFLAGS} ${INCLUDES} ${LIBS} -o $@ $^

clean:
	rm -f ${SHARED_OBJECTS} ${SHARED_LIB} ${TARGET} libuv_test.d

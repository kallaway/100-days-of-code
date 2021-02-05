CPP = g++
CPPFLAGS = -Wall -std=c++11 -MD -Wno-class-conversion -g -fpic
LD = g++
LIBS = $(addprefix -l, pthread dl amqpcpp ev ssl)
LDFLAGS =  -Wall -shared
SHARED_LIB = libev_example.so
TARGET = libev_example
INCLUDES = $(addprefix -I, /home/ryan/3p/libev/include)
CPP_FILES = libev.cpp
SHARED_OBJECTS = libev_test.o

#${TARGET}: ${SHARED_LIB}
#	${LD} ${LDFLAGS} ${LIBS} $^ -o $@

#${SHARED_LIB} : ${SHARED_OBJECTS}
#	${LD} ${LDFLAGS} -o $@ $^

${TARGET} : ${CPP_FILES}
	echo $@
	echo $^
	${CPP} ${CPPFLAGS} ${INCLUDES} ${LIBS} -o $@ $^

clean:
	rm -f ${SHARED_OBJECTS} ${SHARED_LIB} ${TARGET} libev_test.d

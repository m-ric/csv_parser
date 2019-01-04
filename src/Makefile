all: csvparser

clean:
	rm -f *.o *.so csvparser_cffi.c

libcsvparser.so: csvparser.o
	gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic $^

#point: export LD_LIBRARY_PATH = $(shell pwd)
#point: libcsvparser.so
#	./csvparser_build.py

csvparser: export LD_LIBRARY_PATH = $(shell pwd)
csvparser: libcsvparser.so
	./csvparser_build.py

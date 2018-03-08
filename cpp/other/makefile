CC=g++
CFLAGS=-std=c++14 -Wall -Wextra -pedantic -I.
DEPS =
OBJ = template_example.o
TARGET = main
RM = rm

all: $(TARGET) run

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	$(RM) -f *.o $(TARGET)

run: $(TARGET)
	./$(TARGET)

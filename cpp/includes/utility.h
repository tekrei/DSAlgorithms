#ifndef UTILITY_H_
#define UTILITY_H_

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <memory>

/**
 * Generate random integer numbers as an array
 * count: array size to generate
 */
int *generate(int count) {
  unsigned int seed = time(NULL);
  int *result = new int[count];
  for (int i = 0; i < count; i++) {
    // generate integer in the range 0 to 99
    result[i] = rand_r(&seed) % 100;
  }
  return result;
}

/**
 * Print array to the screen
 */
void print(int *numbers, int count) {
  for (int i = 0; i < count - 1; i++) {
    std::cout << numbers[i] << ", ";
  }
  std::cout << numbers[count - 1] << std::endl;
}

#endif  // INCLUDES_UTILITY_H_

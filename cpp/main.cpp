#include "includes/bstree.h"
#include "includes/pair.h"
#include "includes/search.h"
#include "includes/sort.h"
#include "includes/utility.h"

int main() {
  std::cout << "TEMPLATES" << std::endl;
  /*
   * auto: type of the variable is automatically deduced from its initializer
   * make_unique: constructs an object and wraps it in unique_ptr
   * unique_ptr: a smart pointer that owns and manages another object through a
   * pointer and disposes of that object when the unique_ptr goes out of scope
   */
  // create a unique pointer to a Pair object with int values
  auto p1 = std::make_unique<Pair<int, int>>(Pair<int, int>(1, 2));
  // print out the values using output operator overloading
  std::cout << *p1 << std::endl;
  // create another unique pointer to a Pair with int, string values
  auto p2 = std::make_unique<Pair<int, std::string>>(
      Pair<int, std::string>(25, "hello world"));
  std::cout << *p2 << std::endl;
  // directly create and print out a Pair object with int, string values
  auto p3 = Pair<int, std::string>(65, "testing");
  std::cout << p3.to_string() << std::endl;
  // directly create and print out a Pair object with string, string values
  auto p4 = Pair<std::string, std::string>("another", "pair");
  std::cout << p4.getFirst() << "," << p4.getSecond() << std::endl;

  // generate random integer array
  std::cout << "SORTING" << std::endl;
  int numberCount = 25;
  int *numbers = generate(numberCount);
  std::cout << "Unsorted:" << std::endl;
  print(numbers, numberCount);
  std::cout << "Binary search:"
            << binary_search(numbers, numberCount, numbers[10]) << std::endl;
  std::cout << "Linear search:"
            << linear_search(numbers, numberCount, numbers[10]) << std::endl;
  std::cout << "Insertion sort:" << std::endl;
  print(insertion_sort(numbers, numberCount), numberCount);
  std::cout << "Selection sort:" << std::endl;
  print(selection_sort(numbers, numberCount), numberCount);
  std::cout << "Merge sort:" << std::endl;
  print(merge_sort(numbers, 0, numberCount - 1), numberCount);

  std::cout << "BINARY SEARCH TREE" << std::endl;
  BSTree<float> tree;
  for (int i = 0; i < 10; i++) {
    tree.insert(i / 10.0f);
  }
  tree.inorder();
  std::cout << "Current size:" << tree.getSize() << std::endl;
  tree.remove(0.5f);
  tree.remove(0.9f);
  tree.remove(0.0f);
  std::cout << "Current size:" << tree.getSize() << std::endl;
  tree.inorder();
  tree.remove(0.8f);
  std::cout << "Current size:" << tree.getSize() << std::endl;
  return 0;
}

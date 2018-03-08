#include <iostream>
#include <memory>
#include <sstream>

/*
 * An example of templates, unique pointers and operator overloading
 */
using namespace std;

/*
 * A Pair class to store two values with possibility of different types
 */
template <class K, class V> class Pair {
public:
  Pair() : first(0), second(0) {}
  Pair(K k, V v) : first(k), second(v) {}

  K getFirst() const { return first; }

  V getSecond() { return second; }

  /* a method to return string represantation of the object */
  string to_string() {
    stringstream ss;
    ss << "(" << first << "," << second << ")";
    return ss.str();
  }

  /**
   * a method for overloading stream insertion (output) operator
   *
   * friend declaration grants a function or another class access to private
   * and protected members of the class where the friend declaration appears
   *
   * << and >> operators are overloaded as global methods because in operator
   * overloading if an operator is overloaded as a member, then it must be a
   * member of the object on left side of the operator
   */
  friend ostream &operator<<(ostream &os, const Pair<K, V> &pair) {
    return os << "(" << pair.first << "," << pair.second << ")";
  }

private:
  K first;
  V second;
};

int main() {
  /*
   * auto: type of the variable is automatically deduced from its initializer
   * make_unique: constructs an object and wraps it in unique_ptr
   * unique_ptr: a smart pointer that owns and manages another object through a
   * pointer and disposes of that object when the unique_ptr goes out of scope
   */
  // create a unique pointer to a Pair object with int values
  auto p1 = make_unique<Pair<int, int>>(Pair<int, int>(1, 2));
  // print out the values using output operator overloading
  cout << *p1 << endl;
  // create another unique pointer to a Pair with int, string values
  auto p2 = make_unique<Pair<int, string>>(Pair<int, string>(25, "hello world"));
  cout << *p2 << endl;
  // call toString method
  cout << p2->to_string() << endl;
  // directly create and print out a Pair object with int, string values
  cout << Pair<int, string>(65, "testing") << endl;
  // directly create and print out a Pair object with string, string values
  cout << Pair<string, string>("another", "pair") << endl;
  return 0;
}

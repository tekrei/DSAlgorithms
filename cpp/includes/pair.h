#ifndef INCLUDES_PAIR_H_
#define INCLUDES_PAIR_H_

#include <ostream>
#include <sstream>
#include <string>

/*
 * A Pair class to store two values with possibility of different types
 */
template <class K, class V>
class Pair {
 public:
  Pair() : first(0), second(0) {}
  Pair(K k, V v) : first(k), second(v) {}

  K getFirst() const { return first; }

  V getSecond() { return second; }

  /* a method to return string represantation of the object */
  std::string to_string() {
    std::stringstream ss;
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
  friend std::ostream &operator<<(std::ostream &os, const Pair<K, V> &pair) {
    return os << "(" << pair.first << "," << pair.second << ")";
  }

 private:
  K first;
  V second;
};

#endif  // INCLUDES_PAIR_H_

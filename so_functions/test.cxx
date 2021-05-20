#include <iostream>
#include "./lib.hxx"

int main() {
    std::cout << "Calling sum(101, 202) from so... result: " << sum_ints(101, 202) << std::endl;
    std::cout << "Calling mul(101, 202) from so... result: " << mul_ints(101, 202) << std::endl;
    return 0;
}
#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    //Setting the seed
    srand(0);
    //Uniform distribution parameters
    char* numberStr = argv[1];
    int a=1;
    int n = std::atoi(numberStr);
    int value;
    for (int i = 0; i<10; i++) {
        value = a+random()%n;
        std::cout << "Random value = " << value <<std::endl;
    } 
    return 0;
}
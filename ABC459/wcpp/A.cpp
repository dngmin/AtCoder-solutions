#include <iostream>
#include <string>

int main()
{
    std::string string = "HelloWorld";
    int X; std::cin >> X;
    for (int i = 0; i < 10; i++)
    {
        if (i != X-1) std::cout << string[i];
    }
    return 0;
}
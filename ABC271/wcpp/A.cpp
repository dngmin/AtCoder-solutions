#include <iostream>

int main()
{
    int N; std::cin >> N;
    char hexadecimal[] = "0123456789ABCDEF";
    std::cout << hexadecimal[N/16] << hexadecimal[N%16];
    return 0;
}
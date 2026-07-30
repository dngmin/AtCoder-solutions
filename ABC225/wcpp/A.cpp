#include <iostream>

int main()
{
    char S1, S2, S3; std::cin >> S1 >> S2 >> S3;
    if ( S1 == S2 and S1 == S3) std::cout << 1;
    else if (S1 != S2 and S1 != S3 and S2 != S3) std::cout << 6;
    else std::cout << 3;
}
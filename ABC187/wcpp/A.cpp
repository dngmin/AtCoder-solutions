#include <iostream>

int main()
{
    char A[4], B[4]; std::cin >> A >> B;
    int a = int(A[0]) + int(A[1]) + int(A[2]) - 48*3;
    int b = int(B[0]) + int(B[1]) + int(B[2]) - 48*3;
    std::cout << (a < b? b : a);
    return 0;
}
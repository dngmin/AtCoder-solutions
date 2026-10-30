#include <iostream>

int main()
{
    int A, B, C; std::cin >> A >> B >> C;
    bool poor = false;
    if (A == B and A != C) poor = true;
    else if (A == C and A != B) poor = true;
    else if (B == C and A != B) poor = true;
    std::cout << (poor? "Yes" : "No");
    return 0;
}
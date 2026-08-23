#include <iostream>

int main()
{
    int A1, A2, A3; std::cin >> A1 >> A2 >> A3;
    bool a1 = (A2 + A3 - A1 - A1 == 0), a2 = (A1 + A3 - A2 - A2 == 0), a3 = (A1 + A2 - A3 - A3 == 0);
    std::cout << (a1 or a2 or a3? "Yes" : "No");
    return 0;
}
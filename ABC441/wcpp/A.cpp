#include <iostream>

int main()
{
    int P, Q, X, Y;
    std::cin >> P >> Q >> X >> Y;
    std::cout << ((P <= X & X < P+100 & Q <= Y & Y < Q+100)? "Yes" : "No");
    return 0;
}
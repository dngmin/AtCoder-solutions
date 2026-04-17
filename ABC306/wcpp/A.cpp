#include <iostream>
#include <string>

int main()
{
    int N;
    std::string S;
    std::cin >> N >> S;
    for (char s : S) std::cout << s << s;
    return 0;
}
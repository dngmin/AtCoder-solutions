#include <iostream>

int main()
{
    int A, B; std::cin >> A >> B;
    bool nine = true;
    if (A + B == 9);
    else if (A - B == 9);
    else if (A * B == 9);
    else if ((A / B == 9) and (A % B == 0));
    else nine =false;
    std::cout << (nine? "Nine" : "Nein");
    return 0;
}
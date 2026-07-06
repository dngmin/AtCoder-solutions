#include <iostream>

int main()
{
    int A, B, C, D, E, F, X, Aoki, Takahashi;
    std::cin >> A >> B >> C >> D >> E >> F >> X;
    Takahashi = ((X / (A + C)) * A + (X % (A + C) > A? A : X % (A + C))) * B;
    Aoki = ((X / (D + F)) * D + (X % (D + F) > D? D : X % (D + F))) * E;
    if (Aoki == Takahashi) std::cout << "Draw";
    else std::cout << (Aoki > Takahashi? "Aoki" : "Takahashi");
    return 0;
}
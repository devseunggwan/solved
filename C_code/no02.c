#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void)
{
    int num1, num2;
    int Bin[2] = {0, 1};
    char Zero[2] = "0";
    char One[2] = "1";
    int R[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int Q[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    char I[13] = "";
    char J[13] = "";
    char V[13] = "";
    char W[13] = "";
    char X[13] = "";
    char Y[13] = "";
    char Z[13] = "";

    printf("Enter the unsigned number: ");
    scanf("%d", &num1);

    printf("Enter the unsigned number: ");
    scanf("%d", &num2);

    // 2진수 나누기
    for (int i = 7; num1 != 0; i--)
    {
        R[i] = num1 % 2;
        num1 = num1 / 2;
    }

    for (int i = 7; num2 != 0; i--)
    {
        Q[i] = num2 % 2;
        num2 = num2 / 2;
    }

    for (int i = 0; i < 8; i++)
    {
        char str1[10], str2[10];
        sprintf(str1, "%d", R[i]);
        strcat(I, str1);

        sprintf(str2, "%d", Q[i]);
        strcat(J, str2);

        if (R[i] == Bin[0] && Q[i] == Bin[0])
        {
            strcat(V, Zero);
            strcat(W, Zero);
            strcat(X, Zero);
            strcat(Y, One);
            strcat(Z, One);
        }
        else if (R[i] == Bin[1] && Q[i] == Bin[1])
        {
            strcat(V, One);
            strcat(W, One);
            strcat(X, Zero);
            strcat(Y, Zero);
            strcat(Z, Zero);
        }
        else if (R[i] == Bin[1] && Q[i] == Bin[0])
        {
            strcat(V, Zero);
            strcat(W, One);
            strcat(X, One);
            strcat(Y, Zero);
            strcat(Z, One);
        }
        else
        {
            strcat(V, Zero);
            strcat(W, One);
            strcat(X, One);
            strcat(Y, One);
            strcat(Z, Zero);
        }
    }

    printf("%s & %s = %s \n", I, J, V);
    printf("%s | %s = %s \n", I, J, W);
    printf("%s ^ %s = %s \n", I, J, X);
    printf("~%s = %s \n", I, Y);
    printf("~%s = %s \n", J, Z);

    return 0;
}

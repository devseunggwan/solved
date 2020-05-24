#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>


int main(void){
    // initize variable
    char bin[5] = "";
    char exp[4] = "";
    char frac[3] = "";

    char zero2[3] = "00";
    char zero3[4] = "000";
    char zeroone[3] = "01";
    char onezero[3] = "10";
    char one3[4] = "111";
    char one2[3] = "11";
    char one[2] = "1";

    float E = 0;
    float M = 0;

    
    // input case
    printf("Enter the 5bit of binary number: ");
    scanf("%s", &bin);

    // slice
    strncpy(exp, bin+0, 3);
    strncpy(frac, bin+3, 2);
    
    // condition
    // exp == "111"
    if(strcmp(exp, one3) == 0){
        // frac == "00"
        if(strcmp(frac, zero2) == 0){
            printf("The floting point is infinite\n");
        }
        // frac != "00"
        else{
            printf("The floting point is NaN\n");
        }
    }
    // exp == "000"
    else if(strcmp(exp, zero3) == 0){
        // frac == "00"
        if(strcmp(frac, zero2) == 0){
            printf("The floting point is 0");

        }
        // frac != "00"
        else{
            // frac to dec
            int dec = 0;
            for(int i=1; i > -1; i--){
                char det[5];
                strncpy(det, frac+i, 1);
                if(atoi(det) == 1){
                    dec += pow(2, 1-i);
                }
            }

            M = 0.25 * dec;
            E = -2;
            float ans = M * pow(2, E);
            printf("The floting point is %0.3f\n", ans);
        }
    }
    // exp != "000" and exp != "111"
    else{
        int dec = 0;
        int expDec = 0;

        // frac to dec
        for(int i=1; i > -1; i--){
            char det[5];
            strncpy(det, frac+i, 1);
            if(atoi(det) == 1){
                dec += pow(2, (1-i));
            }
        }

        // exp to dec
        for(int i=2; i > -1; i--){
            char det[5];
            strncpy(det, exp+i, 1);
            if(atoi(det) == 1){
                expDec += pow(2, (2-i));
            }
        }

        M = 1 + (0.25 * dec);
        E = expDec - 3;
        float ans = M * pow(2, E);
        printf("The floting point is %0.3f\n", ans);

    }

}

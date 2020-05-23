#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define false 0
#define true 1

void MOV();
void ADD();
void PRT();
int regIndex(char *S);
void addRegTuple(char *reg, int value);

/**
 * 레지스터 값을 저장할 수 있는 구조체 선언
*/
static struct
{
    char strVal[21];
    int intVal;
} regTuple[15];

/**
 * 레지스터 값 추가 및 변경
*/
static int regNum = 0;
void addRegTuple(char *reg, int value)
{
    strcpy(regTuple[regNum].strVal, reg);
    regTuple[regNum++].intVal = value;
}

/**
 * 메모리 값을 저장하는 배열 선언 및 초기화
*/
int memory[100] = {
    0,
};

void main()
{
    // regisiter init
    addRegTuple("%rax", 0);
    addRegTuple("%rbx", 0);
    addRegTuple("%rcx", 0);
    addRegTuple("%rdx", 0);
    addRegTuple("%rsi", 0);
    addRegTuple("%rdi", 0);
    addRegTuple("%rbp", 0);
    addRegTuple("%r8", 0);
    addRegTuple("%r9", 0);
    addRegTuple("%r10", 0);
    addRegTuple("%r11", 0);
    addRegTuple("%r12", 0);
    addRegTuple("%r13", 0);
    addRegTuple("%r14", 0);
    addRegTuple("%r15", 0);


    // input
    while (true)
    {
        char func[10];
        scanf("%s", func);
        fgetc(stdin);

        // 첫번째 파라미터 함수에 따라서 나눈 분기점
        if (!strcmp(func, "MOV"))
        {
            MOV();
        }

        else if (!strcmp(func, "ADD"))
        {
            ADD();
        }

        else if (!strcmp(func, "PRT"))
        {
            PRT();
        }

        else
        {
            printf("I don't check function");
        }
    }
}

// src(arg1)의 데이터를 dst(arg2)로 이동
void MOV()
{
    printf("Function: MOV\n");
    char arg1[20], arg2[20];
    int num = 0;

    scanf("%s %s", arg1, arg2);

    // 첫번째 파라미터가 상수일 경우
    if (!strncmp(arg1, "$", 1))
    {   
        printf("First Parameter(Const): %s\n", arg1);

        // 두 번째 파라미터가 레지스터일 경우(상수, 레지스터) O
        if(!strncmp(arg2, "%", 1)) {
            printf("Second Parameter(Register): %s\n", arg2);

            // 레지스터 찾기
            int regIdx = regIndex(arg2);
        
            // 레지스터를 찾지 못한 경우
            if(regIdx == -1){
                printf("Error: Please Check the Register Name\n");
            }

            // 레지스터를 찾은 경우
            else {
                regTuple[regIdx].intVal = atoi(&arg1[1]);
                printf("Moved: %s -> %d\n", arg2, regTuple[regIdx].intVal);
            }
        }

        // 두 번째 파라미터가 메모리일 경우)(상수, 메모리)
        else {
            printf("Second Parameter(Memory): %s\n", arg2);
        }
    }

    // 첫번째 파라미터가 레지스터일 경우
    else if (!strncmp(arg1, "%", 1))
    {
        printf("First Parameter(Register): %s\n", arg1);

        // 두 번째 파라미터가 레지스터일 경우(레지스터, 레지스터) O
        if(!strncmp(arg2, "%", 1)) {
            printf("Second Parameter(Register): %s\n", arg2);

            // 레지스터 찾기
            int regIdx1 = regIndex(arg1);
            int regIdx2 = regIndex(arg2);
        
            // 레지스터를 찾지 못한 경우
            if(regIdx1 == -1 || regIdx2 == -1){
                printf("Error: Please Check the Register Name\n");
            }

            // 레지스터를 찾은 경우
            else {
                regTuple[regIdx2].intVal = regTuple[regIdx1].intVal;
                printf("Moved: %s -> %s\n", arg2, arg1);
            }

        }

        // 두 번째 파라미터가 메모리일 경우(레지스터, 메모리)
        else {
            printf("Second Parameter(Memory): %s\n", arg2);

            // 레지스터 찾기
            int regIdx = regIndex(arg1);
        
            // 레지스터를 찾지 못한 경우
            if(regIdx == -1){
                printf("Error: Please Check the Register Name\n");
            }

            // 레지스터를 찾은 경우
            else {
                // regTuple[regIdx].intVal = regTuple[regIdx].intVal;
                printf("Moved: %s -> %s\n", arg2, arg1);
            }
        }

    }
}

// 
void ADD()
{
    printf("Select: ADD\n");

    char arg1[20], arg2[20];
    scanf("%s %s", arg1, arg2);

    // 첫번째 파라미터가 상수일 경우
    if (!strncmp(arg1, "$", 1))
    {   
        printf("First Parameter(Const): %s\n", arg1);

        // 두 번째 파라미터가 레지스터일 경우(상수, 레지스터)
        if(!strncmp(arg2, "%", 1)) {
            printf("Second Parameter(Register): %s\n", arg2);

        }

        // 두 번째 파라미터가 메모리일 경우(상수, 메모리)
        else {
            printf("Second Parameter(Memory): %s\n", arg2);
        }

    }

    // 첫번째 파라미터가 레지스터일 경우
    else if (!strncmp(arg1, "%", 1))
    {
        printf("First Parameter(Register): %s\n", arg1);

        // 두 번째 파라미터가 레지스터일 경우(레지스터, 레지스터)
        if(!strncmp(arg2, "%", 1)) {
            printf("Second Parameter(Register): %s\n", arg2);

        }

        // 두 번째 파라미터가 메모리일 경우(레지스터, 레지스터)
        else {
            printf("Second Parameter(Memory): %s\n", arg2);
        }

    }

}

void PRT()
{
    printf("Select: PRT\n");

    char arg1[20];
    scanf("%s", arg1);

    // 두 번째 파라미터가 레지스터일 경우 
    if(!strncmp(arg1, "%", 1)) {
        printf("First Parameter(Register): %s\n", arg1);
        // 레지스터 찾기
        int regIdx = regIndex(arg1);
       
        // 레지스터를 찾지 못한 경우
        if(regIdx == -1){
            printf("Error: Please Check the Register Name\n");
        }

        // 레지스터를 찾은 경우
        else {
            // 레지스터 값 가져오기
            int regVal = regTuple[regIdx].intVal;
            // 레지스터 값 출력
            printf("%d\n", regVal);
        }
    }

    // 두 번째 파라미터가 메모리일 경우
    else {
        printf("First Parameter(Memory): %s\n", arg1);
    }
}

/**
 * 해당 레지스터(위치)를 찾아주는 함수
*/
int regIndex(char *S)
{
    int argLoc = 0;
    for (int i = 0; i < 15; i++)
    {
        if (!strcmp(regTuple[i].strVal, S))
        {
            return i;
        }
    }
    return -1;
}
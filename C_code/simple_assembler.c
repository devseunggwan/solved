#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define false 0
#define true 1
#define PERCENT "%"
#define DOLLOR "$"

void MOV();
void ADD();
void PRT();
int regIndex(char *S);
void addRegTuple(char *reg, int value);

static struct
{
    char strVal[21];
    int intVal;
} regTuple[15];

static int regNum = 0;
void addRegTuple(char *reg, int value)
{
    strcpy(regTuple[regNum].strVal, reg);
    regTuple[regNum++].intVal = value;
}

int memory[100] = {
    0,
};

void main()
{
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

    while (true)
    {
        char func[10];
        scanf("%s", func);
        fgetc(stdin);

        if (!strcmp(func, "MOV"))
        {
            MOV();
            fgetc(stdin);
        }

        else if (!strcmp(func, "ADD"))
        {
            ADD();
            fgetc(stdin);
        }

        else if (!strcmp(func, "PRT"))
        {
            PRT();
            fgetc(stdin);
        }

        else
        {
            printf("I don't check function");
        }
    }
}

void MOV()
{
    char *arg1 = malloc(sizeof(char));
    char *arg2 = malloc(sizeof(char));
    int num = 0;
    int reg1Index = 0;

    scanf("%s %s", arg1, arg2);

    if ((arg1[0] == DOLLOR))
    {
        num = atoi(&arg1[1]);
    }
    else if ((arg1[0] == PERCENT))
    {
        reg1Index = regIndex(arg1);
        printf("%d", reg1Index);
    }
}

void ADD()
{
    char arg1[20], arg2[20];
    scanf("%s %s", arg1, arg2);
}

void PRT()
{
    char arg1[20];
    scanf("%s", arg1);

    printf("%s\n", arg1);
}

int regIndex(char *S)
{
    int argLoc = 0;
    for (int i = 0; i < 15; i++)
    {
        if (regTuple[i].strVal == S)
        {
            return i;
        }
    }
}
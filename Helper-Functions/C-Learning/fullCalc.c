// Program thats a calculator with operation selection

#include <stdio.h>
#include <stdlib.h>

// all function prototypes

void doMath(int num1, int num2, char op);
void printResult(int result);

// Function take in user input
int main(){
    int num1, num2;
    char operation;
    num1 = 3;
    num2 = 5;
    operation = '-';

    printf("v6 \n ");
    // printf("Enter 1st number: \n");
    // scanf("%d", &num1); // lf to scan for double

    // printf("2nd num: \n");
    // scanf("%d", &num2);

    // printf("Operation + - : \n");
    // scanf(" %c", &operation);
    doMath(num1, num2, operation);
}

//Func do operation 

void doMath(int num1, int num2, char op){
    int result;

    if (op == '+'){
        result = num1 + num2;
    } else if (op == '-'){
        result = num1 - num2;
    } else {
        printf("Invalid Operation\n")
    }
    printf("41\n");
    printResult(result);
}

// Func print to user

void printResult(int result){
    printf("%d \n", result);

}
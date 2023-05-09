#include <stdlib.h>
#include <stdio.h>

int main(){
    // Pointer is a type of Data like int, double, char
    int age = 30;
    printf("%p  age mem address: \n", &age); // 0x16d25b1e8 age mem address: 

    int * pAge = &age;

    printf("%p\n", *&pAge); // %p for pointer data
    printf("%d\n", *pAge); // %d for pointer data


    return 0;
}
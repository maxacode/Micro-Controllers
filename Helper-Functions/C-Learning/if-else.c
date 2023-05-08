
#include <stdlib.h>
#include <stdio.h>


// wich num is greatest function
int max(int num1, int num2, int num3){
    int result;
    
    
    if (num1>num2 && num1 > num3) {
        result = num1;
    } else if (num2 > num1 && num2 > num3){
        result = num2;
    } else{
        result = num3;
    }

    return result;
}

int main(){
    printf("v1\n");
    // OR || instead of AND && 
    if (3 != 33 || 3 > 5){
        printf("True\n");
    } else {
        printf("faslse\n");
    }
    printf("%d\n", max(44, 33, 109));


}
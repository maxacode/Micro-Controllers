#include <stdlib.h>
#include <stdio.h>

int main(){
    int index = 1;

    while (index <=  5){
        printf("%d\n", index);
        if (index == 3){
            printf("THIS IS SPARTA\n");
            
        }
        index ++;

    }
// Do While loops

    do {

        printf("%d\n", index);
        index++;
    } while (index <= 10);

    return 0;

}


 
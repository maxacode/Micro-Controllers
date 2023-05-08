#include <stdlib.h>
#include <stdio.h>

//for loops 

int main(){


    // a simplified while loop in less lines
    int i;
    for (i=1; i <= 5; i++){
        printf("%d\n", i);
    }

    // Looping an array
    int nums[] = {9999, 3,4,5,23,3,3313};

    for (i = 0; i < 99; i++){
        printf("%d\n", nums[i]);

    // Why does this happen withthe aboce for loop when i < 99
            //     3313
            // 1
            // 40697856
            // 1
            // -1551761382
            // -98283327
            // 1836299360
            // 1
            // -1728233688
            // 1

    }
    return 0;
}
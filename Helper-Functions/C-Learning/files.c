// writing, creating, appending to files

#include <stdlib.h>
#include <stdio.h>

int main(){
    // FILE * fpointer = fopen("test1.txt", "a"); // a, w, r

    // fprintf(fpointer, "\nTst from C program"); // fprintf is writing to a file 
    // fclose(fpointer);// FILE is a data type poingting to a datatype * to a file on the HD of its MEM address fpointer is file name

    //Reading file 

    char line[255];
    FILE * fpointer = fopen("test1.txt", "r");

    fgets(line,255, fpointer);

    printf("%s\n", fpointer);


    return 0;
}
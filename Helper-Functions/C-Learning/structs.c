#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char name[50];
    char major[50];
    int age;
    double gpa;


};

int main(){
    struct Student student1;
    student1.age = 27;
    student1.gpa = 3.2;
    strcpy(student1.name, "Joe Dirt");
    strcpy(student1.major, "Com Sci");


    printf("%s", student1.name);



    return 0;
}
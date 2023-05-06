// Creator:  Maksim Derevencha
// Date:     2023-05-06
// Purpose:  Test file for C-Learning

#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Variables:
    const int FAV_NUM = 5; // constant variable
    int age = 40;
    double gpa = 3.7;
    char grade = 'A';
    char phrase[] = "Giraffe Academy"; // String
    // print all the above variables
    // printf("Age: %d\n", age);
    // printf("GPA: %f\n", gpa);
    // printf("Grade: %c\n", grade);
   // printf("Phrase: %s\n", phrase); //Phrase: Giraffe Academy
   // printf("test: \n %s \n %c \n %f \n %d\n", phrase, grade, gpa, age);
    // output: test:
    // Phrase: Giraffe Academy 
    // test: 
    //  Giraffe Academy 
    //  A 
    //  3.700000 
    //  40
    printf("My favorite %s is %d", "number", FAV_NUM);
      // output: My favorite number is 500
    // printf("Hello From Main"); // print to console without \n line
    // printf("Hello From Maks\n"); // print to console with \n line
    // output: Hello From MainHello From Maks

    
    return 0; // Return 0 if everything is ok or 1 if something went wrong
}
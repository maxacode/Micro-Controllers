// Creator:  Maksim Derevencha
// Date:     2023-05-06
// Purpose:  Test file for C-Learning

#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Variables:s
    // const int FAV_NUM = 5; // constant variable
    // //FAV_NUM = 500; // error: assignment of read-only variable ‘FAV_NUM’
    // int age = 40;
    // double gpa = 3.7;
    // char grade = 'A';
    // char phrase[] = "Giraffe Academy"; // String
    //grade = 'B'; // change variable value
    printf("%s\n", "test"); // output: Giraffe Academy
    //printf("%f\n", gpa); // output: Giraffe Academy
    
    // print all the above variables
    // printf("Age: %d\n", age); 40
    // printf("GPA: %f\n", gpa);3.7
    // printf("Grade: %c\n", grade); B
   // printf("Phrase: %s\n", phrase); //Phrase: Giraffe Academy
   // printf("test: \n %s \n %c \n %f \n %d\n", phrase, grade, gpa, age);
    // output: test:
    // Phrase: Giraffe Academy 
    // test: 
    //  Giraffe Academy 
    //  A 
    //  3.700000 
    //  40
    //printf("My favorite %s is %d", "number", FAV_NUM);
      // output: My favorite number is 500
    // printf("Hello From Main"); // print to console without \n line
    // printf("Hello From Maks\n"); // print to console with \n line
    // output: Hello From MainHello From Maks

    // Get chars,int, double from user
    // double ageTwo;
    // printf("Enter your age: ");
    // scanf("%lf", &ageTwo); // get input from user
    // printf("You are %f years old", ageTwo);

    // Get string from user
    // char name[20];
    // printf("Enter your name: ");
    // fgets(name, 20, stdin); // get input from user
    // printf("Your name is %s", name);

    // ram or memory address information
    int age = 30;
    double gpa = 3.4;
    char grade = 'A';

    printf("%p\n", &age); // output: 0x16b7671f8 (memory address) value will be different every time
    printf("%p\n", &gpa); // output: 0x16b7671f0 (memory address) value will be different every time
    return 0; // Return 0 if everything is ok or 1 if something went wrong
}
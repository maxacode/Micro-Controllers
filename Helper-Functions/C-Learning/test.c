// Creator:  Maksim Derevencha
// Date:     2023-05-06
// Purpose:  Test file for C-Learning

#include <stdio.h>
#include <stdlib.h>

// creating a function prototype to avoid error, instead of creating a function before main we can create a prototype, put it above main and then create the function below main, must include the function type and the name of the function and the parameters   
void testFunc(char phrase[], int joe);

// cubed function
int cubed(int num)
{ 
    int result = num * num * num;
    return result;
}
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
    //printf("%s\n", "test"); // output: Giraffe Academy
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

    // // ram or memoe ry address information
    // int age = 30;
    // double gpa = 3.4;
    // char grade = 'A';

    // printf("%p\n", *&age); // output: 0x16b7671f8 (memory address) value will be different every time
    // printf("%p\n", &gpa); // output: 0x16b7671f0 (memory address) value will be different every time
    //                 // test
    //                 // 30
    //                 // 0x16fdef1f0
    // return 0; // Return 0 if everything is ok or 1 if something went wrong


    // Calculator
    // catch error if user enters a char instead of a number
    // write code that catches the error and prints a message to the user
    //


    // double num1, num2;
    // printf("Enter first number: ");
    // scanf("%lf", &num1); // lf inztead of f for scanning a double from user
    // printf("SecondnUmber: ");
    // scanf("%lf", &num2);

    // printf("%f", num1 + num2);


    // // error catching this code

    // double num1, num2;
    // char op;
    // printf("Enter a number: ");
    // scanf("%lf", &num1); // lf inztead of f for scanning a double from user
    // printf("Enter operator: ");
    // scanf(" %c", &op); // lf inztead of f for scanning a double from user
    // printf("Enter second number: ");
    // scanf("%lf", &num2);
    // printf("%f", num1 + num2);
    


    // MadLib games
    // %s%s is taking in two strings with scanf - if you only give it one string it will not work
    // char color[20], personF[20], personL[20];
    // double num;
    // printf("Enter color: ");
    // scanf("%s", color);
    // printf("Num: ");
    // scanf("%lf", &num);
    // printf("person: ");
    // scanf("%s%s", personF, personL);

    // printf("Roses are %s\n There are this many %f\n i love %s %s", color, num, personF, personL);


    // Arrays
    // int luckyNumbers[] = {4, 8, 15, 16, 23, 42};
    //int  luckyNums[] = {4, 8, 1,4, 5,33, 993};
    //printf("%d", luckyNums);

    // int luckyNums[10];
    // luckyNums[1] = 80;
    // luckyNums[0] = 10;
    // printf("%d", luckyNums[0]);
    // printf("%d", luckyNums[1]);

    char phrase[20] = "Main Func\n";
    printf("%s", phrase);

    //call testFunction without generating error iso c99 do not support implicit function declaation
    // int age = 23;
    // testFunc("MAKS", age);



    return 0;

}

// void doesnt return anything

// void testFunc(char phrase[], int joe)
// {
//     printf("Hello From Test Func with %s,   %d ", phrase, joe);
//     //return 0;
// }



 
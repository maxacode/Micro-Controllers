#include <stdlib.h>
#include <stdio.h>


// Guessing game with limited attemts


int main(){

    int randNum, userGuess, triesLeft;
    
    randNum = 5;
    triesLeft = 3;

   

    while(triesLeft > 0){
        printf("Enter a number as a guess: \n");
        scanf("%d", &userGuess);
        if (randNum == userGuess){
            printf("Correct\n");
            break;
        } else {
            printf("Sorry try again\n");
            triesLeft --;
        }
    
    }
        
    if (triesLeft ==0){
            printf("Game OVer");

    }
    

}
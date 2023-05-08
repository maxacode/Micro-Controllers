# include <stdio.h>
# include <stdlib.h>

// prototype signature of cubed function
int cubed ( int numUser);


int main(){
    int userInput, answer;

    printf("v1.1Enter any number to be cubed: ");
    scanf("%d", &userInput );

    answer = cubed(userInput);

    printf("%d", answer);
}

// Cubed function

int cubed (int numUser){
    return numUser * numUser * numUser;
}

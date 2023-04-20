#include <stdio.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

int main(){
/*Use this for loop structure whenever you don't know 
or don't want to know how many times you want to loop*/
int x, iNumQuestions, iResponse, iRandNum1, iRandNum2;
srand(time(NULL));

printf("\nEnter number of questions to ask:    ");
scanf("%d", &iNumQuestions);

for(x=0; x < iNumQuestions; x++){
iRandNum1 = (rand() % 10);
iRandNum2 = (rand() % 10) + 1;
printf("\nWhat is %d times %d?", iRandNum1, iRandNum2);
scanf("\t%d", &iResponse);
if (iResponse == iRandNum1 * iRandNum2)
    printf("\nCorrect!\n");
else
    printf("\nThe correct answer was %d \n", iRandNum1 * iRandNum2);
}  

system("pause");
return 0;
}

	/*DAY2*/

/*PT1*/
#include <stdio.h>
#define FN "input.txt"

char conversion(char);
int game(char, char);
int point_score(int, char);


int main(){
    FILE *fl;
    char opponent, me;
    int last = 0;
    int total_score = 0;
    int game_score;

    fl = fopen(FN, "r");

    if(fl){                                     //don't use empty files!
        while(!feof(fl)){
            fscanf(fl, "%c %c ", &opponent, &me);
            me = conversion(me);
            game_score = game(opponent, me);
            total_score += game_score;
        }   
    }

    printf("total score: %d\n", total_score);
    return 0;
}


char conversion(char a){
    a = a-'X'+'A';
    return a;
}


int game(char a, char b){
    int points;
    if((b==(a-2)) || (b==(a+1))){   //win
        points = point_score(1, b);
        printf("win!, score: %d\n", points);
    }
    else if(a==b){                  //draw
        points = point_score(2, b);
        printf("draw!, score: %d\n", points);
    }
    else{                           //lose
        points = point_score(3, b);
        printf("lose!, score: %d\n", points);
    }
    return points;
}


int point_score(int status, char choice){
    int score;
    score = 0;
    switch(choice){
        case 'A':
            score+=1;
            break;
        case 'B':
            score+=2;
            break;
        case 'C':
            score+=3;
            break;
        default:
            break;
    }

    switch(status){
        case 1:
            score+=6;
            break;
        case 2:
            score+=3;
            break;
        default:
            break;
    }
    return score;
}

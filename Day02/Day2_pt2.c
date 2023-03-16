	/*DAY2*/

/*PT2*/
#include <stdio.h>
#define FN "input.txt"

char conversion(char);
int game(char, char);
int point_score(char, char);


int main(){
    FILE *fl;
    char opponent, endgame;
    int last = 0;
    int total_score = 0;
    int game_score;

    fl = fopen(FN, "r");

    if(fl){                                     //don't use empty files!
        while(!feof(fl)){
            fscanf(fl, "%c %c ", &opponent, &endgame);
            game_score = game(opponent, endgame);
            total_score += game_score;
        }   
    }
    
    printf("total score: %d\n", total_score);
    return 0;
}


int game(char a, char b){ //a = opponent, b = endgame
    int points;
    char choice;
    switch(b){
        case 'Z':
            if(a=='C')
                choice = a-2;
            else
                choice = a+1;
            break;
        case 'Y':
            choice = a;
            break;
        case 'X':
            if(a=='A')
                choice = a+2;
            else
                choice = a-1;
            break;
    }
    points = point_score(b, choice);
    printf("choice: %c, endgame: %c, opp: %c\n", choice, b, a);
    return points;
}


int point_score(char status, char choice){
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
        case 'Z':
            score+=6;
            break;
        case 'Y':
            score+=3;
            break;
        default:
            break;
    }
    return score;
}
	/*DAY8*/

/*PT1*/
#include <stdio.h>
#define FN "input.txt"
#define DIM 99
#define BORDER DIM*2+(DIM-2)*2


void input(int[DIM][DIM]);
void print_matrix(int[DIM][DIM]);
int char_to_int(char);
int solve(int[DIM][DIM]);
int check_right(int, int, int[DIM][DIM]);
int check_left(int, int, int[DIM][DIM]);
int check_up(int, int, int[DIM][DIM]);
int check_down(int, int, int[DIM][DIM]);


int main(){
    int sol, matrix[DIM][DIM],i,j;
    input(matrix);
    sol = solve(matrix);
    sol += BORDER;
    print_matrix(matrix);
    printf("solution: %d \n", sol);  
    return 0;
}


void input(int matrix[DIM][DIM]){
    FILE *fl;
    char line[DIM+1];
    int i,j;

    fl = fopen(FN, "r");

    if(fl){                                 //don't use empty files!
        i = 0;                            
        while(!feof(fl)){
            fscanf(fl, "%s", line);
            for(j=0; j<DIM; j++){
                matrix[i][j]= char_to_int(line[j]);
            }
            i++;
        }
    fclose(fl);
    }else{
        printf("ERROR\n");
    }
}


void print_matrix(int matrix[DIM][DIM]){
    int i, j;
    for(i = 0; i<DIM; i++){
        for(j = 0; j<DIM; j++){
            printf("%d", matrix[i][j]);
        }
        printf("\n");
    } 
}


int char_to_int(char c){
    int value;
    value = (int)c - '0';
    return value;
}


int solve(int matrix[DIM][DIM]){
    int num_vis, i, j;
    for(i = 1, num_vis = 0; i < DIM-1; i++){
        for(j = 1; j < DIM-1; j++){
            if(check_right(i, j, matrix)||check_left(i, j, matrix)||
                check_up(i, j, matrix)||check_down(i, j, matrix)){
                num_vis++;
            }
        }
    }
    return num_vis;
}


int check_right(int i, int j, int matrix[DIM][DIM]){
    int k, valmax, val;
    for(k = j+1, val = 0, valmax = DIM-k; k < DIM; k++){
        if(matrix[i][k]<matrix[i][j]){
            val++;
        }
    }
    return(val==valmax);
} 


int check_left(int i, int j, int matrix[DIM][DIM]){
    int k, valmax, val;
    for(k = j-1, val = 0, valmax = k+1; k >= 0; k--){
        if(matrix[i][k]<matrix[i][j]){
            val++;
        }
    }
    return(val==valmax);
}


int check_up(int i, int j, int matrix[DIM][DIM]){
    int k, valmax, val;
    for(k = i-1, val = 0, valmax = k+1; k >= 0; k--){
        if(matrix[k][j]<matrix[i][j]){
            val++;
        }
    }
    return(val==valmax);
} 


int check_down(int i, int j, int matrix[DIM][DIM]){
    int k, valmax, val;
    for(k = i+1, val = 0, valmax = DIM-k; k < DIM; k++){
        if(matrix[k][j]<matrix[i][j]){
            val++;
        }
    }
    return(val==valmax);
} 
/*
Creed Jones

Summary:
Take in a picture and edit the picture
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Image_Editor.c"

void main() {
    int* picture = importColors();
    int run = 1;
    do {
        int choice;
        printf("\n\nHere are your choices:\n[0] exit\n[1] convert to greyscale\n[2] flip horizontally\n[3] negative of red\n[4] negative of green\n[5] negative of blue\n[6] remove red\n[7] remove green\n[8] remove blue\n[9] extreme contrast\n[10] add random noise\n\nEnter choice: ");
        scanf("%i", &choice);
        switch(choice) {
            case 0:
                run = 0; 
                exitProgram(picture);
                break;
            case 3:
                picture = negate_red(picture);
                break;
            case 4:
                picture = negate_green(picture);
                break;
            case 5:
                picture = negate_blue(picture);
                break;
            case 2:
                picture = flip_horizontal(picture);
                break;
            case 1:
                picture = grey_scale(picture);
                break;
            case 6:
                picture = flatten_red(picture);
                break;
            case 7:
                picture = flatten_green(picture);
                break;
            case 8:
                picture = flatten_blue(picture);
                break;
            case 9:
                picture = extreme_contrast(picture);
                break;
            case 10:
                picture = random_noise(picture);
                break;
            default:
                printf("Invalid input\n");
        } 
    } while(run == 1);
} 
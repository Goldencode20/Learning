//Functions in Image_Editor file

int* importColors(void);
//Get a user input then get the file and put the colors of wach pixel into a 1D array and return the array
//The first two spots are for the size then it Red Green Blue repeating for each pixel

int* negate_red(int colors[]);
//Take the array and flip the red in each pixel then return the array

int* negate_green(int colors[]);
//Take the array and flip the green in each pixel then return the array

int* negate_blue(int colors[]);
//Take the array and flip the blue in each pixel then return the array

int* flip_horizontal(int colors[]);
//Take in the array flip each row and return the array

int* grey_scale(int colors[]);
//Take in the array and take the average of the three pixels then set them to that value and return array

int* flatten_red(int colors[]);
//Take in the array and make the red value 0 and return the array

int* flatten_green(int colors[]);
//Take in the array and make the green value 0 and return the array

int* flatten_blue(int colors[]);
//Take in the array and make the blue value 0 and return the array

int* random_noise(int colors[]);
//Take in the array then add/remove a random amount of color to each pixel requested by the user then return the array

int* extreme_contrast(int colors[]);
//Set each color value to 0 or 255 whichever it is closest too then return the array

void exitProgram(int colors[]);
//Take in the array get user input for the name of the file to save it to then save to that file and close the file. 
#include <iostream>
#include <vector>
#include "matrix.h"

int main () {
    
    // assign a 7x5 matrix to the variable initial_grid
    // all values in the matrix are 0.4
	std::vector <std:: vector <float> > 
	    initial_grid (7, std::vector <float>(5, 0.4));

    Matrix matrixa(initial_grid);
    matrixa.matrix_print();
    std::cout << matrixa.getRows() << std::endl;
    std::cout << matrixa.getCols() << std::endl;
    
    Matrix transposea(matrixa.matrix_transpose());
    transposea.matrix_print();
    
    // Now you will use another 7x5 matrix called matrixb to 
    // give the results of the matrix_addition function
    
    // 7x5 2-dimensional vector with values 0.2
	std::vector <std:: vector <float> > 
	    second_grid (7, std::vector <float>(5, 0.2));
	    
    Matrix matrixb(second_grid);
    matrixb.matrix_print();
    Matrix matrixsum(matrixa.matrix_addition(matrixb));
    matrixsum.matrix_print();
    
    // TODO: Instantiate an object called matrixb. Use the second_grid
    // variable as the input to initialize matrixb
    
    // TOOD: Add matrixa and matrixb. Store the results in a new matrix
    // variable called matrixsum
    
    // TODO: Print out the matrix contained in the matrixsum variable

    return 0;
}
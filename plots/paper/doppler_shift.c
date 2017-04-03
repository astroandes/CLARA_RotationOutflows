#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

  //Number of lines in file
  static const int num_xs = 11169;

  //The info with v_rot = 0
  FILE * file;
  file = fopen("vrot0_vout25.dat" , "r");

  //Pointer to save xs
  double *xs;
  xs = malloc(num_xs*sizeof(double));

  if (file) {
    int i = 0;
    while (fscanf(file, "%lf", &xs[i]) != EOF) {
      i++;
    }
    fclose(file);
  }

  printf("%f\n", xs[0]);

  return 0;
}

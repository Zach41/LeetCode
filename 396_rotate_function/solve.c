#include <stdio.h>
#include <limits.h>

int maxRotateFunction(int *A, int ASize) {
    int vec_sum = 0;
    for (int i=0; i<ASize; i++)
	vec_sum += A[i];

    int last_sum = 0;
    for (int i=0; i<ASize; i++)
	last_sum += A[i] * i;
    
    int max = last_sum;
    for (int i=1; i<ASize; i++) {
	last_sum = last_sum + vec_sum - ASize * A[ASize - i];
	if (last_sum > max)
	    max = last_sum;
    }
    return max;
}

int main(void) {
    int A[4], size;
    while (scanf("%d", &size) != EOF) {
	for (int i=0; i<size; i++)
	    scanf("%d", A+i);

	printf("result : %d\n", maxRotateFunction(A, size));
    }
    return 0;
}

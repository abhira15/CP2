#include <stdio.h>

int sqrt(int number){
    float temp, sqrt;
    sqrt = number / 2;
    temp = 0;
    while(sqrt != temp){
        temp = sqrt;
        sqrt = ( number/temp + temp) / 2;
    }
    return sqrt;
}


int main() {
    int n, i, j;
    while(scanf("%d", &n) == 1) {
        int f[50] = {}, tmp;
        f[0] = 1;
        for(i = 2; ; i++) {
            for(j = 0; j < n; j++) {
                tmp = f[j]+i;
                tmp = (int)sqrt(tmp);
                if(tmp*tmp == f[j]+i || f[j] == 0) {
                    f[j] = i;
                    break;
                }
            }
            if(j == n)  break;
        }
        printf("%d\n", i-1);
    }
    return 0;
}

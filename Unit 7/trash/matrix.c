#include<stdio.h>

int change(int input)
{
    if(input == 0)
    {

        input = 1;
        return  input;

    }
    else
    {
        input = 0;

        return  input;
    }
}

int main()
{
while(1){
    int n;
    scanf("%d",&n);
    int arr[100];
    int mat[100][100];
    int input = 0;

    printf("\t");
    for(int i=1; i<=n; i++)
    {
        arr[i]=i;

        printf("%d\t",arr[i]);

    }
    printf("\n\n");


    for(int i = 1 ; i<=n ; i++ )
    {
        for(int j = 1 ; j<=n ; j++)
        {

            if( j%arr[i] == 0 )
            {

            mat[i][j]=change(mat[i-1][j]);

            }
            else
            {
                mat[i][j]=mat[i-1][j];

            }

        }

    }

    for(int i = 1 ; i<=n ; i++ )
    {
        printf("%d \t",i);
        for(int j = 1 ; j<=n ; j++)
        {

            printf("%d\t", mat[i][j]);

        }
        printf("\n");
    }
}
}

#include <stdio.h>

int		g_count;

int		ft_abs(int nb)
{
	if (nb < 0)
		return (-nb);
	return (nb);
}

int		check_Queen(int *matrix, int c)
{
	int i;
	
	i = 0;
	while (i < c)
	{
		if (matrix[i] == matrix[c])
			return (0);
		if (ft_abs(matrix[i] - matrix[c]) == ft_abs(i - c))
			return (0);
		i++;
	}
	return (1);
}

void	ft_N_Queen(int *matrix, int num, int c)
{
	int r;
	
	if (c == num)
		g_count++;
	else
	{
		r = 0;
		while (r < num)
		{
			matrix[c] = r;
			if (check_Queen(matrix, c))
				ft_N_Queen(matrix, num, c + 1);
			r++;
		}
	}
}

int		main()
{
	int input;
	int num;
	int col;
	int count;
	
	count = 1;
	scanf("%d", &input);
	while (input)
	{
		col = 0;
		scanf("%d", &num);
		g_count = 0;
		int matrix[num] = {0};
		ft_N_Queen(matrix ,num, col);
		printf("#%d %d\n", count, g_count);
		input--;
		count++;
	}
	return (0);
}

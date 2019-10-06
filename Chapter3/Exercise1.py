'''
Exercise 1
The find_coor_x_y() function we wrote earlier to find the correlation 
coefficient between two sets of numbers assumes that the two sets of numbers 
the same length. Improve the function so that it first checks the length of the
lists. If they're equal, only then should the function proceed with the 
remaining calculations; otherwise, it should print an error message that the
correlation can't be found.
'''

def find_corr_x_y(x,y):
    if len(x) == len(y):
        n = len(x)
    
        prod = [xi * yi for xi in x for yi in y]
    
        sum_prod_x_y = sum(prod) 
        sum_x = sum(x)
        sum_y = sum(y)
        
        squared_sum_x = sum_x**2
        squared_sum_y = sum_y**2
        
        x_square = [xi**2 for xi in x]
        y_square = [yi**2 for yi in y]
        
        x_square_sum = sum(x_square)
        y_square_sum = sum(y_square)
    
        numerator = n*sum_prod_x_y - sum_x*sum_y
        denominator_term1 = n*x_square_sum - squared_sum_x
        denominator_term2 = n*y_square_sum - squared_sum_y
    
        denominator = (denominator_term1*denominator_term2)**0.5

        return numerator/denominator
    else:
        return '''correlation can't be found'''

    
x = [11, 23, 45, 24, 50, 11]
y = [33, 56, 70, 35, 12, 30]


print(find_corr_x_y(x,y))
    

''' Papa Yaw Owusu Nti
    CS 152 B
    this program develops and tests statistical functions for mean,median,max,min,variance,standard deviation
'''

def sum(numbers):
    '''  Calculates the sum of a list of numbers. Accepts one parameter (numbers) and returns its sum as a float '''
# Create a variable to hold the sum
# Initialize the variable to 0.0 (explicitly make it a floating point number).
    sum_numbers = 0.0
# Define a for loop to iterate over the list passed in as the function parameter. 
    for x in numbers:
        # On each iteration, add the current number to the variable holding the sum. 
        sum_numbers+= x
    return sum_numbers

        # Once the loop completes, return the sum.
    
    
def test():
    '''tests the sum function'''
    list1 = [1,2,3,4]
    list2 = sum(list1)
   # print(list2)
    
    
    
# mean(data) - computes the mean of the list of data.
def mean(data):
    '''  Calculates the mean of a list of data. Accepts one parameter (data) and returns its average as a float '''
    mean= sum(data)/len(data)
    return mean
        

def min(data):

    min_of_data = 10000

    for x in data:
        if x <  min_of_data:
             min_of_data = x
    return min_of_data

    
def max(data):

    max_of_data = -200.0

    for y in data:
        if y >  max_of_data:
             max_of_data = y
    return max_of_data


# variance(data) - 
def variance(data):
    '''this function computes the variance of the list of data.'''
    ##Compute the mean of nums 
    mean= sum(data)/len(data)

    #Make a new empty list: squared_nums_minus_means
    squared_data_minus_means = []
    
    #Loop over the values in nums
    for x in data:
        #For each value, append the square of ( the value minus the mean of nums ) to squared_nums_minus_means
        squared_data_minus_means.append((x-mean)**2)
        #Compute the sum of squared_nums_minus_means and divide it by the size of nums minus 1
        var = sum(squared_data_minus_means)/ (len(data)-1)
        #Return the value you just computed   
    return var


def standard_dev (data):
    '''This function computes the standard deviation for a piece of data.
    It first computes the variance of the data and finds the squareroot of this variance. It returns the value as a float'''
    #find variance of data
    var_data = variance(data)
    
    #since standard deviation is the square root of variance. Also square root = a number to the power half
    st_dev_data = var_data ** 0.5
    return st_dev_data	

def median(data):
    '''Calculates the median of a list of data. Accepts one parameter (data) and returns its median as a float'''
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # If the number of elements is even, average the two middle values.
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median_value = (mid1 + mid2) / 2
    else:
        # If the number of elements is odd, return the middle value.
        median_value = sorted_data[n // 2]
    
    return median_value

#Testing the functions defined to make sure they are working properly
def test():
    sample_data= [1,2,3,4,5]
    sample_mean= mean(sample_data)
    sample_min = min(sample_data)
    sample_max= max(sample_data)
    sample_variance= variance(sample_data)
    sample_stdev = standard_dev(sample_data)
    sample_median = median(sample_data)


    print(sample_mean)
    print(sample_min)
    print(sample_max)
    print(sample_variance)
    print(sample_stdev)
    print(sample_median)

if __name__ == "__main__":
    test()


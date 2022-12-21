import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

def calc_chart():
# calcuating the results and plotting the data

    # calculate the stats
    random_list = random.sample(range(1, 101), 50)

    sorted_list = np.sort(random_list)

    mean = round(np.mean(sorted_list), 1)

    median = np.median(sorted_list)

    std = round(np.std(sorted_list), 1)

    min = float(np.amin(sorted_list))

    max = float(np.amax(sorted_list))


    # scatter plot setup    
    x_axis = [x for x in range(1, len(random_list)+1)]

    plt.subplots_adjust(bottom=0.33)
    
    string = 'The min is: ' + str(min) + '\nThe max is: ' + str(max) + '\nThe mean is: ' + str(mean) + '\nThe median is: ' + str(median) + '\nThe standard deviation is: ' + str(std)
    
    text = plt.text(25, -42, string, ha='center', va='center', size=10)
    
    text.set_path_effects([path_effects.Normal()])
    
    plt.scatter(x_axis, random_list)
    
    plt.ylabel('Random Number Value')

    plt.xlabel('Position in Array')

    plt.title('Scatter Plot of the Random Numbers')

    plt.show(block=False)
    
    plt.waitforbuttonpress(0)
    


if __name__ == "__main__":
    
    calc_chart()


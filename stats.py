# PART 2

import os
import json

def main():

     # Get into the correct directory
    os.chdir(os.path.dirname(__file__))

    # Read in the file
    f = open('foods.json', 'r')
    data = json.load(f)
    f.close()
    
    print('FOOD SUMMARY STATS:\n')

    # Get stats
    low_fat_ct = 0
    high_fiber_ct = 0
    low_gi_ct = 0
    iconic_foods = []

    # Iterate through data to get counts
    for datum in data:

        iconic_food = True
        # Check if low fat
        if (datum['low fat'] == 'yes'):
            low_fat_ct += 1
        else:
            iconic_food = False
        
        # Check if high fiber
        if (datum['high fiber'] == 'yes'):
            high_fiber_ct += 1
        else:
            iconic_food = False
        
        # Check if low GI
        if (datum['low glycemic index'] == 'yes'):
            low_gi_ct += 1
        else:
            iconic_food = False
        
        # See if has all three
        if (iconic_food):
            iconic_foods.append(datum['Foods'])
    
    # Print counts and percentages
    total = len(data)
    print(f'  Count of Low-Fat Foods: {low_fat_ct} ({str(low_fat_ct/total*100)[0:5]}%)')
    print(f'  Count of High-Fiber Foods: {high_fiber_ct} ({str(high_fiber_ct/total*100)[0:5]}%)')
    print(f'  Count of Low-GI Foods: {low_gi_ct} ({str(low_gi_ct/total*100)[0:5]}%)')

    # Get iconic foods
    print(f'These are the food icons, that have low fat, high fiber, and low GI: {iconic_foods}')

main()
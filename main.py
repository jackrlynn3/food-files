import os

# load_in_files: read in files and remove all empty lines
#   file_name: (str) location of the file of interest
#   return: (list(str)) list of strings with file contents
def load_in_files(file_name, all_lower=False, capitalized=False):

    # Get into the correct directory
    os.chdir(os.path.dirname(__file__))

    # Open the file
    f = open(file_name, 'r')

    # Read and clean all of the lines
    lines = []
    for line in f.readlines():
        line = line.strip()
        if (line != '' and line != None):
            if (all_lower):
                lines.append(line.lower())
            elif (capitalized):
                lines.append(line.title())
            else:
                lines.append(line)
    
    # Return the lines
    return lines

def clean_data(data, acceptable_responses, default=None):
    
    clean_data = []
    for datum in data:
        if (datum in acceptable_responses):
            clean_data.append(datum)
        else:
            clean_data.append(default)
    
    return clean_data

# clean_numbers: remove random error numbers in strings
#   data: (list(str)) string data to have numbers removed
#   return: (list(str)) cleaned data
def clean_numbers(data):
    
    # Iterate through each datum and remove unncessary numbers
    clean_data = []
    for datum in data:
        curr_str = ""
        for i in range(len(datum)):
            if (datum[i].isalpha() or datum[i] == '\'' or datum[i] == ' '):
                curr_str += datum[i]
        clean_data.append(curr_str)
    
    # Return data
    return clean_data

def remove_duplicates(dedup_data, *comp_data):

    rem_ind = []
    used_values = []
    for i in range(len(dedup_data)):
        if (dedup_data[i] in used_values):
            rem_ind.append(i)
        else:
            used_values.append(dedup_data[i])
    
    rem_ind.reverse()
    for i in rem_ind:
        dedup_data.pop(i)
        for j in range(len(comp_data)):
            comp_data[j].pop(i)

    return dedup_data, *comp_data

def main():

    # Load in all of the files
    foods = load_in_files('data/foods.txt', capitalized=True)
    high_fiber = load_in_files('data/highfiber.txt', all_lower=True)
    low_gi = load_in_files('data/low-glycemic-index.txt', all_lower=True)
    low_fat = load_in_files('data/lowfat.txt', all_lower=True)

    # Clean out all numbers from
    foods = clean_numbers(foods)
    high_fiber = clean_numbers(high_fiber)
    low_gi = clean_numbers(low_gi)
    low_fat = clean_numbers(low_fat)

    # Clean each datasets to have only acceptable answers
    high_fiber = clean_data(high_fiber, ['high fiber', 'yes', 'no'])
    low_gi = clean_data(low_gi, ['low glycemic index', 'yes', 'no'])
    low_fat = clean_data(low_fat, ['low fat', 'yes', 'no'])

    # Remove Duplicates
    foods, high_fiber, low_gi, low_fat = remove_duplicates(foods, high_fiber, low_gi, low_fat)

    print(len(foods))
    print(len(high_fiber))
    print(len(low_gi))
    print(len(low_fat))

main()
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

def main():

    # Load in all of the files
    foods = load_in_files('data/foods.txt', capitalized=True)
    high_fiber = load_in_files('data/highfiber.txt', all_lower=True)
    low_gi = load_in_files('data/low-glycemic-index.txt', all_lower=True)
    low_fat = load_in_files('data/lowfat.txt', all_lower=True)

    print(foods)
    print(high_fiber)
    print(low_gi)
    print(low_fat)

main()
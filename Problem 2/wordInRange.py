def wordInRange():
    #Type your code here
    file_name = input().strip()
    lower_bound = input().strip()
    upper_bound = input().strip()

    with open(file_name, 'r') as file:
        words = file.readlines()
    
    for word in words:
        current_word = word.strip()
        if lower_bound <= current_word <= upper_bound:
            print(f'{current_word} - in range')
        else:
            print(f'{current_word} - not in range')
    return
if __name__ == '__main__':
    wordInRange()
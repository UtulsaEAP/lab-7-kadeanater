def compute_letter_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average <= 90:
        return 'B'
    elif 70 <= average <= 80:
        return 'C'
    elif 60 <= average <= 70:
        return 'D'
    else:
        return 'F'
    
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    total_students = 0
    total_midterm1 = 0
    total_midterm2 = 0
    total_final = 0
      
    # TODO: Read a file name from the user and read the tsv file here. 
file_name = input()

with open(file_name, 'r') as file:
    lines = file.readlines()
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    with open('report.txt' , 'w') as report_file:
        for line in lines:
            parts = line.strip().split('\t')
            last_name, first_name, midterm1, midterm2, final = parts
            midterm1, midterm2, final = int(midterm1), int(midterm2), int(final)
            
            average_score = (midterm1 + midterm2 + final) / 3
            
            letter_grade = compute_letter_grade(average_score)
            
            report_file.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n')
           
            total_students += 1
            total_midterm1 += midterm1
            total_midterm2 += midterm2
            total_final += final
    avg_midterm1 = total_midterm1 / total_students
    avg_midterm2 = total_midterm2 / total_students
    avg_final = total_final / total_students

    with open('report.txt' , 'a') as report_file:
        report_file.write(f'\nAverages: midterm 1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}')

if __name__ == "__main__":
    courseGrade()
    
    
import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    students = read_dict("students.csv", I_NUMBER_INDEX)
    
    user_input = input("Please enter an I-Number (xxxxxxxxx): ")
    
    user_input = user_input.replace("-", "")
    #print(user_input)
    good_i_number = test_valid_number(user_input)
    if good_i_number == True:
        look_in_dictionary(students, user_input)

def read_dict(filename, I_NUMBER_INDEX):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        
        reader = csv.reader(csv_file)
        
        next(reader)
        
        for row in reader:
        
            key = row[I_NUMBER_INDEX]
        
            dictionary[key] = row
    
    return dictionary

def look_in_dictionary(dictionary, i_number):

    if i_number in dictionary:
        student_name_id = dictionary[i_number]
        student_name = student_name_id[1]
        print(student_name)
    else:
        print("No such student")

class FormulaError(ValueError):
    pass

def test_valid_number(i_number):
    good_i_number = True
    for i in i_number:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            pass
        else:
            good_i_number = False
    if good_i_number == True:
        if len(i_number) < 9:
            print("Invalid I-Number: too few digits")
            good_i_number = False
        elif len(i_number) > 9:
            print("Invalid I-Number: too many digits")
            good_i_number = False
    else:
        print("Invalid I-Number")
    return good_i_number
    
if __name__ == "__main__":
    main()
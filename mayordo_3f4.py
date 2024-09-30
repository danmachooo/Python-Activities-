#python 3.7.1

def problem_one():
  students = {'John', 'Maria', 'David', 'Samantha'} 
  
  while True:
    try:
      index = int(input('Enter index: '))
      
      current_index = 0
      student = None
      
      for stud in students:
        if current_index == index:
          student = stud
          break
        current_index += 1
      
      if student is not None:
        print(f'Student at index {index} is {student}.')
      else:
        raise IndexError('Enter only between -4 and 3')
      break
    except ValueError:
      print('Enter only integer numbers\n')
    except IndexError as ie:
      print(f'Error: {ie}\n')

def problem_two():
  numbers = (1, 4, 7, 10, 13, 16)
  sum_of_even = 0
  
  for x in numbers:
    if x % 2 == 0:
      sum_of_even += x
  
  average = sum_of_even / len(numbers)
  print(f'The average of even numbers in the tuple is {average:.2f}')

def problem_three():
  people = {'users':
            {
             'John': 19,
             'Emily': 21,
             'Sarah': 25,
             'Tom': 18
            }
           }
  print('User/s that is older than 19\n')
  for _, inner in people.items():
    for user, age in inner.items():
      if age > 19:
        print(f'Name: {user}')


def problem_four():
  numbers = (1, 3, 2, 4, 3, 1, 2, 5, 10)
    
  for i in range(len(numbers)):
    count = 0
    is_counted = False
    
    for k in range(i):
      if numbers[k] == numbers[i]:
        is_counted = True
        break
        
    if not is_counted:
      for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
          count += 1
      if count > 1:
           print(f'{numbers[i]} appeared in the tuple {count} times')

def problem_five():
  student_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]
  lowest_score = student_scores[0]
  
  for student, score in student_scores:
    if score < lowest_score[1]:
      lowest_score = (student, score)
  print(f'Student with a lowest score is {lowest_score[0]} with a score of {lowest_score[1]}')
      
 
def divider():
  print("=" * 50)
  print()
  
def main():
  print("Select a problem to solve (1-5):")
  print("1: Problem One")
  print("2: Problem Two")
  print("3: Problem Three")
  print("4: Problem Four")
  print("5: Problem Five")
  print()

  while True:
    try:
      choice = int(input("Enter your choice: "))
      if choice < 1 or choice > 5:
        raise ValueError("Choice must be between 1 and 5.")
        divider()
        break
      else:
        divider()
        break
    except ValueError as ve:
      print(f"Invalid input: {ve}. Please enter an integer between 1 and 5.")
      divider()
    """
    match choice:
      case 1:
        problem_one()
      case 2:
        problem_two()
      case 3:
        problem_three()
      case 4:
        problem_four()
      case 5:
        problem_five()
    """
        
        
  if choice == 1:
    divider()
    problem_one()
  elif choice == 2:
    divider()
    problem_two()
  elif choice == 3:
    divider()
    problem_three()
  elif choice == 4:
    divider()
    problem_four()
  elif choice == 5:
    divider()
    problem_five()
    
if __name__ == "__main__":
    main()        
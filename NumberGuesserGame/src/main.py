import random
rand_num = random.randint(1 , 100)
rand_num


def Validation_Inpute(input_num):
      if input_num == 'E':
         print('Thank You For Playing')
         return False
   
      elif not input_num.isdigit():
         print('Please Enter Valide Value')
         return False


      input_num = int(input_num)
      if input_num > 100 or input_num < 1 :
         print('Your Number Is Not Between 1 to 100')
         return False
      
      return True

def main():
    Score = 70
    while True:
        input_num =  input('Enter Your Guess Number Between 1 to 100 \n (Press E To EXIT) :')
       
        Score -= 10
        Score = max(Score , 0)

        if not Validation_Inpute(input_num):
            continue

        input_num = int(input_num)

        if input_num == rand_num:
            print(f'LOL   Your Score Is = {Score}')
            break

        elif input_num > rand_num:
            print(f'{input_num} Is Too high')
      
        elif input_num < rand_num:
            print(f'{input_num} Is Too Low')


if __name__ == '__main__':
    main()
    


 
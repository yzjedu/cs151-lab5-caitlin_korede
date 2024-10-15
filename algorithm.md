# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. create choice variable and assign it to empty string
2. SENTINEL is equal to E
3. create an initial balance variable and set it equal to $1000
2. while choice is not equal to SENTINEL
   3. Prompt user to input one of the options and store it as choice
    3. if input is D
        4. ask user how much they want to deposit
           5. while deposit is negative
              6. print 'invalid deposit. try again'
              7. ask user how much they want to deposit
        5. set answer equal to deposit variable
        5. add deposit variable to balance and set it as updated balance variable
        6. output updated balance
    4. otherwise if input is w
       5. ask user how much they would like to withdraw
       6. while withdrawal is negative
          7. print 'invalid withdrawal. try again'
          8. ask user how much they would like to withdraw
       7. set answer equal to withdrawal variable 
       8. subtract answer from  balance and set it as updated balance variable
       9. output updated balance
    5. otherwise if input is v
       6. print balance
    6. if balance is less than zero
       7. output 'you will be charged 5% interest'
                        

                  
     
      
                    
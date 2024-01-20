from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(account):
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess,a_followers_count,b_followers_count):
  if a_followers_count > b_followers_count:
    return guess == "a"
  else:
    return guess == "b"
     
    
    
start = 0 
flag = True
account_b=random.choice(data)

while flag==True:
  print(logo)
  account_a=account_b
  account_b=random.choice(data) 
  if account_a==account_b:
    account_b=random.choice(data)
  
  
  
  print(f"Compare A: {format_data(account_a)}")
  
  print(vs)
  
  print(f"Against B: {format_data(account_b)}")
  
  guess = input("Who has more followers? Type  'A' or 'B':").lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  
  clear()
  if is_correct:
    print("you are right ")
    start += 1
    print(f"your current score is: {start}")
      
  else:
    print("you are wrong,final score:",start)
    flag = False
    y = input("do you want to play again? type 'y' or 'n':").lower()
    if y == "y":
      flag =True
      clear()
      










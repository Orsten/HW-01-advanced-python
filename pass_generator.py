import random
import string

def generate_password(length: int) -> str:
    all_chars = string.ascii_letters + string.digits + string.punctuation
    if length < 4:
        print("Password length must be at least 4.")
        return None
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    for _ in range(length-4):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return "".join(password)
  
length = input("Please enter the desired password length: ")

while not length.isdigit() or int(length) < 4:
    length = input("Invalid. Please enter a positive integer greater than 3: ")
      
password = generate_password(int(length))
if password:
    print(f"Generated password: {password}")
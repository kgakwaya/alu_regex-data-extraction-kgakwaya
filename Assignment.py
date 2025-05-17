import re 
while True:
    print("1. email address")
    print("2. phone number")
    print("3. hashtag")
    print("4. Credit Card")
    print("5. currency amounts")
    
    choice = int(input("choose between 1 and 5: "))
    if choice == 1:
        keyword = input("enter the email: ")
        pattern = r'^[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+\.[a-zA-Z.]{2,}$'
        if re.match(pattern, keyword):
            print("email you entered is valid")
        else:
            print("email you entered is invalid")
    elif choice == 2:
        keyword = input("enter the phone number : ")
        pattern = r'^\(?\d{3}\)?[ -.]\d{3}[ -.]\d{4}$'
        if re.match(pattern, keyword):
            print("phone number you entered is valid")
        else:
            print("phone number you entered is invalid")
    elif choice == 3:
        keyword = input("enter the hashtag: ")
        pattern = r'#[a-zA-Z]+'
        if re.match(pattern, keyword):
            print("hashtag you entered is valid")
        else:
            print("hashtag you entered is invalid")
    elif choice == 4:
        keyword = input("enter the credit card: ")
        pattern = r'\d{4}[\s-]\d{4}[\s-]\d{4}[\s-]\d{4}'
        if re.match(pattern, keyword):
            print("credit card you entered is valid")
        else:
            print("credit card you entered is invalid")
    elif choice == 5:
        keyword = input("enter the currency amount: ")
        pattern = r'\$\d{1,3}(,?\d{3})*(.?\d{2})?'
        if re.match(pattern, keyword):
            print("currency amount you entered is valid")
        else:
            print("currency amount you entered is invalid")

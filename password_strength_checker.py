"""
A strong password must contain at least 12 characters, a number, a lowercase, 
an uppercase, a special character and not be in the list of 10K most common
passwords
"""

from string import punctuation

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"

def load_common_passwords():
    """ Check user password against list of 10k common hacked passwords"""
    with open("10k-most-common.txt", "r") as file:
        content = file.read()
    return content

def password_strength(pw):
    """
    Test password against for strength against variables and print if it passes
    or fails
    """
    l, u, n, p, c = 0, 0, 0, 0, 0

    if (len(pw) >= 12):
        for i in pw:

            if i in lowercase:
                l += 1
            elif i in uppercase:
                u += 1
            elif i in number:
                n += 1
            elif i in punctuation:
                p += 1
    
        content = load_common_passwords()

        if (pw not in content):
            c += 1

    strength = 0
    if l:
        strength += 1
    if u:
        strength += 1
    if n:
        strength += 1
    if p:
        strength += 1
    if c:
        strength += 1
    

    if (strength >= 5):
        print("\nYour password is strong and mighty!")
    else:
        print("\nYour password is weaksauce. Try again.")

    print(f"""\nMaking your password stronger:
    - Length (must be 12 or higher)          : {len(pw)}
    - Lowercase (must contain at least 1)   : {l}
    - Uppercase (must contain at least 1)   : {u}
    - Number (must contain at least 1)      : {n}
    - Punctation (must contain at least 1)  : {p}
    - Must not be a common password         : {c}
""")

if __name__=="__main__":
    pw = input("Enter your password: ")
    password_strength(pw)
def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

password = input("Enter a password: ")

if check_password_strength(password):
    print("Password is strong.")
else:
    print("Password is weak.")
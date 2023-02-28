import random

# Define characters for each character set
lower_case_characters = "abcdefghijklmnopqrstuvwxyz"
upper_case_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!-/()!=^^+=%=(%=+?'?:;_"

# Generate a random string made of lower case letters
length = random.randint(1, len(lower_case_characters))
indices = random.sample(range(len(lower_case_characters)), length)
random_lower_str = "".join(lower_case_characters[i] for i in indices)

# Generate a random string made of upper case letters
length = random.randint(1, len(upper_case_characters))
indices = random.sample(range(len(upper_case_characters)), length)
random_upper_str = "".join(upper_case_characters[i] for i in indices)

# Generate a random string made of digits
length = random.randint(1, len(digits))
indices = random.sample(range(len(digits)), length)
random_digit_str = "".join(digits[i] for i in indices)

# Generate a random string made of symbols
length = random.randint(1, len(symbols))
indices = random.sample(range(len(symbols)), length)
random_symbol_str = "".join(symbols[i] for i in indices)

# Combine the generated strings and shuffle the characters
secure_password = random_lower_str + random_upper_str + random_digit_str + random_symbol_str
password_list = list(secure_password)
random.shuffle(password_list)
shuffled_secure_password = "".join(password_list)

# Check the password strength against the security requirements
has_lower = False
has_upper = False
has_digit = False
has_symbol = False

for char in shuffled_secure_password:
    if char in lower_case_characters:
        has_lower = True
    elif char in upper_case_characters:
        has_upper = True
    elif char in digits:
        has_digit = True
    elif char in symbols:
        has_symbol = True

# Print the generated password and its characteristics
print()
print("Generated secure password is " + shuffled_secure_password)
print()
print("Length: " + str(len(shuffled_secure_password)))
print("Contains lower case letters: " + str(has_lower))
print("Contains upper case letters: " + str(has_upper))
print("Contains digits: " + str(has_digit))
print("Contains symbols: " + str(has_symbol))

print()


# Check if the password meets the security requirements
is_secure = True

if len(shuffled_secure_password) < 12:
    is_secure = False

if not has_lower:
    is_secure = False

if not has_upper:
    is_secure = False

if not has_digit:
    is_secure = False

if not has_symbol:
    is_secure = False

# Print whether the password is secure or not
if is_secure:
    print("The generated password meets the security requirements.")
else:
    print("The generated password does not meet the security requirements.")


lower_num = 0
upper_num = 0
digit_num = 0
symbol_num = 0

for i in range(0, len(shuffled_secure_password)):
    if shuffled_secure_password[i] in lower_case_characters:
        lower_num = lower_num + 1
    elif shuffled_secure_password[i] in upper_case_characters:
        upper_num = upper_num + 1
    elif shuffled_secure_password[i] in digits:
        digit_num = digit_num + 1
    elif shuffled_secure_password[i] in symbols:
        symbol_num = symbol_num + 1

print("Generated secure password has " + str(lower_num) + " lowercase characters.")
print("Generated secure password has " + str(upper_num) + " uppercase characters.")
print("Generated secure password has " + str(digit_num) + " digits.")
print("Generated secure password has " + str(symbol_num) + " symbols.")

print()

total_chars = len(shuffled_secure_password)
lower_percentage = lower_num / total_chars * 100
upper_percentage = upper_num / total_chars * 100
digit_percentage = digit_num / total_chars * 100
symbol_percentage = symbol_num / total_chars * 100

print("The percentage of the amount of lowercase characters within the generated secure password is:", lower_percentage, "%")
print("The percentage of the amount of uppercase characters within the generated secure password is:", upper_percentage, "%")
print("The percentage of the amount of digits within the generated secure password is:", digit_percentage, "%")
print("The percentage of the amount of symbols within the generated secure password is:", symbol_percentage, "%")




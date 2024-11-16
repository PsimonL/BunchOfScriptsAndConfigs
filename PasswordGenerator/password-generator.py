import random
import string


def generate_password(l, e, d, a):
    if e + d + a == l:
        list_letters, list_digits, list_non_alphanumeric = [], [], []
        e_counter, d_counter, a_counter = 0, 0, 0
        non_alphanumeric = string.punctuation
        for x in range(l):
            if e_counter < e:
                e_counter += 1
                list_letters.append(random.choice(string.ascii_letters))
            if d_counter < d:
                d_counter += 1
                list_digits.append(random.randint(0, 9))
            if a_counter < a:
                a_counter += 1
                list_non_alphanumeric.append(random.choice(non_alphanumeric))
        final_list = list_letters + list_digits + list_non_alphanumeric
        random.shuffle(final_list)
        return [str(each) for each in final_list]
    else:
        raise Exception("Length of password must be same as sum of numbers for each type of sign!!!")


print("Generate your password")
length = int(input("Enter password length:"))
no_letters = int(input("Enter number of letters:"))
no_digits = int(input("Enter number of digits:"))
no_non_alphanumeric = int(input("Enter number of non-alphanumeric characters:"))
print("Wait...")
generated_password = ''.join(generate_password(length, no_letters, no_digits, no_non_alphanumeric))
print(f"Generated password: {generated_password}")

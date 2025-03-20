import random
import string


def get_replacement_dict():
    replacement_dict = {}
    used_replacements = set()

    for _ in range(5):
        while True:
            letter = input("Enter a lowercase character: ")
            if letter in string.ascii_lowercase and letter not in replacement_dict:
                break
            print("Invalid input or letter already chosen. Try again.")

        replacements = set()
        while len(replacements) < 3:
            rep = input(f"Enter a replacement for '{letter}': ")
            if len(rep) == 1 and rep not in replacements and rep not in used_replacements:
                replacements.add(rep)
                used_replacements.add(rep)
            else:
                print("Invalid or duplicate replacement. Try again.")

        replacement_dict[letter] = list(replacements)
    return replacement_dict


def generate_passwords():
    passwords = []
    for _ in range(5):
        password = ''.join(random.choices(string.ascii_lowercase, k=15))
        passwords.append(password)
    return passwords


def replace_characters(passwords, replacement_dict):
    replaced_passwords = []
    for password in passwords:
        new_password = ""
        for char in password:
            if char in replacement_dict:
                new_char = random.choice(replacement_dict[char])
                new_password += new_char
            else:
                new_password += char
        replaced_passwords.append(new_password)
    return replaced_passwords


def categorize_passwords(replaced_passwords):
    categorized_passwords = {"strong": [], "weak": []}
    special_chars = set(string.punctuation)

    for password in replaced_passwords:
        special_count = sum(1 for char in password if char in special_chars)
        if special_count > 4:
            categorized_passwords["strong"].append(password)
        else:
            categorized_passwords["weak"].append(password)
    return categorized_passwords


def main():
    print("Choose 5 characters (lowercase only) and assign 3 replacement options each:")
    replacement_dict = get_replacement_dict()
    passwords = generate_passwords()
    replaced_passwords = replace_characters(passwords, replacement_dict)
    categorized_passwords = categorize_passwords(replaced_passwords)

    print("\nGenerated Passwords:")
    print("\nSTRONG PASSWORDS:")
    for pwd in categorized_passwords["strong"]:
        print(pwd)

    print("\nWEAK PASSWORDS:")
    for pwd in categorized_passwords["weak"]:
        print(pwd)


if __name__ == "__main__":
    main()

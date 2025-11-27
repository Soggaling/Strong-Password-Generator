import secrets, string, sys

ALL_UPPER = string.ascii_uppercase
ALL_LOWER = string.ascii_lowercase
ALL_DIGITS = string.digits
ALL_SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/|~"

def generate_password(length):
    all_chars = ALL_UPPER + ALL_LOWER + ALL_DIGITS + ALL_SYMBOLS
    return "".join(secrets.choice(all_chars) for _ in range(length))

def main():
    try:
        length = int(input("Password length: ").strip())
    except:
        print("Invalid length")
        sys.exit(1)

    pwd = generate_password(length)
    print("\nGenerated password:\n" + pwd)

if __name__ == "__main__":
    main()

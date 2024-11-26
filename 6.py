class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    if len(password) < 9:
        raise LengthError("Password length should be at least 9 characters.")

    if password.isalpha() or password.isnumeric():
        raise LetterError("Password should contain both letters and numbers.")

    if not any(char.isdigit() for char in password):
        raise DigitError("Password should contain at least one digit.")

    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            raise SequenceError("Password should not contain sequences of 3 consecutive characters.")

    return 'ok'


try:
    password = input("Enter your password: ")
    result = check_password(password)
    print(result)
except PasswordError as e:
    print(f"Password Error: {e}")
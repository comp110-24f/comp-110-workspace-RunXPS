__author__ = "<PID>"


def mimic(message: str) -> str:
    """returns whatever string is given"""
    return message


if __name__ == "__main__":
    print(mimic(message=input("What is your message?")))

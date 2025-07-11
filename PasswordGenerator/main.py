import random
import string
import nltk
from typing import List, Optional

nltk.download('words')


def pin_password_generator(length = 8):
    return ''.join(random.choice(string.digits) for _ in range(length))


def random_password_generator(length = 8 , is_num = False , is_symble = False):
    random_password = string.ascii_letters

    if is_symble:
        random_password += string.punctuation

    if is_num:
        random_password += string.digits
    
    return ''.join(random.choice(random_password) for _ in range(length))


def memorable_password_generator(length, separator = "_", capitalization = False, vocabulary: Optional[List[str]] = None):
    vocabulary = nltk.corpus.words.words()
    password_words = random.sample(vocabulary, length)

    if vocabulary is None:
        vocabulary = ['apple', 'banana', 'cherry', 'dates'] 
    
    if capitalization:
        password_words = [word.capitalize() for word in password_words]

    return separator.join(random.choice(vocabulary) for _ in range(length))


def main():
    print("Random Password Generator:")
    print(random_password_generator(10))  # چاپ نتیجه
    print("\nMemorable Password Generator:")
    print(memorable_password_generator(10))  # چاپ نتیجه
    print("\nPincode Generator:")
    print(pin_password_generator(10))  # چاپ نتیجه

if __name__ == "__main__":
    main()
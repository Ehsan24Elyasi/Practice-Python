from constants import ABOVE_100, TENS, UNDER_20

def num_to_word(num):
    if num < 20:
        return UNDER_20[num]
    elif num < 100:
        remainder = num % 10
        if remainder == 0:
            return TENS[num // 10]
        else:
             return TENS[num // 10] + " " + UNDER_20[remainder]
    else:
        pivot = max ([key for key in ABOVE_100 if key <= num])
        p1 = num_to_word(num // pivot)
        p2 = ABOVE_100[pivot]
        if num % pivot == 0:
            return f'{p1}  {p2}'
        else:
            return f'{p1}  {p2} {num_to_word(num % pivot)}'
        

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    if num >= 0 and num <= 999_999_999_999:
        print(num_to_word(num))
    else:
        print("Number out of range")
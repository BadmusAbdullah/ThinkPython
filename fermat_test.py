# Fermat's Test
def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")


def prompt_and_check_fermat():
    input_a = int(input("Enter the value for a: "))
    input_b = int(input("Enter the value for b: "))
    input_c = int(input("Enter the value for c: "))
    input_n = int(input("Enter the value for n greater than 2: "))
    check_fermat(input_a, input_b, input_c, input_n)


prompt_and_check_fermat()

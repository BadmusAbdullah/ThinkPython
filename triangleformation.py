# Triangle Formation
def is_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("Yes")
    elif side1 + side2 == side3 or side1 + side3 == side2 or side2 + side3 == side1:
        print("Yes, degenerate triangle")
    else:
        print("No")


def three_sides():
    side1 = int(input("Enter the first side: "))
    side2 = int(input("Enter the second side: "))
    side3 = int(input("Enter the third side: "))

    is_triangle(side1, side2, side3)


three_sides()

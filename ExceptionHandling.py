def divideTheInputs(num, den):
    try:
        output = num/den
        print("Returning output: ", output)
        return output
    except ZeroDivisionError as z:
        print("Catch ZeroDivisionError!")
        # raise RuntimeError from z
    else:
        print("No ZeroDivisionError.")
    finally:
        print("Reached end of method.")


print("Valid input")
ans = divideTheInputs(2, 1)
print("Ans: ", ans)

print("Zero div input")
ans = divideTheInputs(2, 0)
print("Ans: ", ans)

print("Invalid input")
ans = divideTheInputs(2, "0")
print("Ans: ", ans)


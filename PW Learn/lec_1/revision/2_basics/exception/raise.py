
try:
    if -1 < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print("Caught exception:", e)
finally:
    print("Validation complete.")


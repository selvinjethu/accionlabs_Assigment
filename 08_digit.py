class Digit:
    def __init__(self, x):
        """Initialize with a single digit."""
        if not isinstance(x, int) or x < 0:
            raise ValueError("Input must be a non-negative integer.")
        self.x = x

    def calculate(self):
        """Calculates x + xx + xxx + xxxx."""
        try:
            return self.x + int(str(self.x) * 2) + int(str(self.x) * 3) + int(str(self.x) * 4)
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

if __name__ == "__main__":
    try:
        num = 3  
        result = Digit(num)
        print("Result:", result.calculate())
    except ValueError as e:
        print(f"Invalid Input: {e}")

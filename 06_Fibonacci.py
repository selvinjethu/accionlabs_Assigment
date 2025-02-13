class EvenFibonacci:
    def __init__(self, count):
        """Initialize the Fibonacci sequence with a count of even numbers to sum."""
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer.")
        self.count = count

    def sum_even_fibonacci(self):
        """Calculates the sum of the first 'count' even Fibonacci numbers efficiently."""
        a, b = 0, 2  
        sum_even = 0

        for _ in range(self.count):
            sum_even += a
            a, b = b, 4 * b + a  

        return sum_even

if __name__ == "__main__":
    try:
        fib = EvenFibonacci(100)
        result = fib.sum_even_fibonacci()
        print("Sum of first 100 even Fibonacci numbers:", result)
    except ValueError as e:
        print(f"Error: {e}")

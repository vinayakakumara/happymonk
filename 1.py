import multiprocessing


# Function to calculate the sum of squares for a given chunk of numbers
def sum_of_squares(chunk):
    total = 0
    for num in chunk:
        total += num ** 2
    return total


if __name__ == "__main__":
    # Input list of numbers (you can modify this list as needed)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Determine the number of CPU cores available for parallel processing
    num_processes = multiprocessing.cpu_count()

    # Split the input list into smaller chunks based on the number of processes
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Create a pool of worker processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Distribute the chunks among the worker processes and calculate the sum of squares
        results = pool.map(sum_of_squares, chunks)

    # Calculate the final sum of squares by combining results
    total_sum_of_squares = sum(results)

    # Print the result
    print(f"Sum of squares: {total_sum_of_squares}")

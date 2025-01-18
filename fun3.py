import time

def timer_program():
    try:
        # Input time in seconds
        total_seconds = int(input("Enter the time for the timer in seconds: "))
        if total_seconds <= 0:
            print("Please enter a positive number of seconds.")
            return

        print("Timer started...")
        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            timer_display = f"{mins:02}:{secs:02}"
            print(timer_display, end="\r")
            time.sleep(1)
            total_seconds -= 1

        print("Time's up!\n")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

def stopwatch_program():
    print("Stopwatch started. Press Ctrl+C to stop.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(int(elapsed_time), 60)
            timer_display = f"{mins:02}:{secs:02}"
            print(timer_display, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        mins, secs = divmod(int(time.time() - start_time), 60)
        print(f"Total time: {mins:02}:{secs:02}")

# Run the timer program
timer_program()

# Run the stopwatch program
stopwatch_program()

import threading
import time


def cook_pasta() -> None:
    """
    Simulates the process of cooking pasta.

    This function prints messages indicating the start and completion
    of the pasta cooking process, with a simulated delay.
    """
    print(f"Thread {threading.current_thread().name}", end="")
    print(": Starting to boil water...")
    time.sleep(3)
    print(f"Thread {threading.current_thread().name}: Pasta is ready!")


if __name__ == "__main__":
    thread1 = threading.Thread(target=cook_pasta, name="Cooker 1")
    thread2 = threading.Thread(target=cook_pasta, name="Cooker 2")
    thread3 = threading.Thread(target=cook_pasta, name="Cooker 3")

    print("Starting pasta cooking with multiple threads...")
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("All pasta is cooked! Dinner is served!")
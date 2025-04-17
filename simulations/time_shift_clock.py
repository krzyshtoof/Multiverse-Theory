import time
import threading

def custom_clock(offset):
    current_time = 0
    while True:
        time.sleep(1)  # Oczekiwanie przez jedną sekundę
        current_time += 1 + offset  # Dodanie przesunięcia
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(current_time))
        print(f"Custom Clock Time: {formatted_time}")

if __name__ == "__main__":
    offset = 0.00000001  # Przesunięcie czasu
    clock_thread = threading.Thread(target=custom_clock, args=(offset,))
    clock_thread.start()

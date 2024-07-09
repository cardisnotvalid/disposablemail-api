import time
import threading
from contextlib import contextmanager


@contextmanager
def spinner(text: str) -> None:
    clock_spinner = {
        "interval": 0.1,
        "frames": "◜◠◝◞◡◟"
    }

    def spinning() -> None:
        start_time = time.time()
        while getattr(spin_thread, "do_run", True):
            elapsed = time.time() - start_time
            frame_index = int(elapsed / clock_spinner["interval"]) % len(clock_spinner["frames"])
            frame = clock_spinner["frames"][frame_index]
            print(f"\r{frame} {text}", end="\033[K", flush=True)
            time.sleep(clock_spinner["interval"])

    spin_thread = threading.Thread(target=spinning)
    spin_thread.do_run = True
    spin_thread.start()

    try:
        yield
    finally:
        spin_thread.do_run = False
        spin_thread.join()
        print("\r", end="\033[K", flush=True)

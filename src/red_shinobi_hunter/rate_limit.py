import random
import time


class PaceController:
    def __init__(self, requests_per_second: float, stealth: bool = False, jitter_min: float = 0.0, jitter_max: float = 0.0):
        if requests_per_second <= 0:
            raise ValueError("requests_per_second must be positive")
        self.interval = 1.0 / requests_per_second
        self.stealth = stealth
        self.jitter_min = jitter_min
        self.jitter_max = jitter_max
        self._last = 0.0

    def wait(self) -> None:
        delay = self.interval
        if self.stealth:
            delay += random.uniform(self.jitter_min, self.jitter_max)
        remaining = delay - (time.monotonic() - self._last)
        if remaining > 0:
            time.sleep(remaining)
        self._last = time.monotonic()

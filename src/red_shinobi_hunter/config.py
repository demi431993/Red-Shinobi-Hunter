from dataclasses import dataclass

@dataclass(frozen=True)
class ScanConfig:
    timeout: float = 5.0
    max_targets: int = 64
    requests_per_second: float = 2.0
    stealth: bool = False
    jitter_min: float = 0.0
    jitter_max: float = 0.0

    def __post_init__(self) -> None:
        if self.timeout <= 0:
            raise ValueError("timeout must be positive")
        if self.max_targets < 1:
            raise ValueError("max_targets must be at least 1")
        if self.requests_per_second <= 0:
            raise ValueError("requests_per_second must be positive")
        if self.jitter_min < 0 or self.jitter_max < 0:
            raise ValueError("jitter values must be non-negative")
        if self.jitter_max < self.jitter_min:
            raise ValueError("jitter_max must be >= jitter_min")

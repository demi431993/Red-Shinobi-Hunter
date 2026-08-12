from dataclasses import asdict, dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .config import ScanConfig
from .rate_limit import PaceController
from .targets import normalize_url


@dataclass
class Result:
    target: str
    status: int | None
    server: str | None
    content_type: str | None
    error: str | None


def probe(target: str, config: ScanConfig) -> Result:
    url = normalize_url(target)
    pace = PaceController(config.requests_per_second, config.stealth, config.jitter_min, config.jitter_max)
    pace.wait()
    request = Request(url, method="HEAD", headers={"User-Agent": "Red-Shinobi-Hunter/0.1"})
    try:
        with urlopen(request, timeout=config.timeout) as response:
            return Result(url, response.status, response.headers.get("Server"), response.headers.get_content_type(), None)
    except HTTPError as exc:
        return Result(url, exc.code, exc.headers.get("Server"), exc.headers.get_content_type(), None)
    except (URLError, TimeoutError, OSError) as exc:
        return Result(url, None, None, None, str(exc))


def result_dict(result: Result) -> dict:
    return asdict(result)

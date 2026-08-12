from ipaddress import ip_address, ip_network
from urllib.parse import urlparse


def normalize_url(value: str) -> str:
    parsed = urlparse(value if "://" in value else f"https://{value}")
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"unsupported target: {value}")
    return parsed.geturl().rstrip("/")


def validate_cidr(value: str) -> str:
    return str(ip_network(value, strict=False))


def validate_ip(value: str) -> str:
    return str(ip_address(value))

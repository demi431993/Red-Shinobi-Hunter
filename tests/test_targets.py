import pytest

from red_shinobi_hunter.targets import normalize_url, validate_cidr, validate_ip


def test_normalize_url():
    assert normalize_url("example.com") == "https://example.com"


def test_ip_and_cidr():
    assert validate_ip("192.0.2.1") == "192.0.2.1"
    assert validate_cidr("192.0.2.0/24") == "192.0.2.0/24"


def test_rejects_non_http_scheme():
    with pytest.raises(ValueError):
        normalize_url("ftp://example.com")

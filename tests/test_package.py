import ratelimiter


def test_package_is_importable() -> None:
    assert ratelimiter.__name__ == "ratelimiter"

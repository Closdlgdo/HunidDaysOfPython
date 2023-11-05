from hello import hello


def test_hello():
    assert hello("Carlos") == "Hello Carlos!"  # This will not work because it is not returning a value.
    # assert hello() == "Hello, World!"

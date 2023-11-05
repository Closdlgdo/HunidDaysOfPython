from hello import hello


def test_default():
    assert hello("Carlos") == "Hello Carlos!"  # This will not work because it is not returning a value.


def test_argument():
    assert hello() == "Hello world!"  # We call hello without any parameters. It is not great practice to have multiple
    # tests in the same function.

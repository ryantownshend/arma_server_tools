"""Test LineConsumer."""
import pytest   # noqa
from arma_server_tools.arma_server import LineConsumer


def test_basic_string():
    """Test basic string parsing."""
    lc = LineConsumer()
    lc.parse("9:22:26 Initializing Steam server - Game Port: 2302, Steam Query Port: 2303")


def test_sample_log():
    """Test with the sample log."""
    lc = LineConsumer()
    with open("tests/arma_server_log.txt") as fp:
        # lines = fp.readlines()
        # for line in lines:
            # print(line)
            # lc.parse(line)
        for line in fp:
            print(line)
"""Tool for taking a look at the output."""
from arma_server_tools.arma_server import LineConsumer


def main():
    """Entry point."""
    print('main')

    lc = LineConsumer()
    with open("tests/arma_server_log.txt", "r") as fp:
        for line in fp:
            lc.parse(line.strip())


if __name__ == '__main__':
    main()

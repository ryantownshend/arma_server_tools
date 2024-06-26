import pytest
from arma_server_tools import PROJECT_ROOT
from arma_server_tools.yaml_tools import load_local_yaml
from arma_server_tools.server_config import SimpleType
import pprint

pp = pprint.PrettyPrinter(indent=4)


def test_config_yaml():

    config_fields = PROJECT_ROOT.joinpath("arma_server_tools", "server_config_fields.yaml")
    data = load_local_yaml(config_fields)

    # pp.pprint(data)

    args = {}

    for k in data.keys():
        print(k)
        d = data[k]
        # object = d['object']
        # print(f"  {object}")

        arg = d["arg"]
        print(f"  {arg}")

        if arg not in args:
            args[arg] = 1
        else:
            args[arg] += 1

    print("---")
    print(args)


def test_simple_type_string():
    result = SimpleType.generate("name", "value", "string")
    expected = 'name = "value";'
    assert result == expected


def test_simple_type_integer():
    result = SimpleType.generate("name", 12, "integer")
    expected = "name = 12;"
    assert result == expected

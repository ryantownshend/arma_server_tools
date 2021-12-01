import pytest
from arma_server_tools.yaml_tools import load_local_yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)


def test_config_yaml():

    data = load_local_yaml("arma_server_tools/server_config_fields.yaml")

    # pp.pprint(data)

    for k in data.keys():
        print(k)
        d = data[k]
        # object = d['object']
        # print(f"  {object}")

        arg = d['arg']
        print(f"  {arg}")
        
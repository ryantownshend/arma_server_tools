"""Server Config tool.

# https://community.bistudio.com/wiki/Arma_3:_Server_Config_File
"""


def is_quoted(arg):
    """Is quoted."""
    quoted = True
    if arg == "integer" or arg == "float":
        quoted = False
    return quoted


class BaseLineType(object):
    """Base line type class."""

    @staticmethod
    def generate(name, value, arg):
        """Generate."""
        pass


class SimpleType(BaseLineType):
    """Simple line type class."""

    @staticmethod
    def generate(name, value, arg):
        """Generate."""
        quoted = is_quoted(arg)
        if quoted:
            return f'{name} = "{value}";'
        else:
            return f'{name} = {value};'


class ListType(BaseLineType):
    """List type class."""

    @staticmethod
    def generate(name, value, arg):
        """Generate."""
        quoted = is_quoted(arg)
        product = []
        newline = "\n"
        if quoted:
            quote = '"'
        else:
            quote = ''

        product.append(f'{name}[] = {{{newline}')
        for item in value:
            product.append(f'  {quote}{item}{quote},{newline}')
        product.append(f'}};{newline}')

        return "".join(product)


class MissionType(BaseLineType):
    """Mission type."""

    pass


class MPMissionType(BaseLineType):
    """MPMission type."""

    pass


class Generator(object):
    """Generator."""

    def __init__(self, data):
        """Initialize."""
        self.data = data

    # # hostname = "Fun and Test Server";
    # # motdInterval = 5;
    # def simple_lineitem(self, key, value, quoted=False):
    #     if quoted:
    #         return f'{key} = "{value}";'
    #     else:
    #         return f'{key} = {value};'

    # # missionWhitelist[] = {
    # #   "direct_action_dev.Altis",
    # # };
    # # list_items('missionWhiteList', 'direct_action_dev.Altis', true, false)
    # def list_items(self, key, values, quoted=False, newlines=True):

    #     product = []
    #     if newlines:
    #         newline = ""
    #     else:
    #         newline = "\n"
    #     if quoted:
    #         quote = '"'
    #     else:
    #         quote = ''

    #     product.append(f'{key}[] = {{{newline}')
    #     for item in values:
    #         product.append(f'  {quote}{item}{quote},{newline}')
    #     product.append(f'}};{newline}')

    #     return "".join(product)

    # def generate(self):
    #     for 

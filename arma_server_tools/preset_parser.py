"""Preset Parser.

Take the exported list of mods from the Arma Launcher and parse it.

<https://docs.python.org/3/library/enum.html>
"""

import re
import click
from bs4 import BeautifulSoup
from enum import Enum

class Output(Enum):
    PLAIN = 'plain'
    UPDATE = 'update'
    MARKDOWN = 'markdown'

FORMAT_OPTION = ('plain', 'update', 'markdown')

class PresetParser(object):

    def __init__(self, html_file, output_format):
        self.html_file = html_file
        self.output_format = output_format

        # if output_format == Output.PLAIN:
        #     self.output_format = Output.PLAIN
        # elif output_format == Output.UPDATE:
        #     self.output_format = Output.UPDATE
        # else: 
        #     self.output_format = Output.MARKDOWN
    def parse(self):
        with open(self.html_file, encoding="ISO-8859-1") as fp:
            self.soup = BeautifulSoup(fp, features="html.parser")

        rows = self.soup.findAll("tr", {"data-type": "ModContainer"})

        product = []
        for r in rows:
            product.append(self.parse_row(r))

        self.prepare_report(product)

    def sanitized_name(self, display_name):
        """We need to clean up the display name for the file system.

        - If there is a leading @ keep it, if not add it
        - lowercase the whole thing
        - dispose of anything that is not letter, number, space, dash
        - translate spaces and dashes to underscores

        Possibly rewrite this for speed later on.

        return a tuple:
            (display_name, sanitized, steam_id, steam_url)
        """
        product = display_name.lower()                      # lowercase
        product = re.sub("[^A-Za-z0-9\s_]", "", product)    # keep only allowed list
        product = product.replace(' ', '_')                 # replace spaces with underscores
        product = product.replace('__', '_')                # replace __ with _
        return f'@{product}'                                # prepend @ and return

    def parse_row(self, row):
        display_name = row.find("td", {"data-type": "DisplayName"}).text
        steam_url = row.find("a", {"data-type": "Link"}).get("href")
        steam_id = steam_url.split("id=")[-1]
        sanitized = self.sanitized_name(display_name)
        # print(f'{display_name} : {steam_id}')
        return (display_name, sanitized, steam_id, steam_url)

    def prepare_report(self, product):
        if self.output_format == 'markdown':
            self.report_markdown(product)
        if self.output_format == 'update':
            self.report_update(product)
        else:
            self.report_plain(product)

    def report_plain(self, product):
        for item in product:
            print(f'{item[0]} : {item[2]}')

    def report_update(self, product):
        print('# update script')
        for item in product:
            print(f'poetry run steam_pull --name {item[1]} --id {item[2]} --mod')

    def report_markdown(self, product):
        pass

@click.command()
@click.argument(
    'html_file',
    required=True,
)
@click.option(
    '--format',
    'output_format',
    type=click.Choice(FORMAT_OPTION),
    default='plain',
    help="Type of output to produce."
)
def main(html_file, output_format):

    pp = PresetParser(html_file, output_format)
    pp.parse()


if __name__ == '__main__':
    main()

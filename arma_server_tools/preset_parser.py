"""Preset Parser.

Take the exported list of mods from the Arma Launcher and parse it.

<https://docs.python.org/3/library/enum.html>
"""

import re
import click
from bs4 import BeautifulSoup

FORMAT_OPTION = ('plain', 'update', 'markdown')


class PresetParser(object):
    """Tool for parsing arma 3 launcher preset exports."""

    def __init__(self, html_file, output_format):
        """Init."""
        self.html_file = html_file
        self.output_format = output_format

        # if output_format == Output.PLAIN:
        #     self.output_format = Output.PLAIN
        # elif output_format == Output.UPDATE:
        #     self.output_format = Output.UPDATE
        # else: 
        #     self.output_format = Output.MARKDOWN

    def parse(self):
        """Parse."""
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
        prod = display_name.lower()                 # lowercase
        prod = re.sub(r"[^A-Za-z0-9\s_]", "", prod) # keep only allowed list
        prod = prod.replace(' ', '_')               # replace spaces with _
        prod = prod.replace('__', '_')              # replace __ with _
        return f'@{prod}'                           # prepend @ and return

    def parse_row(self, row):
        """Parse row."""
        display_name = row.find("td", {"data-type": "DisplayName"}).text
        steam_url = row.find("a", {"data-type": "Link"}).get("href")
        steam_id = steam_url.split("id=")[-1]
        sanitized = self.sanitized_name(display_name)
        # print(f'{display_name} : {steam_id}')
        return (display_name, sanitized, steam_id, steam_url)

    def prepare_report(self, product):
        """Prepare report."""
        if self.output_format == 'markdown':
            self.report_markdown(product)
        if self.output_format == 'update':
            self.report_update(product)
        else:
            self.report_plain(product)

    def report_plain(self, product):
        """Report plain."""
        for item in product:
            print(f'{item[0]} : {item[2]}')

    def report_update(self, product):
        """Report update."""
        print('# update script')
        for i in product:
            print(f'poetry run steam_pull --name {i[1]} --id {i[2]} --mod')

    def report_markdown(self, product):
        """Report markdown."""
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
    """Entry point for the tool."""
    pp = PresetParser(html_file, output_format)
    pp.parse()


if __name__ == '__main__':
    main()

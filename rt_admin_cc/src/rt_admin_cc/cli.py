"""Console script for rt_admin_cc."""
import rt_admin_cc

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for rt_admin_cc."""
    console.print("Replace this message by putting your code into "
               "rt_admin_cc.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()

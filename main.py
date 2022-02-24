import typer
from os import listdir
from rich.console import Console
from rich.markdown import Markdown
from tomli import load
import textdistance

# Parsing config file
config = None
with open('config.toml', 'rb') as f:
    config = load(f)

# Constants
PATH = config['path'] + "/"
console = Console()
cprint = console.print

# List all the files in the dictionary directory ('dict')
# Then remove the '.md' from the file names
dict_names = [f.replace('.md', '') for f in listdir('dict')]

def find_name(name: str):
    """
    Find the name in the dictionary.
    If found return the path to the file with the name, else return None
    """
    if name in dict_names:
        return PATH + name + '.md'
    else:
        return None

app = typer.Typer()

@app.command()
def find(name: str):
    """
    Find the name in the dictionary.
    Return the most similar name in the dictionary. Else print an error message.
    """
    similiar_names = []
    for n in dict_names:
        if textdistance.levenshtein(name, n) <= 2:
            similiar_names.append(n)

    if similiar_names:
        typer.echo(f"I found:")
        for n in similiar_names:
            cprint(f"\t- [i]{n}[/i]")
    else:
        cprint(f"Cannot found '{name}' in the dictionary", style="red")

@app.command()
def name(name: str):
    path = find_name(name)
    if path:
        with open(path, 'r') as f:
            cprint(Markdown(f.read()))
    else:
        cprint(f"[red]Cannot found '{name}' in the dictionary. [/red]")
        # Find similar names
        similiar_names = []
        for n in dict_names:
            if textdistance.levenshtein(name, n) <= 2:
                similiar_names.append(n)

        if similiar_names:
            typer.echo(f"Do you mean:")
            for n in similiar_names:
                cprint(f"\t- [i]{n}[/i]")
        else:
            cprint("[red]Make sure you entered the name right"
                   " or use Markdown (.md) the definition file of the name.[/red]")

@app.command()
def list():
    typer.echo(f"The dictionary contains the following names:")
    for n in dict_names:
        cprint(f"\t- [i]{n}[/i]")

if __name__ == "__main__":
    app()

import click
from pathlib import Path
from heavywait.heavywait import HeavyWait

pass_service = click.make_pass_decorator(HeavyWait, ensure=True)


@click.group(
    invoke_without_command=False,
    help="""
    Heavywait is a CLI for decorating markdown files or directories of markdown files with AI generated metadata
    """,
    )
@click.pass_context
def cli(ctx):
    ctx.client = HeavyWait()


@cli.command("file")
@click.argument("src", type=click.Path(exists=True))
@click.argument("dst", type=click.Path())
@pass_service
def file(client: HeavyWait, src: str, dst: str):
    """
    Decorate given markdown file with AI generated metadata
    """
    client.file(Path(src), Path(dst))


@cli.command("dir")
@click.argument("src", type=click.Path(exists=True))
@click.argument("dst", type=click.Path(exists=True))
@pass_service
def dir(client: HeavyWait, src: str, dst: str):
    """
    Decorate files in given directory with AI generated metadata
    """
    client.directory(Path(src), Path(dst))


if __name__ == "__main__":
    cli()


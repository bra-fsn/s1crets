import sys
import click
import s1crets


@click.group()
def main():
    pass


@main.command()
@click.option('--provider', help='Secrets provider', default='aws.sm',
              show_default=True, type=click.Choice(['aws.sm', 'aws.ps']))
@click.argument('path', nargs=1, required=True)
def get(provider, path):
    print(s1crets.get(provider, path))


@main.command()
@click.option('--provider', help='Secrets provider', default='aws.sm',
              show_default=True, type=click.Choice(['aws.sm', 'aws.ps']))
@click.argument('path', nargs=1, required=True)
def get_by_path(provider, path):
    for k, v in s1crets.get_by_path(provider, path).items():
        print(k, v)

import os

import click

import woidb.config
import woidb.db
import woidb.importer

@click.command()
@click.argument('database')
@click.option('--user', '-u', prompt=True)
@click.option('--password', '-p', hide_input=True)
@click.option('--host', '-h')
@click.option('--port', '-p')
@click.pass_context
def init(ctx, database, user, password, host, port):
    woidb.db.init(database, user, password, host, port)
    woidb.config.save_db(database, user, password, host, port)


@click.command()
@click.argument('f', type=click.Path(exists=True))
@click.pass_context
def load(ctx, f):
    if os.path.isdir(f):
        files = [os.path.join(f, fn) for fn in os.listdir(f)]
    else:
        files = [f]
    with click.progressbar(files, label='Loading data files') as bar:
        for fi in bar:
            woidb.importer.import_csv(fi)


@click.group()
@click.version_option()
@click.pass_context
def main(ctx):
    ctx.obj = None

main.add_command(load)
main.add_command(init)

if __name__ == '__main__':
    main()
import os

import click

import woidb.config
import woidb.db
import woidb.models
import woidb.importer

@click.command()
@click.argument('database')
@click.pass_context
def init(ctx, database):
    engine = woidb.db.connect(database)
    woidb.models.Base.metadata.create_all(engine)
    woidb.config.save_db(database)


@click.command()
@click.argument('f', type=click.Path(exists=True))
@click.pass_context
def load(ctx, f):
    if os.path.isdir(f):
        files = [os.path.join(f, fn) for fn in os.listdir(f)]
    else:
        files = [f]
    with woidb.db.create_session() as session:
        with click.progressbar(files, label='Loading data files') as bar:
            for fi in bar:
                woidb.importer.import_csv(fi, session)


@click.group()
@click.version_option()
@click.pass_context
def main(ctx):
    ctx.obj = None

main.add_command(load)
main.add_command(init)

if __name__ == '__main__':
    main()
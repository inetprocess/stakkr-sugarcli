import click

from stakkr import docker
from sugarcli import sugarcli_wrapper


@click.command(help="Run a sugarcli command", context_settings=dict(ignore_unknown_options=True))
@click.pass_context
@click.argument('run_args', nargs=-1, type=click.UNPROCESSED)
def sugarcli(ctx, run_args: tuple):
    run_args = ' '.join(run_args)

    stakkr = ctx.obj['STAKKR']
    docker.check_cts_are_running(stakkr.project_name)

    if stakkr.cwd_abs.find(stakkr.stakkr_base_dir) != 0:
        raise Exception('You are not in a sub-directory of your stakkr instance')

    sugarcli_wrapper.run(docker.get_ct_item('php', 'name'), stakkr.cwd_relative, run_args)

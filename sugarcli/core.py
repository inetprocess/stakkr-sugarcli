import click

from sugarcli import sugarcli_wrapper


@click.command(help="Run a sugarcli command", context_settings=dict(ignore_unknown_options=True))
@click.pass_context
@click.argument('run_args', nargs=-1, type=click.UNPROCESSED)
def sugarcli(ctx, run_args: tuple):
    run_args = ' '.join(run_args)

    stakkr = ctx.obj['STAKKR']
    stakkr.check_cts_are_running()

    if stakkr.current_dir.find(stakkr.stakkr_base_dir) != 0:
        raise Exception('You are not in a sub-directory of your stakkr instance')

    sugarcli_wrapper.run(stakkr.get_ct_item('php', 'name'), stakkr.current_dir_relative, run_args)

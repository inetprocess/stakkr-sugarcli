import click

from plugins.sugarcli.lib import sugarcli_wrapper


@click.command(help="Run a sugarcli command", context_settings=dict(ignore_unknown_options=True))
@click.pass_context
@click.argument('run_args', nargs=-1, type=click.UNPROCESSED)
def sugarcli(ctx, run_args: tuple):
    run_args = ' '.join(run_args)

    lamp = ctx.obj['LAMP']
    lamp.check_vms_are_running()

    if lamp.current_dir.find(lamp.lamp_base_dir) != 0:
        raise Exception('You are not in a sub-directory of your lamp instance')

    sugarcli_wrapper.run(lamp.get_vm_item('php', 'name'), lamp.current_dir_relative, run_args)

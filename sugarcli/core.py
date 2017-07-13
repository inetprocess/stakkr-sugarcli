import click

from sugarcli import sugarcli_wrapper


@click.command(help="Run a sugarcli command", context_settings=dict(ignore_unknown_options=True))
@click.pass_context
@click.argument('run_args', nargs=-1, type=click.UNPROCESSED)
def sugarcli(ctx, run_args: tuple):
    run_args = ' '.join(run_args)

    marina = ctx.obj['MARINA']
    marina.check_vms_are_running()

    if marina.current_dir.find(marina.marina_base_dir) != 0:
        raise Exception('You are not in a sub-directory of your marina instance')

    sugarcli_wrapper.run(marina.get_vm_item('php', 'name'), marina.current_dir_relative, run_args)

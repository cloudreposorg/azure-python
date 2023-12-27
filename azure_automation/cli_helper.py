import os
import time
from azure.cli.core import get_default_cli

LOG_FILE = os.path.join(os.getcwd(), 'az_cli.log')

def az_cli(args_str):
    args = args_str.split()
    print("args", args)
    time.sleep(60)
    # for idx, item in enumerate(args):
    #     if '%' in item:
    #         item = item.replace('%', ' ')
    #         args[idx] = item
    cli = get_default_cli()
    cli.only_show_errors = True
    with open(LOG_FILE, 'w') as fw:
        cli.invoke(args, out_file=fw)
    return cli.result.exit_code, cli.result.result, cli.result.error


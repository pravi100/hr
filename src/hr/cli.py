from argparse import Action, ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    manage users on a server based on an inventory JSON file
    """)
    parser.add_argument('path', help='the path to the inventory file (JSON)')
    parser.add_argument("--export", action='store_true', help='export current settings to inventory file')
    return parser

def main():
    from hr import inventory, users

    args = create_parser().parse_args()

    if args.export:
        inventory.dump(args.path)
    else:
        users_info = inventory.load(args.path)
        users.sync(users_info)

import argparse
import os
import sys

from config_loader import load_rules
from sorter import sort_directory
from undo import undo_last_run


def parse_args():
    parser = argparse.ArgumentParser(
        description='Sortifile - simple file sorter with undo functionality'
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subcommand: sort
    sort_parser = subparsers.add_parser('sort', help='Sort a folder according to rules')
    sort_parser.add_argument(
        'target',
        type=str,
        help='Path of directory to sort'
    )
    sort_parser.add_argument(
        '--silent', '-s',
        action='store_true',
        help='If set, suppress logging of moved files'
    )
    sort_parser.add_argument(
        '--config', '-c',
        type=str,
        help='Path of custom rules.json (optional)',
        default=None
    )
    sort_parser.add_argument(
        '--dry-run', '-d',
        action='store_true',
        help='Show what would be done, without actually moving files'
    )

    # Subcommand: undo
    undo_parser = subparsers.add_parser('undo', help='Undo the last sort operation')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == 'sort':
        target_dir = os.path.expanduser(args.target)
        if not os.path.isdir(target_dir):
            print(f"Error: '{target_dir}' is not a valid directory.")
            sys.exit(1)

        rules = load_rules(args.config)
        sort_directory(target_dir, rules, dry_run=args.dry_run, silent=args.silent)

    elif args.command == 'undo':
        undo_last_run()


if __name__ == '__main__':
    main()

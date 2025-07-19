import argparse
import os

from config_loader import load_rules
from sorter import sort_directory


def parse_args():
    parser = argparse.ArgumentParser(
        description='Sortifile'
    )
    parser.add_argument(
        'target',
        type=str,
        help='Path of directory to sort'
    )
    parser.add_argument(
        '--silent', '-s',
        action='store_true',
        help='If set, suppress logging of moved files'
    )
    parser.add_argument(
        '--config', '-c',
        type=str,
        help='Path of custom set of rules (optional)',
        default=None
    )
    parser.add_argument(
        '--dry-run', '-d',
        action='store_true',
        help='Shows what files would be moved, but does not move anything'
    )
    return parser.parse_args()

def main():
    args = parse_args()
    target_dir = os.path.expanduser(args.target)
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is no valid directory.")
        return

    rules = load_rules(args.config)
    sort_directory(target_dir, rules, dry_run=args.dry_run, silent=args.silent)

if __name__ == '__main__':
    main()
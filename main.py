import argparse
from handlers import mine_handler

def main():
    parser = argparse.ArgumentParser(description="Technion Data Mining & Utility Tool")
    subparsers = parser.add_subparsers(dest="command", help="The action you would like to perform")

    # --- 'mine' subcommand ---
    mine_parser = subparsers.add_parser('mine', help='Run the scraper to collect course data')
    mine_parser.add_argument('-i', '--input', default='data/course_ids.json', help='Path to course IDs JSON')
    mine_parser.add_argument('-o', '--output', default='data/technion_courses.json', help='Where to save results')

    args = parser.parse_args()

    command_dispatcher = {
        'mine' : mine_handler
    }
    
    handler = command_dispatcher.get(args.command)
    if handler:
        handler(args)   
    else:
        parser.print_help()
if __name__ == "__main__":
    main()

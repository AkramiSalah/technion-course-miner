from utils.course_loader import load
from scrapers.miner import mine
from utils.course_saver import save

def mine_handler(args):
    print(f"--- Mining in proggress (Input: {args.input}) ---")
    ids = load(args.input)
    if not ids:
        print("Mining Interrupt: No valid IDs found.")
        return
    
    data = mine(ids)
    save(data, args.output)

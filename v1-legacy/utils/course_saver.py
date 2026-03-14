import json

def save(data, output_path="data/technion_courses.json"):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"\nScraping complete! Saved {len(data)} courses to {output_path}")
import requests
import json
import time
import random
from bs4 import BeautifulSoup

def scrape_course_data(course_id):
    url = f"https://students.technion.ac.il/local/technionsearch/course/{course_id}?lang=en"
    
    # weird header i gotta use otherwise nothing works
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')


        return {
            "course_id": course_id,
            "course_name": course_name,
            "pre_requisites": prereq,
            "parallel_courses": parallel,
            "no_extra_credit_courses": no_extra_credit,
            "recent_semesters": recent_semesters,
            "syllabus": syllabus
        }

    except Exception as e:
        print(f"Failed {course_id}: {e}")
        return None

courses = []
with open("course_ids.json" ,'r') as course_ids:
    courses = json.load(course_ids)["ids"]


all_course_data = {}

for index, cid in enumerate(courses):
    print(f"Scraping [{index+1}/{len(courses)}]: {cid}")
    
    data = scrape_course_data(cid)
    if data:
        key = f"{cid} - {data['course_name']}"
        all_course_data[key] = data
    
    # delay to not F up the technion servers, PLEASE! DO! NOT! REMOVE!!!!!!!!
    # uniform as to seem like a real user, i dont wanna get banned lol.
    time.sleep(random.uniform(0.5, 1.5))


with open('technion_courses.json', 'w', encoding='utf-8') as f:
    json.dump(all_course_data, f, indent=4, ensure_ascii=False)

print("Scraping complete. Data saved to technion_courses.json")
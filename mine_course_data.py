import requests
import json
import time
import random
from bs4 import BeautifulSoup

def get_course_name(soup):
    course_name_idx = 3
    raw_title_tag = soup.find('title')
    if not raw_title_tag:
        print("-- no title found!!!")
        return "--NO NAME--"
    
    title_text = raw_title_tag.get_text(strip=True)

    # assuming this is the foramt: <title> <course_id> - <course_name> | my.technion</title>
    try:
        title_text = title_text.split('|')
        title_text = title_text[0].split('-', 1)
        course_name = title_text[1]
        return course_name.strip()
    except Exception:
        print("-- NON EXPECTED COURSE TITLE FORMAT:")
        print(raw_title_tag)
        print(f"{'-'*10}")
        return "--WEIRD AHH COURSE NAME--"



def get_general_info_card(soup):
    card = soup.find("div", id="general_information")

    if not card:
        print("-- general info card not found!!!!!!")
        return None

    return card

def get_syllabus_text(general_info_card):
    syllabus_P = general_info_card.find("p", class_="card-text")
    if not syllabus_P:
        print("-- NO SYLLABUS FOUND!!!!")
        return "NO SYLLABUS FOUND"

    return syllabus_p.get_text(strip=True)

def get_prereqs(content_p):
    return content_p.get_text(" ", strip=True)
def get_anchor_list(content_p):
    return [a.get('data-course') for a in content_p.find_all("a") if a.get('data-course')]

def handle_course_info_section(h5_tag):
    title = h5_tag.get_text(strip=True).lower()
    content_p = h5_tag.find_next_sibling("p")
    if not content_p:
            print("--- Encountered section with no p elemnt!!!")
            print(title)
            print(f"{"-" * 10}")
        return None

    handlers = {
        "pre-required": get_prereqs,
        "parallel": get_anchor_list,
        "no extra credit": get_anchor_list,
        
    }
    
    for keyword, func in handlers.items():
        if keyword in title:
            return func(content_p)

    print("--- Encountered unknown section!!!")
    print(title)
    print(content_p)
    print(f"{"-" * 10}")
    return None
            



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
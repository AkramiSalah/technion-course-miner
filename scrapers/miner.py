import requests
import json
import time
import random
from bs4 import BeautifulSoup

def get_course_name(soup):
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
    if not general_info_card:
        print("-- general info card is None!!!!!!")
        return "no general info!!!!!!"
    
    syllabus_p = general_info_card.find("p", class_="card-text")
    if not syllabus_p:
        print("-- NO SYLLABUS FOUND!!!!")
        return "NO SYLLABUS FOUND"

    return syllabus_p.get_text(strip=True)

def get_prereqs(content_p):
    return content_p.get_text(" ", strip=True)

def get_anchor_list(content_p):
    if not content_p:
        return []

    return [a.get_text(strip=True) for a in content_p.find_all("a")]

def handle_course_info_section(h5_tag):
    title = h5_tag.get_text(strip=True).lower()
    content_p = h5_tag.find_next_sibling("p")
    if not content_p:
            print("--- Encountered section with no p elemnt!!!")
            print(title)
            print(f"{"-" * 10}")
            return None, None

    handlers = {
        "pre-required": ("pre_requisites", get_prereqs),
        "parallel": ("parallel_courses", get_anchor_list),
        "no extra credit": ("no_extra_credit_courses", get_anchor_list),
    }
    
    for keyword, (json_key, func) in handlers.items():
        if keyword in title:
            return json_key, func(content_p)

    print("--- Encountered unknown section!!!")
    print(title)
    print(content_p)
    print(f"{"-" * 10}")
    return None, None
            

def get_recent_semesters(soup):
    semester_card = soup.find("div", id="semester_information")
    if not semester_card:
        return []

    tabs = semester_card.find_all("a", class_="nav-link")
    semesters = [tab.get_text(strip=True) for tab in tabs]
    return semesters

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

        general_info_card = get_general_info_card(soup)
        course_name = get_course_name(soup)
        syllabus = get_syllabus_text(general_info_card)
        recent_semesters = get_recent_semesters(soup)

        course_data = {
            "course_id": course_id,
            "course_name": course_name,
            "pre_requisites": "NULL",
            "parallel_courses": "NULL",
            "no_extra_credit_courses": "NULL",
            "recent_semesters": recent_semesters,
            "syllabus": syllabus
        }

        if general_info_card:
            for h5 in general_info_card.find_all("h5"):
                key, value = handle_course_info_section(h5)
                if key:
                    course_data[key] = value

        return course_data

    except Exception as e:
        print(f"Failed {course_id}: {e}")
        return None


def mine(courses):
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

    return all_course_data
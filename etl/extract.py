import requests
from etl.models.course_query import CourseQuery
from etl.models.nav_segment import  NavSegment

session = requests.Session()

headers = {
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Sec-GPC": "1",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Origin": "https://portalex.technion.ac.il",
    "Referer": "https://portalex.technion.ac.il/ovv/",
    "X-Requested-With": "X",
    "sap-contextid-accept": "header",
    "sap-cancel-on-close": "true",
    "Accept": "application/json",
    "Accept-Language": "he",
    "DataServiceVersion": "2.0",
    "MaxDataServiceVersion": "2.0",
}


def request_query(requested_course : CourseQuery, nav_segment : NavSegment = None):
    base_url = "https://portalex.technion.ac.il/sap/opu/odata/sap/Z_CM_EV_CDIR_DATA_SRV/"
    entity_url = f"{base_url}{requested_course}"

    if nav_segment:
        entity_url += f"{nav_segment}"
    

    query_params = "?$format=json&sap-language=EN"
    full_url = f"{entity_url}{query_params}"

    print(f"  GET {full_url}")
    response = session.get(full_url, headers=headers, timeout=10)
    print(f"  HTTP {response.status_code}")
    response.raise_for_status()
    return response.json()["d"]


def extract_course_general(requested_course : CourseQuery):
    return request_query(requested_course)

def extract_course_relations(requested_course : CourseQuery):
    return request_query(requested_course, NavSegment.RELATIONS)
     
def extract_course_relations_reverse(requested_course : CourseQuery):
    return request_query(requested_course, NavSegment.RELATIONS_REVERSE)

def extract_course_period(requested_course : CourseQuery):
    return request_query(requested_course, NavSegment.PERIOD)
     
def extract_course_prereq(requested_course : CourseQuery):
    return request_query(requested_course, NavSegment.PREREQ)
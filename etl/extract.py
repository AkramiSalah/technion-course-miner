import requests
from etl.models.course_query import CourseQuery
from etl.models.course_offering import  CourseOffering


def request_query(requested_course : CourseQuery, section = None):
    base_url = f"https://portalex.technion.ac.il/sap/opu/odata/sap/Z_CM_EV_CDIR_DATA_SRV/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }


    entity_url = f"{base_url}{requested_course}"

    if section:
        entity_url += f"/{section}"
    

    query_params = "?$format=json&sap-language=EN"

    response = requests.get(f"{entity_url}{query_params}", headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()["d"]


def extract_course_general(requested_course : CourseQuery):
    return request_query(requested_course)

def extract_course_prereqs(requested_course : CourseQuery):
    return request_query(requested_course, "/SmPrereq")




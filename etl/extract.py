import requests
from etl.models.course_query import CourseQuery
from etl.models.course_offering import  CourseOffering

def extract_course(requested_course : CourseQuery):
        
    base_url = f"https://portalex.technion.ac.il/sap/opu/odata/sap/Z_CM_EV_CDIR_DATA_SRV/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    def request_query(url):
        query_params = "?$format=json&sap-language=EN"

        response = requests.get(f"{url}{query_params}", headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()["d"]

    entity_url = f"{base_url}{requested_course}"

    course_data = request_query(f"{entity_url}")
    prereq_data = request_query(f"{entity_url}/SmPrereq")
    
    return course_data, prereq_data



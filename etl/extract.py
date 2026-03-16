import requests
from models.course_offering import CourseOffering

def extract_course(requested_course : CourseOffering):
        
    base_url = f"https://portalex.technion.ac.il/sap/opu/odata/sap/Z_CM_EV_CDIR_DATA_SRV/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    def get(url):
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()

    entity_url = f"{base_url}{requested_course}"
    course_data = get(f"{entity_url}?$foramt=json")
    prereq_data = get(get(f"{entity_url}/SmPrereq?$foramt=json"))
    
    return course_data, prereq_data



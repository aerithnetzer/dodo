import requests
from pydantic import BaseModel
from shared.models import Activity


work = Activity(context="", actor="", summary="new_work", type="new_work", object="")
response = requests.post(
    "http://localhost:8000/activities/", data=work.model_dump_json()
)
if response.status_code != 404:
    print(f"  SUCCESS: {response.content}")

import requests
from pydantic import BaseModel


class Work(BaseModel):
    name: str


work = Work(name="Meow")
response = requests.post("http://localhost:8001/works/", data=work.model_dump_json())
if response.status_code != 404:
    print(f"  SUCCESS: {response.content}")

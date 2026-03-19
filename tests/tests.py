import requests
from shared.models import Activity, Object, CollectionObjectLink, Collection
from test_data import get_test_activity_data
import unittest
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("uvicorn.error")

headers = {
    "Authorization": "Bearer token",
    "Content-Type": "application/json",
    "token": "token",
}


class TestCreateActivity(unittest.TestCase):
    def test_new_activity(self):
        activity = Activity(
            context="",
            actor_id="",
            summary="new_work2",
            type="new_works",
            object_id="",
        )
        response = requests.post(
            "http://localhost:8001/activities/",
            data=activity.model_dump_json(),
            headers=headers,
        )
        self.assertIs(response.status_code, 200)


class TestCreateObject(unittest.TestCase):
    def test_new_objects(self):
        object = Object(type="Work")
        response = requests.post(
            "http://localhost:8001/objects/",
            data=object.model_dump_json(),
            headers=headers,
        )
        if response.status_code != 200:
            LOGGER.error(f"Object Creation Failed with status {response.status_code}")
        self.assertIs(response.status_code, 200)


class TestCreateCollection(unittest.TestCase):
    def test_new_collection(self):
        collection = Collection(type="Works")
        response = requests.post(
            "http://localhost:8001/collections/",
            data=collection.model_dump_json(),
            headers=headers,
        )
        if response.status_code != 200:
            LOGGER.error(
                f"Collection creation failed with status {response.status_code}.\nResponse content: {response.content}"
            )
        self.assertIs(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

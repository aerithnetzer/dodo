import requests
from shared.models import Activity, Object, CollectionObjectLink, Collection
from test_data import activities
import unittest
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("uvicorn.error")

headers = {
    "Authorization": "Bearer token",
    "Content-Type": "application/json",
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
    def test_new_object(self):
        object = Object()
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
        collection = Collection()
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


class TestCreateObjectCollectionLink(unittest.TestCase):
    def test_new_object_collection_link(self):
        object_collection_link = CollectionObjectLink(
            collection_id="",
            object_id="",
        )
        response = requests.post(
            "http://localhost:8001/collections/cc6198f2-7d68-4673-af7d-d8e788b97b0e/7b0a6be5-5ff6-4452-a313-48c9e5e83853",
            data=object_collection_link.model_dump_json(),
            headers=headers,
        )
        self.assertIs(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

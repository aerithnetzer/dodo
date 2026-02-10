import requests
from shared.models import Activity
import unittest


class TestCreateActivity(unittest.TestCase):
    def test_new_activity(self):
        activity = Activity(
            context="", actor="", summary="new_work2", type="new_works", object=""
        )
        response = requests.post(
            "http://localhost:8001/activities/", data=activity.model_dump_json()
        )
        self.assertIs(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

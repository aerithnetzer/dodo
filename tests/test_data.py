from shared.models import Activity, Actor, Object


def get_test_actor_data():
    actors: list[Actor] = []
    actors.append(Actor(type="Person", preferred_username="aerithnetzer"))
    actors.append(Actor(type="Person", preferred_username="kelseyrydland"))
    actors.append(Actor(type="Person", preferred_username="aihanliu"))
    actors.append(Actor(type="Person", preferred_username="basiakapolka"))
    actors.append(Actor(type="Person", preferred_username="dieyunsong"))
    actors.append(Actor(type="Person", preferred_username="mechfrazier"))
    return actors


def get_object_data() -> list[Object]:
    objects: list[Object] = []
    objects.append(
        Object(
            attributed_to="some-uuid", content="https://www.library.northwestern.edu"
        )
    )
    objects.append(
        Object(
            attributed_to="some-uuid",
            content="https://www.library.northwestern.edu/people",
        )
    )
    return objects


def get_test_activity_data():
    activities: list[Activity] = []
    activities.append(Activity(object_id="some-uuid", actor_id="some-uuid"))
    return activities

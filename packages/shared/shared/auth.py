from shared.models import Actor


def fake_decode_token(token):
    return Actor(
        username=token + "fakedecoded",
        email="myemail@outlook.com",
    )

from datetime import datetime, timedelta
import json
import hashlib
import os

import pytest
import pytest_mock

from data_producer.app import generate_fake_msg

# assert that the item was written to dynamodb, and that the hash PK is properly 32 characters long
def test_generate_fake_msg(faker_object):
    payload = generate_fake_msg(faker_object)
    assert isinstance(payload, dict) == True
    assert ['id', 'name', 'scrape_ts'] == list(payload.keys())
    assert len(payload['id']) == 32     # id hash should be 32 characters
    assert len(payload['name'].split()) >= 2 # name should have at least 2 words (first + last name)
    assert isinstance(payload['scrape_ts'], datetime) == True
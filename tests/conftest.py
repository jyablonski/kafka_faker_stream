from datetime import datetime, timedelta
import os

from faker import Faker
import pytest
import pytest_mock

@pytest.fixture(scope="session")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    os.environ["test"] = "test456"

@pytest.fixture
def faker_object():
    faker = Faker()
    return faker
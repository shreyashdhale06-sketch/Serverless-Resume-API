
import json
import os
import sys
from pathlib import Path

import boto3
import pytest
from moto import mock_aws
from boto3.dynamodb.conditions import Key

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "lambda"), str(ROOT)]

os.environ.update({
    "RESUME_TABLE": "ResumeData",
    "AWS_DEFAULT_REGION": "ap-south-1",
    "AWS_REGION": "ap-south-1",
    "AWS_ACCESS_KEY_ID": "testing",
    "AWS_SECRET_ACCESS_KEY": "testing"
})

import app as handler


@pytest.fixture
def db():
    with mock_aws():
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="ap-south-1"
        )

        table = dynamodb.create_table(
            TableName="ResumeData",
            KeySchema=[
                {"AttributeName": "PK", "KeyType": "HASH"},
                {"AttributeName": "SK", "KeyType": "RANGE"}
            ],
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"}
            ],
            BillingMode="PAY_PER_REQUEST"
        )

        table.wait_until_exists()
        yield table


def ev(path="/resume", section=None, method="GET"):
    return {
        "httpMethod": method,
        "path": path,
        "pathParameters": {"section": section} if section else None
    }


def test_full_resume_seeds_dynamodb(db):
    response = handler.lambda_handler(ev(), None)
    body = json.loads(response["body"])

    stored_items = db.query(
        KeyConditionExpression=Key("PK").eq("RESUME")
    )["Items"]

    assert response["statusCode"] == 200
    assert "personal" in body["data"]
    assert len(stored_items) >= 4


def test_personal(db):
    response = handler.lambda_handler(
        ev("/resume/personal", "personal"), None
    )

    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert body["data"]["name"] == "Shreyash Dhale"


def test_skills(db):
    response = handler.lambda_handler(
        ev("/resume/skills", "skills"), None
    )

    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert "Python" in body["data"]["programming"]


def test_invalid_section(db):
    response = handler.lambda_handler(
        ev("/resume/nope", "nope"), None
    )

    assert response["statusCode"] == 404


def test_post_not_allowed(db):
    response = handler.lambda_handler(
        ev(method="POST"), None
    )

    assert response["statusCode"] == 405


def test_local_auth():
    import local_api

    response = local_api.app.test_client().get("/resume")

    assert response.status_code == 401


def test_local_skills():
    import local_api

    client = local_api.app.test_client()

    response = client.get(
        "/resume/skills",
        headers={"x-api-key": "local-demo-key"}
    )

    assert response.status_code == 200
    assert "Python" in response.get_json()["data"]["programming"]

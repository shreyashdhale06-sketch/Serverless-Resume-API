import json, os
from pathlib import Path
import boto3
from boto3.dynamodb.conditions import Key

TABLE = os.environ.get("RESUME_TABLE", "ResumeData")
JSON_FILE = Path(__file__).resolve().parents[1] / "data" / "resume.json"
SECTIONS = {"personal", "experience", "education", "skills", "projects"}

def table():
    return boto3.resource("dynamodb", region_name=os.environ.get("AWS_REGION", "ap-south-1")).Table(TABLE)

def seed_if_empty(t):
    if t.query(KeyConditionExpression=Key("PK").eq("RESUME"), Limit=1).get("Items"):
        return
    # Read source JSON and persist each resume section in DynamoDB.
    with JSON_FILE.open(encoding="utf-8") as f:
        data = json.load(f)
    with t.batch_writer() as batch:
        for name, value in data.items():
            batch.put_item(Item={"PK":"RESUME","SK":name.upper(),"section":name,"content":value})

def reply(code, data):
    return {"statusCode":code,"headers":{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"},"body":json.dumps(data,ensure_ascii=False,default=str)}

def lambda_handler(event, context):
    if event.get("httpMethod","GET") != "GET":
        return reply(405, {"error":"Method not allowed; use GET"})
    params = event.get("pathParameters") or {}
    section = params.get("section")
    if not section:
        parts = [p for p in event.get("path","/resume").strip("/").split("/") if p]
        section = parts[-1] if len(parts)>1 else None
    if section and section not in SECTIONS:
        return reply(404, {"error":"Section not found","available_sections":sorted(SECTIONS)})
    try:
        t = table()
        seed_if_empty(t)
        if section:
            item = t.get_item(Key={"PK":"RESUME","SK":section.upper()}).get("Item")
            return reply(200, {"section":section,"data":item["content"]}) if item else reply(404,{"error":"Not found"})
        items = t.query(KeyConditionExpression=Key("PK").eq("RESUME")).get("Items",[])
        return reply(200, {"data":{i["section"]:i["content"] for i in items}})
    except Exception as exc:
        print(type(exc).__name__, str(exc))
        return reply(500, {"error":"Internal server error"})

import json
from pathlib import Path
from functools import wraps
from flask import Flask, jsonify, request

app=Flask(__name__)
DATA=Path(__file__).parent/"data"/"resume.json"
KEY="local-demo-key"

def auth(fn):
    @wraps(fn)
    def wrapped(*a,**kw):
        if request.headers.get("x-api-key") != KEY:
            return jsonify({"error":"Valid x-api-key header required"}),401
        return fn(*a,**kw)
    return wrapped

def load():
    with DATA.open(encoding="utf-8") as f: return json.load(f)

@app.get("/")
def home():
    return jsonify({"message":"Serverless Resume API local demo","api_key_header":"x-api-key: local-demo-key","routes":["/resume","/resume/personal","/resume/experience","/resume/education","/resume/skills","/resume/projects"]})

@app.get("/resume")
@auth
def all_resume(): return jsonify({"data":load()})

@app.get("/resume/<section>")
@auth
def one(section):
    data=load()
    if section not in data: return jsonify({"error":"Section not found","available_sections":sorted(data)}),404
    return jsonify({"section":section,"data":data[section]})

if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=False)

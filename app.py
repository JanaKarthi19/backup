from flask import Flask,request

app = Flask(__name__)

Info=[
    {
        "Name":"John k",
        "Father Name":"Kevin N",
        "Mother Name":"Leesa",
        "Phone Number":2589637410
    }
]

@app.get("/Info")
def get_info():
    return{"Information":Info}

@app.post("/Info")
def create_store():
    request_data = request.get_json()
    new_Info = {"name":request_data["name"],"Father Name":request_data["Father Name"]}
    Info.append(new_Info)
    return new_Info, 201
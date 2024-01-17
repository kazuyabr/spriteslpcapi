import json

from bson import json_util


def ResponseModel(data, message):
    json_data = json.loads(json_util.dumps(data))
    return {
        "data": json_data,
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
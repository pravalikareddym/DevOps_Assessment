import azure.functions as func
import json
from nested_lookup import get_value_by_path

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        obj = data.get("object")
        path = data.get("path")

        value = get_value_by_path(obj, path)
        return func.HttpResponse(json.dumps({"value": value}), status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)

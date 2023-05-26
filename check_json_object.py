import json

import jsonschema.exceptions
from jsonschema import validate

file = open("example.json", "r", encoding="UTF-8")
content = json.load(file)

schema1 = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "full-schema",
    "description": "test_output_object",
    "type": "object",
    "properties": {
        "dialog_id": {
            "type": "string",
        },
        "base_he_task_id": {
            "type": "string",
        },
        "ques_and_ans": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "task_type": {
                            "type": "string"
                        },
                        "prompt": {
                            "type": "string"
                        },
                        "canonical_solution": {
                            "type": "string"
                        },
                        "evaluation_method": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "type": {
                                            "type": "string"
                                        },
                                        "data_for_eval": {
                                            "type": "string"
                                        },
                                        "metrics": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "string"
                                                }
                                            ]
                                        }
                                    }
                                }
                            ]
                        },
                        "answers": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "time_cost": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "task_type",
                        "answers",
                        "time_cost"
                    ]
                }
            ]
        }
    },
    "required": [  # 必填字段
        "dialog_id",
        "ques_and_ans"
    ]
}

try:
    validate(instance=content, schema=schema1)
    print("validated")
except jsonschema.exceptions.ValidationError as e:
    print(e.message)
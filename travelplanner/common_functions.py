import sys
from rest_framework.response import Response

STATUS = "status"
MESSAGE = "message"
DATA = "data"

def ResponseFunction(status, message, data):
    false_list = [0, "false", False, "0"]
    if status in false_list:
        status = False
    else:
        status = True

    return Response({
        STATUS: status,
        MESSAGE: message,
        DATA: data
    })

    # Sample output structure
    # {
    #     "status": True,
    #     "message": "Data saved",
    #     "data": {
    #         "id": 1,
    #         "name": "Hotel 1",
    #         "is_active": true,
    #         "rate": "100.00",
    #         "actual_price": "100.00",
    #         "description": "Hotel 1",
    #         "location": 1,
    #         "type": 1,
    #         "address": "Hotel 1"
    #     }
    # }


def ValidateRequest(required, data_dic, **kwargs):
    errors = []
    message = ""
    for field in required:
        if field not in data_dic:
            message = f"Required {field}"
            errors.append({"error": message})
        else:
            if data_dic[field] == "" or not data_dic[field]:
                message = f"{field} cannot be empty"
                errors.append({"error": message})
                # print(message)

            else:
                message = f"{field} found"
    if len(errors):
        'Print if there where errors'
        print(errors)
    return errors


def printLineNo():
    return str(format(sys.exc_info()[-1].tb_lineno))
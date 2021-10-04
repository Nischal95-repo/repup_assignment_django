from django.http import HttpResponse
# from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
import json
import os


@action(detail=True, methods=['POST'])
def create(request):
    name = json.loads(request.body.decode("utf-8")).get("name")
    json_file = open('./board/board.json', mode='r')
    data = json.load(json_file)
    json_file.close()
    data.append({
        "name": name,
        "id": len(data)+1,
        "stage": 1
    })
    json_string = json.dumps(data, indent=2)
    json_file = open('./board/board.json', mode='w')
    json_file.write(json_string)
    json_file.close()
    return HttpResponse("Created Kanban board item")


@action(detail=True, methods=['PUT'])
def update(request, id):
    stage = json.loads(request.body.decode("utf-8")).get("stage")
    json_file = open('./board/board.json', mode='r')
    data = json.load(json_file)
    json_file.close()
    temp = []
    for rec in data:
        if(rec["id"] == id):
            temp.append(
                {
                    "name": rec["name"],
                    "id": rec["id"],
                    "stage": stage
                })
        else:
            temp.append(rec)

    json_string = json.dumps(temp, indent=2)
    json_file = open('./board/board.json', mode='w')
    json_file.write(json_string)
    json_file.close()
    return HttpResponse("Updated Kanban board item")

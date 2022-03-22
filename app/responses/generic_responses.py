"""Generic Responses"""
import json

class Responses():
    """Clase for make generic responses"""
    @staticmethod
    def index_response(data):
        """Response for index operation"""
        response = {
            "statusCode": 200,
            "status": "Success",
            "text": "Index have been made successfully",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

    @staticmethod
    def create_response(data):
        """Response for create operation"""
        response = {
            "statusCode": 201,
            "status": "Created",
            "text": "Resource have been created successfully",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

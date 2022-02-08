"""Generic Responses"""
import json

class Responses():
    """Clase for make generic responses"""
    @staticmethod
    def index_response(data):
        """Response for index operation"""
        response = {
            "status_code": 200,
            "status": "Success",
            "text": "Index have been made successfully",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

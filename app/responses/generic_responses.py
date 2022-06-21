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

    @staticmethod
    def show_response(data):
        """Response for show operation"""
        response = {
            "statusCode": 200,
            "status": "Success",
            "text": "Success show of resource",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

    @staticmethod
    def update_response(data):
        """Response for update operation"""
        response = {
            "statusCode": 201,
            "status": "Updated",
            "text": "Success update of resource",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

    @staticmethod
    def not_found_response(data):
        """Error response for not found resource"""
        response = {
            "statusCode": 404,
            "status": "Not Found",
            "text": "No resource found according to the given data",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

    @staticmethod
    def logical_delete(data):
        """Response for logical delete of a resource"""
        response = {
            "statusCode": 200,
            "status": "Deleted",
            "text": "Resource has been successfully deleted",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)

    @staticmethod
    def destroy_resource():
        """Response for a resource destroy"""
        response = {
            "statusCode": 204,
            "status": "Destroyed",
            "text": "Resource has been permanently deleted",
            "data": None
        }
        return json.dumps(response, ensure_ascii=False)

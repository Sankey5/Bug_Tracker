from flask import request, make_response, jsonify
from gateway import gateway
import mysql.connector.errorcode

code400 = jsonify([{"message": "name is not between 1 and 100 characters"},
                                          {"message": "description is not between 1 and 500 characters"},
                                          {"message": "priority not between 1 and 4"}], 400)



def getBugs():
    """
    Get all available bugs currently in the database
    """

    if request.method == 'GET':
        # reach out to database to get information
        bug = gateway.getBugs()

        bugs =


def deleteBug(id):


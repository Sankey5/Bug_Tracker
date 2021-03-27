from flask import request, make_response, jsonify
from gateway import gateway

code400 = make_response(jsonify([{"message": "name is not between 1 and 100 characters"},
                                          {"message": "description is not between 1 and 500 characters"},
                                          {"message": "priority not between 1 and 4"}]), 400)



def createBug():
    """
    Greate a bug and but it into the database
    :return:
    """
    if request.method == 'POST':

        # Get the necessary data from the post request (if it exists)
        name = request.form.get('name')
        description = request.form.get('description')
        priority = request.form.get('priority')

        # Checks to see if the given data meets the requirements
        if not (name and description and priority):
            return code400

        # If all checks have passed, attempt to make a new bug
        # The object itself should attempt to put the data into the database
        # Once the object is created, it should return a message with the id of the newly created object
        bug_id = gateway.createBug()
        response = make_response(jsonify({"message": "added", "id": bug_id}), 200)



def getBugs():
    """
    Get all available bugs currently in the database
    """

    if request.method == 'GET':
        # reach out to database to get information
        bug = gateway.getBugs()

        # return list of bugs




def deleteBug(id):

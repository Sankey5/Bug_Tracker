from flask import request, make_response, jsonify
from gateway import bugGateway

code400 = None #make_response(jsonify([{"message": "bug name is not between 1 and 100 characters"},
                                          #{"message": "description is not between 1 and 500 characters"},
                                          #{"message": "priority not between 1 and 4"}]), 400)



def create_bug():
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
        if not (name and description and priority) and len(name) < 100 and len(description) < 500 and 1 < int(priority) < 4:
            return code400

        # If all checks have passed, attempt to make a new bug
        # The object itself should attempt to put the data into the database
        # Once the object is created, it should return a message with the id of the newly created object
        bug_id = bugGateway.create_bug(name, description, priority)
        response = make_response(jsonify({"message": "added", "id": bug_id}), 200)
        return response


def get_bugs():
    """
    Get all available bugs currently in the database
    """

    if request.method == 'GET':
        # reach out to database to get information
        bugs = bugGateway.get_bugs()

        print(bugs)

        # return list of bugs
        bugs = [{"id": int(bug[0]),
                 "name": bug[1].decode(),
                 "description": bug[2].decode(),
                 "priority": bug[3]} for bug in bugs]

        response = make_response(jsonify(bugs), 200)
        return response


#def deleteBug(id):

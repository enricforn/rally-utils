import requests
import argparse

def assign_editor_permission(api_url, token, project_id, user_id):
    """
    Assigns editor permission to a user for a specific Rally TeamProject.

    :param api_url: The Rally API URL.
    :param token: The API token for authentication.
    :param project_id: The ID of the TeamProject.
    :param user_id: The ID of the user.
    """
    headers = {
        'ZSESSIONID': token,
        'Content-Type': 'application/json'
    }

    # Define the payload with the permissions
    payload = {
        "Permission": {
            "Role": "Editor",  # Set permission to Editor
            "WorkspacePermission": None,
            "User": f"/user/{user_id}",  # User reference
            "Project": f"/project/{project_id}"  # Project reference
        }
    }

    # Make the API request to create the permission
    response = requests.post(f"{api_url}/projectpermission/create", json=payload, headers=headers)

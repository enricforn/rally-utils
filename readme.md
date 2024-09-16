# Rally Utils

This repo include some scripts the improve your performance while operating Rally SaaS.

## Assign Permission

This Python script assigns editor permissions to a specified user for a Rally Broadcom TeamProject using the Rally API. The script accepts input parameters for the TeamProject ID, User ID, and optionally the API URL and API token. This script is useful for automating permission assignments within Rally, making it easier to manage access controls programmatically.

### How to Use the Script

#### Requirements

- Python installed on your system (Python 3 recommended).
- `requests` library installed (`pip install requests`).
- A valid Rally API token with permissions to assign roles.

#### Script Parameters

- **`project_id`**: (Required) The ID of the Rally TeamProject where the user will be assigned permissions.
- **`user_id`**: (Required) The ID of the user to whom editor permissions will be granted.
- **`--api_url`**: (Optional) The Rally API URL. Defaults to `https://rally1.rallydev.com/slm/webservice/v2.0`.
- **`--token`**: (Required) The API token for authentication with the Rally API.

#### Command-Line Usage

Run the script using the following format:

```bash
python assign_permission.py <project_id> <user_id> --token <your_token> [--api_url <custom_api_url>]

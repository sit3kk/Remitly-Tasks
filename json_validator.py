import json
import sys
import logging

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def verify_policy_input(file_path):
    """
    Verify the JSON IAM policy file.

    This function checks if any of the resources specified in the policy contains
    a single asterisk "*", which would signify a wildcard permission.

    Parameters:
    - file_path: str, the path to the JSON policy file.

    Terminal usage:
    - $ python json_validator.py /path/to/policy.json

    Returns:
    - bool: False if any resource is a wildcard "*", True otherwise.
    """

    try:
        with open(file_path, "r") as file:
            policy = json.load(file)

            statements = policy.get("PolicyDocument", {}).get("Statement", [])

            if not isinstance(statements, list):
                statements = [statements]

            for statement in statements:
                if statement.get("Resource", "") == "*":
                    return False

        return True
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        return True
    except json.JSONDecodeError:
        logging.error("Incorrect JSON format in file: %s", file_path)
        return True
    except Exception as e:
        logging.exception("An unexpected error occurred")
        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_policy_file>")
    else:
        file_path = sys.argv[1]
        result = verify_policy_input(file_path)
        print(result)

import os
from json_validator import verify_policy_input


def test_verify_policy_input_single_asterix():
    valid_file_path = os.path.join(
        os.path.dirname(__file__), "data", "test_data_1.json"
    )
    assert verify_policy_input(valid_file_path) is False


def test_verify_policy_input_without_single_asterix():
    valid_file_path = os.path.join(
        os.path.dirname(__file__), "data", "test_data_2.json"
    )
    assert verify_policy_input(valid_file_path) is True


def test_verify_policy_input_with_list_resources():
    valid_file_path = os.path.join(
        os.path.dirname(__file__), "data", "test_data_3.json"
    )
    assert verify_policy_input(valid_file_path) is True


def test_verify_policy_input_without_body():
    valid_file_path = os.path.join(
        os.path.dirname(__file__), "data", "test_data_4.json"
    )
    assert verify_policy_input(valid_file_path) is True


def test_verify_policy_input_with_multiple_statements_and_asterix():
    valid_file_path = os.path.join(
        os.path.dirname(__file__), "data", "test_data_5.json"
    )
    assert verify_policy_input(valid_file_path) is False


def test_verify_policy_input_with_multiple_statements_without_asterix():
    valid_file_path = os.path.join(
        os.path.dirname(__file__), "data", "test_data_6.json"
    )
    assert verify_policy_input(valid_file_path) is True

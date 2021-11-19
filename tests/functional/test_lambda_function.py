import json

from src.users import lambda_function


def test_lambda_handler(apigw_event, lambda_context):
    ret = lambda_function.lambda_handler(apigw_event, lambda_context)
    expected = json.dumps({"message": "hello universe"}, separators=(",", ":"))

    assert ret["statusCode"] == 200
    assert ret["body"] == expected

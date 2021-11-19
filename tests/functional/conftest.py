import uuid

import pytest


class MockContext(object):
    function_name = "func_name"
    invoked_function_arn = "func_arn"
    memory_limit_in_mb = 512
    aws_request_id = uuid.uuid4()


@pytest.fixture
def lambda_context():
    return MockContext()


@pytest.fixture
def apigw_event():
    return {
        "version": "2.0",
        "routeKey": "ANY /hello",
        "rawPath": "/hello",
        "headers": {
            "content-type": "application/json",
            "x-amzn-trace-id": "Root=1-60a0949a-4386c766717308f80e2072ba",
        },
        "requestContext": {
            "http": {
                "method": "GET",
                "path": "/hello",
            },
            "stage": "$default",
        },
    }

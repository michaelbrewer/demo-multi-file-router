from typing import List, Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.tracing.tracer import Tracer

router = Router()
logger = Logger(child=True)
tracer = Tracer()


@router.get("/users")
def users() -> List:
    logger.debug("Users called")
    return [{"name": "Foo"}]


@router.get("/users/<name>")
@tracer.capture_method
def user_by_name(name: str):
    return {"name": name, "version": 6}


@router.get("/hello")
def hello() -> Dict:
    # For the unit test
    return {"message": "hello universe"}

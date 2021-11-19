from typing import List, Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import Router

router = Router()
logger = Logger(child=True)


@router.get("/users")
def users() -> List:
    logger.debug("Users called")
    return [{"name": "Foo"}]


@router.get("/users/<name>")
def user_by_name(user: str):
    return {"name": user}


@router.get("/hello")
def hello() -> Dict:
    # For the unit test
    return {"message": "hello universe"}

from typing import Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.tracing import tracer

router = Router()
logger = Logger(child=True)


@router.get("/status")
@tracer.capture_method
def health() -> Dict:
    logger.debug("Health check called!")
    return {"status": "OK"}

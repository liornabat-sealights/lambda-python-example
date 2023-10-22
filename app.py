import os, json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler.api_gateway import ALBResolver
from aws_lambda_powertools.event_handler.api_gateway import (
    ALBResolver,
    ProxyEventType,
    Response,
)
from aws_lambda_powertools.event_handler.exceptions import (
    BadRequestError,
    InternalServerError,
    NotFoundError,
    UnauthorizedError,
)
URL_PREFIX = ""

logger = Logger()
tracer = Tracer()
#
# A aws_lambda_powertools application is used to route the ALB event to various
# endpoints.  The @app markup below maps the functions to various endpoints and HTTP methods 
app = ALBResolver()

@app.get("/health")
@tracer.capture_method
def health_check():
    """A health check endpoint needed to register an API with the DevExchange

    Parameters
    ----------

    Returns
    -------
    An ALB response.
    """
    
    response_body = {
        "status": "healthy"
    }
    return Response(
        status_code=200,
        body=json.dumps(response_body),
        content_type="application/json"
    )

@app.get(f"{URL_PREFIX}/example")
@app.get(f"{URL_PREFIX}/example/")
@tracer.capture_method
def example_get():
    """An example API endpoint that could be registered with the DevExchange.  Change
       this endpoint and the associated path to be specific to the API being implemented

    Parameters
    ----------

    Returns
    -------
    An ALB response.
    """    
    event = app.current_event
    response_body = {
        "data": {
            "message": "Hello World"
        }
    }
    #
    # Response must be in the format that the ALB understands
    return Response(
        status_code=200,
        body=json.dumps(response_body),
        content_type="application/json"
    )


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER
)
@tracer.capture_lambda_handler
def handler(event, context):
    """The Lambda handler utilizes the ALBResolver to route the event to 
       the appropriate function.
    """
    return app.resolve(event, context)
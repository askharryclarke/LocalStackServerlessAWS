import pytest
import localstack_client.session


def initialise_localstack_session():
    return localstack_client.session.Session()


def create_aws_client(resource_name: str):
    return initialise_localstack_session().client(resource_name)


def test_sqs_initialized():
    sqs = create_aws_client('sqs')
    assert sqs.list_queues() is not None

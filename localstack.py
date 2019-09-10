from subprocess import call


def main():
    list_dynamodb_tables()


def create_sqs_queue():
    create_queue_command = 'aws --endpoint-url=http://localhost:4576 sqs create-queue --queue-name {}'
    call(create_queue_command.format('hello_queue'), shell=True)


def create_another_sqs_queue():
    create_queue_command = 'aws --endpoint-url=http://localhost:4576 sqs create-queue --queue-name {}'
    call(create_queue_command.format('another_queue'), shell=True)


def list_sqs_queues():
    list_queues_command = 'aws --endpoint-url=http://localhost:4576 sqs list-queues'
    call(list_queues_command.format(), shell=True)


def list_dynamodb_tables():
    list_tables_command = 'aws --endpoint-url=http://localhost:4569 dynamodb list-tables'
    call(list_tables_command.format(), shell=True)


if __name__ == "__main__":
    main()

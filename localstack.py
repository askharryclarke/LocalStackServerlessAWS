from subprocess import call]


def main():
    create_queue()
    create_another_queue()
    list_queues()


def create_queue():
    create_queue_command = 'aws --endpoint-url=http://localhost:4576 sqs create-queue --queue-name {}'
    call(create_queue_command.format('hello_queue'), shell=True)


def create_another_queue():
    create_queue_command = 'aws --endpoint-url=http://localhost:4576 sqs create-queue --queue-name {}'
    call(create_queue_command.format('another_queue'), shell=True)


def list_queues():
    list_queues_command = 'aws --endpoint-url=http://localhost:4576 sqs list-queues'
    call(list_queues_command.format(), shell=True)


if __name__ == "__main__":
    main()

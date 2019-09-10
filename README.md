# LocalStack-Serverless Basic Template
LocalStack Serverless deploying AWS resources locally on host.

This is a simple setup for beginning to work with AWS resources locally using the 
LocalStack-Serverless framework.

Included in this repo is the following:
- A basic serverless.yml which will contain the necessary configuration for deployment to
localstack including a sample DynamoDB resource declaration.
- A localstack.py/test_localstack.py file which you can configure to deploy extra 
AWS resources and test against while your LocalHost is active.
- A localstack_endpoints.json which states which ports each AWS service should deploy to.
You can add and remove these as often as required, just ensure LocalStack supports the service
you're attempting to map.

## First Time Installation

Firstly we need to install local stack.

> pip install localstack

The following two commands are LocalStack's recommended way of installing their Serverless plugin

> npm install -g serverless
>
> npm install -save-dev serverless-localstack

## Starting the LocalStart host & Deploying the serverless template

Let's begin by creating the service endpoints on localhost.

> localstack start --host

__NOTE:__ This will take a long time as it needs to install the local servers for various
AWS services.

Once you receive the following message:
> Ready.

You can begin deploying your serverless stack, __make sure you receive the ready message
before you attempt to launch the stack.__ Open up a new terminal for this.

> sls deploy

## Checking your launched services

Once launched, you can interact with these services as you would using the standard AWS CLI.
The main difference is that you must declare the localhost url.

As this example only deploys a single DynamoDB table, let's check that it exists.

> aws dynamodb —endpoint-url=http://localhost:4569 list-tables
>
> aws dynamodb —endpoint-url=http://localhost:4569 describe-table —table-name HelloTable

Alternatively, LocalStack provides a lightweight wrapper for your CLI called 'awslocal' 
which removes the need to declare the endpoint url:
https://github.com/localstack/awscli-local

Finally, to stop these services, on the terminal window you launched the host, just hit
Control+C.
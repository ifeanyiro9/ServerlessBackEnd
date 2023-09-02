# **Serverless BackEnd**
## Alyx's Coffee Haven Serverless Backend

This repository contains the code and instructions to set up a basic serverless backend for Alyx's Coffee Haven. Alyx wants to create an API for her coffee shop's orders and test its functionality using Postman before building a frontend application.

## Prerequisites
**AWS Account**: You need an AWS account to create and manage the necessary resources like DynamoDB tables, Lambda functions and API Gateway.

**AWS CLI:** Install and configure the AWS Command Line Interface (CLI) to interact with AWS services.

**Postman:** Download and install Postman to test the API endpoints. You can get it [here](https://www.postman.com/).

## Objectives
**Create a DynamoDB Table:**
We will start by creating a DynamoDB table to store CoffeeOrder details. To set up the table, follow the instructions in the create-dynamodb-table directory.

**Develop and Deploy Lambda Functions:**
In this step, we will develop the Lambda functions responsible for handling coffee orders. These functions will interact with the DynamoDB table. To develop and deploy Lambda functions, follow the instructions in the lambda-functions directory.

**Create Coffee Haven API using Amazon API Gateway:**
Next, we will create an API using Amazon API Gateway to expose the Lambda functions as HTTP endpoints. To create the API, follow the instructions in the api-gateway directory.

**Integrate API Gateway to Lambda Functions:**
Now that we have an API, we need to integrate it with the Lambda functions we developed earlier. Follow the instructions in the api-integration directory to link the API Gateway and Lambda functions.

**Test the API using Postman:**
To ensure the functionality of the backend, we will test the API using Postman. You can import the Postman collection provided in the postman directory and follow the instructions in the collection to interact with the API.

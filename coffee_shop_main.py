import boto3
import json
import time
import os
import coffee_shop_table
import coffee_shop_lambdas
import coffee_shop_api

api_gateway = boto3.client('apigateway')
lambda_client = boto3.client('lambda')

# Create Coffee Shop Table
coffee_shop_table.create_table()

# Create Coffee Shop Lambdas 
role_arn = coffee_shop_lambdas.create_iam_role()

# Get the current directory of the Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

#Set Lambda function names and get corresponding zip files to upload to AWS
zip_paths = {
    'get_order': os.path.join(current_dir, 'get_order.zip'),
    'post_order': os.path.join(current_dir, 'post_order.zip'),
    'put_order': os.path.join(current_dir, 'put_order.zip'),
    'delete_order': os.path.join(current_dir, 'delete_order.zip')
}

time.sleep(10)  # Wait for IAM to full deploy
#Create each Lambda function
for key, value in zip_paths.items():
    coffee_shop_lambdas.create_lambda_function(role_arn, key, value)

# Create Coffee Shop API 
api_name = 'CoffeeShopAPI'
api_id = coffee_shop_api.create_api(api_name, api_gateway)
print(f'API ID: {api_id}\n')

resource_path = 'Orders'
function_names = ['get_order', 'post_order', 'put_order', 'delete_order']  # Replace with your Lambda function names
resource_id = coffee_shop_api.create_resource_and_methods(api_id, resource_path, api_gateway, function_names, lambda_client)
print(f'Resource ID for "{resource_path}": {resource_id}\n')

stage_name = 'Prod'
coffee_shop_api.create_stage(api_id, stage_name, api_gateway)
print(f"API '{api_name}' with ID '{api_id}' deployed to stage '{stage_name}'.")
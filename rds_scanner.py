import boto3
import json
import argparse
import sys

def get_rds_instances(region):
    """
    Retrieve metadata of all RDS instances in the specified AWS region.
    Returns a list of dictionaries containing instance metadata.
    """
    try:
        # Initialize the RDS client for the specified region
        rds_client = boto3.client('rds', region_name=region)
        
        # Get all RDS instances
        response = rds_client.describe_db_instances()
        
        # List to store instance metadata
        instances = []
        
        # Iterate through each DB instance
        for db_instance in response['DBInstances']:
            instance_info = {
                'DBInstanceIdentifier': db_instance['DBInstanceIdentifier'],
                'Engine': db_instance['Engine'],
                'Status': db_instance['DBInstanceStatus'],
                'Endpoint': db_instance.get('Endpoint', {}).get('Address', 'N/A')
            }
            instances.append(instance_info)
        
        return instances
    
    except Exception as e:
        print(f"Error retrieving RDS instances: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Scan AWS RDS instances in a specified region.')
    parser.add_argument('--region', required=True, help='AWS region (e.g., us-east-1)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get RDS instances
    instances = get_rds_instances(args.region)
    
    # Output the results in JSON format
    print(json.dumps(instances, indent=4))

if __name__ == '__main__':
    main()
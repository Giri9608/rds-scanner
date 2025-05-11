AWS RDS Scanner
A Python tool to list details of AWS RDS databases in a specified region, including engine type, status, and endpoint, in JSON format. This project includes both the Python script and a Docker container for easy deployment.
Prerequisites

Python 3.8 or higher (for running the script directly)

AWS CLI configured with credentials

IAM permissions for rds:DescribeDBInstances (e.g., AmazonRDSReadOnlyAccess)

Git

Docker (for running the containerized version)

Setup (Python Script)

Clone the repository:git clone https://github.com/Giri8608/aws-rds-scanner.git

cd aws-rds-scanner


Set up a virtual environment:python3 -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Configure AWS CLI:aws configure



Usage (Python Script)
Run the tool with a region:
python3 rds_scanner.py --region ap-south-1

Setup (Docker Container)

Pull the Docker image from Docker Hub:docker pull giri8608/rds-scanner


Run the container with your AWS credentials:docker run --rm \
  -e AWS_ACCESS_KEY_ID=<your-access-key> \
  -e AWS_SECRET_ACCESS_KEY=<your-secret-key> \
  -e AWS_DEFAULT_REGION=ap-south-1 \
  giri8608/rds-scanner --region ap-south-1

Replace <your-access-key> and <your-secret-key> with your AWS credentials.

Example Output
[

    {
        "DBInstanceIdentifier": "test-db-2",
        "Engine": "mysql",
        "Status": "available",
        "Endpoint": "test-db-2.xyz123456.ap-south-1.rds.amazonaws.com"
    }
    
]


Troubleshooting

Wrong region: Use valid regions like ap-south-1 or us-east-1.
Permission error: Ensure your IAM user has the required permissions.
Empty list: This is normal if no databases exist in the specified region.
Docker credential error: Ensure AWS credentials are passed correctly via environment variables.

License
MIT License

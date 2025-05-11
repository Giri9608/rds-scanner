# Use Alpine Linux as the base image

FROM alpine:3.18

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Install AWS SDK (boto3)
RUN pip3 install boto3

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY rds_scanner.py /app/

# Command to run the script (region will be passed at runtime)
CMD ["python3", "rds_scanner.py", "--region"]
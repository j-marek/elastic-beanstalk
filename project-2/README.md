# Dockerized Flask App with RDS Database

This project demonstrates how to deploy a containerized Flask application with an RDS database using the Elastic Beanstalk CLI.

## Prerequisites

1. AWS CLI installed and configured
2. Elastic Beanstalk CLI installed
3. Docker and Docker Compose installed
4. Python 3.9+

## Local Testing

1. Build and run with Docker Compose:
   ```
   docker-compose up --build
   ```

2. Visit `http://localhost:5000` in your browser to verify the application works.

## Deployment via EB CLI

1. Initialize the EB CLI in the project directory (if not already done):
   ```
   eb init
   ```
   Follow the prompts to select:
   - Your AWS region
   - The application name (project-2)
   - Docker as the platform
   - Optional: Set up SSH for instance access


2. Create the EB application:
   ```
   eb create project-2-docker-env
   ```

3. Open the application in a browser:
   ```
   eb open
   ```

## Environment Variables

The application requires the following environment variables:

- `DATABASE_URL`: Connection string for the RDS database (set automatically by Elastic Beanstalk)
- `FLASK_ENV`: Set to 'production' for deployed environments

## Monitoring and Management

- View application logs:
  ```
  eb logs
  ```

- View environment status:
  ```
  eb status
  ```

- SSH into the EC2 instance:
  ```
  eb ssh
  ```

- View environment health:
  ```
  eb health
  ```

- Terminate the environment when no longer needed:
  ```
  eb terminate project-2-docker-env
  ```

## Working with the RDS Database

The RDS database is automatically created and connected to your application. To access it directly:

1. Get the database connection information:
   ```
   eb printenv
   ```

2. Look for the database environment variables:
   - `RDS_HOSTNAME`: Database endpoint
   - `RDS_PORT`: Database port (typically 3306 for MySQL)
   - `RDS_DB_NAME`: Database name
   - `RDS_USERNAME`: Master username
   - `RDS_PASSWORD`: Master password

3. Connect using a MySQL client:
   ```
   mysql -h <RDS_HOSTNAME> -P <RDS_PORT> -u <RDS_USERNAME> -p <RDS_DB_NAME>
   ```

## Troubleshooting

- If the database connection fails, verify the security group settings to ensure the EC2 instances can connect to the RDS database.
- Check the application logs for detailed error messages: `eb logs`
- For Docker-specific issues, SSH into the instance and use `docker ps` and `docker logs` to investigate.
- If deployment fails, check the EB events: `eb events -f`
- For database connectivity issues, verify that the security group for the RDS instance allows inbound traffic from the EC2 security group.

## Cleanup

To avoid incurring charges, remember to terminate your environment when you're done:
```
eb terminate project-2-docker-env
```

This will delete the environment including the EC2 instances and the RDS database.
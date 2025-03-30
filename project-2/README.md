# Dockerized Flask App

This project demonstrates how to deploy a containerized Flask application using the Elastic Beanstalk CLI.

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
   eb create project-2-docker-env --single
   ```

3. Open the application in a browser:
   ```
   eb open
   ```

## Environment Variables

The application requires the following environment variables:

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


## Troubleshooting

- Check the application logs for detailed error messages: `eb logs`
- For Docker-specific issues, SSH into the instance and use `docker ps` and `docker logs` to investigate.
- If deployment fails, check the EB events: `eb events -f`

## Cleanup

To avoid incurring charges, remember to terminate your environment when you're done:
```
eb terminate project-2-docker-env
```

This will delete the environment including the EC2 instances.
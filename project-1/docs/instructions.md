# Deploying to AWS Elastic Beanstalk Using the AWS Console

This guide will walk you through deploying the Python application to AWS Elastic Beanstalk using the AWS Management Console.

## Prerequisites

1. An AWS account with appropriate permissions
2. Python 3.8+ installed on your development machine
3. Your application files ready for deployment (as provided in this project)


## Local Testing

1. Run the application locally:
   ```
   python application.py
   ```

2. Visit `http://localhost:5000` in your browser to verify the application works.

## Prepare for Deployment

1. Create a ZIP file of your application:
   - Make sure to include all necessary files: application.py, requirements.txt, .ebextensions folder, and templates folder
   - Do not include the virtual environment folder (venv) or any __pycache__ directories
   - Example command to create a ZIP file (run from your project root):
     ```
     zip -r eb-app.zip application.py requirements.txt .ebextensions/ templates/
     ```

## Deploy Using AWS Console

1. **Sign in to the AWS Management Console**:
   - Go to https://console.aws.amazon.com/
   - Sign in with your AWS account credentials

2. **Navigate to Elastic Beanstalk**:
   - In the AWS Management Console, search for "Elastic Beanstalk" or find it under the "Compute" section
   - Click on "Elastic Beanstalk" to open the service

3. **Create a New Application**:
   - Click the "Create application" button
   - Enter an application name (e.g., "my-eb-app")
   - Click "Create"

4. **Create a New Environment**:
   - Within your new application, click "Create a new environment"
   - Select "Web server environment"
   - Click "Next"

5. **Configure Environment**:
   - Enter an Environment name (e.g., "my-eb-app-env")
   - For Domain, either use the auto-generated one or enter a custom subdomain
   - For Platform, select "Python" and choose Python 3.8 (or later)
   - For Application code, select "Upload your code"
   - Click "Upload" and select the ZIP file you created
   - Click "Create environment"

6. **Wait for Deployment**:
   - AWS will now create your environment and deploy your application
   - This process may take 5-10 minutes
   - You can monitor the progress on the environment dashboard

7. **Access Your Application**:
   - Once deployment is complete, you'll see a green checkmark next to your environment name
   - Click the URL provided in the environment dashboard to access your application

## Managing Your Application in the Console

### Viewing Logs
1. Go to your environment in the Elastic Beanstalk console
2. In the left navigation pane, click "Logs"
3. Click "Request Logs" to generate and download the latest logs

### Monitoring
1. Go to your environment in the Elastic Beanstalk console
2. In the left navigation pane, click "Monitoring"
3. View metrics such as CPU utilization, network traffic, and request counts

### Environment Configuration
1. Go to your environment in the Elastic Beanstalk console
2. In the left navigation pane, click "Configuration"
3. Here you can modify:
   - Instance types
   - Environment variables
   - Load balancer settings
   - Auto-scaling options
   - Database connections
   - And more

### Updating Your Application
1. Create a new ZIP file with your updated application code
2. Go to your environment in the Elastic Beanstalk console
3. Click the "Upload and deploy" button
4. Select your new ZIP file and enter a version label
5. Click "Deploy"

### Terminating Your Environment
1. Go to your environment in the Elastic Beanstalk console
2. In the Actions dropdown menu, select "Terminate environment"
3. Confirm the termination
4. Note: This will delete all resources associated with your environment to avoid unnecessary charges

## Troubleshooting

1. **Health Check Issues**:
   - Verify that your application responds correctly at the `/health` endpoint
   - Check your application logs for errors
   - Make sure your application is listening on the correct port (port 5000 for Flask applications)

2. **Deployment Failures**:
   - Check the event log in the environment dashboard
   - Review the logs for specific error messages
   - Ensure your application.py file contains the correct application callable

3. **Performance Issues**:
   - Check the monitoring tab for resource utilization
   - Consider scaling up the instance type or enabling auto-scaling
   - Review your application code for potential bottlenecks
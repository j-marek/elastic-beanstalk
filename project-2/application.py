from flask import Flask, render_template, jsonify
import os
import pymysql
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
application = Flask(__name__)


# Database connection function
def get_db_connection():
    try:
        # Check for standard RDS environment variables that Elastic Beanstalk sets
        rds_host = os.environ.get("RDS_HOSTNAME")
        rds_port = os.environ.get("RDS_PORT")
        rds_dbname = os.environ.get("RDS_DB_NAME")
        rds_username = os.environ.get("RDS_USERNAME")
        rds_password = os.environ.get("RDS_PASSWORD")

        # Log connection attempt (without password)
        logger.info(
            f"Attempting to connect to DB: {rds_username}@{rds_host}:{rds_port}/{rds_dbname}"
        )

        if rds_host and rds_dbname and rds_username and rds_password:
            conn = pymysql.connect(
                host=rds_host,
                port=int(rds_port or 3306),
                user=rds_username,
                password=rds_password,
                database=rds_dbname,
                connect_timeout=5,  # Add timeout to prevent hanging
            )
            return conn
        else:
            logger.warning("Missing required RDS environment variables")
            return None
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        return None


# Routes
@application.route("/")
def home():
    # Check database connection
    db_status = "Not Connected"
    db_info = "No database connection established"

    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                if result:
                    db_status = "Connected"

                # Get database version
                cursor.execute("SELECT VERSION()")
                version = cursor.fetchone()
                db_info = (
                    f"MySQL version: {version[0]}" if version else "Connected to MySQL"
                )
        except Exception as e:
            logger.error(f"Database query error: {str(e)}")
            db_info = f"Error: {str(e)}"
        finally:
            conn.close()

    # Get environment information
    env_info = {
        "FLASK_ENV": os.environ.get("FLASK_ENV", "not set"),
        "Database Host": os.environ.get("RDS_HOSTNAME", "not set"),
        "Database Name": os.environ.get("RDS_DB_NAME", "not set"),
    }

    return render_template(
        "index.html", db_status=db_status, db_info=db_info, env_info=env_info
    )


@application.route("/health")
def health():
    # Simple health check that doesn't depend on database connectivity
    # This ensures the application passes health checks even if DB is unavailable
    return jsonify(status="healthy")


@application.route("/db-health")
def db_health():
    # Separate endpoint to check database health
    conn = get_db_connection()
    db_healthy = False

    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                if result:
                    db_healthy = True
        except Exception as e:
            logger.error(f"DB health check error: {str(e)}")
        finally:
            conn.close()

    return jsonify(status="healthy" if db_healthy else "unhealthy", database=db_healthy)


@application.route("/api/info")
def info():
    return jsonify(
        {
            "service": "Dockerized Flask App with RDS",
            "version": "1.0.0",
            "environment": os.environ.get("FLASK_ENV", "development"),
            "database_host": os.environ.get("RDS_HOSTNAME", "not connected"),
            "database_name": os.environ.get("RDS_DB_NAME", "not set"),
        }
    )


# Run the application
if __name__ == "__main__":
    # For local development only
    application.run(host="0.0.0.0", port=5000, debug=True)

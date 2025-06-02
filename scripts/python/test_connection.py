import os
import sys

print("Starting connection test...")

# Check username
username = os.getenv('USER')
print(f"Username: {username}")

# Try importing required modules
try:
    import psycopg2
    print("✓ psycopg2 imported")
except ImportError as e:
    print(f"✗ psycopg2 import failed: {e}")
    sys.exit(1)

try:
    from sqlalchemy import create_engine
    print("✓ sqlalchemy imported")
except ImportError as e:
    print(f"✗ sqlalchemy import failed: {e}")
    sys.exit(1)

# Try basic connection
try:
    print("\nTrying to connect to PostgreSQL...")
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user=username
    )
    print("✓ Connected to PostgreSQL!")
    
    # Check if our database exists
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database WHERE datname = 'power_grid_analysis';")
    result = cursor.fetchone()
    
    if result:
        print("✓ Database 'power_grid_analysis' exists!")
    else:
        print("✗ Database 'power_grid_analysis' NOT FOUND")
        print("\nCreating database...")
        conn.autocommit = True
        cursor.execute("CREATE DATABASE power_grid_analysis;")
        print("✓ Database created!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"✗ Connection failed: {e}")
    print("\nDebug info:")
    print(f"- Username: {username}")
    print("- Make sure PostgreSQL is running")
    print("- Try: brew services restart postgresql@15")

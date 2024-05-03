import mysql.connector

# Connect to the database
dbconfig = {
    'host':"localhost",
    'user':"root",
    "password": "0111284Tony!",
    "database":"User_test",
}

# Initialize connection pool
cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="my_practice_pool",
                                                       pool_size=5,  # Adjust pool size based on need
                                                       **dbconfig)
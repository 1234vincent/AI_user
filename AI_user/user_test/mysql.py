import pymysql

# 数据库连接配置
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '0111284Tony!',  # 确保使用安全的密码处理方法
    'database': 'User_test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# 连接数据库
connection = pymysql.connect(**config)

try:
    # 创建 cursor 对象
    with connection.cursor() as cursor:
        
        # 创建 user 表
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS user (
        #     user_id INT AUTO_INCREMENT PRIMARY KEY,
        #     username VARCHAR(255) NOT NULL,
        #     email VARCHAR(255) NOT NULL UNIQUE,
        #     password VARCHAR(255) NOT NULL,
        #     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        # )
        # """)
        # connection.commit()

        # # 创建 membership 表
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS membership (
        #     membership_id INT AUTO_INCREMENT PRIMARY KEY,
        #     user_id INT,
        #     level ENUM('Bronze', 'Silver', 'Gold', 'Platinum') NOT NULL,
        #     start_date DATE,
        #     end_date DATE,
        #     FOREIGN KEY (user_id) REFERENCES user(user_id)
        # )
        # """)
        # connection.commit()

        # # 创建 points 表
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS points (
        #     points_id INT AUTO_INCREMENT PRIMARY KEY,
        #     user_id INT,
        #     total_points INT DEFAULT 0,
        #     last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        #     FOREIGN KEY (user_id) REFERENCES user(user_id)
        # )
        # """)
        # connection.commit()

        # # 创建 activities 表
        # cursor.execute("""
        # CREATE TABLE IF NOT EXISTS activities (
        #     activity_id INT AUTO_INCREMENT PRIMARY KEY,
        #     user_id INT,
        #     activity_name VARCHAR(255) NOT NULL,
        #     activity_date DATE,
        #     FOREIGN KEY (user_id) REFERENCES user(user_id)
        # )
        # """)
        # connection.commit()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS privileges (
            privilege_id INT AUTO_INCREMENT PRIMARY KEY,
            privilege_name VARCHAR(255) NOT NULL,
            description TEXT
        )
        """)
        connection.commit()

        # 创建 membership_activity_privileges 表
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS membership_activity_privileges (
            level_id INT,
            activity_id INT,
            privilege_id INT,
            FOREIGN KEY (level_id) REFERENCES membership(membership_id),
            FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
            FOREIGN KEY (privilege_id) REFERENCES privileges(privilege_id),
            PRIMARY KEY (level_id, activity_id, privilege_id)
        )
        """)
        connection.commit()
finally:
    # 关闭数据库连接
    connection.close()

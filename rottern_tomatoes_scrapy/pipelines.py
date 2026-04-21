# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector
from mysql.connector import Error



class RotternTomatoesScrapyPipeline:

    def __init__(self):
        # Database configuration
        self.host = "localhost"
        self.user = "root"
        self.password = "actowiz"  # replace with your MySQL password
        self.port = "3306"
        self.database = "rotten_tomatoes_scrapy_db"

    def open_spider(self, spider):
        """Runs when spider starts"""
        try:
            # Connect to MySQL server
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.conn.cursor()

            # Create database if not exists
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.conn.database = self.database


            # ================================
            #  1. Create all_category table
            # ================================
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie_urls (
                id INT AUTO_INCREMENT PRIMARY KEY,
                movie_name VARCHAR(255),
                movie_url TEXT,
                status VARCHAR(50) DEFAULT 'pending'
            )
            """)

            # # ==================================
            # # 2. Create product_api table
            # # ==================================
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie_details (
                id INT AUTO_INCREMENT PRIMARY KEY,
                movie_name VARCHAR(200),
                movie_url TEXT,   
                description TEXT,   
                image_url TEXT,
                reviews VARCHAR(100),
                scorePercent VARCHAR(100),
                cast_and_crew JSON, 
                review_data_details JSON, 
                video_url JSON
            )
            """)

            self.conn.commit()
        except Error as e:
            spider.logger.error(f"Error connecting to MySQL: {e}")


    def process_item(self, item, spider):
        print("---process_item---", item)

        # -------------------------------
        # Insert into all_category
        # -------------------------------
        if item.get("type") == "all_movie_url":
            query = """
            INSERT INTO movie_urls (movie_name, movie_url, status)
            VALUES (%s, %s, %s)
            
            """

            values = (
                item.get("movie_name"),
                item.get("movie_url"),
                item.get("status", "pending")
            )

            self.cursor.execute(query, values)
            self.conn.commit()

        # -------------------------------
        #  Insert into product_api
        # -------------------------------
        elif item.get("type") == "movie_details":
            query = """
            INSERT INTO movie_details (movie_name, movie_url, description, image_url, reviews, scorePercent, cast_and_crew, review_data_details, video_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                item.get("movie_name"),
                item.get("movie_url"),
                item.get("description"),
                item.get("image_url"),
                item.get("reviews"),
                item.get("scorePercent"),
                item.get("cast_and_crew"), 
                item.get("review_data_details"), 
                item.get("video_url")
            )

            self.cursor.execute(query, values)
            self.conn.commit()

        return item





    # ====================================
    #  Close Connection
    # ====================================
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

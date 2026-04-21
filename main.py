
from extract_data import *
import time
from store_data_database import *
from fetch_movie_detail import *


file_name = "Amul Gold Milk Price in India - Buy Amul Gold Milk online at Flipkart.com.html"

def main():
    create_movie_urls_table()
    print("table and db create")

    # movies url 
    extract_movies_url()

    # fetch_movie_urls_table
    movie_urls_data_list = fetch_movie_urls_table()
    
    # create table 
    create_movie_details_table()

    fetch_movie_details(list_data= movie_urls_data_list)



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("time different  : ", end - start)






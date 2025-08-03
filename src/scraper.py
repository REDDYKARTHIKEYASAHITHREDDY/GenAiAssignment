from db_handler import insert_tournament

def insert_tournament_from_input():
    name = input("Enter Tournament Name: ")
    level = input("Enter Level: ")
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")
    official_url = input("Enter Official URL: ")
    streaming_links = input("Enter Streaming Links: ")
    image_url = input("Enter Image URL: ")
    summary = input("Enter Summary (max 50 words): ")

    data = (name, level, start_date, end_date, official_url, streaming_links, image_url, summary)
    insert_tournament(data)
    print("Tournament Data Inserted Successfully.")

if __name__ == '__main__':
    insert_tournament_from_input()
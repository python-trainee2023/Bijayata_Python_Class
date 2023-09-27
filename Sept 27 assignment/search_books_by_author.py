# Function to search for and display book records by a specific author
def search_books_by_author(author_name):
    try:
        with open("author.txt", "r") as file:
            found_books = []
            for line in file:
                book_info = line.strip().split(',')
                if len(book_info) == 2:
                    book_title, book_author = book_info
                    if book_author.strip() == author_name:
                        found_books.append(book_title.strip())

            if found_books:
                print(f"Books by {author_name}:")
                for book in found_books:
                    print(book)
            else:
                print(f"No books found by {author_name}.")
    except FileNotFoundError:
        print("The 'book.txt' file does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main program
if __name__ == "__main__":
    author_name = input("Enter the author's name: ")
    search_books_by_author(author_name)

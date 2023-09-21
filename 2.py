import requests


def fetch_books(api_url):
    """
    Fetches all available books from the API, handling pagination.
    Returns a list of book dictionaries.
    """
    books = []
    page = 1
    per_page = 100  # Adjust per_page as needed

    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            page_books = response.json()
            if not page_books:
                break
            books.extend(page_books)
            page += 1
        else:
            # Handle API request error
            print(f"Error fetching data: {response.status_code}")
            break

    return books


def analyze_books(books):
    """
    Analyzes the list of books and answers specific questions.
    """
    num_books = len(books)

    if num_books == 0:
        print("No books found in the database.")
        return

    # Calculate average publication year
    total_years = sum(book['publication_year'] for book in books)
    average_year = total_years / num_books

    # Find the most prolific author
    author_counts = {}
    for book in books:
        author = book['author']
        author_counts[author] = author_counts.get(author, 0) + 1
    most_prolific_author = max(author_counts, key=author_counts.get)

    # Find the top 5 genres with the most books
    genre_counts = {}
    for book in books:
        for genre in book['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    top_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    print(f"Number of books: {num_books}")
    print(f"Average publication year: {int(average_year)}")
    print(f"Most prolific author: {most_prolific_author} ({author_counts[most_prolific_author]} books)")
    print("Top 5 genres with the most books:")
    for i, (genre, count) in enumerate(top_genres, start=1):
        print(f"{i}. {genre} ({count} books)")


if _name_ == "__main__":
    api_url = "https://api.example.com/books"
    books = fetch_books(api_url)
    analyze_books(books)
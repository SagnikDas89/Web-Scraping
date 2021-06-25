from urllib.request import urlopen
from bs4 import BeautifulSoup
url = urlopen('https://bookpage.com/')
soup = BeautifulSoup(url, "html.parser")
books = soup.find_all('div', class_='content')

counter=0
for book in books:
    counter=counter+1
    if counter==6: break
    print("Book Number:",counter)
    

    book_name = book.find('h4', class_='italic')
    author_name = book.find('p', class_='sans bold')
    genre=book.find('p', class_='genre-links hidden-phone')
    review=book.find('p', class_='excerpt')
    print('Book Title :', book_name)
    print('Author :', author_name)
    print('Genre :', genre)
    print('Review :', review, sep='\n\n')
    
    

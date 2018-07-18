**Поиск всех файлов**.

`GET` /file/all



**Поиск файлов прикрепленных к определенной книге**

`GET` /file/<book_id: int>



**Поиск дат на которые забронирована определенная книга**

`GET` /loan/<book_id: int>


**Забронировать книгу**

`POST` /loan/add

- loanStart = [date] например: 2018-04-29

- loanDuration = [int]

- book = [int]


**Поиск книг по полям**

`GET` /book/search

- title = [str]

- author = [str]

- isbn = [int]

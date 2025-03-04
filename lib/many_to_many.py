class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Contract:
    all_contracts = []
    all = all_contracts  # Initial alias, but test overrides it

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        # No sync here—rely on all_contracts being populated by __init__
        return [contract for contract in cls.all_contracts if contract.date == date]
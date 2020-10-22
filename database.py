from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv('./books.csv')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/book_club')

df.to_sql('books', engine)


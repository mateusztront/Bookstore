from create import create_db, create_table
from tables import users_columns, messages_columns

create_db('bookstore')
create_table('users', users_columns)
create_table('messages', messages_columns)


from datetime import datetime


users_columns = """
id serial NOT NULL PRIMARY KEY,
username varchar(255),
password varchar(80)
"""


messages_columns = f"""
id serial  NOT NULL PRIMARY KEY,
from_id  int,
to_id int,
FOREIGN KEY (from_id) REFERENCES users(id),
FOREIGN KEY (to_id) REFERENCES users(id),
creation_date timestamp default current_timestamp
"""


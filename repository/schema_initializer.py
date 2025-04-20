from config.db_config import connectToDB

def create_table():
  conn = connectToDB()
  cursor = conn.cursor()
  
  cursor.execute(
    """
    create table if not exists todos (
      id char(36) primary key,
      title varchar(255) not null,
      completed boolean default false
    );
    """)
  
  conn.commit()
  cursor.close()
  conn.close()
# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine
engine = create_engine('sqlite:///automation.db')

# Write a SQL query
query = 'SELECT * FROM Blocker'

# Execute the query and store the result in a dataframe
df = pd.read_sql_query(query, engine)

# Print the dataframe
print(df)
df['Start'] = df['Start'].dt.tz_convert(None)
html_content = df.to_html()

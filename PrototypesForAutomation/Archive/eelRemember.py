import eel
from CollectBlockers import df
eel.init('')
# Function that Eel can expose to JavaScript
@eel.expose
def get_data():
    df_html = df.to_html(escape=False, index=False)

    # Replace "No" text with a link and add a data-index attribute for the row's index
    df_html = df_html.replace('>No<', f'><a href="#"  class="no-link" data-index="{df.index}">No</a><')

    return df_html

@eel.expose
def trigger_python(index):
    print(f'Row #{index} "No" link was clicked!')
    # Call your function when 'No' is clicked

eel.start('my_file.html')

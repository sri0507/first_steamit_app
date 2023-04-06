import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


#import streamlit
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 🥗 🐔 🥑🍞 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 🥗 🐔 🥑🍞 Kale spinach & Rocket smoothie')
streamlit.text('🥣 🥗 🐔 🥑🍞 Hard-Boiled Free-Range Egg' )
streamlit.text('🥣 🥗 🐔 🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[ 'Avocado' ,'Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return  fruityvice_normalized


# New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
                  streamlit.error('please select a fruit to get information.')
  else:
           
          back_from_function = get_fruityvice_data(fruit_choice)
          streamlit.dataframe(back_from_function)
          
except URLError as e:
  streamlit.error()

# don't run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()
      
      
 # add a button to load the fruit
if steamlit.button('Get fruit Load List'): 
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_row = get_fruit_load_list()
   streamlit.dataframe(my_data_row)


# Allow the end user to add fruit to the list
#Add_my_fruit = streamlit.text_input('What fruit would you like information about?','Kiwi')
#output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)



add_my_fruit = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', add_my_fruit)






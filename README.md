# Forestly
A forest management app


## Running instructions

- Clone down the repo.

- Install Flask (https://flask.palletsprojects.com/en/2.0.x/installation/).

- Install psycopg2 (https://pypi.org/project/psycopg2/).

- Navigate to wherever you stored the forest directory in your command line.

- $ createdb forest_manager
- $ psql -d forest_manager -f db/forest_manager.sql
- $ python3 console.py
- $ q (to quit pdb)

- $ flask run

- Click on/copy the address where the app is running into your browser’s address bar



## Brief 

### Forest Manager

Build an app that allows the user to manage a forest. 


#### MVP

- A tree should have an approximate_age, a variety, and a location (x and y coordinates).
- An area should have a grid reference (easting and northing) and a method that displays the grid reference. 
- A tree variety should have a name.
- The app should allow the user to create and edit trees.
- The app should allow the user to create and edit tree varieties.
- The app should allow the user to create and edit areas.
- The app should show a list of all tree types. 
- The app should show a list of all trees of one variety and their locations.


#### Extensions

- Add CSS styling to the app.
- The app should display all trees in a specific area.
- The app should display all locations for a particular species of tree.
- The user should be able to delete a tree.
- The user should be able to delete a tree type. 
- The user should be able to enter and store information about a particular tree in notes.


#### Advanced Extensions

- Plot each tree onto a simple grid map.

#### Future Possibilities

- Store each tree's historical data.
- Give the user options for the map.




### Technologies used

Flask, psycopg2, postgreSQL, VSCode, Google Chrome

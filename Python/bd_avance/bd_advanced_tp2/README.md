# App
After installing the requirements, the flask app can be ran using `flask run`.

All the data from the app is taken from DBPedia. 

The app will show some movies and 
by clicking on a movie, you can see other movies made by the same director 
or starring the same main actor

### Improvements
We could improve the app to show more information about movies and offer more suggestions based on more film information such as country of production, ...

# Graph
in `helper.py`, you can see a function called `add_data` that was used to create the `data.ttl` file. 

At the end of this function is a small film recommendation algorithm. This algorithm will recommend a movie if a friend has watched it. 

#### Improvements

We could improve the algorithm so that it takes into account if the friend has liked the movie or not. 
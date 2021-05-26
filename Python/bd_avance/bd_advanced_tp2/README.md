# App
![screenshot](https://siasky.net/3ABA-TunJ2VeOoFi-frb27ZcIdx1-w_ukQ3WpwbKhdoYsw)
### Installation
1. make sure you are in the right repo -> `../python`
2. installing the requirements
3. if using PyCharm, make sure you've set the `python`directory to main and the `template` one to template
3. setting the flask app using `export FLASK_APP=main.py`,
4. run the flask app can be ran using `flask run`.

All the data from the app is taken from DBPedia. 

The app will show some movies and 
by clicking on a movie, you can see other movies made by the same director 
or starring the same main actor

> Note: Some edge cases are not handled such as when an actor's name has some weird syntax. In this case the app will return a 500 error.

### Improvements
We could improve the app to show more information about movies and offer more suggestions based on more film information such as country of production, ...

# Graph
in `helper.py`, you can see a function called `add_data` that was used to create the `data.ttl` file. 

At the end of this function is a small film recommendation algorithm. This algorithm will recommend a movie if a friend has watched it. 

#### Improvements

We could improve the algorithm so that it takes into account if the friend has liked the movie or not. 

-- 

*Nathan Ganser*
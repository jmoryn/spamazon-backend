# spamazon-backend

<h1>Spamazon</h1>

<h4>A shopping app by Troy Redway, Andy Checo, and Jesse Moryn</h4>

Link to Deployed backend on Heroku: https://spamazon-ga-backend.herokuapp.com/api/products

The backend of Spamazon was made using Django and is hosted on Heroku. It's a typical JSON API with full CRUD operations which are performed on our 'products' model.

<h2>Process and Issues</h2>
Creating and deploying our backend to Heroku was the first thing we did for this project. We started by making a repo in Github, cloning to our local devices, and then one of us went through the process of building the Django API. It was all very straightforward <i>until</i> we tried to deploy to Heroku.

Unfortunately we ran into the same issue as many other groups, that being that our Procfile and requirements.txt files weren't at the "top level" of the project, and thus Heroku couldn't detect what kind of app we were trying to build. After moving those up to the main directory, it still didn't work. It turns out we had to alter the filepath in our Procfile so it could find our wsgi file, which as it turns out requires pretty weird syntax to do correctly. Once we ironed all that out, our backend was all set up and properly deployed on Heroku.  

One final issue we ran into occurred the day before the project was due. We attempted to change our model a little bit but then found that our create route wasn't working anymore. After some needless fretting, we figured out that we just needed to do another migration so Heroku had access to those model changes we made. After that it worked just fine!

<h2>Unresolved Issues</h2>
A few days into the project, we altered the 'price' field in our model to the "DecimalField" type, which we found in the Django documentation. The theory was that this would allow us to properly list items with prices listed to two decimal places.

We had a weird error where every time we'd add a product with a nonzero number in the decimal places, it would round the number after posting it to the site. For example, if we listed a product for 12.50, it would round to 13 when we posted and if we put 12.49, it would round down to 12. We have no idea why this was the case and tried a bunch of different things, including messing with the model more, looking at the HTML for our addProduct component, and more. I don't think the issue was with DecimalField, as I couldn't find any other posts about it online, so it's more likely it's either an issue with some other aspect of our backend, or something weird that's happening on our frontend. Whatever the case, we gave up on finding a solution as it was consuming too much time. 

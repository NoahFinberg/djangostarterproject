# Django Starter Project - Allauth, Postgres, Redis, RqWorker

Most webapps have a common initial configuration -- and there is no reason to spend hours doing the exact same config over and over for each new project. This is the first in a series of starter Django projects that follow common starting app patterns.

Following this repo will enable you to setup a standard development environment, webapp, and deploy to Heroku in less than 5 minutes and with fewer than ten lines of code (seriously) -- thank you Docker.
## Resources
This starter app leverages the following resources, but you don't need to worry about installing and configuring most of these. Just see prequisites below for what you need on your machine to make this work:

  - [Docker](https://www.docker.com/) - for virtual development environment and easy deployment
  - [Allauth](https://github.com/pennersr/django-allauth) - for user authentication
  - [Psycogpg](https://github.com/psycopg/psycopg2) - python client for postgres db
  - [django-redis-cache](https://github.com/sebleier/django-redis-cache#readme) - A Redis cache backend to store background jobs
  - [django-rq](https://github.com/rq/django-rq) - for managing Redis background jobs
  - [sbadmin2](https://startbootstrap.com/theme/sb-admin-2) - A Free Bootstrap Template from [Start Bootstrap](https://startbootstrap.com/).
  - [Heroku](http://www.heroku.com/) - for very easy production deployment.

## Prerequisites
As a prerequisite please make sure you have the following tools already installed on your machine:
1. [Git](https://git-scm.com/)
2. [Docker](https://docs.docker.com/get-docker/)
3. [Docker Compose](https://docs.docker.com/compose/install/)
4. [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) - Note: you'll need to create a Heroku account and there may be a cost associated with the servers you use.

## Setup in under 5 minutes!
1. Clone this repo
```sh
$ git clone
```
2. Build the Docker Container
```sh
$ cd django-starter-project
$ docker-compose up --build
```
You should see all the resources including the web server startup in your terminal. Now, open up another terminal window in the same directory.

3. Populate Postgres DB
```sh
docker-compose exec web python manage.py migrate
```
Now refresh localhost:8000. That should be enough for you to run the starter project locally. Seriously, that's it! One thing to note is if you change some settings in the Dockerfile or docker-compose.yml files, you'll need to rebuild the docker container.

If you'd like to deploy your project to Heroku, that's also pretty simple now. Just use the following commands:
```sh
# generates a new Heroku app
heroku create 
# creates new postgres db
heroku addons:create heroku-postgresql:hobby-dev 
# creates redis cache
heroku addons:create heroku-redis:hobby-dev

# sets the SECRET KEY in production. You'll need to generate one.
heroku config:set SECRET_KEY='replace me with a generated secret key'

# deploy to Heroku
git push heroku master
heroku ps:scale worker=1
heroku open
```
Congrats! You now have a pretty great starting point for your Django project.

## Screenshots
Here is what your app should look like when you visit localhost:8000 or your live app on Heroku.


## Acknowledgements
I followed a few great tutorials to get this all set up:
- The Beginners Guide to Django User Management and User Authentication...
- Integrating Bootstrap to Django
- [Django Docker Heroku Tutorial](https://github.com/jbarham/django-docker-heroku-tutorial)

To get up to speed with Django, I'd also recommend checking out the following tutorials that I used to get up to speed myself:
- [Python Django - Build a Web App in 60 minutes: Blog Application](https://www.youtube.com/watch?v=FinjKyFEAO4&t=910s) by Jamie Gullbrand
- [Django 1.10 Tutorial](https://overiq.com/django-1-10/) by OverIQ.com

## License
I've made this starter application freely available under an MIT license. 

Please feel free to use for commercial and non-commercial products alike. I would respectfully ask that you just cite this repo and provide a reference link back to it. If you appreciate this work, please don't forget to give this repo a star!

## Notes and Next Steps
Although I've been doing web development for more than five years, I've primarily worked with Rails (and a bit of Flask). As a result, please excuse (and point out) any unconventional practices in my Django code. Though it's very similar to Rails, I've only just started learning Django in the last two weeks.

As I build more Django projects, I'll update this repo to reflect best practices. I also plan to build additional stater applications as I begin to recognize more common Django patterns and resources. 

I'll also try to build a bunch of basic starter projects like this one, but with different pages and Bootstrap templates. Please check out [Start Bootstrap](https://startbootstrap.com/). I'll likely implement some of their "pro" resources. In which case, I'll buy the developer license. If you make use of any of their resources through my starter projects, you'll need to make sure to also buy your own license from them and any other templates sites. This starter app only uses the free template they offer so I don't think they require a license.

I welcome contributors to this project and future series of starter projects. I think helping other developers through this project has the potential to have a huge impact by saving countless development hours. If you'd like to contribute, please fork this project, make a new branch, and make a merge request.

### Todos
 - Refactor Templates for additional modularity

## Authors and Contributors
Noah Finberg

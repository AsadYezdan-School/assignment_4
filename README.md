# assignment_4
Github repository for assignment 4 for FOP class:
  - CRUD Capable Book Collection Manager
  - Stack : JS + HTML + CSS +DJANGO + POSTGRESQL
FOR ALEX : HOW TO GET THIS THING RUNNNING (im sure you know this already but just in case)
1) Clone this repo
2) Set up python virtual environment (python -m venv <insertNameOfVenvHere>)
3) Once the venv is loaded up, activate it (i was ina bash terminal so 'source path/to/activate') or other wise navigate to the directory in the venv where the venv is and run 'activate'
4) To get all the libraries i used, run 'pip install -r requirements.txt'. regquirements.txt should be defined in the repo
5) navigate tp .../collectionManager and run 'python manage.py runserver', this should take a couple secs and eventually say something like
'Starting development server at http://127.0.0.1:8000/', go to a browser (i wrote this in Firefox so i know it works there, not sure whatll happen if you try elsewhere but it should be fine.) and hit the dev server url.
6) you will (probably) see an error page, this is expected, the home page is at http://127.0.0.1:8000/books/home , so add '/books/home' to the url and hit enter this should take you to the home page and from there it should run like a regular website.

I hope this makes sense and was helpful. Please email me and id be more than happy to show you on my PC if nothing else works,(you can check the timestamps on commmits to make sure that if i show it to you on my PC after the deadline that i didnt write any more code)

TIPS FOR TESTING MY APP

1) For testing the upload via JSON, i wrote some mock JSON i this file 'testAdd.json', you can copy and paste it into the entry box, its supposed to make it more straightforward to test that what i wrote works.

2) All the titles end with -test, so you can test by uploading and then going to the home page and searching for '-test', all the books you add via json should have robots for pictures.

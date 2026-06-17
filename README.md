# Pets App

## Setup

1. Create and activate virtual environment:
    ```bash
    python3 -m venv .venv
    source venv/bin/activate
    ```
2. Install Django package:
    ```bash
    pip install django
    ```
3. Run migrations:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
4. Start the server:
    ```bash
    python3 manage.py runserver
    ```

## Database

Install sqlite 3 SQL client
    ```
        sudo yum install -y sqlite
    ```

Create tables
    ```
    sqlite3 -line db.sqlite3 '.tables'
    ``` 

Run the following command to show data
    ```
    sqlite3 -line db.sqlite3 'SELECT * FROM pets_app_pet'
    ```

## Django Shell

1. Start the Django shell:
    ```
    ./manage.py shell
    ```
2. Create an object:
    .save() -> commits changes to the database 
    ```
    from pets_app.models import Breed
    husky = Breed(name='Husky', weight=10, height=10)
    husky.save()
    ```
3. Create a vaccination card:
    ```
    from pets_app.models import VaccinationCard
    from datetime import datetime
    card1 = VaccinationCard (rabies = datetime(2021, 7, 19), hepatitis =
    datetime(2021, 8, 1), distemper = datetime(2021, 2, 9))
    card1.save()
    card2 = VaccinationCard (rabies = datetime(2024, 8, 16), hepatitis =
    datetime(2023, 7, 6), distemper = datetime(2023, 12, 9))
    card2.save()
    ```
4. Exit Shell:
    ```
    quit() or Ctrl+D
    ```

### Object Lookup

1. Open the shell:
    ```
    ./manage.py shell
    ```

2. Check all models:
    ```
    from pets_app.models import Pet, Gender, Breed, VaccinationCard
    ```

3. Retrieve all objects:
    ```
    all_breeds = Breed.objects.all()
    all_breeds
    ```
4. Retrieves a specifi object:
    ```
    all_breeds[0]
    ```

5. Update Vaccination Card:
    ```
    card1 = VaccinationCard.object.get(id=1)
    print(card1.borrelia)
    ```

6. Delete object & Check it doesn't exist:
    ```
    husky = Breed.objects.filter(name="Husky")[0]
    husky.delete()
    Breed.objects.all()
    ```
-----
-----

## Apps

### pets_app

Models:
- `Breed` - stores breed name, weight, and height
- `VaccinationCard` - tracks rabies, hepatitis, borrelia, and distemper vaccination dates
- `Pet` - stores pet info (name, gender, birth, owner, weight, height) linked to a `Breed` and `VaccinationCard`
- `VetVisit` - records vet visits with date and notes, linked to a `Pet`

## Notes

- `venv/` is excluded from version control via `.gitignore`

## Additional Notes

### Django uses MVT (Model View Template) Design Pattern: 
To Structure a Web App into Layers.

- Model: Handles data

- View: Processes requests and contains business logic

- Template: Defines how data is presented


#### Relationship Among Models:

- Many-to-one: (ForeignKey) Defines a many-to-one relationship between two models.

- One-to-one: Similar to a ForeignKey, but it ensures only one related object can exist.

- Many-to-many: Defines a many-to-many relationship between two models.


----
#### The VIEW:

The view processes the web request from the user and returns a web response.
Typically, the view accesses the model and decides what data to send back to the user.
It contains the application's business logic, which determines how to access the model. 
The view also typically uses a template to build the response containing the data that is sent back to the user.

#### How a view works:

- The view is the server-side component that receives an HTTP request and returns and HTTP response.
- When the browser sends an HTTP request to the application, a view defined in the application receives the 
request, runs the business logic to process the request, and returns an HTTP response.

#### Types of views

- Views can be implemented in Django using a function or a class.

##### _Function-based view_:

is a simple Python function that takes an object of type HttpRequest as its first parameter.  
The object contains the data from the incoming HTTP request. The function defines all the code that
implements the business logic from the view. When the function finishes running, the function returns
an object of type HttpResponse.

##### _Class-based view_:

This class defines properties and methods that give you the ability to respond to different HTTP request methods.
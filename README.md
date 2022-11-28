# Backend Coding Challenge

At aspaara a squad of superheroes works on giving superpowers to planning teams.
Through our product dashboard, we give insights into data – a true super-vision
superpower. Join forces with us and build a dashboard of the future!

![aspaara superhero](aspaara_superhero.png)

## Goal

Create a simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.

You will find the corresponding data that needs to be imported into the database
in `planning.json`, which contains around 10k records.

## Requirements

1. Create proper database tables that can fit the data model.
2. Create a script that imports the data into the database (sqlite).
3. Create REST APIs to get the planning data from the database.
    1. The APIs don't need to be complete, just create what you can in the
       available time.
    2. Please include at least one example on how to do each of the following:
        1. pagination
        2. sorting
        3. filtering / searching

## Data Model

* ID: integer (unique, required)
* Original ID: string (unique, required)
* Talent ID: string (optional)
* Talent Name: string (optional)
* Talent Grade: string (optional)
* Booking Grade: string (optional)
* Operating Unit: string (required)
* Office City: string (optional)
* Office Postal Code: string (required)
* Job Manager Name: string (optional)
* Job Manager ID: string (optional)
* Total Hours: float (required)
* Start Date: datetime (required)
* End Date: datetime (required)
* Client Name: string (optional)
* Client ID: string (required)
* Industry: string (optional)
* Required Skills: array of key-value pair (optional)
* Optional Skills: array of key-value pair (optional)
* Is Unassigned: boolean

## Preferred Tech Stack

* Python 3.8+
* FastAPI
* SQLAlchemy

## Submission

* Please fork the project, commit and push your implementation and add
  `sundara.amancharla@aspaara.com` as a contributor.
* Please update the README with any additional details or steps that are
  required to run your implementation.
* We understand that there is a limited amount of time, so it does not have to
  be perfect or 100% finished. Plan to spend no more than 2-3 hours on it.

For any additional questions on the task please feel free to email
`sundara.amancharla@aspaara.com`.

## STEPS TO RUNNING THE APP

## Technology Stack

* FastAPI
* SQLAchemy
* SQLITE
* fastapi-pagination

###  Setting Up For Local Development

*   Check that python 3 is installed:
    ```
    python --version
    >> Python 3.x.x
    ```
*   Install virtualenv or pipenv:
  ```
    pip install virtualenv
    ```
*    Create a virtual enviroment
  you can create one with virtualenv using
  `virtualenv venv`
  or
	```
	python3 -m venv venv
	```
*   Activate the virtual enviroment:
    - On Linux/Mac:
	    ```
	    source venv/bin/activate
	    ```
    -  On Windows:
      ```
	    venv/scripts/activate
	    ```
	Feel free to use other tools such as pipenv

*   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt
    ```

*   Ensure you are in the root folder and Run the application with the command

    ```
    uvicorn planner_api.main:app --reload
    ```

*   To load the sqlite db run the following command
    ```
    python populate_db.py 
    ```

*   To check the list of the planners go the this route on your browser after running the uvicorn server
    ```
    http://127.0.0.1:8000/planners
    ```

*   You can check the documentation on how to filter, sort, or change the default pagination parameters
    ```
    http://127.0.0.1:8000/docs
    ```

*   To run the app test
    ```
    python -m pytest tests/ 
    ```

## Pagination

* pagination is applied by default with size of 50 and page of 1,
* To change the default pagination, specify the queryparam `size` or `page` with the desired number
    ```
    http://127.0.0.1:8000/planners?size=10&page=1
    ```

## Filter and Sort
* To sort, use the `sort`  query parameter, providing the value you want to sort as
    ```
    http://127.0.0.1:8000/planners?sort=talent_name
    ```

* To filter, use the `filter`  query parameter, providing the value you want to filter as in this form `filter=query_key,query_value-another_query_key,another_query_value`
  For example
    ```
    http://127.0.0.1:8000/planners?filter=industry,Retail
    ```
    or 
    ```
    http://127.0.0.1:8000/planners?filter=industry,Retail-talent_id,tln_7794
    ```

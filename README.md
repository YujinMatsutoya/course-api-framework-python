# course-api-framework-python

Based on Gaurav Singh's course on building an API framework with Python on Test Automation University. 

The application under test is the `people-api`, which you can find the Github repo
[here](https://github.com/automationhacks/people-api).

Note: These tests expect the `people-api` xPI to be up. You can find
instructions in the `people-api` repo

## Tests Covered
- Retrieving a specific person
- Creating a new person
- Deleting a person
- Updating a person's details


## Running the Tests
Clone this repo and run:

```
# change directory
cd course-api-framework-python

# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest
```

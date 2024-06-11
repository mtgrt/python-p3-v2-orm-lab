from __init__ import CURSOR, CONN
from department import Department
from employee import Employee


class Review:

    def __init__(self, employee_id, year, summary):
        self._employee_id = None
        self._year = None
        self._summary = None
        self.employee_id = employee_id  # Use the setter
        self.year = year  # Use the setter
        self.summary = summary  # Use the setter

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        if not isinstance(value, int):
            raise ValueError("employee_id must be an integer")
        self._employee_id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("year must be an integer")
        if value < 2000:
            raise ValueError("year must be >= 2000")
        self._year = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if not isinstance(value, str):
            raise ValueError("summary must be a string")
        if len(value) == 0:
            raise ValueError("summary cannot be an empty string")
        self._summary = value

    def save(self):
        # Implementation to save the review instance to the database
        pass

    @classmethod
    def create(cls, employee_id, year, summary):
        # Implementation to create a new review in the database
        pass

    @classmethod
    def instance_from_db(cls, db_row):
        if db_row is None:
            raise ValueError("No data found")
        return cls(
            employee_id=db_row['employee_id'],
            year=db_row['year'],
            summary=db_row['summary']
        )

    @classmethod
    def find_by_id(cls, review_id):
        # Implementation to find a review by ID
        db_row = None  # Replace with actual db query
        if db_row is None:
            raise ValueError("No review found with the given ID")
        return cls.instance_from_db(db_row)

    def update(self):
        # Implementation to update the review in the database
        pass

    def delete(self):
        # Implementation to delete the review from the database
        pass

    @classmethod
    def get_all(cls):
        # Implementation to return all reviews
        pass

    # Other methods...


    

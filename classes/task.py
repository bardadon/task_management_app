
import sys
import datetime
sys.path.append('/projects/task_management')
from classes.system import System
from classes.comment import Comment
from classes.notification import Notification


class Task:

    # Create a system instance
    system = System()

    # General task status
    task_status = ['active', 'inactive', 'pending']

    # Create task constructor
    def __init__(self, project_id, title, description, due_date = datetime.datetime.today() + datetime.timedelta(days=365), start_date = datetime.datetime.today(), last_update_date = datetime.datetime.today() ) -> None:
        self._project_id = project_id
        self._title = title
        self._description = description
        self._status = Task.task_status[0]
        self._due_date = due_date
        self._start_date = start_date
        self._last_update_date = last_update_date

        # Grab the last id from the database and add 1 to it
        task_id = Task.system.grab_max_object_id(object='task') + 1
        
        # Insert user to db
        Task.system.insert_task(task_id, project_id, title, description, self.status, due_date, start_date, last_update_date)
        self._task_id = task_id   

        # Create an empty list for comments
        self.comments = []

        # Create an empty list for notifications
        self.notifications = []



    # get methods for Task
    @property
    def task_id(self):
        return self._task_id
    @property
    def project_id(self):
        return self._project_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def status(self):
        return self._status
    
    @property
    def due_date(self):
        return self._due_date
    
    @property
    def start_date(self):
        return self._start_date
        
    @property
    def last_update_date(self):
        return self._last_update_date
    
    # Set methods for Task
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            Task.system.update_task_attributes(self.project_id, self.task_id, new_title, self.description, self.status, self.due_date, self.start_date, self.last_update_date)
            self._title = new_title
        else:
            raise TypeError("Title must be a text!")
        
    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            Task.system.update_task_attributes(self.project_id, self.task_id, self.title, new_description, self.status, self.due_date, self.start_date, self.last_update_date)
            self._description = new_description
        else:
            raise TypeError("Description must be a text!")
        
    @status.setter
    def status(self, new_status):
        if isinstance(new_status, str):
            Task.system.update_task_attributes(self.project_id, self.task_id, self.title, self.description, new_status, self.due_date, self.start_date, self.last_update_date)
            self._status = new_status
        else:
            raise TypeError("Status must be a text!")
    
    @due_date.setter
    def due_date(self, new_due_date):
        if isinstance(new_due_date, datetime.datetime):
            Task.system.update_task_attributes(self.project_id, self.task_id, self.title, self.description, self.status, new_due_date, self.start_date, self.last_update_date)
            self._due_date = new_due_date
        else:
            raise TypeError("Due date must be a datetime!")
    
    @start_date.setter
    def start_date(self, new_start_date):
        if isinstance(new_start_date, datetime.datetime):
            Task.system.update_task_attributes(self.project_id, self.task_id, self.title, self.description, self.status, self.due_date, new_start_date, self.last_update_date)
            self._start_date = new_start_date
        else:
            raise TypeError("Start date must be a datetime!")

    @last_update_date.setter
    def last_update_date(self, new_last_update_date):
        if isinstance(new_last_update_date, datetime.datetime):
            Task.system.update_task_attributes(self.project_id, self.task_id, self.title, self.description, self.status, self.due_date, self.start_date, new_last_update_date)
            self._last_update_date = new_last_update_date
        else:
            raise TypeError("Last update date must be a datetime!")
        
    def create_comment(self, content):
        '''
        Create a task for the project
        Args:
            title: task title
            description: task description
            create_date: task create date (default: today)
            update_date: task update date (default: today)
            end_date: task end date (default: today + 365 days)
        Returns:
            Task object
        Notes:
            - This method will insert the task to the database.
            - Only Project class can create a task.
        '''
        self.comments.append(Comment(self.task_id, content, datetime.datetime.today(), datetime.datetime.today()))
        return self.comments[-1]
    
    # delete comment
    def delete_comment(self, comment_id):
        '''
        Delete a project from the user
        Args:
            project_title: project title
        Returns:
            None
        Notes:
            - This method will delete the project from the database
            - This method will delete the project from the User.projects list
        '''
        for comment in self.comments:
            if comment.comment_id == comment_id:
                self.comments.remove(comment)
                Task.system.delete_comment(comment_id)
                break

    def create_notification(self, notification_content):
        self.notifications.append(Notification(self.task_id, notification_content))
        return self.notifications[-1]


if __name__ == '__main__':
    #test_task = Task(project_id=1, title='test', description='test')
    #test_comment = test_task.create_comment(content='hello')
    pass
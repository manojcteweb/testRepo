```python
from datetime import datetime, timedelta
from collections import defaultdict

class DiaryManager:
    def __init__(self):
        self.tasks = {}
        self.notifications = defaultdict(list)
        self.audit_trail = []

    def set_reminder(self, task_id, user, date, urgency):
        self.tasks[task_id] = {'user': user, 'date': date, 'urgency': urgency, 'completed': False}
        self.audit_trail.append((task_id, 'created', datetime.now()))

    def send_notifications(self):
        for task_id, task in self.tasks.items():
            if not task['completed'] and task['date'] <= datetime.now() + timedelta(days=1):
                self.notifications[task['user']].append(f"Reminder for task {task_id} due on {task['date']}")
                self.notifications['investigator'].append(f"Reminder for task {task_id} due on {task['date']}")

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            self.audit_trail.append((task_id, 'completed', datetime.now()))

    def view_tasks(self, user=None, date=None, urgency=None):
        return [task_id for task_id, task in self.tasks.items()
                if (user is None or task['user'] == user) and
                   (date is None or task['date'] == date) and
                   (urgency is None or task['urgency'] == urgency)]

    def get_audit_trail(self):
        return self.audit_trail

# Example usage
diary_manager = DiaryManager()
diary_manager.set_reminder('task1', 'LSO', datetime(2023, 10, 15), 'high')
diary_manager.send_notifications()
diary_manager.mark_task_completed('task1')
tasks = diary_manager.view_tasks(user='LSO')
audit = diary_manager.get_audit_trail()
```
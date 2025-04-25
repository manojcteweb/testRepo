```python
class TimeTrackingIntegration:
    def __init__(self, project_management_system):
        self.pms = project_management_system
        self.integrated_tools = []

    def configure_integration(self, tool):
        if tool not in self.integrated_tools:
            self.integrated_tools.append(tool)
            self.pms.add_integration(tool)

    def import_time_data(self):
        for tool in self.integrated_tools:
            time_data = tool.get_time_data()
            self.pms.update_time_tracking(time_data)

    def sync_data(self):
        for tool in self.integrated_tools:
            time_data = tool.sync_time_data()
            self.pms.update_time_tracking(time_data)

class ProjectManagementSystem:
    def __init__(self):
        self.integrations = []

    def add_integration(self, tool):
        self.integrations.append(tool)

    def update_time_tracking(self, time_data):
        # Update the system with the new time data
        pass

# Example usage
pms = ProjectManagementSystem()
integration = TimeTrackingIntegration(pms)
integration.configure_integration(SomeTimeTrackingTool())
integration.import_time_data()
integration.sync_data()
```
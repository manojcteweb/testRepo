```python
class TimeTrackingIntegration:
    def __init__(self, project_management_system):
        self.pms = project_management_system
        self.integrated_tools = []

    def configure_integration(self, tools):
        self.integrated_tools = tools

    def import_time_data(self):
        for tool in self.integrated_tools:
            time_data = tool.fetch_time_data()
            self.pms.update_time_tracking(time_data)

    def sync_real_time(self):
        for tool in self.integrated_tools:
            tool.on_time_update(self.import_time_data)

class TimeTrackingTool:
    def fetch_time_data(self):
        # Implementation to fetch time data from the tool
        pass

    def on_time_update(self, callback):
        # Implementation to trigger callback on time data update
        pass

class ProjectManagementSystem:
    def update_time_tracking(self, time_data):
        # Implementation to update time tracking data in the system
        pass

# Example usage
pms = ProjectManagementSystem()
integration = TimeTrackingIntegration(pms)
tool1 = TimeTrackingTool()
tool2 = TimeTrackingTool()
integration.configure_integration([tool1, tool2])
integration.sync_real_time()
```
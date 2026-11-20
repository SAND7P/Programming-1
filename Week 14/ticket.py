from datetime import date

class Ticket:
    def _init_(self, ticket_id, employee_id, employee_name, issue_description):

        self.ticket_id = ticket_id
        self.submission_date = date.today()
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.issue_description = issue_description
        self.priority = self.assign_priority()
        self.resolution_message = ""

        if "password reset" in issue_description.lower():
            self.status = "Resolved"
            new_password = employee_id[:2] + employee_name[:2]
            self.resolution_message = "Password reset successfully. New password: " + new_password

        else:
            self.status = "In Progress"
            if self.priority == "High":
                self.resolution_message = "Pending Manager Approval"
            else:
                self.resolution_message = "Waiting for IT Support"


    def assign_priority(self):

        issue = self.issue_description.lower()
      


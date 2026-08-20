from datetime import datetime


class Reporter:

    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team


class Issue:

    def __init__(
        self,
        id,
        title,
        description,
        status,
        priority,
        reporter_id,
        created_at=None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = created_at or datetime.now()




reporter = Reporter(
    1,
    "Ashish",
    "ashish@example.com",
    "backend"
)

issue = Issue(
    101,
    "Login API failing",
    "Users are getting a 500 error.",
    "open",
    "high",
    reporter.id
)

print(reporter.name)
print(issue.title)
print(issue.reporter_id)
print(issue.created_at)
# Smart Leave

Author: James Riall

TODO(jriall): Write overview description of application.

## Prerequisites

TODO(jriall): Detail development prerequisites.

## Tech Stack

TODO(jriall): Detail tech stack.

## Getting started

### Creating the database

If a local SQLite database does not exist (`/backend/app.db`), you can create
one by entering an interactive python3 session and running the following
commands:

```python
>>> from app import db
>>> db.create_all()
```

Every time you update any of the models, run `python3 manage.py migrate` to
migrate the database to use the latest values.

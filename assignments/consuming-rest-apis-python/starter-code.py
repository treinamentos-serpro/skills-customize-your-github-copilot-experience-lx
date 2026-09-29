import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_todos():
    """Fetch and decode the todo list from the REST API."""
    request = Request(API_URL, headers={"Accept": "application/json"})

    # TODO: Open the request, read the response, and return decoded JSON.
    pass


def print_summary(todos):
    """Print counts and a short preview of the returned tasks."""
    # TODO: Count completed and pending tasks and print the first three titles.
    pass


def get_pending_tasks(todos, user_id):
    """Return pending tasks that belong to the selected user."""
    # TODO: Filter by both user_id and completed == False.
    pass


def main():
    try:
        todos = fetch_todos()
    except HTTPError as error:
        print(f"The API returned HTTP status {error.code}.")
        return
    except URLError as error:
        print(f"Could not connect to the API: {error.reason}")
        return

    print_summary(todos)

    try:
        user_id = int(input("\nEnter a user ID (1-10): "))
    except ValueError:
        print("Please enter a whole number.")
        return

    pending_tasks = get_pending_tasks(todos, user_id)
    print(f"\nPending tasks for user {user_id}:")

    if not pending_tasks:
        print("No pending tasks found.")
        return

    for todo in pending_tasks:
        print(f"- [{todo['id']}] {todo['title']}")


if __name__ == "__main__":
    main()
from typing import Dict, List


def filter_active_users(users: List[Dict[str, str | bool]]) -> List[str]:
    """Extract names of active users from a list of user profiles."""
    return [user["name"] for user in users if user.get("is_active")]


if __name__ == "__main__":
    user_data = [
        {"name": "Alice", "is_active": True},
        {"name": "Bob", "is_active": False},
        {"name": "Charlie", "is_active": True},
    ]

    active_users = filter_active_users(user_data)
    print("Active Users:", ", ".join(active_users))

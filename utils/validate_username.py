import re
from typing import Tuple


async def validate_username(username: str) -> bool:
    """
    Validates username according to the rules:
    - Length between 4 and 32 characters
    - Starts with a Latin letter
    - Contains only Latin letters (a-z), numbers (0-9) and underscores

    Returns:
    - Tuple[bool, str]: (is_valid, error_message)
    """

    # Check length
    if not 4 <= len(username) <= 32:
        return False

    # Check if starts with letter
    if not username[0].isalpha():
        return False

    # Check allowed characters
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
    if not re.match(pattern, username):
        return False

    return True

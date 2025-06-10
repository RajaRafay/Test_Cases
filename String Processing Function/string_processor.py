def format_name(first_name, last_name):
    """Format name to Title Case"""
    if not first_name or not last_name:
        return "Invalid name"
    return f"{first_name.strip().title()} {last_name.strip().title()}"

def count_words(text):
    """Count number of words in text"""
    if not text or text.strip() == "":
        return 0
    return len(text.strip().split())

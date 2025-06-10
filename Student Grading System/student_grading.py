
def get_grade(score):
    """Return letter grade based on numeric score"""
    if score >= 90:
        if score <=100:
            return 'A'
        else:
            return 'No grade above 100'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score < 0:
        return 'No grade below 0'
    else:
        return 'F'


# ============================================
# PERSON 2: Filter & Map — "Over 30" Logic
# ============================================

def get_filtered_users(users):
    """
    Filter users: age > 30 AND purchase_amount > 100
    Input:  list of dicts from Person 1
    Output: filtered list of dicts
    """
    filtered = list(
        filter(
            lambda user: int(user["Age"]) > 30 and float(user["Purchase_Amount"]) > 100,
            users
        )
    )
    return filtered


def get_filtered_emails(filtered_users):
    """
    Map filtered users to a list of their emails only.
    Input:  filtered list of dicts
    Output: list of email strings
    """
    emails = list(
        map(
            lambda user: user["Email"],
            filtered_users
        )
    )
    return emails
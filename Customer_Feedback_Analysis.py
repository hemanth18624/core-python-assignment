def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."

    positive_ratings = [rating for rating in ratings if rating >= 4]
    percentage = (len(positive_ratings) / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.2f}%"


ratings = [5, 4, 3, 5, 2, 4, 1, 5]


print(calculate_positive_feedback_percentage(ratings))

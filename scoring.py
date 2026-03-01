POINT_VALUES = {
    "FS9": 5, "FS10": 5, "FS11": 5, "FS12": 5,
    "FS13": 3, "FS14": 3, "FS15": 3, "FS16": 3,
    "FS17": 3, "FS18": 5, "FS19": 5, "FS20": 3,
    "FS21": 3, "FS22": 1, "FS23": 5, "FS24": 3,
    "FS25": 3, "FS26": 3, "FS27": 5, "FS28": 5,
    "FS29": 5, "FS30": 5, "FS31": 5, "FS32": 5,
    "FS33": 5,
}

def calculate_score(responses):
    total = sum(POINT_VALUES.values())
    achieved = 0

    for question, value in responses.items():
        if value == "Correct":
            achieved += POINT_VALUES.get(question, 0)

    percentage = round((achieved / total) * 100, 1)

    if percentage >= 90:
        result = "Excellent"
    elif percentage >= 85:
        result = "Acceptable"
    else:
        result = "Needs Improvement"

    return achieved, total, percentage, result

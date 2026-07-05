def generate_questions(
    company: str,
    role: str,
    difficulty: str,
):

    return [

        {
            "question":
            f"Explain your experience related to {role}.",
            "category":
            "Technical"
        },

        {
            "question":
            f"What challenges would you expect while working at {company}?",
            "category":
            "Behavioral"
        },

        {
            "question":
            "Explain REST API.",
            "category":
            "Technical"
        },

        {
            "question":
            "Explain OOP principles.",
            "category":
            "Technical"
        },

        {
            "question":
            "Difference between SQL and NoSQL.",
            "category":
            "Database"
        }

    ]
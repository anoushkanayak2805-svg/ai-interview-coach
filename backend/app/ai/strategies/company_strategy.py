COMPANY_STRATEGIES = {

    "Google": {
        "backend": 40,
        "dsa": 30,
        "behavioral": 20,
        "system_design": 10,
    },

    "Amazon": {
        "leadership": 40,
        "backend": 25,
        "behavioral": 20,
        "dsa": 15,
    },

    "Microsoft": {
        "backend": 35,
        "oop": 25,
        "cloud": 20,
        "behavioral": 20,
    },

    "Atlassian": {
        "backend": 35,
        "api_design": 25,
        "product_thinking": 20,
        "behavioral": 20,
    },

    "Default": {
        "technical": 50,
        "behavioral": 30,
        "projects": 20,
    },
}

def get_company_strategy(
    company: str,
):

    return COMPANY_STRATEGIES.get(
        company,
        COMPANY_STRATEGIES["Default"],
    )
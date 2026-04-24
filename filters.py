def get_linkedin_filter(date_filter):
    mapping = {
        "1h":  "r3600",
        "24h": "r86400",
        "3d":  "r259200",
        "7d":  "r604800",
        "any": None
    }
    return mapping.get(date_filter, None)


def get_adzuna_filter(date_filter):
    mapping = {
        "1h":  1,
        "24h": 1,
        "3d":  3,
        "7d":  7,
        "any": None
    }
    return mapping.get(date_filter, None)
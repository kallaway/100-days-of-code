# Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited":[
        "Paris", 
        "Lille", 
        "Dijon"
    ]
    },
    "Germany": {
        "cities_visited": [
        "Berlin", 
        "Hamburg", 
        "Stuttgart"
    ],
    "number_of_visits": 4
    },
}

# Nesting a dictionary in a list
travel_log = [
    {"country":
        "France", 
            "cities_visited":[
                "Paris", 
                "Lille", 
                "Dijon"
            ],
        "number_of_visits": 10},
    {"country":
        "Germany",
            "cities_visited": [
                "Berlin", 
                "Hamburg", 
                "Stuttgart"
    ],
        "number_of_visits": 4
    },
]
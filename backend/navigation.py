from fastapi import APIRouter

router = APIRouter()

@router.get("/navigate/{dress_name}")
def navigate(dress_name: str):

    location = {
        "Black Blazer": {
            "floor": 2,
            "section": "Formal Wear",
            "rack": "F-12"
        },
        "Blue Jeans": {
            "floor": 1,
            "section": "Casual Wear",
            "rack": "C-05"
        },
        "Party Suit": {
            "floor": 3,
            "section": "Party Wear",
            "rack": "P-18"
        }
    }

    return location.get(
        dress_name,
        {"message": "Dress not available"}
    )

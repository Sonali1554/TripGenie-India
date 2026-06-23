def get_packing_list(destination):

    packing = {

        "Kashmir": [
            "Warm Jacket",
            "Gloves",
            "Woolen Cap",
            "Power Bank",
            "Medicines"
        ],

        "Manali": [
            "Warm Clothes",
            "Trekking Shoes",
            "Sunglasses",
            "Power Bank",
            "Medicines"
        ],

        "Goa": [
            "Sunscreen",
            "Sunglasses",
            "Beachwear",
            "Flip Flops",
            "Water Bottle"
        ],

        "Kerala": [
            "Umbrella",
            "Light Cotton Clothes",
            "Sunscreen",
            "Water Bottle",
            "Medicines"
        ],

        "Jaipur": [
            "Cap",
            "Sunglasses",
            "Water Bottle",
            "Comfortable Shoes",
            "Sunscreen"
        ]
    }

    return packing.get(
        destination,
        [
            "Comfortable Clothes",
            "Power Bank",
            "Medicines",
            "Water Bottle"
        ]
    )
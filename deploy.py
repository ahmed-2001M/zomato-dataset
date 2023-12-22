import streamlit as st
import pandas as pd
import joblib


class RestaurantPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def preprocess_input(self, input_data):
        # Convert checkboxes to integers
        try:
            # Convert numeric columns to appropriate data types
            input_data["cost2people"] = input_data["cost2people"].astype(float)

        except Exception as e:
            print(e)

        return input_data

    def predict(self, input_data):
        # Apply preprocessing
        input_data = self.preprocess_input(input_data)

        # Make predictions using the loaded model
        prediction = self.model.predict(input_data)

        return prediction


def main():
    # Load your model
    model_path = r"./ensample_tree_model.h5"
    predictor = RestaurantPredictor(model_path)

    # Create a Streamlit app
    st.title("Restaurant Prediction App")

    # Input form for user to enter data
    online_order = st.selectbox("Onine Order", options=["Yes", "No"])
    book_table = st.selectbox("Book Table", options=["Yes", "No"])
    location = st.selectbox(
        "Location",
        options=[
            "Banashankari",
            "Basavanagudi",
            "others",
            "Jayanagar",
            "JP Nagar",
            "Bannerghatta Road",
            "BTM",
            "Bommanahalli",
            "Electronic City",
            "Wilson Garden",
            "Shanti Nagar",
            "Koramangala 5th Block",
            "Richmond Road",
            "HSR",
            "Koramangala 7th Block",
            "Bellandur",
            "Sarjapur Road",
            "Marathahalli",
            "Whitefield",
            "Old Airport Road",
            "Indiranagar",
            "Koramangala 1st Block",
            "Frazer Town",
            "MG Road",
            "Brigade Road",
            "Lavelle Road",
            "Church Street",
            "Ulsoor",
            "Residency Road",
            "Shivajinagar",
            "St. Marks Road",
            "Cunningham Road",
            "Commercial Street",
            "Vasanth Nagar",
            "Domlur",
            "Koramangala 8th Block",
            "Ejipura",
            "Jeevan Bhima Nagar",
            "Kammanahalli",
            "Koramangala 6th Block",
            "Brookefield",
            "Koramangala 3rd Block",
            "Koramangala 4th Block",
            "Banaswadi",
            "Kalyan Nagar",
            "Malleshwaram",
            "Rajajinagar",
            "New BEL Road",
        ],
    )
    rest_type = st.selectbox(
        "Rest Type",
        options=[
            "Casual Dining",
            "other",
            "Quick Bites",
            "Cafe",
            "Delivery",
            "Dessert Parlor",
            "Bakery",
            "Takeaway, Delivery",
            "Beverage Shop",
            "Bar",
            "Casual Dining, Bar",
            "Food Court",
        ],
    )
    cuisines = st.selectbox(
        "Cuisines",
        options=[
            "North Indian, Mughlai, Chinese",
            "other",
            "South Indian, North Indian",
            "North Indian",
            "Pizza, Cafe, Italian",
            "Cafe",
            "Cafe, Continental",
            "Cafe, Fast Food",
            "Cafe, Bakery",
            "Cafe, Fast Food, Beverages",
            "Cafe, Italian",
            "Bakery, Desserts",
            "Pizza",
            "North Indian, Biryani, Fast Food",
            "Biryani",
            "North Indian, Chinese, Fast Food",
            "Chinese, Thai, Momos",
            "North Indian, Mughlai, South Indian, Chinese",
            "South Indian",
            "Street Food, Fast Food",
            "Burger, Fast Food",
            "Pizza, Fast Food",
            "North Indian, Chinese",
            "Chinese, Thai",
            "Ice Cream, Desserts",
            "Biryani, Fast Food",
            "Fast Food, Burger",
            "Desserts, Beverages",
            "Chinese",
            "Bakery",
            "Burger, Fast Food, Beverages",
            "Fast Food, Rolls, Momos",
            "Biryani, South Indian",
            "Fast Food",
            "South Indian, Chinese, North Indian",
            "Beverages, Desserts, Ice Cream",
            "Mithai, Street Food",
            "Biryani, North Indian, Chinese",
            "Desserts",
            "Ice Cream",
            "South Indian, North Indian, Chinese",
            "Fast Food, Street Food",
            "South Indian, Biryani",
            "Chinese, North Indian",
            "South Indian, North Indian, Chinese, Street Food",
            "South Indian, North Indian, Chinese, Beverages",
            "Cafe, Beverages",
            "South Indian, Chinese",
            "Beverages, Ice Cream",
            "Italian, Pizza",
            "Street Food",
            "Italian",
            "Arabian",
            "North Indian, Chinese, BBQ",
            "Chinese, Fast Food",
            "North Indian, Chinese, Continental",
            "Desserts, Ice Cream",
            "Andhra",
            "North Indian, Street Food",
            "Pizza, Italian",
            "Mithai, Desserts",
            "South Indian, Beverages",
            "Fast Food, Rolls",
            "North Indian, Chinese, Rolls",
            "Beverages, Fast Food",
            "North Indian, Chinese, South Indian",
            "South Indian, Fast Food",
            "North Indian, Fast Food",
            "Fast Food, Chinese",
            "Juices, Fast Food",
            "Beverages, Desserts",
            "Biryani, Chinese, North Indian",
            "Andhra, North Indian, Chinese",
            "Beverages",
            "Rolls",
            "Mithai",
            "North Indian, Continental",
            "Tibetan, Momos",
            "Juices",
            "Tea, Beverages, Fast Food",
            "North Indian, South Indian",
            "Andhra, Biryani, North Indian, Chinese",
            "North Indian, Biryani",
            "Cafe, Continental, Beverages",
            "Finger Food",
            "Continental",
            "Fast Food, Beverages",
            "North Indian, Mughlai",
            "North Indian, Chinese, Mughlai",
            "North Indian, South Indian, Chinese, Continental",
            "North Indian, South Indian, Chinese",
            "North Indian, Continental, Chinese",
            "Cafe, Desserts",
            "Cafe, Continental, Italian",
            "Cafe, Healthy Food",
            "Andhra, North Indian, Biryani",
            "Biryani, North Indian",
            "Bengali, North Indian",
            "Chinese, Momos",
            "Andhra, Biryani",
            "Kerala, South Indian",
            "North Indian, Mughlai, Biryani",
            "Biryani, North Indian, Kebab",
            "Andhra, North Indian",
            "Biryani, Kebab",
            "Bengali",
            "North Indian, Chinese, Biryani",
            "Fast Food, North Indian",
            "Healthy Food",
            "Continental, American",
            "Chinese, North Indian, South Indian",
            "South Indian, Kerala",
            "Bakery, Desserts, Beverages",
            "South Indian, North Indian, Fast Food",
            "Street Food, North Indian",
            "Bakery, Fast Food",
            "Ice Cream, Beverages",
            "Fast Food, Juices",
            "Desserts, Bakery",
            "Continental, North Indian, Chinese",
            "Kerala",
            "Fast Food, Desserts",
            "Beverages, Juices",
            "North Indian, Fast Food, Street Food",
            "North Indian, Biryani, Chinese",
            "Street Food, Mithai",
            "Kerala, North Indian, Chinese",
            "North Indian, Chinese, Seafood",
            "Cafe, Continental, Burger",
            "Cafe, Continental, Italian, Burger",
            "Andhra, Chinese, North Indian",
            "Modern Indian",
            "Continental, North Indian",
            "Cafe, Italian, Burger, American, Steak",
            "Desserts, Cafe",
            "Biryani, Chinese",
            "Continental, Chinese",
            "Desserts, Fast Food",
            "Japanese",
            "American, Continental",
            "North Indian, Chinese, Arabian",
        ],
    )
    cost2people = st.number_input(
        "Cost for 2 People", min_value=0, max_value=10000, step=1
    )
    restaurant_type = st.selectbox(
        "Restaurant Type",
        options=[
            "Buffet",
            "Cafes",
            "Delivery",
            "Desserts",
            "Dine-out",
            "Drinks & nightlife",
            "Pubs and bars",
        ],
    )
    city = st.selectbox(
        "City",
        options=[
            "Banashankari",
            "Bannerghatta Road",
            "Basavanagudi",
            "Bellandur",
            "Brigade Road",
            "Brookefield",
            "BTM",
            "Church Street",
            "Electronic City",
            "Frazer Town",
            "HSR",
            "Indiranagar",
            "Jayanagar",
            "JP Nagar",
            "Kalyan Nagar",
            "Kammanahalli",
            "Koramangala 4th Block",
            "Koramangala 5th Block",
            "Koramangala 6th Block",
            "Koramangala 7th Block",
            "Lavelle Road",
            "Malleshwaram",
            "Marathahalli",
            "MG Road",
            "New BEL Road",
            "Old Airport Road",
            "Rajajinagar",
            "Residency Road",
            "Sarjapur Road",
            "Whitefield",
        ],
    )

    # Create a dictionary with user input
    user_input = {
        "online_order": online_order,
        "book_table": book_table,
        "location": location,
        "rest_type": rest_type,
        "cuisines": cuisines,
        "cost2people": cost2people,
        "type": restaurant_type,
        "city": city,
    }

    # Convert user input to a DataFrame
    input_df = pd.DataFrame([user_input])

    if st.button("Predict"):
        # Get prediction from the model
        st.write(input_df)

        prediction = predictor.predict(input_df)

        # Display the prediction
        st.write("Prediction:", prediction[0])


if __name__ == "__main__":
    main()




 #   Column                       Non-Null Count  Dtype 
---  ------                       --------------  ----- 
 0   url                          51717 non-null  object
 1   address                      51717 non-null  object
 2   name                         51717 non-null  object
 3   online_order                 51717 non-null  object
 4   book_table                   51717 non-null  object
 5   rate                         43942 non-null  object
 6   votes                        51717 non-null  int64 
 7   phone                        50509 non-null  object
 8   location                     51696 non-null  object
 9   rest_type                    51490 non-null  object
 10  dish_liked                   23639 non-null  object
 11  cuisines                     51672 non-null  object
 12  approx_cost(for two people)  51371 non-null  object
 13  reviews_list                 51717 non-null  object
 14  menu_item                    51717 non-null  object
 15  listed_in(type)              51717 non-null  object
 16  listed_in(city)              51717 non-null  object







## Columns have nulls
rate==>15.03 
phone==>2.34 
location==>0.04 
rest_type==>0.44 
dish_liked==>54.29 
cuisines==>0.09 
approx_cost(for two people)==>0.67 



## usles columns
- url
- address
- phone
- reviews_list
- menu_item
- dish_liked

## cleaning
- votes:
    - rows that have 0 values contain new or null value in rate
- listed_in(type):
    - renamed to type
- listed_in(city):
    - renamed to city
- 
- rate:
    - have ( NEW and - ) values should replaced with nan
    - should remove /5 from rate values
- location:
    - replace locations with value count lower than 1000 with other 
- rest_type:
    - reeplace rest types with value count lower than 1000 with other



## Feature Transformation
### Numerical Features
- votes:
    - have outliers | with range from 0 ---> 16832
- rate:
    - have range from 1.8  ---> 4.9
- cost2people:
    - have range from 40 ---> 6000
    
### Categorical Feaures
- online_order:
    - need encoding | have 2 unique values
- book_table:
    - need encoding | have 2 unique values
- type:
    - need encoding | have 7 unique values
- city:
    - need encoding | have 30 unique values
- name:
    - need encoding | have 8792 unique values
- loacation:
    - need encoding | have 48 unique values
- res_type:
    - need encoding | have 12 unique values
- cuisines:
    - need encoding | have 141 unique values






location :
['Banashankari',
 'Basavanagudi',
 'others',
 'Jayanagar',
 'JP Nagar',
 'Bannerghatta Road',
 'BTM',
 'Bommanahalli',
 'Electronic City',
 'Wilson Garden',
 'Shanti Nagar',
 'Koramangala 5th Block',
 'Richmond Road',
 'HSR',
 'Koramangala 7th Block',
 'Bellandur',
 'Sarjapur Road',
 'Marathahalli',
 'Whitefield',
 'Old Airport Road',
 'Indiranagar',
 'Koramangala 1st Block',
 'Frazer Town',
 'MG Road',
 'Brigade Road',
 'Lavelle Road',
 'Church Street',
 'Ulsoor',
 'Residency Road',
 'Shivajinagar',
 'St. Marks Road',
 'Cunningham Road',
 'Commercial Street',
 'Vasanth Nagar',
 'Domlur',
 'Koramangala 8th Block',
 'Ejipura',
 'Jeevan Bhima Nagar',
 'Kammanahalli',
 'Koramangala 6th Block',
 'Brookefield',
 'Koramangala 3rd Block',
 'Koramangala 4th Block',
 'Banaswadi',
 'Kalyan Nagar',
 'Malleshwaram',
 'Rajajinagar',
 'New BEL Road']





rest_type :

['Casual Dining',
 'other',
 'Quick Bites',
 'Cafe',
 'Delivery',
 'Dessert Parlor',
 'Bakery',
 'Takeaway, Delivery',
 'Beverage Shop',
 'Bar',
 'Casual Dining, Bar',
 'Food Court']



cuisines :

['North Indian, Mughlai, Chinese',
 'other',
 'South Indian, North Indian',
 'North Indian',
 'Pizza, Cafe, Italian',
 'Cafe',
 'Cafe, Continental',
 'Cafe, Fast Food',
 'Cafe, Bakery',
 'Cafe, Fast Food, Beverages',
 'Cafe, Italian',
 'Bakery, Desserts',
 'Pizza',
 'North Indian, Biryani, Fast Food',
 'Biryani',
 'North Indian, Chinese, Fast Food',
 'Chinese, Thai, Momos',
 'North Indian, Mughlai, South Indian, Chinese',
 'South Indian',
 'Street Food, Fast Food',
 'Burger, Fast Food',
 'Pizza, Fast Food',
 'North Indian, Chinese',
 'Chinese, Thai',
 'Ice Cream, Desserts',
 'Biryani, Fast Food',
 'Fast Food, Burger',
 'Desserts, Beverages',
 'Chinese',
 'Bakery',
 'Burger, Fast Food, Beverages',
 'Fast Food, Rolls, Momos',
 'Biryani, South Indian',
 'Fast Food',
 'South Indian, Chinese, North Indian',
 'Beverages, Desserts, Ice Cream',
 'Mithai, Street Food',
 'Biryani, North Indian, Chinese',
 'Desserts',
 'Ice Cream',
 'South Indian, North Indian, Chinese',
 'Fast Food, Street Food',
 'South Indian, Biryani',
 'Chinese, North Indian',
 'South Indian, North Indian, Chinese, Street Food',
 'South Indian, North Indian, Chinese, Beverages',
 'Cafe, Beverages',
 'South Indian, Chinese',
 'Beverages, Ice Cream',
 'Italian, Pizza',
 'Street Food',
 'Italian',
 'Arabian',
 'North Indian, Chinese, BBQ',
 'Chinese, Fast Food',
 'North Indian, Chinese, Continental',
 'Desserts, Ice Cream',
 'Andhra',
 'North Indian, Street Food',
 'Pizza, Italian',
 'Mithai, Desserts',
 'South Indian, Beverages',
 'Fast Food, Rolls',
 'North Indian, Chinese, Rolls',
 'Beverages, Fast Food',
 'North Indian, Chinese, South Indian',
 'South Indian, Fast Food',
 'North Indian, Fast Food',
 'Fast Food, Chinese',
 'Juices, Fast Food',
 'Beverages, Desserts',
 'Biryani, Chinese, North Indian',
 'Andhra, North Indian, Chinese',
 'Beverages',
 'Rolls',
 'Mithai',
 'North Indian, Continental',
 'Tibetan, Momos',
 'Juices',
 'Tea, Beverages, Fast Food',
 'North Indian, South Indian',
 'Andhra, Biryani, North Indian, Chinese',
 'North Indian, Biryani',
 'Cafe, Continental, Beverages',
 'Finger Food',
 'Continental',
 'Fast Food, Beverages',
 'North Indian, Mughlai',
 'North Indian, Chinese, Mughlai',
 'North Indian, South Indian, Chinese, Continental',
 'North Indian, South Indian, Chinese',
 'North Indian, Continental, Chinese',
 'Cafe, Desserts',
 'Cafe, Continental, Italian',
 'Cafe, Healthy Food',
 'Andhra, North Indian, Biryani',
 'Biryani, North Indian',
 'Bengali, North Indian',
 'Chinese, Momos',
 'Andhra, Biryani',
 'Kerala, South Indian',
 'North Indian, Mughlai, Biryani',
 'Biryani, North Indian, Kebab',
 'Andhra, North Indian',
 'Biryani, Kebab',
 'Bengali',
 'North Indian, Chinese, Biryani',
 'Fast Food, North Indian',
 'Healthy Food',
 'Continental, American',
 'Chinese, North Indian, South Indian',
 'South Indian, Kerala',
 'Bakery, Desserts, Beverages',
 'South Indian, North Indian, Fast Food',
 'Street Food, North Indian',
 'Bakery, Fast Food',
 'Ice Cream, Beverages',
 'Fast Food, Juices',
 'Desserts, Bakery',
 'Continental, North Indian, Chinese',
 'Kerala',
 'Fast Food, Desserts',
 'Beverages, Juices',
 'North Indian, Fast Food, Street Food',
 'North Indian, Biryani, Chinese',
 'Street Food, Mithai',
 'Kerala, North Indian, Chinese',
 'North Indian, Chinese, Seafood',
 'Cafe, Continental, Burger',
 'Cafe, Continental, Italian, Burger',
 'Andhra, Chinese, North Indian',
 'Modern Indian',
 'Continental, North Indian',
 'Cafe, Italian, Burger, American, Steak',
 'Desserts, Cafe',
 'Biryani, Chinese',
 'Continental, Chinese',
 'Desserts, Fast Food',
 'Japanese',
 'American, Continental',
 'North Indian, Chinese, Arabian']
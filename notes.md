

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

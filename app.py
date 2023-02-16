import streamlit as st

# Define the product data
product_data = [
    {"name": "Product 1", "image": "https://m.media-amazon.com/images/I/71tHbGjt8iL._AC_SY355_.jpg", "price": 9.99},
    {"name": "Product 2", "image": "https://m.media-amazon.com/images/I/71tHbGjt8iL._AC_SY355_.jpg", "price": 19.99},
    {"name": "Product 3", "image": "https://m.media-amazon.com/images/I/71tHbGjt8iL._AC_SY355_.jpg", "price": 29.99},
]

# Define the layout of the app
st.set_page_config(page_title="Product Catalogue", page_icon=":moneybag:")

st.title("Product Catalogue")

# Display each product in a row of 3 columns
for i in range(0, len(product_data), 3):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(product_data[i]["image"])
        st.write(product_data[i]["name"])
        st.write("$" + str(product_data[i]["price"]))
    with col2:
        if i+1 < len(product_data):
            st.image(product_data[i+1]["image"])
            st.write(product_data[i+1]["name"])
            st.write("$" + str(product_data[i+1]["price"]))
    with col3:
        if i+2 < len(product_data):
            st.image(product_data[i+2]["image"])
            st.write(product_data[i+2]["name"])
            st.write("$" + str(product_data[i+2]["price"]))

import streamlit as st
import math

# ----- Logic functions -----
def task1_logic(number):
    return math.factorial(number)

def task2_logic(numbers_str):
    items = [int(x) for x in numbers_str.split() if x.strip() != ""]
    seen = set()
    out = []
    for v in items:
        if v not in seen:
            out.append(v)
            seen.add(v)
    return out

def task3_logic(radius):
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return diameter, circumference, area


# ----- Streamlit UI -----
st.title("Multi-Task App 🚀")

task = st.selectbox("Choose a task:", ["Factorial", "Remove Duplicates", "Circle Properties"])

if task == "Factorial":
    n = st.number_input("Enter a non-negative integer:", min_value=0, step=1, value=5)
    if st.button("Compute Factorial"):
        try:
            result = task1_logic(n)
            st.success(f"Factorial of {n} = {result}")
        except OverflowError:
            st.error("Number too large for factorial.")

elif task == "Remove Duplicates":
    numbers_str = st.text_area("Enter numbers (space-separated):", "1 2 2 3 4 4 5")
    if st.button("Remove Duplicates"):
        try:
            result = task2_logic(numbers_str)
            st.success(f"List without duplicates: {result}")
        except ValueError:
            st.error("Please enter valid integers separated by spaces.")

elif task == "Circle Properties":
    r = st.number_input("Enter radius:", min_value=0.0, step=0.1, value=5.0)
    if st.button("Compute Properties"):
        d, c, a = task3_logic(r)
        st.write(f"**Diameter:** {d}")
        st.write(f"**Circumference:** {c}")
        st.write(f"**Area:** {a}")


import streamlit as st

def main():
    st.title("Simple Calculator App")

    # Get user input
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Perform calculation
    operation = st.radio("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])
    result = calculate(num1, num2, operation)

    # Display the result
    st.write(f"Result: {result}")

def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            st.error("Division by zero is not allowed.")
            return None

if __name__ == "__main__":
    main()

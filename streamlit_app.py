from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit as st

def sum_numbers(num1, num2):
    return num1 + num2

def main():
    st.title("Calculadora de Soma")
    
    num1 = st.number_input("Digite o primeiro número:")
    num2 = st.number_input("Digite o segundo número:")
    
    result = sum_numbers(num1, num2)
    
    st.write(f"A soma de {num1} e {num2} é igual a {result}")

if __name__ == "__main__":
    main()


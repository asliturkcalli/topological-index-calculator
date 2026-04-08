import streamlit as st

# --- SEO & PAGE CONFIG ---
st.set_page_config(
    page_title="Topological Index Calculator | Fibonacci & Lucas Cubes",
    page_icon="🧬",
    layout="centered"
)

# --- MATHEMATICAL FUNCTIONS ---
def get_fib(n):
    if n < 0: return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_indices(n):
    # Pre-calculating necessary Fibonacci numbers
    fn = get_fib(n)
    fn_minus_1 = get_fib(n-1)
    fn_plus_1 = get_fib(n+1)
    f2n_plus_1 = get_fib(2*n + 1)
    f2n_plus_2 = get_fib(2*n + 2)
    
    # 1. Fibonacci Wiener Index
    w_fib = (1/25) * (4*(n+1)*(fn**2) + (9*n+2)*fn*fn_plus_1 + 6*n*(fn_plus_1**2))
    
    # 2. Fibonacci Mostar Index
    mo_fib = (1/25) * ((3*n-2)*f2n_plus_2 + n*f2n_plus_1 + (3*n+2)*((-1)**n))
    
    # 3. Lucas Wiener Index (n >= 1)
    w_lucas = n * fn_minus_1 * fn_plus_1 if n >= 1 else 0
    
    # 4. Lucas Mostar Index (n >= 2)
    mo_lucas = n * fn * fn_minus_1 if n >= 2 else 0
    
    return w_fib, mo_fib, w_lucas, mo_lucas

# --- USER INTERFACE ---
st.title("🧪 Topological Index Calculator")
st.subheader("Analysis of Fibonacci and Lucas Cubes")
st.markdown(f"**Author:** [Aslıtürk Çallı]")
st.write("---")

# SEO Friendly Description
st.markdown("""
This tool calculates the **Wiener Index** and **Mostar Index** for partial cubes, 
specifically focusing on **Fibonacci Cubes** ($\Gamma_n$) and **Lucas Cubes** ($L_n$). 
It is designed for researchers in **Discrete Mathematics**, **Graph Theory**, and **Chemical Graph Theory**.
""")

# Input Section
n_input = st.number_input("Enter the cube dimension (n):", min_value=0, max_value=40, value=2)

if st.button("Calculate Indices"):
    w_f, mo_f, w_l, mo_l = calculate_indices(n_input)
    
    # Results for Fibonacci Cubes
    st.markdown(f"### 🟦 Fibonacci Cubes ($\Gamma_{n_input}$)")
    col1, col2 = st.columns(2)
    col1.metric("Wiener Index (W)", f"{w_f:.2f}")
    col2.metric("Mostar Index (Mo)", f"{mo_f:.2f}")
    
    # Results for Lucas Cubes
    st.markdown(f"### 🟥 Lucas Cubes ($L_{n_input}$)")
    if n_input < 1:
        st.warning("Lucas indices are defined for n ≥ 1 (Wiener) and n ≥ 2 (Mostar).")
    else:
        col3, col4 = st.columns(2)
        col3.metric("Wiener Index (W)", f"{w_l:.2f}")
        if n_input >= 2:
            col4.metric("Mostar Index (Mo)", f"{mo_l:.2f}")
        else:
            col4.write("Mostar: n ≥ 2 required")

st.write("---")
# Academic References for Authority
st.markdown("""
**References & Methodology:**
* **Fibonacci Cubes:** Calculations based on *'Fibonacci Cubes with Applications and Variations'* (Klavžar, S.).
* **Indices:** Formulas for Wiener and Mostar indices in partial graphs.
* **SEO Keywords:** Discrete Math, Graph Theory Calculator, Topological Indices, Wiener Index Formula.
""")

# Footer for Ownership
st.caption(f"© 2024 [Your Name]. All rights reserved. Developed for academic purposes.")
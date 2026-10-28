
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="LCG Calculator",
    page_icon="🎰",
    layout="centered"
)

# Custom white theme and button styling
st.markdown("""
<style>
    /* White page background */
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stHeader"] {
        background-color: #FFFFFF;
        color: #000000;
    }

    /* Black text */
    h1, h2, h3, h4, p, label,
    [data-testid="stMarkdownContainer"] {
        color: #000000;
    }

    /* Input fields */
    input, textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CCCCCC !important;
    }

    /* Primary Generate button */
    .stButton > button[kind="primary"] {
        background-color: #af6de9 !important;
        color: #FFFFFF !important;
        border: 1px solid #6C63FF !important;
        border-radius: 6px;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #5548D9 !important;
        color: #FFFFFF !important;
        border-color: #5548D9 !important;
    }

    /* Table background */
    [data-testid="stDataFrame"] {
        background-color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)


# Application title
st.title("Linear Congruential Generator (LCG)")

st.write(
    "Generate a sequence of pseudo-random numbers "
    "using the Linear Congruential Generator formula."
)

# LCG formula
st.latex(r"X_{n+1} = (aX_n + c) \bmod m")


# Input section
st.subheader("Enter inputs")

col1, col2 = st.columns(2)

with col1:
    multiplier = st.number_input(
        "Multiplier (a)",
        min_value=0,
        value=5,
        step=1
    )

    seed = st.number_input(
        "Seed (X₀)",
        min_value=0,
        value=7,
        step=1
    )

with col2:
    increment = st.number_input(
        "Increment (c)",
        min_value=0,
        value=3,
        step=1
    )

    modulus = st.number_input(
        "Modulus (m)",
        min_value=2,
        value=16,
        step=1
    )


# Generate button
if st.button("Generate", type="primary"):

    # Validate seed
    if seed >= modulus:
        st.error(
            "Seed must be smaller than the modulus. "
            "Choose X₀ such that 0 ≤ X₀ < m."
        )

    else:
        a = int(multiplier)
        c = int(increment)
        x0 = int(seed)
        m = int(modulus)

        # Generate the first 8 values
        count = 8
        x = x0
        rows = []

        for n in range(1, count + 1):
            previous = x
            x = (a * x + c) % m

            rows.append({
                "Step": n,
                "Previous value": previous,
                "Calculation": (
                    f"({a} × {previous} + {c}) mod {m}"
                ),
                "New value": x
            })

        # Display sequence
        st.subheader("Output")
        st.write("First 8 generated values:")

        sequence = [row["New value"] for row in rows]
        st.code(", ".join(map(str, sequence)))

        # Display calculation table
        st.subheader("Step-by-step calculation")

        st.dataframe(
            pd.DataFrame(rows),
            width="stretch",
            hide_index=True
        )

        # Analyze the complete cycle independently
        x_cycle = x0
        seen_cycle = {}
        cycle_states = []

        while x_cycle not in seen_cycle:
            seen_cycle[x_cycle] = len(cycle_states)
            cycle_states.append(x_cycle)
            x_cycle = (a * x_cycle + c) % m

        cycle_start = seen_cycle[x_cycle]
        period = len(cycle_states) - cycle_start

        full_period = (
            cycle_start == 0 and period == m
        )

else:
    st.info(
        "Enter the four parameters and click 'Generate' to see the sequence and calculations."
    )

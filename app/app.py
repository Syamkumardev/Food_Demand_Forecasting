import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Food Demand Forecasting1",
    page_icon="🍽️",
    layout="wide"
)

model = joblib.load("models/food_demand_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

df = pd.read_csv("data/Food demand.csv")

center_options = sorted(df["center_id"].unique())
meal_options = sorted(df["meal_id"].unique())


st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

html, body, [class*="css"] {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 38px 42px;
    border-radius: 22px;
    margin-bottom: 35px;
    box-shadow: 0 8px 30px rgba(102, 126, 234, 0.25);
}

.hero h1 {
    font-size: 40px;
    font-weight: 800;
    color: white;
    margin: 0 0 10px 0;
    line-height: 1.2;
}

.hero p {
    color: #eee9ff;
    font-size: 16px;
    font-weight: 400;
    margin: 0;
    line-height: 1.6;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 20px;
    line-height: 1.3;
}

label {
    font-size: 14px !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

div[data-testid="stNumberInput"] > div {
    border-radius: 10px;
}

div[data-baseweb="select"] input {
    font-size: 15px;
}

div[data-testid="stNumberInput"] input {
    font-size: 15px;
}

div.stButton > button {
    height: 54px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 700;
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border: none;
    box-shadow: 0 5px 18px rgba(102, 126, 234, 0.30);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.40);
}

.result-card {
    background: linear-gradient(145deg, #1b2030, #151925);
    border: 1px solid #343b52;
    border-radius: 16px;
    padding: 24px;
    min-height: 125px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.18);
}

.result-label {
    color: #aab2c2;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 10px;
}

.result-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: 750;
    line-height: 1.2;
}

.info-card {
    background: linear-gradient(145deg, #1b2030, #151925);
    border: 1px solid #343b52;
    border-radius: 16px;
    padding: 20px;
    min-height: 95px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.18);
}

.info-label {
    color: #aab2c2;
    font-size: 14px;
    font-weight: 600;
}

.info-value {
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    margin-top: 8px;
    line-height: 1.3;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
    font-size: 14px;
}

.stCaption {
    color: #8f98aa;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>🍽️ Food Demand Forecasting</h1>
    <p>
        Predict food demand and estimate potential surplus or shortage
        using machine learning.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="section-title">📋 Enter Details</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    center_id = st.selectbox(
        "Center ID",
        center_options,
        index=center_options.index(99) if 99 in center_options else 0
    )

    meal_id = st.selectbox(
        "Meal ID",
        meal_options,
        index=meal_options.index(2290) if 2290 in meal_options else 0
    )

    week = st.number_input(
        "Week",
        min_value=1,
        max_value=145,
        value=120,
        step=1
    )

    checkout_price = st.number_input(
        "Checkout Price",
        min_value=0.0,
        value=300.0,
        step=1.0
    )


with col2:

    base_price = st.number_input(
        "Base Price",
        min_value=0.0,
        value=320.0,
        step=1.0
    )

    emailer_for_promotion = st.selectbox(
        "Email Promotion",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    homepage_featured = st.selectbox(
        "Homepage Featured",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    planned_quantity = st.number_input(
        "Planned Food Quantity",
        min_value=0,
        value=250,
        step=1
    )


st.write("")


if st.button(
    "🔮 Predict Food Demand",
    use_container_width=True
):

    week_sin = np.sin(2 * np.pi * week / 145)
    week_cos = np.cos(2 * np.pi * week / 145)


    input_data = pd.DataFrame({
        "week": [week],
        "center_id": [center_id],
        "meal_id": [meal_id],
        "checkout_price": [checkout_price],
        "base_price": [base_price],
        "emailer_for_promotion": [emailer_for_promotion],
        "homepage_featured": [homepage_featured],
        "week_sin": [week_sin],
        "week_cos": [week_cos]
    })


    input_encoded = preprocessor.transform(input_data)


    predicted_demand = max(
        0,
        model.predict(input_encoded)[0]
    )


    surplus = planned_quantity - predicted_demand


    st.markdown(
        '<div class="section-title">📊 Prediction Results</div>',
        unsafe_allow_html=True
    )


    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">📈 Predicted Demand</div>
            <div class="result-value">
                {predicted_demand:.0f} meals
            </div>
        </div>
        """, unsafe_allow_html=True)


    with result_col2:

        if surplus >= 0:
            label = "🟢 Potential Surplus"
            value = f"{surplus:.0f} meals"
        else:
            label = "🔴 Potential Shortage"
            value = f"{abs(surplus):.0f} meals"


        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">{label}</div>
            <div class="result-value">
                {value}
            </div>
        </div>
        """, unsafe_allow_html=True)


    with result_col3:

        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">🍱 Planned Quantity</div>
            <div class="result-value">
                {planned_quantity} meals
            </div>
        </div>
        """, unsafe_allow_html=True)


    st.write("")


    if surplus > 0:

        st.success(
            f"Potential surplus of approximately "
            f"{surplus:.0f} meals. "
            "Consider reviewing the preparation quantity or evaluating "
            "feasible redistribution options."
        )

    elif surplus < 0:

        st.warning(
            f"Potential shortage of approximately "
            f"{abs(surplus):.0f} meals. "
            "Consider increasing the planned preparation quantity."
        )

    else:

        st.info(
            "Planned quantity closely matches the predicted demand."
        )


    st.markdown(
        '<div class="section-title">'
        '📊 Predicted Demand vs Planned Quantity'
        '</div>',
        unsafe_allow_html=True
    )


    chart_data = pd.DataFrame({
        "Category": [
            "Planned Quantity",
            "Predicted Demand"
        ],
        "Meals": [
            planned_quantity,
            predicted_demand
        ]
    })


    st.bar_chart(
        chart_data,
        x="Category",
        y="Meals",
        height=400
    )


    st.markdown(
        '<div class="section-title">'
        '📈 Historical Demand Trend'
        '</div>',
        unsafe_allow_html=True
    )


    historical_data = df[
        (df["center_id"] == center_id) &
        (df["meal_id"] == meal_id)
    ]


    if not historical_data.empty:

        weekly_demand = (
            historical_data
            .groupby("week")["num_orders"]
            .mean()
            .reset_index()
            .sort_values("week")
        )


        st.line_chart(
            weekly_demand,
            x="week",
            y="num_orders",
            height=400
        )


        st.caption(
            f"Historical average demand for Center {center_id} "
            f"and Meal {meal_id}. "
            f"Showing {len(weekly_demand)} available weeks."
        )


    else:

        st.info(
            "No historical demand data is available for the selected "
            "center and meal combination."
        )


    st.markdown(
        '<div class="section-title">'
        '🤖 Model Information'
        '</div>',
        unsafe_allow_html=True
    )


    model_col1, model_col2, model_col3 = st.columns(3)


    with model_col1:

        st.markdown("""
        <div class="info-card">
            <div class="info-label">🤖 Model</div>
            <div class="info-value">
                Gradient Boosting
            </div>
        </div>
        """, unsafe_allow_html=True)


    with model_col2:

        st.markdown("""
        <div class="info-card">
            <div class="info-label">🎯 R² Score</div>
            <div class="info-value">
                0.6074
            </div>
        </div>
        """, unsafe_allow_html=True)


    with model_col3:

        st.markdown("""
        <div class="info-card">
            <div class="info-label">📉 RMSE</div>
            <div class="info-value">
                191.36
            </div>
        </div>
        """, unsafe_allow_html=True)


    st.caption(
        "Gradient Boosting was selected as the best-performing model "
        "among the evaluated baseline models based on R² and RMSE."
    )
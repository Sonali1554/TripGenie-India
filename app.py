import streamlit as st

from agents.planner_agent import create_trip_plan
from agents.budget_agent import estimate_budget
from rag.chatbot import ask_question
from utils.pdf_generator import generate_trip_pdf

st.set_page_config(
    page_title="TripGenie AI",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ TripGenie AI")
st.subheader("Agentic AI Travel Assistant")

tab1, tab2, tab3 = st.tabs(
    [
        "✈️ Trip Planner",
        "💬 Travel Chat",
        "💰 Budget Analyzer"
    ]
)

# ==================================================
# TAB 1 : TRIP PLANNER
# ==================================================

with tab1:

    st.header("Generate AI Travel Itinerary")

    destination = st.text_input(
        "Destination",
        placeholder="Goa"
    )

    days = st.number_input(
        "Number of Days",
        min_value=1,
        max_value=30,
        value=4
    )

    budget = st.number_input(
        "Budget (₹)",
        min_value=1000,
        value=25000
    )

    if st.button("Generate Trip Plan"):

        if destination.strip() == "":
            st.warning("Please enter a destination.")
        else:

            with st.spinner("Planning your trip..."):

                plan = create_trip_plan(
                    destination,
                    days,
                    budget
                )

                budget_data = estimate_budget(
                    days,
                    budget
                )

                pdf_path = generate_trip_pdf(
                    destination,
                    days,
                    budget,
                    plan,
                    budget_data
                )

            st.success("Trip Generated Successfully!")

            st.header("🗺️ Itinerary")

            st.markdown(plan)

            st.header("💰 Budget Breakdown")

            st.json(budget_data)

            st.header("📄 Download Report")

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📥 Download Travel Report",
                    data=pdf_file,
                    file_name="Trip_Report.pdf",
                    mime="application/pdf"
                )

# ==================================================
# TAB 2 : RAG TRAVEL CHATBOT
# ==================================================

with tab2:

    st.header("Travel Knowledge Assistant")

    question = st.text_input(
        "Ask a travel-related question"
    )

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")
        else:

            with st.spinner("Searching travel knowledge base..."):

                answer = ask_question(question)

            st.success("Answer Generated")

            st.write(answer)

# ==================================================
# TAB 3 : BUDGET ANALYZER
# ==================================================

with tab3:

    st.header("Trip Budget Analyzer")

    budget_input = st.number_input(
        "Enter Budget",
        min_value=1000,
        value=25000,
        key="budget_tab"
    )

    days_input = st.number_input(
        "Trip Days",
        min_value=1,
        max_value=30,
        value=4,
        key="days_tab"
    )

    if st.button("Analyze Budget"):

        result = estimate_budget(
            days_input,
            budget_input
        )

        st.success("Budget Analysis Complete")

        st.json(result)

        st.metric(
            "Hotel Budget",
            f"₹{result['hotel']}"
        )

        st.metric(
            "Food Budget",
            f"₹{result['food']}"
        )

        st.metric(
            "Transport Budget",
            f"₹{result['transport']}"
        )

        st.metric(
            "Activities Budget",
            f"₹{result['activities']}"
        )
import os
import time
import streamlit as st

from supervisor.intelligent_supervisor import run_tripgenie
from utils.pdf_generator import generate_trip_pdf

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="TripGenie India",
    page_icon="🇮🇳",
    layout="wide"
)

# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.title("🇮🇳 TripGenie")

    st.markdown("""
### ✨ Features

✅ AI Trip Planner

✅ Research Agent

✅ Weather Agent

✅ Hotel Agent

✅ Budget Agent

✅ Packing Agent

✅ PDF Travel Report

✅ Multi-Agent Architecture
""")

    st.markdown("---")

    st.info(
        "Plan trips across India with AI-powered recommendations."
    )

# ==================================
# HEADER
# ==================================

st.title("🇮🇳 TripGenie India")
st.subheader("AI Powered Travel Concierge")

query = st.text_area(
    "Describe your trip",
    placeholder="Plan a family trip to Kerala for 5 days under ₹50,000",
    height=120
)

# ==================================
# GENERATE BUTTON
# ==================================

if st.button("🚀 Generate Complete Trip"):

    if not query.strip():

        st.warning(
            "Please enter your trip request."
        )

    else:

        start_time = time.time()

        with st.spinner("Planning your trip..."):

            result = run_tripgenie(query)

            if result.get("clarification"):

                st.warning(
                    "Please provide: " +
                    ", ".join(result["missing"])
                )

                st.stop()

            pdf_path = generate_trip_pdf(result)

        total_time = round(
            time.time() - start_time,
            2
        )

        profile = result.get("profile", {})
        hotel = result.get("hotel", {})
        budget_data = result.get("budget", {})
        packing = result.get("packing", [])

        # ==================================
        # TIME TAKEN
        # ==================================

        st.success(
            f"⏱ Trip generated in {total_time} seconds"
        )

        # ==================================
        # PROFILE
        # ==================================

        st.divider()
        st.header("👤 Travel Profile")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "📍 Destination",
                profile.get("destination", "N/A")
            )

        with c2:
            st.metric(
                "📅 Days",
                profile.get("days", "N/A")
            )

        with c3:
            st.metric(
                "💰 Budget",
                f"₹{profile.get('budget', 0):,}"
            )

        with c4:
            st.metric(
                "👤 Travel Type",
                profile.get(
                    "travel_type",
                    "General"
                )
            )

        # ==================================
        # DESTINATION IMAGE
        # ==================================

        destination = profile.get(
            "destination",
            ""
        )

        image_path = f"assets/{destination}.png"

        if os.path.exists(image_path):

            st.image(
                image_path,
                use_container_width=True
            )

        # ==================================
        # TRIP SUMMARY
        # ==================================

        st.info(
            f"""
🌍 Destination: {profile.get('destination', 'N/A')}

📅 Duration: {profile.get('days', 'N/A')} Days

💰 Budget: ₹{profile.get('budget', 0):,}

👤 Travel Type: {profile.get('travel_type', 'General')}
"""
        )

        # ==================================
        # RESEARCH
        # ==================================

        st.divider()
        st.header("🔍 Destination Insights")

        with st.expander(
            "View Destination Research",
            expanded=False
        ):

            st.markdown(
                result.get(
                    "research",
                    "No research available."
                )
            )

        # ==================================
        # WEATHER
        # ==================================

        st.divider()
        st.header("🌦 Weather")

        st.success(
            result.get(
                "weather",
                "Weather unavailable"
            )
        )

        # ==================================
        # HOTEL
        # ==================================

        st.divider()
        st.header("🏨 Hotel Recommendation")

        h1, h2 = st.columns(2)

        with h1:

            st.metric(
                "Category",
                hotel.get(
                    "category",
                    "N/A"
                )
            )

        with h2:

            st.metric(
                "Recommendation",
                hotel.get(
                    "recommendation",
                    "N/A"
                )
            )

        # ==================================
        # PACKING CHECKLIST
        # ==================================

        st.divider()
        st.header("🎒 Packing Checklist")

        for item in packing:

            st.write(f"✅ {item}")

        # ==================================
        # BUDGET
        # ==================================

        st.divider()
        st.header("💰 Budget Breakdown")

        b1, b2, b3, b4 = st.columns(4)

        with b1:

            st.metric(
                "🏨 Hotel",
                f"₹{budget_data.get('hotel', 0):,}"
            )

        with b2:

            st.metric(
                "🍽 Food",
                f"₹{budget_data.get('food', 0):,}"
            )

        with b3:

            st.metric(
                "🚕 Transport",
                f"₹{budget_data.get('transport', 0):,}"
            )

        with b4:

            st.metric(
                "🎯 Activities",
                f"₹{budget_data.get('activities', 0):,}"
            )

        # ==================================
        # ITINERARY
        # ==================================

        st.divider()
        st.header("🗺 Personalized Itinerary")

        with st.expander(
            "View Complete Itinerary",
            expanded=True
        ):

            st.markdown(
                result.get(
                    "itinerary",
                    "No itinerary generated."
                )
            )

        # ==================================
        # PDF DOWNLOAD
        # ==================================

        st.divider()

        if os.path.exists(pdf_path):

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="📄 Download Trip Report",
                    data=pdf_file,
                    file_name="Trip_Report.pdf",
                    mime="application/pdf"
                )
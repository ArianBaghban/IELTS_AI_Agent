import re
def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group()
    return text



import streamlit as st
import json
from engine import analyze_essay

st.set_page_config(
    page_title="IELTS AI Assistant",
    layout="wide"
)

st.title("🎯 IELTS Writing Task 2 AI Analyzer")

essay = st.text_area(
    "Paste your Writing Task 2 Essay (Max 320 words)",
    height=250
)

if st.button("Analyze Essay"):

    if not essay.strip():
        st.warning("Please enter an essay first.")

    else:

        with st.spinner("Analyzing essay..."):
            result = analyze_essay(essay)

        try:

            clean_result = extract_json(result)
            data = json.loads(clean_result)

            st.subheader("📊 IELTS Scores")

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric(
                    "Task Response",
                    data["task_response"]["score"]
                )

            with col2:
                st.metric(
                    "Coherence",
                    data["coherence_cohesion"]["score"]
                )

            with col3:
                st.metric(
                    "Lexical",
                    data["lexical_resource"]["score"]
                )

            with col4:
                st.metric(
                    "Grammar",
                    data["grammar_accuracy"]["score"]
                )

            with col5:
                st.metric(
                    "Overall",
                    data["overall_band"]
                )

            st.divider()

            st.subheader("❌ Errors")
            st.json(data["errors"])

            st.divider()

            st.subheader("💡 Recommendations")
            st.write(data["recommendations"])

            st.divider()

            st.subheader("✍️ Improved Essay")
            st.write(data["improved_essay"])

            st.divider()

            st.subheader("📘 Band 8 Sample Essay")
            st.write(data["sample_band_8_essay"])

        except Exception as e:

            st.error("Failed to parse AI response")

            st.subheader("Raw Response")
            st.write(result)

            st.write(e)
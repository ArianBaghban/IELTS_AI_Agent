import streamlit as st

# ---------------------------
# Page Config
# ---------------------------

st.set_page_config(
    page_title="IELTS AI Agent",
    page_icon="🎯"
)

# ---------------------------
# Functions
# ---------------------------

def count_words(text):
    return len(text.split())


def calculate_band_score(word_count, paragraph_count):
    score = 5.0

    if word_count >= 250:
        score += 1

    if paragraph_count >= 4:
        score += 1

    return score


# ---------------------------
# UI
# ---------------------------

st.title("🎯 IELTS AI Agent")

st.write(
    "Paste your IELTS Writing Task 2 essay below and click Analyze."
)

essay = st.text_area(
    "Your Essay",
    height=300,
    placeholder="Write or paste your IELTS essay here..."
)

# ---------------------------
# Analysis
# ---------------------------

if st.button("Analyze Essay"):

    if essay.strip() == "":
        st.warning("Please enter your essay first.")

    else:

        # Word Count
        word_count = count_words(essay)

        # Paragraph Count
        paragraphs = [p for p in essay.split("\n\n") if p.strip()]
        paragraph_count = len(paragraphs)

        # Score
        score = calculate_band_score(
            word_count,
            paragraph_count
        )

        # IELTS Criteria (Temporary)
        task_response = score
        coherence = score
        lexical = score
        grammar = score

        # Statistics
        st.subheader("📈 Essay Statistics")

        st.write(f"Word Count: {word_count}")
        st.write(f"Paragraph Count: {paragraph_count}")

        if word_count < 250:
            st.error(
                "Essay is below the IELTS recommended minimum of 250 words."
            )
        else:
            st.success(
                "Essay meets the minimum word requirement."
            )

        if paragraph_count < 4:
            st.warning(
                "Essay may need a clearer IELTS structure (usually 4+ paragraphs)."
            )
        else:
            st.success(
                "Essay structure looks reasonable."
            )

        # IELTS Scores
        st.subheader("📊 IELTS Band Breakdown")

        st.write(f"Overall Band: {score}")
        st.write(f"Task Response: {task_response}")
        st.write(f"Coherence & Cohesion: {coherence}")
        st.write(f"Lexical Resource: {lexical}")
        st.write(f"Grammatical Range & Accuracy: {grammar}")

        # Feedback
        strengths = []
        weaknesses = []

        if word_count >= 250:
            strengths.append("Good essay length")
        else:
            weaknesses.append("Essay is too short")

        if paragraph_count >= 4:
            strengths.append("Reasonable paragraph structure")
        else:
            weaknesses.append("Essay structure needs improvement")

        # Strengths
        st.subheader("✅ Strengths")

        for item in strengths:
            st.write("- " + item)

        # Weaknesses
        st.subheader("⚠️ Weaknesses")

        for item in weaknesses:
            st.write("- " + item)

        # Improvement Plan
        st.subheader("🚀 Improvement Plan")

        if word_count < 250:
            st.write("- Write essays with at least 250 words.")

        if paragraph_count < 4:
            st.write(
                "- Use Introduction, Body Paragraph 1, Body Paragraph 2 and Conclusion."
            )

        st.write("- Practice complex sentence structures.")
        st.write("- Expand your academic vocabulary.")
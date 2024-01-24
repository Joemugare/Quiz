import streamlit as st
import pandas as pd

# Load Jeopardy dataset
file_path = "jeopardy.csv"  # Update with the correct path to your CSV file
df = pd.read_csv(file_path)

# Print DataFrame for verification
print("DataFrame:", df)

# Strip whitespaces in column names
df.columns = df.columns.str.strip()

# Define quiz logic with a unique key for st.text_input
def display_question(question, question_index):
    answer = st.text_input("Your Answer for Question {}".format(question_index), key="answer_{}_{}".format(question['Category'], question_index))
    if st.button("Submit", key="submit_{}_{}".format(question['Category'], question_index)):
        if answer.lower() == question['Answer'].lower():
            st.success("Correct!")
        else:
            st.error("Incorrect. The correct answer is: {}".format(question['Answer']))

# Create Streamlit UI
def main():
    st.title("Jeopardy Quiz")

    for index, question in df.iterrows():
        st.header("Question for Category {}".format(question['Category']))

        # Modify this section based on the columns available in your dataset
        st.subheader("Round: {}".format(question.get('Round', 'N/A')))
        st.write("Value: ${}".format(question.get('Value', 'N/A')))
        st.write("Question: {}".format(question.get('Question', 'N/A')))

        display_question(question, index + 1)

if __name__ == "__main__":
    main()

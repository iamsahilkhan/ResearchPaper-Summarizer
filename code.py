import openai
from openai import ChatCompletion
from metaphor_python import Metaphor
from datetime import datetime, timedelta

# Set up API keys
openai.api_key = ""
metaphor_api_key = ""

# Define the timeframe mapping
timeframe_mapping = {
    "Within 1 Month": 1,
    "Within 3 Months": 3,
    "Within 6 Months": 6,
    "Within 9 Months": 9,
    "Within a Year": 12,
}

# Define the user's question and metaphor query
meta_query = (
    "Act as a helpful assistant that specializes in conducting extensive research based on a topic and generate "
    "search queries based on user questions. Only generate one search query."
)

# Define the user's question and metaphor query for research topic
def generate_openai_query(topic, timeframe_months):
    return f"List out all the recent research papers on {topic} within {timeframe_months} months."

def display_paper_list_with_indexes(paper_urls, paper_titles):
    if len(paper_urls) != len(paper_titles):
        print("Mismatch between paper URLs and titles.")
        return

    print("List of Research Papers:")
    for i, (url, title) in enumerate(zip(paper_urls, paper_titles), start=1):
        print(f"{i}. {title}")
        print(f"   URL: {url}")
        print()

def display_paper_summary(paper_title, paper_summary):
    print(f"Summary for '{paper_title}':")
    print(paper_summary)
    print()

def get_paper_summary(paper_index, paper_urls):
    if paper_index < 1 or paper_index > len(paper_urls):
        print("Invalid paper index. Please provide a valid index.")
        return

    paper_url = paper_urls[paper_index - 1]
    meta_summ = f"You are a helpful assistant that summarizes the content of a webpage. Summarize the paper at this URL: {paper_url}"

    try:
        # Generate a summary for the selected paper
        completion = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": meta_summ},
                {"role": "user", "content": "Summarize the paper."},
            ],
        )
        summary = completion.choices[0].message.content
        print(f"\nSummary for Paper {paper_index}: {summary}")
    except Exception as e:
        print("An error occurred during the summarization:", str(e))

try:
    # Get user input for topic and timeframe
    user_topic = input("Enter the topic for research papers: ")
    user_timeframe_input = input("Enter the timeframe (e.g., 'Within 1 Month'): ")
    timeframe_months = timeframe_mapping.get(user_timeframe_input, None)

    if timeframe_months is None:
        print("Invalid timeframe input. Please provide a valid timeframe.")
        exit()

    # Generate the openai_query based on user input
    openai_query = generate_openai_query(user_topic, timeframe_months)

    # Generate a search query based on the user's question
    completion = ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": meta_query},
            {"role": "user", "content": openai_query},
        ],
    )
    query = completion.choices[0].message.content

    # Search for recent research papers on the given topic and timeframe
    start_published_date = (datetime.now() - timedelta(days=timeframe_months * 30)).strftime("%Y-%m-%d")
    metaphor = Metaphor(api_key= "")
    search_response = metaphor.search(query, use_autoprompt=True)

    # Obtain the paper URLs and titles
    paper_urls = [result.url for result in search_response.results]
    paper_titles = [result.title for result in search_response.results]

    # Display the list of papers with titles, URLs, and indexes
    display_paper_list_with_indexes(paper_urls, paper_titles)

    # Ask the user for a paper index to summarize
    while True:
        paper_index_input = input("Enter the index of the paper to summarize (or 'exit' to quit): ")
        if paper_index_input.lower() == 'exit':
            break

        try:
            paper_index = int(paper_index_input)
            if 1 <= paper_index <= len(paper_urls):
                paper_title = paper_titles[paper_index - 1]
                get_paper_summary(paper_index, paper_urls)
            else:
                print("Invalid index. Please enter a valid index or 'exit' to quit.")
        except ValueError:
            print("Invalid input. Please enter a valid index or 'exit' to quit.")

except Exception as e:
    print("An error occurred during the search or summarization:", str(e))

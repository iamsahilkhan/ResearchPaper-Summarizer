## Overview
The project is a research assistance tool that helps users find recent research papers on a specified topic within a given timeframe. It utilizes OpenAI's GPT-3.5 Turbo for generating search queries and summarizing research papers, and the Metaphor API for conducting the actual research paper search. The tool aims to streamline the process of research paper discovery and provide users with concise summaries of the papers they are interested in.

## Project Flow
1. User Input: The user provides input regarding the research topic and the desired timeframe for recent research papers (e.g., "Artificial Intelligence," "Within 3 Months").
2. OpenAI GPT-3.5 Turbo: Generating Search Query: The user input is used to generate a search query using GPT-3.5 Turbo. The system message provides context and instructions for the model.
3. Metaphor API: Research Paper Search: The generated search query is sent to the Metaphor API, which searches for recent research papers based on the query and timeframe.
4. Displaying Research Papers: The tool displays the list of research papers found, including titles and URLs, allowing the user to choose a paper of interest.
5. User Selection and Summarization: The user selects a specific research paper by providing its index. The tool uses GPT-3.5 Turbo to generate a summary for the selected research paper.








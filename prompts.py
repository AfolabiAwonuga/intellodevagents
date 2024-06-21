# Agent Prompts
question_agent_system_prompt = """
You are an expert in the field of {FIELD}, you have extensive knowledge and experience in examining candidates in {FIELD}, 
your task is to generate multiple-choice questions(MCQ) including three distractor choices and one correct choice that answers the question, 
the questions should test a users fundamental knowledge in {FIELD}.

Follow the guidelines below to generate the MCQ: {GUIDLINES}

Few shot examples: {FEWSHOT}

Example session: {SESSION}
""".strip()


critique_agent_system_prompt = """
As a critical thinker and expert in {FIELD}, 
evaluate the given multiple-choice question (MCQ) "{MCQ}" using these guidelines {GUIDLINES}:

Use the session state tool to:
1. Ensure the MCQ is not a duplicate.
2. Ensure a wide range of topics are covered.

If the MCQ does not follow the guidelines, you should output "REJECTED" and return your reason for the rejection.
If the MCQ follows the guidelines, you should output "ACCEPTED" and return the MCQ

Few shot examples: {FEWSHOT}

Example session: {SESSION}
"""


modelling_agent_system_prompt = """
You are an expert at extracting information from text and you have extensive knowledge about {FIELD}.
For the given multiple-choice question (MCQ) "{MCQ}", your task is to do the following:

1. Extract the topic which the MCQ covers, do not guess, if you are not sure, use the internet search tool available to you.
2. Use your extensive knowledge in the {FIELD} to extract the difficulty level of the MCQ.

Few shot examples: {FEWSHOT}

Example session: {SESSION}
"""


solution_agent_system_prompt = """
You are a problem solver, the best in {FIELD}, you love to teach and can break things down to a level anyone can understand.
Your task is to solve MCQ problems given to you, teach your solution, and engage in an educational conversation about the problem.

Your first action should be:
1. Solve the problem {MCQ}, choose an answer from the available choices in the MCQ.
2. Return the answer.
2. Call the eval tool(evaluates a test-takers solution against yours) available to you - then return PAUSE.
3. Wait for Observation - Observation will be the result of calling the eval tool.

If you are called again based on the observation, Use the following "REACT" framework to provide a response:
1. Reason step: You use this step to describe your thoughts about the problem, your solution, and how you arrived at it.
2. Action step: Output your response from the reason step - then return PAUSE.
3. Observation step: Observation might be follow up questions, 
   be ready to engage in an educational conversation utilising your teaching skills and the tools available to you.

Few shot examples: {FEWSHOT}

Example session: {SESSION}
"""


# Propmt Variables
guidlines = """
1. Ensure Clarity and Precision:
    - Write questions that are clear, concise, and unambiguous.
    - Avoid using complex language or jargon unless it is essential to the topic.

2. Focus on Key Concepts and Fundamentals:
    - Create questions that test foundational knowledge rather than obscure details.
    - Ensure that questions require application of principles, not just rote memorisation.

3. Use Real-World Scenarios:
    - Incorporate practical examples and scenarios to test the application of knowledge.
    - Ensure scenarios are relevant to the field and encourage critical thinking.

3. Balance Difficulty Levels:
    - Include a range of questions from basic to advanced difficulty.

4. Avoid Ambiguity and Trick Questions:
    - Ensure that questions have one clear, correct answer.
    - Avoid phrasing that could mislead or confuse test-takers.

5. Provide Adequate Answer Options:
    - For multiple-choice questions, include plausible distractors (incorrect answers).
    - Ensure that all answer options are reasonable and that there is a clear best choice.

6. Cover a wide range of Topics

7. The questions should test specific facts and concepts.
""".strip()

question_agent_fewshot = """
----------------------------------------------------------------
EXAMPLE 1: FIELD - Machine Learning and Artificial Intelligence

MCQ 1:
What is the primary goal of supervised learning in machine learning?

a) To find patterns in data without labeled outcomes
b) To generate new data from a given dataset
c) To predict the output based on given input-output pairs
d) To reduce the dimensionality of the dataset

MCQ 2:
Which algorithm is commonly used for classification problems?

a) K-means clustering
b) Linear regression
c) Decision trees
d) Principal Component Analysis (PCA)

MCQ 3:
In the context of neural networks, what is the function of the activation layer?

a) To initialize the weights
b) To introduce non-linearity into the model
c) To combine multiple models into one
d) To normalize the input data

MCQ 4:
A company wants to categorize customer reviews as positive, neutral, or negative. 
Which type of machine learning problem does this scenario describe?

a) Regression
b) Clustering
c) Classification
d) Reinforcement learning

MCQ 5:
Which of the following best describes the concept of overfitting in machine learning?

a) When the model performs well on the training data but poorly on new, unseen data
b) When the model performs well on both training and test data
c) When the model fails to find patterns in the training data
d) When the model uses too many computational resources
----------------------------------------------------------------

----------------------------------------------------------------
EXAMPLE 2: FIELD - Front End Development

MCQ 1:
What is the primary purpose of HTML in web development?

a) To define the structure and content of a webpage
b) To style the webpage with colors and fonts
c) To add interactive features to a webpage
d) To store data on the server

MCQ 2:
Which CSS property is used to change the background color of an element?

a) color
b) font-size
c) background-color
d) border

MCQ 3:
What does the DOM stand for in JavaScript?

a) Data Object Model
b) Document Object Model
c) Digital Object Management
d) Dynamic Object Module

MCQ 4:
A developer needs to make an HTML element disappear when a button is clicked. Which JavaScript method is commonly used to accomplish this?

a) document.getElementById().remove()
b) document.querySelector().hide()
c) document.getElementById().style.display = 'none'
d) document.querySelector().delete()

MCQ 5:
Which of the following best describes the concept of overfitting in machine learning?

a) When the model performs well on the training data but poorly on new, unseen data
b) When the model performs well on both training and test data
c) When the model fails to find patterns in the training data
d) When the model uses too many computational resources
----------------------------------------------------------------

----------------------------------------------------------------
EXAMPLE 3: FIELD - Back End Development

MCQ 1:
What is the primary role of a backend server in web development?

a) To design the user interface of a website
b) To manage and store data, and handle business logic
c) To optimize the website for search engines
d) To provide styling for web pages

MCQ 2:
Which type of database is known for storing data in tables and using SQL for querying?

a) NoSQL database
b) Graph database
c) Relational database
d) Key-Value store

MCQ 3:
A company needs to ensure that only authenticated users can access certain parts of their web application. 
Which backend concept is used to manage this?

a) API management
b) User authentication and authorization
c) Database indexing
d) Caching


MCQ 4:
What does REST stand for in the context of web services?

a) Representational State Transfer
b) Random Execution of Server Transactions
c) Real-time Execution and Storage Transfer
d) Reliable Server Technology
----------------------------------------------------------------
""".strip()


question_agent_example_session = """
"""


critique_agent_fewshot = """
----------------------------------------------------------------
Given MCQ: What is the main purpose of a convolutional layer in a neural network?

a) To add non-linearity to the model
b) To perform dimensionality reduction
c) To detect and extract features from input images
d) To normalize the input data

Evaluation = {
    "status": "ACCEPTED",
    "reason": "The question is clear and focuses on a key concept in neural networks. It uses practical application (convolutional layer), has an appropriate difficulty level, and includes plausible distractors."
} 
----------------------------------------------------------------

----------------------------------------------------------------
Given MCQ: Which algorithm is used to find the shortest path in a graph?

a) Bubble Sort
b) Dijkstra's Algorithm
c) K-Nearest Neighbors
d) Decision Tree

Evaluation = {
    "status": "ACCEPTED",
    "reason": "The question is clear and tests a fundamental algorithm concept. It has real-world application, appropriate difficulty, and plausible distractors."
} 
----------------------------------------------------------------

----------------------------------------------------------------
Given MCQ:
What is the main function of a machine learning model?

a) To calculate the exact outcome of every possible input
b) To model the relationship between input data and output predictions
c) To store large amounts of data
d) To visualize data effectively

Evaluation = {
    "status": "REJECTED",
    "reason": "The question is too broad and not specific enough to test a particular concept. The distractors are not all plausible."
} 
----------------------------------------------------------------

----------------------------------------------------------------
Given MCQ:
Which of the following is not a machine learning algorithm?

a) Linear Regression
b) Support Vector Machine
c) Decision Tree
d) JavaScript

Evaluation = {
    "status": "REJECTED",
    "reason": "The distractor "JavaScript" is too obvious and not a plausible answer, making the question too easy and not challenging enough."
} 
----------------------------------------------------------------

----------------------------------------------------------------
Given MCQ:
What is the main advantage of using a very deep neural network?

a) They are easier to train
b) They require less data
c) They can learn very complex patterns in data
d) They are always more accurate than shallow networks

Evaluation = {
    "status": "REJECTED",
    "reason": "The distractor "They are always more accurate than shallow networks" is misleading as it is not always true, adding ambiguity to the question."
} 
"""



























































































































"""
STEM:
OPTIONS:
SOLUTION: 
TAG:

- solve mcq
- call eval tool 
- observation - correct >  END
- observation - incorrect / ask > REACT

Review and Revise:

Review questions for accuracy, clarity, and relevance.
Revise based on feedback from peers or trial runs with a sample audience.

You may be called again (decision node if user input true, if Next -> end) to provide more information on why you chose the answer you chose,
engage in conversation to explain why you chose the answer
and provide useful resources using the tools available to you"""
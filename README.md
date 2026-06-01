https://github.com/elliemsprice-coder/proj6-recipe
## RECIPE RECOMMENDER
User enters ingredients and AI returns suggested recipes and saves favorites 

## TECH STACK
Backend
Flask 3.x

Python 3.10+

MongoDB 6 (running in Docker)

HuggingFace Inference API (text generation)

Frontend
Vanilla JavaScript

HTML/CSS

No external JS libraries required

Infrastructure
Docker (Docker Desktop)

Docker Compose 3.9

## HOW TO RUN

clone the repository 

Update credentials.ini in the project root

open project folder and start the app using docker compose up --build
in your browser, visit http://localhost:3000


## ASSIGNMENT QUESTIONS
The cool part about this project, I think, is what it does.  This project is useful in many ways for indidividuals as it comples a task needed by everyone- the practicality of this projectis what made me decide on it. 

I used the Huggingface chat completions. The backend sent prompts such as sys:“Generate 3 recipes in valid JSON only. No explanations. Format must include title, description, ingredients, and instructions.” user:“User ingredients: chicken, rice, broccoli” and the model endpoint was https://api.openai.com/v1/chat/completions. The job of AI is this porject was to take the infredients and return a structures JSON object containing three recipe options. 

In working on this project I learned how to structure and send prompts to an AI model, store generated data in a database and how to work with API keys and debug API errors.  

A major challenge was that Docker on my local machine couldn’t resolve DNS, so the backend couldn’t reach any cloud AI endpoints.

## AUTHOR
Elizabeth Price
elliemsprice@gmail.com
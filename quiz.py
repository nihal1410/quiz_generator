import openai

def generate_quiz(subject, difficulty):
    api_key = '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'
    openai.api_key = api_key
    prompt = f"Generate {difficulty} difficulty level quiz questions on {subject}."

    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.5
    )

    generated_content = response['choices'][0]['message']['content']
    return generated_content

subject = "Physics"
difficulty = "medium"
quiz = generate_quiz(subject, difficulty)
print(quiz)




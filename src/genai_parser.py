import openai

def parse_tournament_data(content):
    openai.api_key = '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'

    prompt = f"Extract Tournament Name, Level, Start Date, End Date, Official URL, Streaming Links, Image URL, and Summary from this content: {content}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(response['choices'][0]['message']['content'])

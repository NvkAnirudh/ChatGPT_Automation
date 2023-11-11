import sys
import os
from openai import OpenAI
client = OpenAI()

# Gets summary from the Gpt3.5-Turbo model used by OpenAI
def get_summary(file_path):
    t_file = open(new_file_path, 'r')
    content = t_file.read()
    # Appropriate prompt to the model
    content = content + "\n" + "\n" + "Please summarize the above text in simple points"

    # Calling the model for the response
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": content}
    ]
    )

    t_file.close()
    # Returning the response along with the total tokens used for tracking the cost
    return completion.choices[0].message.content, completion.usage.total_tokens

if __name__ == "__main__":
    # Checking the length of arguments passed
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <new_file_path>")
        sys.exit(1)

    new_file_path = sys.argv[1]
    print(f"Processing new file: {new_file_path}")

    response, total_tokens = get_summary(new_file_path)
    response = str(response)

    # OpenAI's Pricing: $0.001 /1K tokens for input and $0.002 /1K tokens for output
    input_cost = 0.001
    output_cost = 0.002

    input_cost_incurred = (total_tokens / 1000) * input_cost
    output_cost_incurred = (total_tokens / 1000) * output_cost

    total_cost = input_cost_incurred + output_cost_incurred

    print("Total cost incurred for GPT3.5-Turbo: {total_cost}")

    # Output folder named Summaries
    output_dir = 'path/to/output/summary/folder'
    output_path = new_file_path.split("/")[-1][:-4] +'_summary' + '.txt'

    if not os.path.exists(output_dir):
        # If it doesn't exist, create the folder
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, output_path), 'w') as file:
        file.write(response)

    print("Summary successfully written to {output_path}")

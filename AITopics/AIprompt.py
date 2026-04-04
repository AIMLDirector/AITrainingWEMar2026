from promptvalidation import prompt_validation, prompt_cleanup


def generate_response(prompt):
    try:
        # Validate the prompt
        prompt_validation(prompt)
        
        # Clean up the prompt
        cleaned_prompt = prompt_cleanup(prompt)
        
        # Simulate generating a response (for demonstration purposes)
        response = f"Response to: {cleaned_prompt}"
        
        return response
    except ValueError as e:
        return str(e)


prompt_input = input("Enter your prompt: ")
response = generate_response(prompt_input)
print(response)
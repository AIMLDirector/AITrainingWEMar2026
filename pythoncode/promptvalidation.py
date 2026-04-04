import re
def prompt_validation(prompt):
    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string.")
    if len(prompt) == 0:
        raise ValueError("Prompt cannot be empty.")
    if len(prompt) > 1000:
        raise ValueError("Prompt is too long. Maximum length is 1000 characters.")
    return True


def prompt_cleanup(prompt):
      masked_prompt = prompt.replace("password", "******")
      masked_bank_account = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '***-**-****', masked_prompt)  # Mask SSN pattern
      return masked_bank_account
      

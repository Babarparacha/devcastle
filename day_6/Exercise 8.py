# 1. Define our custom error (just two simple lines)
class EmptyTextError(Exception):
    pass

# 2. A simple AI function that expects some text
def ai_translate(text):
    if text == "":
        # Trigger our custom error if the user sends a blank message
        raise EmptyTextError("The AI cannot translate empty text!")
    else:
        print("Translating your text:", text)

# 3. Safely testing the AI with an empty string
try:
    ai_translate("")  # We are passing empty text here
except EmptyTextError as error:
    print("AI Alert caught:", error)



    
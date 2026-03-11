# Global variable
message = "I am a Global variable"

def test_scope():
    # Local variable (only exists inside this function)
    message = "I am a Local variable"
    print("Inside the function:", message)

test_scope()
print("Outside the function:", message)


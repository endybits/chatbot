from app.main import virtual_assistant


# Tests that the virtual assistant returns a dictionary
def test_returns_dict():
    response = virtual_assistant()
    assert isinstance(response, dict)


# Tests that the virtual assistant returns a dictionary with the correct key-value pair
def test_returns_correct_kv_pair():
    response = virtual_assistant()
    assert "Hi" in response


# Tests that the virtual assistant returns a dictionary with a string value
def test_returns_string_value():
    response = virtual_assistant()
    assert isinstance(response["Hi"], str)


# Tests that the virtual assistant returns a dictionary with a 'Hi' key that has the value 'Hello, I'm a Chatbot. What can I do for you?'
def test_returns_hi_key_with_correct_value():
    response = virtual_assistant()
    assert response["Hi"] == "Hello, I'm a Chatbot. What can I do for you? "

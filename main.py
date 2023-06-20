import openai
import gradio

openai.api_key = "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"
#You are an expert Python developer and more programming languages with years of experience writing Python code and teaching Python to other programmers
messages = [{"role": "system", "content": """you are a professional programmer at Customttkinter in python and need you to just give me a code like that code only for """}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    user_input = ' '
    x=str(ChatGPT_reply)
    start_index = x.find('```')  # Find the first occurrence of ```
    end_index = x.find('```', start_index + 1)  # Find the next occurrence of ``` after start_index
    
    if start_index != -1 and end_index != -1:
        extracted_string = x[start_index + 1:end_index]
        print(x)
        x = extracted_string
        
        file = open("output.py", "w")
        # Write the string to the file
        string_to_write = x
        file.write(string_to_write)

        # Close the file
        file.close()
        
    else:
        x = "#sorry try again"
    
    return x


demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "ALPHABOT")

demo.launch(share=True)
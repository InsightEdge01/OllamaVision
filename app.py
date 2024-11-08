#pip install ollama
import ollama

response = ollama.chat(
    model='llama3.2-vision:11b',
    messages=[{
        'role': 'user',
        'content': 'Which day has the highest temperature',
        'images': ['linechart.jpg']
    }]
)

print(response)
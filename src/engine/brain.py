# 2026/03/20

import requests


DRAFT_URL = "http://localhost:8081/completion"
MAIN_URL = "http://localhost:8080/completion"


def get_response(url, prompt, max_tokens=128, temp=0.7):
    try:
        payload = {
            "prompt": prompt,
            "n_predict": max_tokens,
            "temperature": temp,
            "stream": False
        }
        response = requests.post(url, json=payload, timeout=60)

        return response.json()["content"].strip()

    except Exception as e:
        return f"Error connect to model: {e}"


def spud_brain(user_input):
    router_prompt = f"<|im_start|>system\nClassify the user's request. \nREPLY 'complex' IF: the user asks for code, scripts, long stories, math, or deep analysis.\nREPLY 'simple' IF: the user says hello, asks a short factual question, or wants a joke.\nRespond ONLY with one word: 'simple' or 'complex'.<|im_end|>\n<|im_start|>user\n{user_input}<|im_end|>\n<|im_start|>assistant\n<think>Decided!</think>\n"
    complexity = get_response(DRAFT_URL, router_prompt, max_tokens=10, temp=0.0)
    is_simple = ("simple" in complexity.lower())
    
    if is_simple:
        print("Using turbo mode")
        prompt = f"<|im_start|>system\nYou are Spud-Turbo, a high-speed efficiency expert. Give a brief, direct answer in 2 sentences or less. No fluff.<|im_end|>\n<|im_start|>user\n{user_input}<|im_end|>\n<|im_start|>assistant\n<think>Such a simple task requires minimal thinking...\n"

        return get_response(DRAFT_URL, prompt, max_tokens=150, temp=0.3)
    else:
        print("Using Thoughful mode")
        prompt = f"<|im_start|>system\nYou are Spud-DeepThought, a highly intelligent reasoning engine. Break down the problem, consider edge cases, and provide a comprehensive, accurate solution. Use your internal monologue to verify your logic.<|im_end|>\n<|im_start|>user\n{user_input}<|im_end|>\n<|im_start|>assistant\n<think>\n"
        
        return get_response(MAIN_URL, prompt, max_tokens=1024, temp=0.6)


def chat():
    print("You are now chatting to The SpudBrain!\n")

    while True:
        query = input("\nUser: ")

        if query.lower() in ['/exit', '/quit', '/kill']:    break

        print(f"Assistant: {spud_brain(query)}")


if __name__ == '__main__':
    main()

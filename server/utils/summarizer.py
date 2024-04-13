from langchain_community.llms import CTransformers

def getLLAmaSummary(input_text, max_length=1000):
    try:
        # Initialize the LLM model
        llm = CTransformers(
            model="./model/llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            config_type={"max_new_tokens": 256, "temperature": 0.01},
        )

        # If input_text is longer than max_length, split it into parts
        if len(input_text) > max_length:
            parts = [input_text[i:i+max_length] for i in range(0, len(input_text), max_length)]
            summaries = []
            for i, part in enumerate(parts):
                part_prompt = f"This is part {i+1} of the input text. {part}"
                response = llm(part_prompt)
                summary = response['text']
                summaries.append(summary)
            return "\n".join(summaries)
        else:
            response = llm(input_text)
            summary = response['text']
            return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


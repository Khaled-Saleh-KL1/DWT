# libraries import
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# files import
from models import LLMEnum

class LLMService:
    def __init__(self):
        print("-"*20, "\nLoading Qwen 2.5 3B Instruct model...")
        self.model_name = "Qwen/Qwen2.5-3B-Instruct"

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype = "auto",
                device_map = "auto" # Where the model layers are placed
            )
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None
        print("Qwen 2.5 3B Loaded Successfully\n","-"*20)

    def generate_answer(self, question: str, context: str) -> str:
        if not self.model:
            return "Error: Model not loaded."

        messages = [
            {
                "role": "system", 
                "content": (
                    "You are a helpful assistant. "
                    "Answer the question strictly based on the provided context. "
                    "Always answer in the same language as the user's question (e.g., if the question is in Arabic, answer in Arabic)."
                )
            },
            {
                "role": "user", 
                "content": f"Context: {context}\n\nQuestion: {question}"}
        ]

        # Qwen chat template shape based on huggingface website
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=LLMEnum.MAX_NEW_TOKENS.value,
            do_sample=LLMEnum.DO_SAMPLE.value,
            temperature=LLMEnum.TEMPERATRUE.value,
            top_p=LLMEnum.TOP_P.value,
        )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in 
            zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        return response

from abc import ABC, abstractmethod
from transformers import AutoTokenizer, AutoModelForCausalLM
from config.config import LLMConfig


class LLMService(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass


class HuggingFaceLLM(LLMService):
    def __init__(self, config: LLMConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(config.model_name)

    def generate_response(self, post_text: str) -> str:
        # Create prompt by inserting post text into template
        prompt = self.config.prompt_template.replace("<INSERT TARGET HANDLE post>", post_text)
        
        # Tokenize and generate response
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=self.config.input_token_length, truncation=True)
        outputs = self.model.generate(
            inputs.input_ids,
            max_length=self.config.output_token_length,
            num_return_sequences=1,
            temperature=self.config.temperature
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

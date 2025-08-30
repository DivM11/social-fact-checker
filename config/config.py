"""Configuration models for the Threads fact-checking bot."""

from pydantic import BaseModel, Field
from typing import List


class ThreadsConfig(BaseModel):
    """Configuration for Threads API and monitoring settings.
    
    Attributes:
        target_handles: List of Threads usernames to monitor
        ping_interval: Time between checks in seconds
    """
    target_handles: List[str] = Field(..., description="List of Threads usernames to monitor")
    ping_interval: int = Field(..., description="Time between checks in seconds", gt=0)


class LLMConfig(BaseModel):
    """Configuration for the Language Model settings.
    
    Attributes:
        model_name: Name of the Hugging Face model to use
        prompt_template: Template for fact-checking prompts
        input_token_length: Maximum input token length
        output_token_length: Maximum output token length
        temperature: Sampling temperature for text generation
    """
    model_name: str = Field(..., description="Name of the Hugging Face model to use")
    prompt_template: str = Field(..., description="Template for fact-checking prompts")
    input_token_length: int = Field(..., description="Maximum input token length", gt=0)
    output_token_length: int = Field(..., description="Maximum output token length", gt=0)
    temperature: float = Field(0.7, description="Sampling temperature for text generation", ge=0.0, le=1.0)


class Config(BaseModel):
    """Main configuration class combining all settings.
    
    Attributes:
        threads_config: Configuration for Threads API
        llm_config: Configuration for the Language Model
        threads_api_key: API key for Threads API
        openai_api_key: API key for OpenAI (if used)
    """
    threads_config: ThreadsConfig = Field(..., description="Configuration for Threads API")
    llm_config: LLMConfig = Field(..., description="Configuration for the Language Model")
    threads_api_key: str = Field(..., description="API key for Threads API")
    openai_api_key: str = Field(..., description="API key for OpenAI (if used)")

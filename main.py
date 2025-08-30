"""Main module for the Threads fact-checking bot."""

import os
import time
import logging
from typing import NoReturn
from requests.exceptions import RequestException
from dotenv import load_dotenv
from config.config import Config, ThreadsConfig, LLMConfig
from services.threads_service import ThreadsAPIService
from services.llm_service import HuggingFaceLLM


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_config() -> Config:
    """Load configuration from environment variables and create config object.
    
    Returns:
        Config: Application configuration object
        
    Raises:
        ValueError: If required environment variables are missing
    """
    load_dotenv()
    
    threads_api_key = os.getenv("THREADS_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not threads_api_key:
        raise ValueError("THREADS_API_KEY environment variable is required")
    
    threads_config = ThreadsConfig(
        target_handles=["example_handle1", "example_handle2"],  # Replace with actual handles
        ping_interval=300  # 5 minutes
    )
    
    llm_config = LLMConfig(
        model_name="gpt2",  # Replace with your chosen model
        prompt_template="Fact check what the user is saying below in a helpful tone with high degree of factuality <INSERT TARGET HANDLE post>",
        input_token_length=512,
        output_token_length=256,
        temperature=0.7
    )
    
    return Config(
        threads_config=threads_config,
        llm_config=llm_config,
        threads_api_key=threads_api_key,
        openai_api_key=openai_api_key
    )


def main() -> NoReturn:
    """Main function to run the Threads fact-checking bot.
    
    This function runs indefinitely, monitoring specified Threads handles
    and posting fact-check replies to new posts.
    """
    try:
        config = load_config()
    except ValueError as e:
        logger.error("Configuration error: %s", str(e))
        return
    
    threads_service = ThreadsAPIService(config.threads_config, config.threads_api_key)
    llm_service = HuggingFaceLLM(config.llm_config)
    
    logger.info("Starting Threads fact-checking bot...")
    
    while True:
        try:
            new_posts = threads_service.monitor_handles()
            
            for _, post_id, post_text in new_posts:  # Underscore for unused handle
                try:
                    response = llm_service.generate_response(post_text)
                    threads_service.post_reply(post_id, response)
                    logger.info("Posted fact-check reply to post %s", post_id)
                except (RequestException, ValueError) as e:
                    logger.error("Error processing post %s: %s", post_id, str(e))
                    continue
            
            time.sleep(config.threads_config.ping_interval)
            
        except RequestException as e:
            logger.error("API error: %s", str(e))
            time.sleep(60)  # Wait a minute before retrying
        except (KeyboardInterrupt, SystemExit):
            logger.info("Bot shutting down...")
            break
        except Exception as e:  # pylint: disable=broad-except
            logger.error("Unexpected error: %s", str(e), exc_info=True)
            time.sleep(60)  # Wait a minute before retrying


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()

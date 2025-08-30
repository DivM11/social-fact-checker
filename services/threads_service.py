"""Service module for interacting with the Threads API."""

import time
from abc import ABC, abstractmethod
from typing import List, Tuple
import requests
from requests.exceptions import RequestException
from config.config import ThreadsConfig


class ThreadsService(ABC):
    """Abstract base class for Threads service implementation.

    This class defines the interface for monitoring Threads posts
    and posting replies.
    """

    @abstractmethod
    def monitor_handles(self) -> List[Tuple[str, str, str]]:
        """Monitor handles for new posts.

        Returns:
            List[Tuple[str, str, str]]: List of (handle, post_id, post_text) for new posts.
        """

    @abstractmethod
    def post_reply(self, thread_id: str, reply_text: str) -> None:
        """Post a reply to a specific thread.

        Args:
            thread_id (str): ID of the thread to reply to
            reply_text (str): Content of the reply

        Raises:
            RequestException: If the reply could not be posted
        """


class ThreadsAPIService(ThreadsService):
    """Implementation of ThreadsService using the Threads API.

    This class handles all interactions with the Threads API, including
    monitoring user posts and posting replies.
    """

    def __init__(self, config: ThreadsConfig, api_key: str):
        """Initialize the ThreadsAPIService.

        Args:
            config (ThreadsConfig): Configuration for the service
            api_key (str): API key for authentication
        """
        self.config = config
        self.api_key = api_key
        self.base_url = "https://www.threads.net/api/v1"
        self.last_thread_ids = {handle: None for handle in config.target_handles}
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.timeout = 10  # seconds

    def _get_user_id(self, username: str) -> str:
        """Get user ID from username.

        Args:
            username (str): The Threads username

        Returns:
            str: The user's ID

        Raises:
            RequestException: If the request fails
        """
        response = requests.get(
            f"{self.base_url}/users/web_profile",
            params={"username": username},
            headers=self.headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()["data"]["user"]["id"]

    def _get_user_threads(self, user_id: str, count: int = 5) -> List[dict]:
        """Get user's recent threads.

        Args:
            user_id (str): The user's ID
            count (int, optional): Number of threads to fetch. Defaults to 5.

        Returns:
            List[dict]: List of thread objects

        Raises:
            RequestException: If the request fails
        """
        response = requests.get(
            f"{self.base_url}/users/{user_id}/threads",
            params={"count": count},
            headers=self.headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()["data"]["threads"]

    def monitor_handles(self) -> List[Tuple[str, str, str]]:
        """Monitor target handles for new threads.

        Returns:
            List[Tuple[str, str, str]]: List of tuples (handle, thread_id, thread_text)
            for new threads.
        """
        new_threads = []

        for handle in self.config.target_handles:
            try:
                user_id = self._get_user_id(handle)
                threads = self._get_user_threads(user_id)

                if not threads:
                    continue

                latest_thread = threads[0]

                if (self.last_thread_ids[handle] is None or 
                    latest_thread["id"] != self.last_thread_ids[handle]):

                    self.last_thread_ids[handle] = latest_thread["id"]
                    new_threads.append(
                        (handle, latest_thread["id"], latest_thread["text"])
                    )

                time.sleep(1)  # Respect rate limits

            except RequestException as e:
                print(f"Error monitoring handle {handle}: {str(e)}")
                continue

        return new_threads

    def post_reply(self, thread_id: str, reply_text: str) -> None:
        """Post a reply to a specific thread.

        Args:
            thread_id (str): ID of the thread to reply to
            reply_text (str): Content of the reply

        Raises:
            RequestException: If the reply could not be posted
        """
        try:
            response = requests.post(
                f"{self.base_url}/text",
                headers=self.headers,
                json={
                    "text": reply_text,
                    "reply_to": thread_id
                },
                timeout=self.timeout
            )
            response.raise_for_status()
        except RequestException as e:
            print(f"Error posting reply to thread {thread_id}: {str(e)}")
            raise

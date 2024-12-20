#!/usr/bin/env python3
"""
Auth module for API Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """
    Auth class for authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        It determines if authentication is required for a given path

        Args:
        path (str): The path to check.
        excluded_paths (list): List of paths or patterns to
        exclude from authentication.

        Returns:
        bool: True if authentication is required, False otherwise.
        """
        # Return True if path is None
        if path is None:
            return True

        # Return True if excluded_paths is None or empty
        if not excluded_paths:
            return True

        # Normalize path to ensure it ends with a slash
        if not path.endswith('/'):
            path += '/'

        # Check if the normalized path is in the excluded_paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.endswith(excluded_path[:-1]):
                    return False
                elif (excluded_path == path
                      or excluded_path == path.rstrip('/')):
                    return False

        # If no match found, return True indicating auth is required
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request
        """
        return None

#!/usr/bin/env python3
"""Auth module"""
from typing import List, TypeVar
from flask import request, abort

app = __import__('flask').Flask(__name__)


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require auth
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None

    @app.before_request
    def before_request():
        auth = app.config.get('AUTH')
        if auth is None:
            return
        if not auth.require_auth(request.path, [
                                '/api/v1/status/',
                                '/api/v1/unauthorized/',
                                '/api/v1/forbidden/']):
            return
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

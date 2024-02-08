#!/usr/bin/env python3
"""Encrypt password"""
import bcrypt


def hash_password(password):
    """
    Returns a salted, hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

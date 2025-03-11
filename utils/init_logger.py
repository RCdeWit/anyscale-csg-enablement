#!/usr/bin/env python3
"""
Logger initialization utility function.
"""

import logging
from typing import Optional


def init_logger(name: Optional[str] = None, 
                level: str = "INFO", 
                log_file: Optional[str] = None, 
                format_str: Optional[str] = None) -> logging.Logger:
    """
    Initialize and configure a logger with console and optional file handlers.
    
    Args:
        name: Logger name. If None, the root logger is returned.
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_file: Optional path to log file. If provided, logs will be written to this file.
        format_str: Custom log format string. If None, default format is used.
    
    Returns:
        Configured logging.Logger instance
    """
    # Set default format if not provided
    if not format_str:
        format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))
    
    # Clear any existing handlers
    logger.handlers = []
    
    # Create formatter
    formatter = logging.Formatter(format_str)
    
    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Add file handler if log_file is specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
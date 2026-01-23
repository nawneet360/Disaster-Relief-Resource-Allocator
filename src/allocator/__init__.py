"""
Disaster Relief Resource Allocator
A smart platform for efficient resource allocation during disasters.
"""

__version__ = "1.0.0"
__author__ = "Disaster Relief Resource Allocator Contributors"

from .resource import Resource
from .location import Location
from .allocator import ResourceAllocator

__all__ = ['Resource', 'Location', 'ResourceAllocator']

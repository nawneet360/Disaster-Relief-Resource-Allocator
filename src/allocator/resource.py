"""
Resource module for managing disaster relief resources.
"""

from typing import Optional
from enum import Enum


class ResourceType(Enum):
    """Types of disaster relief resources."""
    FOOD = "food"
    MEDICAL = "medical"
    WATER = "water"
    SHELTER = "shelter"
    RESCUE_TEAM = "rescue_team"
    TRANSPORTATION = "transportation"
    COMMUNICATION = "communication"


class Resource:
    """Represents a disaster relief resource."""
    
    def __init__(self, resource_id: str, resource_type: ResourceType, 
                 quantity: int, unit: str, location: Optional[str] = None):
        """
        Initialize a Resource.
        
        Args:
            resource_id: Unique identifier for the resource
            resource_type: Type of resource (food, medical, etc.)
            quantity: Available quantity
            unit: Unit of measurement (kg, liters, people, etc.)
            location: Current location of the resource
        """
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.quantity = quantity
        self.unit = unit
        self.location = location
        self.allocated = 0
    
    def allocate(self, amount: int) -> bool:
        """
        Allocate a specified amount of the resource.
        
        Args:
            amount: Amount to allocate
            
        Returns:
            True if allocation successful, False otherwise
        """
        if amount <= 0:
            return False
        
        available = self.quantity - self.allocated
        if amount <= available:
            self.allocated += amount
            return True
        return False
    
    def available_quantity(self) -> int:
        """Get the available (unallocated) quantity."""
        return self.quantity - self.allocated
    
    def __repr__(self) -> str:
        return (f"Resource(id={self.resource_id}, type={self.resource_type.value}, "
                f"quantity={self.quantity}, allocated={self.allocated}, "
                f"available={self.available_quantity()})")

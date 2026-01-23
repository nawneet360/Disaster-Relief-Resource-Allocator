"""
Location module for managing disaster-affected locations.
"""

from typing import Optional
from enum import Enum


class SeverityLevel(Enum):
    """Severity levels for disaster-affected areas."""
    CRITICAL = 5
    HIGH = 4
    MEDIUM = 3
    LOW = 2
    MINIMAL = 1


class Location:
    """Represents a disaster-affected location."""
    
    def __init__(self, location_id: str, name: str, 
                 population: int, severity: SeverityLevel,
                 latitude: Optional[float] = None,
                 longitude: Optional[float] = None):
        """
        Initialize a Location.
        
        Args:
            location_id: Unique identifier for the location
            name: Name of the location
            population: Affected population count
            severity: Severity level of the disaster
            latitude: Latitude coordinate
            longitude: Longitude coordinate
        """
        self.location_id = location_id
        self.name = name
        self.population = population
        self.severity = severity
        self.latitude = latitude
        self.longitude = longitude
        self.needs = {}  # Dict of resource type to required quantity
    
    def add_need(self, resource_type: str, quantity: int):
        """
        Add a resource need for this location.
        
        Args:
            resource_type: Type of resource needed
            quantity: Quantity needed
        """
        self.needs[resource_type] = quantity
    
    def get_priority_score(self) -> float:
        """
        Calculate priority score based on severity and population.
        Higher score means higher priority.
        
        Returns:
            Priority score
        """
        return self.severity.value * (self.population / 1000)
    
    def __repr__(self) -> str:
        return (f"Location(id={self.location_id}, name={self.name}, "
                f"population={self.population}, severity={self.severity.name}, "
                f"priority={self.get_priority_score():.2f})")

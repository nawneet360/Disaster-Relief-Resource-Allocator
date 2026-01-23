"""
Resource Allocator module for optimizing disaster relief resource distribution.
"""

from typing import List, Dict, Tuple, Any
from .resource import Resource, ResourceType
from .location import Location, SeverityLevel


class AllocationResult:
    """Represents the result of a resource allocation."""
    
    def __init__(self, location: Location, resource: Resource, allocated_amount: int):
        self.location = location
        self.resource = resource
        self.allocated_amount = allocated_amount
    
    def __repr__(self) -> str:
        return (f"AllocationResult(location={self.location.name}, "
                f"resource={self.resource.resource_type.value}, "
                f"amount={self.allocated_amount})")


class ResourceAllocator:
    """Manages the allocation of disaster relief resources to affected locations."""
    
    def __init__(self):
        """Initialize the ResourceAllocator."""
        self.resources: List[Resource] = []
        self.locations: List[Location] = []
        self.allocations: List[AllocationResult] = []
    
    def add_resource(self, resource: Resource):
        """Add a resource to the allocator."""
        self.resources.append(resource)
    
    def add_location(self, location: Location):
        """Add a location to the allocator."""
        self.locations.append(location)
    
    def allocate_resources(self) -> List[AllocationResult]:
        """
        Allocate resources to locations based on priority.
        Uses a priority-based allocation algorithm.
        
        Returns:
            List of allocation results
        """
        self.allocations = []
        
        # Sort locations by priority (highest first)
        sorted_locations = sorted(
            self.locations, 
            key=lambda loc: loc.get_priority_score(), 
            reverse=True
        )
        
        # For each location in priority order
        for location in sorted_locations:
            # For each resource need
            for resource_type_str, needed_quantity in location.needs.items():
                # Try to find available resources of this type
                try:
                    resource_type = ResourceType(resource_type_str)
                except ValueError:
                    continue
                
                available_resources = [
                    r for r in self.resources 
                    if r.resource_type == resource_type and r.available_quantity() > 0
                ]
                
                remaining_need = needed_quantity
                
                # Allocate from available resources
                for resource in available_resources:
                    if remaining_need <= 0:
                        break
                    
                    allocatable = min(remaining_need, resource.available_quantity())
                    if resource.allocate(allocatable):
                        allocation = AllocationResult(location, resource, allocatable)
                        self.allocations.append(allocation)
                        remaining_need -= allocatable
        
        return self.allocations
    
    def get_allocation_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the allocation results.
        
        Returns:
            Dictionary containing allocation statistics
        """
        total_allocations = len(self.allocations)
        allocations_by_location = {}
        allocations_by_resource_type = {}
        
        for allocation in self.allocations:
            # By location
            loc_name = allocation.location.name
            if loc_name not in allocations_by_location:
                allocations_by_location[loc_name] = []
            allocations_by_location[loc_name].append(allocation)
            
            # By resource type
            res_type = allocation.resource.resource_type.value
            if res_type not in allocations_by_resource_type:
                allocations_by_resource_type[res_type] = 0
            allocations_by_resource_type[res_type] += allocation.allocated_amount
        
        return {
            'total_allocations': total_allocations,
            'locations_served': len(allocations_by_location),
            'allocations_by_location': allocations_by_location,
            'allocations_by_resource_type': allocations_by_resource_type
        }
    
    def reset(self):
        """Reset all allocations."""
        for resource in self.resources:
            resource.allocated = 0
        self.allocations = []

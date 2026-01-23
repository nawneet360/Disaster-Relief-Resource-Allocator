"""
Example usage of the Disaster Relief Resource Allocator.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from allocator import Resource, Location, ResourceAllocator
from allocator.resource import ResourceType
from allocator.location import SeverityLevel


def main():
    """Demonstrate the resource allocator with a realistic scenario."""
    
    print("=" * 60)
    print("Disaster Relief Resource Allocator - Example Scenario")
    print("=" * 60)
    print()
    
    # Create the allocator
    allocator = ResourceAllocator()
    
    # Add available resources
    print("Available Resources:")
    print("-" * 60)
    
    resources = [
        Resource("R001", ResourceType.FOOD, 5000, "kg", "Warehouse A"),
        Resource("R002", ResourceType.WATER, 10000, "liters", "Warehouse A"),
        Resource("R003", ResourceType.MEDICAL, 500, "units", "Hospital"),
        Resource("R004", ResourceType.FOOD, 3000, "kg", "Warehouse B"),
        Resource("R005", ResourceType.SHELTER, 200, "tents", "Supply Center"),
    ]
    
    for resource in resources:
        allocator.add_resource(resource)
        print(f"  {resource}")
    
    print()
    
    # Add affected locations
    print("Affected Locations:")
    print("-" * 60)
    
    # Critical area - flooded city center
    city_center = Location("L001", "City Center (Flooded)", 15000, SeverityLevel.CRITICAL)
    city_center.add_need("food", 3000)
    city_center.add_need("water", 6000)
    city_center.add_need("medical", 300)
    allocator.add_location(city_center)
    print(f"  {city_center}")
    print(f"    Needs: {city_center.needs}")
    
    # High priority - coastal village
    coastal_village = Location("L002", "Coastal Village", 8000, SeverityLevel.HIGH)
    coastal_village.add_need("food", 2000)
    coastal_village.add_need("water", 4000)
    coastal_village.add_need("shelter", 150)
    allocator.add_location(coastal_village)
    print(f"  {coastal_village}")
    print(f"    Needs: {coastal_village.needs}")
    
    # Medium priority - mountain community
    mountain_community = Location("L003", "Mountain Community", 5000, SeverityLevel.MEDIUM)
    mountain_community.add_need("food", 1500)
    mountain_community.add_need("medical", 100)
    mountain_community.add_need("shelter", 80)
    allocator.add_location(mountain_community)
    print(f"  {mountain_community}")
    print(f"    Needs: {mountain_community.needs}")
    
    # Low priority - suburban area
    suburban_area = Location("L004", "Suburban Area", 3000, SeverityLevel.LOW)
    suburban_area.add_need("food", 800)
    suburban_area.add_need("water", 1500)
    allocator.add_location(suburban_area)
    print(f"  {suburban_area}")
    print(f"    Needs: {suburban_area.needs}")
    
    print()
    
    # Perform allocation
    print("Performing Resource Allocation...")
    print("-" * 60)
    allocations = allocator.allocate_resources()
    
    print()
    print("Allocation Results:")
    print("-" * 60)
    
    for allocation in allocations:
        print(f"  → {allocation.location.name}:")
        print(f"    {allocation.resource.resource_type.value}: {allocation.allocated_amount} {allocation.resource.unit}")
        print(f"    (from {allocation.resource.location or 'unknown location'})")
    
    print()
    
    # Display summary
    summary = allocator.get_allocation_summary()
    
    print("Allocation Summary:")
    print("-" * 60)
    print(f"  Total Allocations: {summary['total_allocations']}")
    print(f"  Locations Served: {summary['locations_served']}")
    print()
    print("  Resources Allocated by Type:")
    for resource_type, amount in summary['allocations_by_resource_type'].items():
        print(f"    {resource_type}: {amount}")
    
    print()
    
    # Display remaining resources
    print("Remaining Resources:")
    print("-" * 60)
    for resource in resources:
        if resource.available_quantity() > 0:
            print(f"  {resource.resource_type.value}: {resource.available_quantity()} {resource.unit}")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()

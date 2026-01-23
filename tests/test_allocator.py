"""
Tests for the Resource Allocator system.
"""

import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from allocator import Resource, Location, ResourceAllocator
from allocator.resource import ResourceType
from allocator.location import SeverityLevel


class TestResource:
    """Tests for Resource class."""
    
    def test_resource_creation(self):
        """Test creating a resource."""
        resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
        assert resource.resource_id == "R001"
        assert resource.resource_type == ResourceType.FOOD
        assert resource.quantity == 1000
        assert resource.unit == "kg"
        assert resource.allocated == 0
    
    def test_resource_allocation(self):
        """Test allocating resources."""
        resource = Resource("R001", ResourceType.WATER, 500, "liters")
        assert resource.allocate(200) is True
        assert resource.allocated == 200
        assert resource.available_quantity() == 300
    
    def test_resource_over_allocation(self):
        """Test that over-allocation is prevented."""
        resource = Resource("R001", ResourceType.MEDICAL, 100, "units")
        resource.allocate(80)
        assert resource.allocate(30) is False
        assert resource.allocated == 80
    
    def test_negative_allocation(self):
        """Test that negative allocation is prevented."""
        resource = Resource("R001", ResourceType.FOOD, 100, "kg")
        assert resource.allocate(-10) is False
        assert resource.allocated == 0


class TestLocation:
    """Tests for Location class."""
    
    def test_location_creation(self):
        """Test creating a location."""
        location = Location("L001", "City Center", 10000, SeverityLevel.CRITICAL)
        assert location.location_id == "L001"
        assert location.name == "City Center"
        assert location.population == 10000
        assert location.severity == SeverityLevel.CRITICAL
    
    def test_add_need(self):
        """Test adding resource needs."""
        location = Location("L001", "Village", 5000, SeverityLevel.HIGH)
        location.add_need("food", 500)
        location.add_need("water", 1000)
        assert location.needs["food"] == 500
        assert location.needs["water"] == 1000
    
    def test_priority_score(self):
        """Test priority score calculation."""
        loc1 = Location("L001", "City", 10000, SeverityLevel.CRITICAL)
        loc2 = Location("L002", "Town", 5000, SeverityLevel.HIGH)
        assert loc1.get_priority_score() > loc2.get_priority_score()


class TestResourceAllocator:
    """Tests for ResourceAllocator class."""
    
    def test_allocator_creation(self):
        """Test creating an allocator."""
        allocator = ResourceAllocator()
        assert len(allocator.resources) == 0
        assert len(allocator.locations) == 0
    
    def test_add_resources_and_locations(self):
        """Test adding resources and locations."""
        allocator = ResourceAllocator()
        
        resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
        allocator.add_resource(resource)
        
        location = Location("L001", "City", 10000, SeverityLevel.CRITICAL)
        allocator.add_location(location)
        
        assert len(allocator.resources) == 1
        assert len(allocator.locations) == 1
    
    def test_basic_allocation(self):
        """Test basic resource allocation."""
        allocator = ResourceAllocator()
        
        # Add resources
        food_resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
        allocator.add_resource(food_resource)
        
        # Add location with needs
        location = Location("L001", "City", 10000, SeverityLevel.CRITICAL)
        location.add_need("food", 500)
        allocator.add_location(location)
        
        # Allocate
        results = allocator.allocate_resources()
        
        assert len(results) == 1
        assert results[0].allocated_amount == 500
        assert food_resource.available_quantity() == 500
    
    def test_priority_based_allocation(self):
        """Test that higher priority locations get resources first."""
        allocator = ResourceAllocator()
        
        # Limited food resource
        food_resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
        allocator.add_resource(food_resource)
        
        # Two locations with different priorities
        critical_loc = Location("L001", "Critical Area", 10000, SeverityLevel.CRITICAL)
        critical_loc.add_need("food", 800)
        allocator.add_location(critical_loc)
        
        low_loc = Location("L002", "Low Area", 5000, SeverityLevel.LOW)
        low_loc.add_need("food", 500)
        allocator.add_location(low_loc)
        
        # Allocate
        results = allocator.allocate_resources()
        
        # Critical location should get resources first
        critical_allocation = [r for r in results if r.location.location_id == "L001"]
        low_allocation = [r for r in results if r.location.location_id == "L002"]
        
        assert len(critical_allocation) == 1
        assert critical_allocation[0].allocated_amount == 800
        assert len(low_allocation) == 1
        assert low_allocation[0].allocated_amount == 200  # Only 200 left
    
    def test_allocation_summary(self):
        """Test getting allocation summary."""
        allocator = ResourceAllocator()
        
        # Add resources
        allocator.add_resource(Resource("R001", ResourceType.FOOD, 1000, "kg"))
        allocator.add_resource(Resource("R002", ResourceType.WATER, 2000, "liters"))
        
        # Add locations with needs
        loc1 = Location("L001", "City A", 10000, SeverityLevel.CRITICAL)
        loc1.add_need("food", 500)
        loc1.add_need("water", 1000)
        allocator.add_location(loc1)
        
        loc2 = Location("L002", "City B", 5000, SeverityLevel.HIGH)
        loc2.add_need("food", 300)
        allocator.add_location(loc2)
        
        # Allocate
        allocator.allocate_resources()
        
        # Get summary
        summary = allocator.get_allocation_summary()
        
        assert summary['total_allocations'] == 3
        assert summary['locations_served'] == 2
        assert 'food' in summary['allocations_by_resource_type']
        assert 'water' in summary['allocations_by_resource_type']

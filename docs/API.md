# API Documentation

## Core Classes

### Resource

Represents a disaster relief resource.

#### Constructor

```python
Resource(resource_id: str, resource_type: ResourceType, quantity: int, unit: str, location: Optional[str] = None)
```

**Parameters:**
- `resource_id` (str): Unique identifier for the resource
- `resource_type` (ResourceType): Type of resource (FOOD, WATER, MEDICAL, etc.)
- `quantity` (int): Total available quantity
- `unit` (str): Unit of measurement (kg, liters, units, etc.)
- `location` (str, optional): Current location of the resource

#### Methods

##### allocate(amount: int) -> bool

Allocate a specified amount of the resource.

**Parameters:**
- `amount` (int): Amount to allocate

**Returns:**
- `bool`: True if allocation successful, False otherwise

**Example:**
```python
resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
success = resource.allocate(500)  # Returns True
```

##### available_quantity() -> int

Get the available (unallocated) quantity.

**Returns:**
- `int`: Available quantity

**Example:**
```python
resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
resource.allocate(300)
print(resource.available_quantity())  # Outputs: 700
```

---

### Location

Represents a disaster-affected location.

#### Constructor

```python
Location(location_id: str, name: str, population: int, severity: SeverityLevel, 
         latitude: Optional[float] = None, longitude: Optional[float] = None)
```

**Parameters:**
- `location_id` (str): Unique identifier for the location
- `name` (str): Name of the location
- `population` (int): Affected population count
- `severity` (SeverityLevel): Severity level (CRITICAL, HIGH, MEDIUM, LOW, MINIMAL)
- `latitude` (float, optional): Latitude coordinate
- `longitude` (float, optional): Longitude coordinate

#### Methods

##### add_need(resource_type: str, quantity: int)

Add a resource need for this location.

**Parameters:**
- `resource_type` (str): Type of resource needed
- `quantity` (int): Quantity needed

**Example:**
```python
location = Location("L001", "City Center", 10000, SeverityLevel.CRITICAL)
location.add_need("food", 500)
location.add_need("water", 1000)
```

##### get_priority_score() -> float

Calculate priority score based on severity and population.

**Returns:**
- `float`: Priority score (higher = higher priority)

**Example:**
```python
location = Location("L001", "City Center", 10000, SeverityLevel.CRITICAL)
score = location.get_priority_score()  # Returns 50.0 (5 * 10)
```

---

### ResourceAllocator

Manages the allocation of disaster relief resources to affected locations.

#### Constructor

```python
ResourceAllocator()
```

**Example:**
```python
allocator = ResourceAllocator()
```

#### Methods

##### add_resource(resource: Resource)

Add a resource to the allocator.

**Parameters:**
- `resource` (Resource): Resource to add

**Example:**
```python
food = Resource("R001", ResourceType.FOOD, 1000, "kg")
allocator.add_resource(food)
```

##### add_location(location: Location)

Add a location to the allocator.

**Parameters:**
- `location` (Location): Location to add

**Example:**
```python
city = Location("L001", "City Center", 10000, SeverityLevel.CRITICAL)
allocator.add_location(city)
```

##### allocate_resources() -> List[AllocationResult]

Allocate resources to locations based on priority.

**Returns:**
- `List[AllocationResult]`: List of allocation results

**Example:**
```python
allocations = allocator.allocate_resources()
for allocation in allocations:
    print(f"{allocation.location.name}: {allocation.allocated_amount}")
```

##### get_allocation_summary() -> Dict[str, any]

Get a summary of the allocation results.

**Returns:**
- `dict`: Dictionary containing allocation statistics with keys:
  - `total_allocations`: Total number of allocations
  - `locations_served`: Number of locations served
  - `allocations_by_location`: Allocations grouped by location
  - `allocations_by_resource_type`: Allocations grouped by resource type

**Example:**
```python
summary = allocator.get_allocation_summary()
print(f"Total allocations: {summary['total_allocations']}")
print(f"Locations served: {summary['locations_served']}")
```

##### reset()

Reset all allocations.

**Example:**
```python
allocator.reset()
```

---

## Enums

### ResourceType

Available resource types:
- `FOOD`
- `MEDICAL`
- `WATER`
- `SHELTER`
- `RESCUE_TEAM`
- `TRANSPORTATION`
- `COMMUNICATION`

**Example:**
```python
from allocator.resource import ResourceType
resource = Resource("R001", ResourceType.FOOD, 1000, "kg")
```

### SeverityLevel

Available severity levels:
- `CRITICAL` (value: 5)
- `HIGH` (value: 4)
- `MEDIUM` (value: 3)
- `LOW` (value: 2)
- `MINIMAL` (value: 1)

**Example:**
```python
from allocator.location import SeverityLevel
location = Location("L001", "City", 10000, SeverityLevel.CRITICAL)
```

---

## Complete Example

```python
from allocator import Resource, Location, ResourceAllocator
from allocator.resource import ResourceType
from allocator.location import SeverityLevel

# Create allocator
allocator = ResourceAllocator()

# Add resources
food = Resource("R001", ResourceType.FOOD, 5000, "kg")
water = Resource("R002", ResourceType.WATER, 10000, "liters")
medical = Resource("R003", ResourceType.MEDICAL, 500, "units")
allocator.add_resource(food)
allocator.add_resource(water)
allocator.add_resource(medical)

# Add locations with needs
city = Location("L001", "City Center", 15000, SeverityLevel.CRITICAL)
city.add_need("food", 3000)
city.add_need("water", 6000)
city.add_need("medical", 300)
allocator.add_location(city)

village = Location("L002", "Coastal Village", 8000, SeverityLevel.HIGH)
village.add_need("food", 2000)
village.add_need("water", 4000)
allocator.add_location(village)

# Perform allocation
allocations = allocator.allocate_resources()

# Print results
for allocation in allocations:
    print(f"{allocation.location.name} receives:")
    print(f"  {allocation.allocated_amount} {allocation.resource.unit} "
          f"of {allocation.resource.resource_type.value}")

# Get summary
summary = allocator.get_allocation_summary()
print(f"\nTotal allocations: {summary['total_allocations']}")
print(f"Locations served: {summary['locations_served']}")
```

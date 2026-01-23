# Disaster Relief Resource Allocator 🆘

A smart platform that helps authorities quickly allocate food, medical aid, and rescue teams during disasters, ensuring timely support reaches affected communities when it matters most.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

The Disaster Relief Resource Allocator is a Python-based system designed to optimize the distribution of critical resources during emergency situations. It uses a priority-based allocation algorithm that considers disaster severity and affected population to ensure resources reach the most critical areas first.

## Features

✅ **Priority-Based Allocation**: Automatically prioritizes locations based on disaster severity and population affected  
✅ **Multiple Resource Types**: Supports food, water, medical supplies, shelter, rescue teams, and more  
✅ **Smart Distribution**: Optimizes resource allocation to maximize impact  
✅ **Flexible Architecture**: Easy to extend with custom resource types and allocation strategies  
✅ **Comprehensive Testing**: Includes unit tests for reliability  
✅ **Simple API**: Clean, intuitive interface for rapid deployment  

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/nawneet360/Disaster-Relief-Resource-Allocator.git
cd Disaster-Relief-Resource-Allocator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

Here's a simple example to get you started:

```python
from allocator import Resource, Location, ResourceAllocator
from allocator.resource import ResourceType
from allocator.location import SeverityLevel

# Create the allocator
allocator = ResourceAllocator()

# Add available resources
food = Resource("R001", ResourceType.FOOD, 1000, "kg")
water = Resource("R002", ResourceType.WATER, 2000, "liters")
allocator.add_resource(food)
allocator.add_resource(water)

# Add affected location
critical_area = Location("L001", "Flooded City", 10000, SeverityLevel.CRITICAL)
critical_area.add_need("food", 500)
critical_area.add_need("water", 1000)
allocator.add_location(critical_area)

# Perform allocation
allocations = allocator.allocate_resources()

# View results
for allocation in allocations:
    print(f"{allocation.location.name} receives {allocation.allocated_amount} "
          f"{allocation.resource.unit} of {allocation.resource.resource_type.value}")
```

## Usage

### Running the Example

See a complete demonstration with multiple locations and resources:

```bash
python examples/basic_usage.py
```

### Resource Types

The system supports the following resource types:
- `FOOD` - Food supplies
- `WATER` - Water and drinking supplies
- `MEDICAL` - Medical supplies and equipment
- `SHELTER` - Temporary shelters and tents
- `RESCUE_TEAM` - Rescue personnel
- `TRANSPORTATION` - Transportation vehicles
- `COMMUNICATION` - Communication equipment

### Severity Levels

Locations are categorized by disaster severity:
- `CRITICAL` (5) - Highest priority
- `HIGH` (4) - High priority
- `MEDIUM` (3) - Medium priority
- `LOW` (2) - Low priority
- `MINIMAL` (1) - Lowest priority

Priority score is calculated as: `severity_level × (population / 1000)`

## Testing

Run the test suite to ensure everything is working correctly:

```bash
pytest tests/
```

For verbose output:
```bash
pytest -v tests/
```

## Project Structure

```
Disaster-Relief-Resource-Allocator/
├── src/
│   └── allocator/
│       ├── __init__.py          # Package initialization
│       ├── resource.py          # Resource management
│       ├── location.py          # Location management
│       └── allocator.py         # Core allocation logic
├── tests/
│   └── test_allocator.py        # Unit tests
├── examples/
│   └── basic_usage.py           # Example usage
├── docs/
│   └── CONTRIBUTING.md          # Contribution guidelines
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](docs/CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run tests: `pytest tests/`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/nawneet360/Disaster-Relief-Resource-Allocator/issues)
- Contact the maintainers

## Roadmap

Future enhancements planned:
- [ ] Web-based dashboard for visualization
- [ ] Real-time tracking and updates
- [ ] Geographic distance calculations for logistics
- [ ] Machine learning-based demand prediction
- [ ] Mobile app integration
- [ ] Multi-language support
- [ ] API for third-party integrations

## Acknowledgments

This project was created to support disaster relief efforts and help communities in times of crisis. We're grateful to all contributors and organizations working to make disaster response more efficient and effective.

---

**Made with ❤️ for disaster relief efforts worldwide**

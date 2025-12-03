# ISS_location
Real-time tracker that shows which country or ocean the International Space Station is currently flying over. Fetches live coordinates from NASA data and converts them to human-readable locations.

## Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/kybik0606/ISS_location.git
cd ISS_location

# Install dependencies
pip install requests geopy
```
### Basic Usage
```bash
python ISS_location.py
```

### Example Output
```bash
--- Где же сейчас МКС? ---
Широта: 31.80° - южная      
Долгота: 126.36° - восточная
Местоположение: Австралия
```

## API Endpoints Used
Open Notify: http://api.open-notify.org

Nominatim: https://nominatim.openstreetmap.org

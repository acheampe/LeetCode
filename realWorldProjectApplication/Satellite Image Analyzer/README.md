# 🌊 Satellite Image Analyzer: Grid & Flood Fill Practice  

## 📌 Problem Statement  
You are tasked with building a simplified **satellite image analyzer** to detect and analyze water bodies (e.g., lakes, rivers, flood zones) from satellite images.  

The image is represented as an `m x n` binary grid:  
- `0` = land  
- `1` = water  

Your analyzer should implement algorithms that:  
1. **Count distinct water bodies, water bodies at border can still be considered distinct**  
2. **Find the largest water body (by area)**  
3. **Detect enclosed lakes** (water bodies not touching the grid border)  
4. **Simulate flood risk zones** by expanding from border-connected water bodies  

Input Grid:      Flood Risk Zones (neighbors_4)
1 0 1            X 1 X
0 0 0     =>     1 1 1
1 0 1            X 1 X

Connectivity is defined as **8-directional adjacency**:  
- Horizontal: up, down  
- Vertical: left, right  
- Diagonal: top-left, top-right, bottom-left, bottom-right  

--- 

# Directory Structure
grid-project/
├─ pyproject.toml
├─ src/
│  └─ gridtools/
│     ├─ __init__.py
│     ├─ connectivity.py         # neighbors4(), neighbors8()  ← you’ll default to neighbors8()
│     ├─ floodfill.py            # components() / flood_fill() core
│     ├─ predicates.py           # is_water(), is_land()
│     └─ features/
│        ├─ count_water_bodies.py     # (1) count distinct 8-connected water components
│        ├─ max_water_area.py         # (2) max area among 8-connected water components
│        ├─ count_enclosed_lakes.py   # (3) components not touching border
│        └─ flood_risk_expand.py      # (4) multi-source expansion from border water
└─ tests/
   ├─ test_floodfill_core.py
   ├─ test_count_water_bodies.py
   ├─ test_max_water_area.py
   ├─ test_count_enclosed_lakes.py
   └─ test_flood_risk_expand.py

# Future Extension
- Rewrite in Golang for performance (concurrency)
- Add visualization
- Integrate real sattelite raster data (e.g., from GeoTIFFs)
- Wrap features in API for end-user interaction
- Integrate real world data (flood terrain elevation, probabilistic flood modeling)
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

Connectivity is defined as **8-directional adjacency**:  
- Horizontal: up, down  
- Vertical: left, right  
- Diagonal: top-left, top-right, bottom-left, bottom-right  

--- 
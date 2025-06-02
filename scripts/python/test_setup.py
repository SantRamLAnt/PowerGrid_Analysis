print("Testing package imports...")

try:
    import pandas as pd
    print("✓ Pandas imported successfully")
    
    import geopandas as gpd
    print("✓ GeoPandas imported successfully")
    
    import folium
    print("✓ Folium imported successfully")
    
    import plotly
    print("✓ Plotly imported successfully")
    
    print("\nAll packages imported successfully! Setup is complete.")
    
except ImportError as e:
    print(f"✗ Error importing package: {e}")
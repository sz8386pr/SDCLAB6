import folium

# MCTC marker on Twincities map saved as map.html
map_mn = folium.Map(location=[45, -93.2])
folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)
map_mn.save('map.html')

# Create a US map
map_us = folium.Map(location=[40,-120], zoom_start=3)
map_us.save('map_us.html')

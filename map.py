import folium
import os
import json

# Create map object
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Global tooltip
tooltip = 'Click For More Info'

# Create markers
folium.Marker([42.363600, -71.099500],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([42.333600, -71.109500],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([42.377120, -71.062400],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([42.374150, -71.122410],
              popup='<strong>Location Four</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),


# Generate map
m.save('map.html')
import folium 
import pandas

df = pandas.read_csv(r"C:\Python_\10_apps\Volcanos_Web_mapping\volcanoes.txt")
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='stamen terrain')

for lat, lon, name, elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
  folium.Marker(location=[lat,lon],popup=name).add_to(map)
    
map.save(outfile=r"C:\Python_\10_apps\Volcanos_Web_mapping\Volcanoes.html")



    


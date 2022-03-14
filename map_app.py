import folium ## folium is a lib where it creates html,js file based on the python script

map = folium.Map(location=[80,-100]) ## location =[latitute,longitute] latitute ranges(-90,90),longitute ranges(180,180)
map.save('Map.html') ## this will create a html code for the map object
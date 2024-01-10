import requests, webbrowser
import folium
response = requests.get('http://api.open-notify.org/iss-now.json')
data = response.json()

latitude=data['iss_position']['latitude']
longitude=data['iss_position']['longitude']

# creating custom map using folium
custom_map =folium.Map(location=[latitude,longitude],zoom_start=6,zoom_end=50,tiles="cartodb positron")
custom_map.add_child(folium.Marker(location=[latitude,longitude],icon=folium.Icon(color='red',fill_color="RdY1Gn_r",icon="home")))

custom_map.save('iss.html')
url='file://C:/Users/hp/PycharmProjects/ISI plateform/iss.html'
webbrowser.open(url)
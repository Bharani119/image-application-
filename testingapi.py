import requests
import urllib.request as urllib
# phu = input('enter search term')
# r = requests.get(
#     f'https://api.unsplash.com/search/collections?query={phu}&page=1&per_page=20&client_id=a3LeIdw1sJLTf4wV3b-9K9GUZ8UJ-PF9QkwL1mLAUYc')
r = requests.get(
    f'https://api.unsplash.com/photos/random?orientation=landscape&count=21&client_id=a3LeIdw1sJLTf4wV3b-9K9GUZ8UJ-PF9QkwL1mLAUYc')
print(r)
data = r.json()
print(data[0].keys())
# print(data['results'][0]['preview_photos'][0]['urls']['small'])
# for img_data in data['results']:
#     file_name = str(img_data['id']) + ".jpg"
#     img_url = img_data['preview_photos'][0]['urls']['small']
#     print(img_url)
for i in data:
    print(i['urls']['small'])
# print(data[0]['urls']['small'])
# print(data['urls']['small'])

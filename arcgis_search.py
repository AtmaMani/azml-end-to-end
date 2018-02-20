from arcgis.gis import GIS
gis = GIS()
print('Imported ArcGIS module')

def search_fire(search_string='Fire'):
    print('Searching for items titled {1} on ArcGIS Online'.format(search_string))
    search_result = gis.content.search(search_string, max_items=20)
    webmap_count = 0
    for item in search_result:
        if item.type == 'Web Map':
            webmap_count +=1
        print(item.title)
    return webmap_count
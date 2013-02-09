import json
import geojson

zips = [98001, 98002, 98003, 98004, 98005, 98006, 98007, 98008, 98010, 98011, 98014, 98019, 98023, 98024, 98027, 98028, 98029, 98030, 98031, 98032, 98033, 98034, 98038, 98040, 98042, 98045, 98052, 98053, 98055, 98056, 98057, 98058, 98059, 98065, 98072, 98074, 98075, 98077, 98092, 98101, 98102, 98103, 98104, 98105, 98106, 98107, 98108, 98109, 98112, 98115, 98116, 98117, 98118, 98119, 98121, 98122, 98125, 98126, 98133, 98134, 98136, 98144, 98146, 98148, 98155, 98166, 98168, 98177, 98178, 98188, 98198, 98199]


# data_string = json.loads("newjson.json")

# with open("newjson.json") as map_js:
#     data_string = json.load(map_js)

#     new_geojson = [x for x in data_string["features"] if x['properties']['NAME'] in str(zips)]

    # print new_geojson

    # with open('newfile.js', "w") as newfile:
    #     newfile.write(json.dumps(new_geojson))


with open("seattle_geojson.js") as s:
    seattle = json.load(s)

    with open("geekdata.json") as geek_js:
        geekdata = json.load(geek_js)


    for x in seattle:
        for y in geekdata:
            if (str(y['Zip Code']) == x['properties']['NAME']):
                x['properties'] = dict(x['properties'].items() + y.items())


        print x['properties']["Geek Media %"]
    # print json.dumps(seattle[0])
    # with open("newjs.js", "w") as newjs:
    #     newjs.write(json.dumps(seattle))

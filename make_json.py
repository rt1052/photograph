import json
import glob
import os

def make_json():
    # init dict
    dict = {"data":[]}

    a = glob.glob(r'../media/image/*.jpg')
    for x in a:
        # get filename
        name = os.path.join(x[15:])
        temp = {"src":name}
        # add key-value
        dict["data"].append(temp)
    print(dict)
    # open json file
    with open("../json/image.json","w") as f:
        json.dump(dict, f)

    print('Done')

if __name__=='__main__':
    make_json()

import os, json

class EzUtil(object):
    @staticmethod
    def jsonToFile(jsonobj, outfile='output/json_output.json'):
         #outfile filepath - create dir if not exists
        fpath, fname = os.path.split(outfile)
        fpath = fpath if fpath else 'output'
        if not os.path.exists(fpath):
            os.makedirs(fpath)

        with open(outfile, 'w+') as fo:
            json.dump(jsonobj, fo, separators=(',',':'), sort_keys=True, indent=4)
        return jsonobj   

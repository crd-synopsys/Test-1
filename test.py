import json
import sys
from collections import OrderedDict

def remove_USAF_junk(anchore_data):
	#Remove junk data from USAF that breaks Code Dx import
	del anchore_data['base_digest']
	del anchore_data['imageFullTag']

	modified_anchore_data = OrderedDict(('imageDigest' if k == 'image_digest' else k, v) for k, v in anchore_data.items())

	return modified_anchore_data

anchore_json_obj = sys.argv[1] #anchore_security.json
with open(anchore_json_obj) as f:
	anchore_data = json.load(f, object_pairs_hook=OrderedDict)


o = open('anchore_security_fixed.json', 'w')
json.dump(remove_USAF_junk(anchore_data), o, indent=4)
o.close()
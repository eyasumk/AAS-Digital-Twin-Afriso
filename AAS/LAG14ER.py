import os
import pandas as panda
from basyx.aas.adapter.json import read_aas_json_file
from basyx.aas.adapter import aasx
from basyx.aas.model import DictObjectStore


#read xlsx file.
df = panda.read_excel("../LAG14ER.xlsx")

# parsing 


#to json
df.to_json("../LAG14ER.json", orient='records', indent=4)


base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "..", "LAG14ER.json")

with open(json_path, "r", encoding="utf-8") as json:
    object_store = DictObjectStore(read_aas_json_file(json))

# file container
file_store = aasx.DictSupplementaryFileContainer()

aasx_path = os.path.join(base_dir, "LAG14ER.aasx")

# AASX package save
# write_ass_objects : to make AASX file.
with aasx.AASXWriter(aasx_path) as writer:
    writer.write_aas_objects(
        part_name="/aasx/data.json",
        object_ids=[obj.id for obj in object_store],
        file_store=file_store,
        object_store=object_store,
        write_json=True
    )

print("AASX Created")

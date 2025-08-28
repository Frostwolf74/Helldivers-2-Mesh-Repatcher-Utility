import bpy
import HD2_SDK_API as API

id_list = [
        
]

# create patch
API.create_patch()

# compile all meshes into a single patch
for i, id in enumerate(id_list):
    if bpy.context.object == None or bpy.context.view_layer.objects.active.select_get() == False:
        raise Exception("No mesh selected!")
    
    # AO will be deselected after the meshes are saved, AO is saved after a selected mesh is confirmed
    AO = bpy.context.active_object

    bpy.context.object["Z_SwapID"] = str(id)
    # save meshes
    API.save_meshes()

    # reselect object
    bpy.context.view_layer.objects.active = AO
    AO.select_set(True)


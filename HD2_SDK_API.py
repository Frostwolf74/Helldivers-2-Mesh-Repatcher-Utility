import bpy

def create_patch():
    """
    Creates a new patch from the base archive
    """
    bpy.ops.helldiver2.archive_createpatch()

def write_patch():
    bpy.ops.helldiver2.archive_export()

def export_patch(filepath):
    bpy.ops.helldiver2.export_patch(filepath=filepath)

def save_meshes():
    bpy.ops.helldiver2.archive_mesh_batchsave()
    
    



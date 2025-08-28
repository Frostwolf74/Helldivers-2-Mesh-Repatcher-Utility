import bpy
import asyncio

# active object
AO = bpy.context.active_object

def create_patch():
    """
    Creates a new patch from the base archive
    """
    bpy.ops.helldiver2.archive_createpatch()
    
    # bpy.ops.HD2SDK.CreatePatchFromActiveOperator().execute()
    #HD2SDK.CreatePatchFromActiveOperator().execute()
    pass

def load_patch_by_name():
    """
    Unconfigured
    """
    pass

def write_patch():
    bpy.ops.helldiver2.archive_export()

def export_patch(filepath):
    bpy.ops.helldiver2.export_patch(filepath=filepath)

    #HD2SDK.ExportPatchAsZipOperator(ExportHelper).execute()

def load_archive_by_name():
    """
    Unconfigured
    """
    pass

def save_meshes():
    # bpy.ops.helldiver2.archive_mesh_save() 
    bpy.ops.helldiver2.archive_mesh_batchsave()
    
    #HD2SDK.BatchSaveStingrayMeshOperator().execute()
    


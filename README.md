# Helldivers 2 Mesh Repatcher Utility
## Usage
Open blender with the HD2 SDK installed, go to the scripting tab and import the script.py file. Populate `id_list` with a list of Object IDs corresponding to a Helldivers 2 mesh to replace (only tested with helmets so far).

 Run the script and allow it to finish, then export the patch manually, attempting to do this automatically will create a patch that will crash the game. All meshes from `id_list` will be merged into a single patch that can be used immediately.

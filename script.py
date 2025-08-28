import bpy
import HD2_SDK_API as API

# create patch
API.create_patch()

id_list = [
        13556064353924354700, 4131421001356999706, 3954130796314399534, 
        8399161923851875572, 11313096106785347680, 7601348670501265665, 
        8678656197582665224, 7902265795160533902, 12730382597307458442, 
        13254993767511698164, 8648711675149544067, 16001723592336083491, 
        15819689819915417733, 10583934180552236525, 17438525524839299421, 
        7876815139290439352, 6075028763446045879, 7341024049703618466, 
        5252955854116479892, 3148179888321948003, 17016371081593995329, 
        6469607965781156094, 3910569372330332832, 14676861962345020465, 
        18429449806859828280, 8379182691508484484, 10683583799272006843, 
        862174694943184392, 5555255822099584608, 9396741587218288497, 
        230434125355632415, 18435226424678019495, 4541334684346792740, 
        1619799062283423855, 5574513890160481015, 7648023769279353857, 
        13556064353924354700, 13135626165718134923, 9689159159731344788, 
        7285925993452441626, 2123465521732463246, 13164148178108423800
]

names = [
        "B-01 Tactical (Variation 1)",
        "B-08 Light Gunner",
        "B-24 Enforcer",
        "B-27 Fortified Commando",
        "CE-101 Guerilla Gorilla",
        "CE-27 Ground Breaker",
        "CE-35 Trench Engineer",
        "CE-64 Grenadier",
        "CE-67 Titan",
        "CE-74 Breaker",
        "CE-81 Juggernaut",
        "CM-09 Bonesnapper",
        "CM-14 Physician",
        "CM-17 Butcher",
        "CW-22 Kodiak",
        "CW-36 Winter Warrior",
        "CW-4 Arctic Ranger",
        "CW-9 White Wolf",
        "DP-11 Champion of the People",
        "DP-40 Hero of the Federation",
        "DP-53 Savior of the Free",
        "EX-00 Prototype X",
        "EX-03 Prototype 3",
        "EX-16 Prototype 16",
        "FS-05 Marksman",
        "FS-11 Executioner",
        "FS-23 Battle Master - TR-62 Knight",
        "FS-34 Exterminator",
        "FS-37 Ravager",
        "FS-38 Eradicator",
        "FS-55 Devastator",
        "FS-61 Dreadnought",
        "PH-202 Twigsnapper",
        "PH-56 Jaguar",
        "PH-9 Predator",
        "SA-04 Combat Technician",
        "SA-25 Steel Trooper",
        "SA-32 Dynamo",
        "SC-15 Drone Master",
        "SC-30 Trailblazer Scout",
        "SC-37 Legionaire",
        "SR-24 Street Scout"
]

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

    # # export patch  
    # try:
    #     API.export_patch("F:/export/prepped/" + names[i])
    # except Exception as e:
    #     # raise Exception(str(e))
    #     print("Warning, ignoring exception: " + str(e))
    #     continue

    
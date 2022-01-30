import re
import bpy
bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}


class SelectByQuery(bpy.types.Operator):
    bl_idname = "object.select_by_query"
    bl_label = "Selection of object by query"

    def execute(self, context):
        try:
            pattern = re.compile(context.scene.regex)
            for object in bpy.data.objects:
                match = pattern.match(object.name)
                if match is not None:
                    object.select_set(True)
            return {'FINISHED'}
        except:
            return {'CANCELLED'}


PROPS = [
    ('regex', bpy.props.StringProperty(name='Regex'))
]


class PanelThree(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_SelectionQuery"
    bl_label = "Selection Query"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        for name, value in PROPS:
            row = col.row()
            row.prop(context.scene, name)
        col.operator("object.select_by_query", text='select')


CLASSES = [PanelThree, SelectByQuery]


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)


def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)
    for (prop_name, prop_value) in PROPS:
        delattr(bpy.types.Scene, prop_name)


if __name__ == "__main__":
    register()

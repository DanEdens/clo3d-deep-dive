from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *

#If you want to load your python file, please type "sys.path.append(input path where file is located here)" in console.
#ex) sys.path.append("C:/Users/Young/Downloads/") or sys.path.append("C:\\\\Users\\\\Young\\\\Downloads\\\\")
class example():
    mdsa = None
    avatar_listWidget = None
    garment_listWidget = None
    animation_listWidget = None
    save_listWidget = None
    avatar_ext_comboBox = None
    garment_ext_comboBox = None
    animation_ext_comboBox = None
    save_ext_comboBox = None
    widget = None
    save_folder_path = ""

    #this function is an exmaple of single process
    #single process defines a series of actions, which is 'set an option' .'set a path to be loaded'.'set a simulation option'.'set a save path'.'call a processing function'.
    #You can designate the path for each file you want to load.
    #Also You can designate a save path for each file
    #object is mdsa (MarvelousDesigner Script API)
    def run_single_process_example(self, object): 
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize() 
        #set exporting option
        object.set_open_option("mm", 30) 
        #set importing option
        object.set_save_option("mm", 30, False)
        #set Alembic Format True = Ogawa, False = hdf5. Default is hdf5. (This function is only valid when exporting alembic file.)
        object.set_alembic_format_type(True)
        #Set the path of an Avatar file you want to load.
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")
        #Set simulation option.
        object.set_simulation_options(0, 0, 5000) 
        #Set the saving file path.
        object.set_save_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\test_01.abc")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(True)
        #If you finish setting file paths and options. You must call process function.
        object.process() 

    #this function is anohter exmaple for single process 
    #call 'single_process' function with the each file path, options and paths to save file
    #also designate the folder where the files will be stored.
    def run_single_process_second_example(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize() 
        #set exporting option
        object.set_open_option("cm", 30)
        #set importing option
        object.set_save_option("mm", 30, False) 
        #designate the folder where the files will be stored and file extension setting
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999", "mc") 
        #call the "single_process" function
        object.single_process(
            "C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\default.zpac",
            "C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt",
            "C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Pose\\Female_A\\F_A_pose_02_attention.pos") 

    #this function is example for multi process 
    def run_multi_example(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")

        #object.set_export_unified_uv_texcoordnate(True, 1000, 5)

        #In case want to simulate/record one garment and avatar with multiple animation
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\ambient_test.zpac")

        #set path of one avatar file
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")
        #set folder path of multiple animation folder and extension (file extension must be supported by Marvelous Designer)
        object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Pose\\Female_A", "pos")
        #set save folder and extension (file extension must be supported by Marvelous Designer)
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "fbx")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    #this function is example for multi process 
    def fbx(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")

        object.set_export_unified_uv_texcoordnate(True, 1000, 5)

        #In case want to simulate/record one garment and avatar with multiple animation
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\ambient_test.zpac")

        #set path of one avatar file
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")
        #set folder path of multiple animation folder and extension (file extension must be supported by Marvelous Designer)
        object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Pose\\Female_A", "pos")
        #set save folder and extension (file extension must be supported by Marvelous Designer)
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "abc")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    #this function is example for multi process 
    def run_example_simulation(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")
        
        #Set simulation property settings
        #Set Simulation property options(simulation quality) of integer type
        # qulity = 0 Complete
        # qulity = 1 Normal
        # qulity = 2 Custom
        object.set_simulation_quality(2)
        #Set Simulation property options(simulation time step) of floating point type
        object.set_simulation_time_step(0.030000)
        #Set Simulation property options(number of simulation) of integer type
        object.set_simulation_number_of_simulation(2)
        #Set Simulation property options(simulation cg finish condition type) of integer type
        # cg finish condition type = 0 ITERATION
        # cg finish condition type = 1 RESIDUAL
        object.set_simulation_cg_finish_condition(0)
        #Set Simulation property options(simulation cg iteration count) of integer type
        object.set_simulation_cg_iteration_count(40)
        #Set Simulation property options(simulation cg residual) of floating point type
        #object.on_simulation_cg_residual(0.00020)
        #Set Simulation property options(self collision iteration count) of integer type
        object.set_simulation_self_collision_iteration_count(2)
        #Set Simulation property options(air damping) of floating point type
        object.set_simulation_air_damping(2.0)
        #Set Simulation property options(gravity) of floating point type
        object.set_simulation_gravity(-9000.00)
        #Set Simulation property options(number of CPU in use) of integer type
        object.set_simulation_number_of_cpu_in_use(3)
        #Set Simulation property options(nonlinear simulation) of boolean type
        object.set_simulation_nonlinear_simulation(True)
        #Set Simulation property options(ground collision) of boolean type
        object.set_simulation_ground_collision(False)
        #Set Simulation property options(ground height) of floating point type
        object.set_simulation_ground_height(2.0)
        #Set Simulation property options(avatar-cloth collision detection triangle-vertex) of boolean type
        object.set_simulation_avatar_cloth_collision_detection_triangle_vertex(False)
        #Set Simulation property options(self collision detection triangle-vertex) of boolean type
        object.set_simulation_self_collision_detection_trianlge_vertex(False)
        #Set Simulation property options(self collision detection edge-edge) of boolean type
        object.set_simulation_self_collision_detection_edge_edge(False)
        #Set Simulation property options(self collision detection avoidance stiffness) of floating point type
        object.set_simulation_self_collision_detection_avoidance_stiffness(0.001111)
        #Set Simulation property options(proximity detection vertex-triangle) of boolean type
        object.set_simulation_proximity_detection_vertex_triangle(False)
        #Set Simulation property options(proximity detection edge-edge) of boolean type
        object.set_simulation_proximity_detection_edge_edge(False)
        #Set Simulation property options(intersection resolution) of boolean type
        object.set_simulation_intersection_resolution(False)
        #Set Simulation property options(layer based collision detection) of boolean type
        object.set_simulation_layer_based_collision_detection(False)

        #In case want to simulate/record one garment and avatar with multiple animation
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\Women_Set.zpac")

        #set path of one avatar file
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")
        #set folder path of multiple animation folder and extension (file extension must be supported by Marvelous Designer)
        object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Pose\\Female_A", "pos")
        #set save folder and extension (file extension must be supported by Marvelous Designer)
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "obj")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    #this function is example for multi process 
    def run_example_windcontroller(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")

        #Set wind controller settings
        #Set wind controller property options(activate) of boolean type
        object.set_windcontroller_wind_activate(True)
        #Set wind controller property options(wind type) of integer type
        object.set_windcontroller_wind_type(1)
        #Set wind controller property options(wind strength) of integer type
        object.set_windcontroller_wind_strength(5500)
        #Set wind controller property options(wind decay) of integer type
        object.set_windcontroller_wind_decay(0)
        #Set wind controller property options(wind frequency) of floating point type
        object.set_windcontroller_wind_frequency(0.0)
        #Set wind controller property options(wind turbulence) of integer type
        object.set_windcontroller_wind_turbulence(30)
        #Set wind controller property options(translate) of floating point type
        object.set_windcontroller_translate_x(-262.47)
        object.set_windcontroller_translate_y(1000.00)
        object.set_windcontroller_translate_z(612.41)

        #In case want to simulate/record one garment and avatar with multiple animation
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\Women_Set.zpac")

        #set path of one avatar file
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")

        #set folder path of multiple animation folder and extension (file extension must be supported by Marvelous Designer)
        object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Pose\\Female_A", "pos")

        #set save folder and extension (file extension must be supported by Marvelous Designer)
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "obj")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    #this function is example for multi process 
    def run_multi_example_with_obj_exoprt_option(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")

        #Set exporting options (only export option)
        object.on_export_garment_with_relative_objects_only()

        #Set exporting options (multi object option)
        object.on_export_multi_object()
        #Set exporting options (weld option)
        object.on_export_weld()
        #Set exporting options (thick option)
        object.on_export_thick()

        #Set exporting options (unified UV coordinates option)
        # first value : Unified Textures of boolean type
        # second value : Texture Size(Width & Height) of integer type
        # third value : Fill Texture Seams of integer type
        object.set_export_unified_uv_texcoordnate(True, 1000, 5)

        #Set exporting options (include inner shape option)
        #object.on_export_include_inner_shape()
        #Set exporting options (save with texture files(ZIP) option)
        #object.on_export_save_with_texture()
        #Set exporting options (save with meta data(XML) option)
        #object.on_export_save_meta_data()
        #Set exporting options (Diffuse Color Combined on Texture option)
        object.on_export_diffuse_color_combined()
        #Set exporting options (Exclude Ambient Color option)
        object.on_export_exclude_ambient_color()

        #Set exporting options (Axis Conversion option) of string type
        object.set_export_axis_x("Y")
        object.set_export_axis_y("Z")
        object.set_export_axis_z("X")

        #Set exporting options (Axis Invert option)
        object.on_export_invert_x()
        object.on_export_invert_y()
        object.on_export_invert_z()

        #In case want to simulate/record one garment and avatar with multiple animation
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\Women_Set.zpac")

        #set path of one avatar file
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")
        #set save folder and extension (file extension must be supported by Marvelous Designer)
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "obj")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    #this function is example for multi process 
    def example_change_axis(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")

        #Set exporting options (Axis Conversion option) of string type
        object.set_export_axis_x("X")
        object.set_export_axis_y("Z")
        object.set_export_axis_z("Y")

        #In case want to simulate/record one garment and avatar with multiple animation
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\Women_Set.zpac")

        #set path of one avatar file
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Avatar\\Avatar\\Female_A_V3.avt")
        #set save folder and extension (file extension must be supported by Marvelous Designer)
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "obj")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    #this function is example for serial multiple process  
    def run_multi_second_example(self, object):
        # clear console window
        object.clear_console() 
        #initialize mdsa module
        object.initialize()
        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")
        #Set importing options (fps) of integer type
        object.set_import_fps(30)
        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")
        #Set exporting options (fps) of integer type
        object.set_export_fps(30)
        #Set exporting options (unified UV coordinates option) without unified textures
        #object.set_export_unified_uv_texcoordnate(False)
        #object.set_export_unified_uv_texcoordnate(True, 1000, 5)
        #Set exporting options (thin option)
        object.on_export_thin()
        #Set exporting options (unweld option)
        object.on_export_unweld()
        #Set Save Zpac File With MetaData 
        object.on_save_zprj_with_metadata_info(True, 9, 0)
        #set path of one garment file
        object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\Women_Set.zpac")
        #set path of one avatar file
        #alembic does not need an avatar file.
        #If you use a different format, delete "#"
        #set folder path of multiple animation folder and extension (file extension must be supported by Marvelous Designer)
        object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999", "abc")
        #must call object.sync_file_lists for serial multiple process
        object.sync_file_lists("animation")
        #next multi process
        #object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\Women_Set.zpac")
        #object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\pose02", "abc")
        #object.sync_file_lists("animation")
        #next multi process
        #object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\T-shirt_men.zpac")
        #object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\pose02", "abc")
        #object.sync_file_lists("animation")
        #next multi process
        #object.set_garment_file_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Garment\\T-shirt_men.zpac")
        #object.set_animation_folder("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\pose02", "abc")
        #object.sync_file_lists("animation")
        #setting file path for serial multiple process is done, designate path for save and extension
        object.set_save_folder_path("C:\\Users\\Public\\Documents\\MarvelousDesigner\\Assets_ver_3.0.9999\\Output", "mc")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(False)
        #Call the "process" function
        object.process()

    def set_mdsa(self, object):
            self.mdsa = object

    def gui_example(self, object):
        self.set_mdsa(object)
        dialog = QtGui.QDialog()
        dialog.setObjectName("dialog")
        dialog.resize(858, 555)
        
        gridLayout_5 = QtGui.QGridLayout(dialog)
        gridLayout_5.setObjectName("gridLayout_5")

        avatar_groupBox = QtGui.QGroupBox(dialog)
        avatar_groupBox.setObjectName("save_groupBox")

        gridLayout = QtGui.QGridLayout(avatar_groupBox)
        gridLayout.setObjectName("gridLayout")

        avatar_load_toolButton = QtGui.QToolButton(avatar_groupBox)
        avatar_load_toolButton.setObjectName("avatar_load_toolButton")

        gridLayout.addWidget(avatar_load_toolButton, 0, 0, 1, 1)

        avatar_refresh_toolButton = QtGui.QToolButton(avatar_groupBox)
        avatar_refresh_toolButton.setObjectName("avatar_refresh_toolButton")

        gridLayout.addWidget(avatar_refresh_toolButton, 0, 1, 1, 1)

        self.avatar_ext_comboBox = QtGui.QComboBox(avatar_groupBox);
        self.avatar_ext_comboBox.setObjectName("avatar_ext_comboBox");
        self.avatar_ext_comboBox.clear();
        self.avatar_ext_comboBox.insertItem(0, "avt")
        self.avatar_ext_comboBox.insertItem(1, "obj")
        self.avatar_ext_comboBox.insertItem(2, "fbx")
        self.avatar_ext_comboBox.insertItem(3, "dae")

        gridLayout.addWidget(self.avatar_ext_comboBox, 0, 2, 1, 1);


        horizontalSpacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        gridLayout.addItem(horizontalSpacer, 0, 3, 1, 1)

        self.avatar_listWidget = QtGui.QListWidget(avatar_groupBox)
        self.avatar_listWidget.setObjectName("listWidget")

        gridLayout.addWidget(self.avatar_listWidget, 1, 0, 1, 3)

        gridLayout_5.addWidget(avatar_groupBox, 1, 0, 1, 1)

        garment_groupBox = QtGui.QGroupBox(dialog)
        garment_groupBox.setObjectName("laod_groupBox")
        gridLayout_2 = QtGui.QGridLayout(garment_groupBox);
        gridLayout_2.setObjectName("gridLayout_2")
        garment_load_toolButton = QtGui.QToolButton(garment_groupBox)
        garment_load_toolButton.setObjectName("garment_load_toolButton")

        gridLayout_2.addWidget(garment_load_toolButton, 0, 0, 1, 1)

        garment_refresh_toolButton = QtGui.QToolButton(garment_groupBox)
        garment_refresh_toolButton.setObjectName("garment_refresh_toolButton")

        gridLayout_2.addWidget(garment_refresh_toolButton, 0, 1, 1, 1)

        self.garment_ext_comboBox = QtGui.QComboBox(garment_groupBox);
        self.garment_ext_comboBox.setObjectName("garment_ext_comboBox");

        self.garment_ext_comboBox.clear();
        self.garment_ext_comboBox.insertItem(0, "zpac")
        self.garment_ext_comboBox.insertItem(1, "pac")

        gridLayout_2.addWidget(self.garment_ext_comboBox, 0, 2, 1, 1);

        horizontalSpacer_2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        gridLayout_2.addItem(horizontalSpacer_2, 0, 3, 1, 1)

        self.garment_listWidget = QtGui.QListWidget(garment_groupBox)
        self.garment_listWidget.setObjectName("garment_listWidget")

        gridLayout_2.addWidget(self.garment_listWidget, 1, 0, 1, 3)


        gridLayout_5.addWidget(garment_groupBox, 1, 1, 1, 1)

        animation_groupBox = QtGui.QGroupBox(dialog)
        animation_groupBox.setObjectName("animation_groupBox")

        gridLayout_3 = QtGui.QGridLayout(animation_groupBox)
        gridLayout_3.setObjectName("gridLayout_3")

        anim_load_toolButton = QtGui.QToolButton(animation_groupBox)
        anim_load_toolButton.setObjectName("anim_load_toolButton")

        gridLayout_3.addWidget(anim_load_toolButton, 0, 0, 1, 1)

        anim_refresh_toolButton = QtGui.QToolButton(animation_groupBox)
        anim_refresh_toolButton.setObjectName("anim_refresh_toolButton")
        gridLayout_3.addWidget(anim_refresh_toolButton, 0, 1, 1, 1)

        self.animation_ext_comboBox = QtGui.QComboBox(animation_groupBox);
        self.animation_ext_comboBox.setObjectName("animation_ext_comboBox");
        
        self.animation_ext_comboBox.clear();
        self.animation_ext_comboBox.insertItem(0, "pos")
        self.animation_ext_comboBox.insertItem(1, "mtn")
        self.animation_ext_comboBox.insertItem(2, "abc")
        self.animation_ext_comboBox.insertItem(3, "mc")
        self.animation_ext_comboBox.insertItem(4, "pc2")
        self.animation_ext_comboBox.insertItem(5, "mdd")

        gridLayout_3.addWidget(self.animation_ext_comboBox, 0, 2, 1, 1);

        horizontalSpacer_3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        gridLayout_3.addItem(horizontalSpacer_3, 0, 3, 1, 1)

        self.animation_listWidget = QtGui.QListWidget(animation_groupBox)
        self.animation_listWidget.setObjectName("animation_listWidget")

        gridLayout_3.addWidget(self.animation_listWidget, 1, 0, 1, 3)


        gridLayout_5.addWidget(animation_groupBox, 1, 2, 1, 1)

        save_groupBox = QtGui.QGroupBox(dialog)
        save_groupBox.setObjectName("save_groupBox")
        gridLayout_4 = QtGui.QGridLayout(save_groupBox)
        gridLayout_4.setObjectName("gridLayout_4")
        save_toolButton = QtGui.QToolButton(save_groupBox)
        save_toolButton.setObjectName("save_toolButton")

        gridLayout_4.addWidget(save_toolButton, 0, 0, 1, 1)

        self.save_ext_comboBox = QtGui.QComboBox(save_groupBox);
        self.save_ext_comboBox.setObjectName("save_ext_comboBox");

        self.save_ext_comboBox.clear();
        self.save_ext_comboBox.insertItem(0, "zprj")
        self.save_ext_comboBox.insertItem(1, "zpac")
        self.save_ext_comboBox.insertItem(2, "obj")
        self.save_ext_comboBox.insertItem(3, "fbx")
        self.save_ext_comboBox.insertItem(4, "abc")
        self.save_ext_comboBox.insertItem(5, "mc")
        self.save_ext_comboBox.insertItem(6, "pc2")
        self.save_ext_comboBox.insertItem(7, "mdd")

        gridLayout_4.addWidget(self.save_ext_comboBox, 0, 1, 1, 1);

        self.save_listWidget = QtGui.QListWidget(save_groupBox)
        self.save_listWidget.setObjectName("save_listWidget")

        gridLayout_4.addWidget(self.save_listWidget, 1, 0, 1, 2)

        horizontalSpacer_4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        gridLayout_4.addItem(horizontalSpacer_4, 0, 2, 1, 1)

        gridLayout_5.addWidget(save_groupBox, 2, 0, 1, 3)

        horizontalSpacer_5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        gridLayout_5.addItem(horizontalSpacer_5, 3, 0, 1, 1);
        
        process_button = QtGui.QPushButton(dialog)
        process_button.setObjectName("process_button")

        gridLayout_5.addWidget(process_button, 3, 1, 1, 1)

        cancel_button = QtGui.QPushButton(dialog)
        cancel_button.setObjectName("cancel_button")
        gridLayout_5.addWidget(cancel_button, 3, 2, 1, 1)

        horizontalSpacer_6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        gridLayout_5.addItem(horizontalSpacer_6, 3, 3, 1, 1);

        sync_button = QtGui.QToolButton(dialog);
        sync_button.setObjectName("sync_button");

        gridLayout_5.addWidget(sync_button, 0, 0, 1, 2);

        dialog.setWindowTitle("Dialog")
        avatar_groupBox.setTitle("Avatar")
        avatar_load_toolButton.setText("Load")
        avatar_refresh_toolButton.setText("Refresh")
        garment_groupBox.setTitle("Garement")
        garment_load_toolButton.setText("Load")
        garment_refresh_toolButton.setText("Refresh")
        animation_groupBox.setTitle("Animation")
        anim_refresh_toolButton.setText("Refresh")
        anim_load_toolButton.setText("Load")
        save_groupBox.setTitle("Save File")
        save_toolButton.setText("Save")
        process_button.setText("Process")
        cancel_button.setText("Cancel")
        sync_button.setText("Sync File List")

        process_button.connect("clicked(bool)", self.run_process)
        avatar_load_toolButton.connect("clicked(bool)", self.set_avatar_path_list)
        garment_load_toolButton.connect("clicked(bool)", self.set_garment_path_list)
        anim_load_toolButton.connect("clicked(bool)", self.set_animation_path_list)
        sync_button.connect("clicked(bool)", self.sync_file_list)
        avatar_refresh_toolButton.connect("clicked(bool)", self.refresh_avatar_list)
        garment_refresh_toolButton.connect("clicked(bool)", self.refresh_garment_list)
        anim_refresh_toolButton.connect("clicked(bool)", self.refresh_animation_list)
        save_toolButton.connect("clicked(bool)", self.set_save_path_list)
        cancel_button.connect("clicked(bool)", self.cancel)

        self.widget = dialog
        return dialog

    def cancel(self, flag):
        self.mdsa.open_avatar_file_list = []
        self.mdsa.open_garment_file_list = []
        self.mdsa.open_animation_file_list = []
        self.mdsa.save_folder_path = ""
        self.mdsa.save_file_extension = ""
        self.avatar_listWidget.clear()
        self.garment_listWidget.clear()
        self.animation_listWidget.clear()
        self.save_listWidget.clear()
        self.avatar_ext_comboBox.setCurrentIndex(0)
        self.garment_ext_comboBox.setCurrentIndex(0)
        self.animation_ext_comboBox.setCurrentIndex(0)
        self.save_ext_comboBox.setCurrentIndex(0)
        self.widget.hide()

    def recive_function(self):
        filter = self.mdsa.convert_qstring_to_py(str(raw_input(self.save_ext_comboBox.currentText())))
        file_list = self.mdsa.get_entry_list(self.save_folder_path)
       
        self.save_listWidget.clear()

        for char in file_list:
            fileInfo = QtCore.QFileInfo(char)
            fileName = fileInfo.fileName()
            item = QtGui.QListWidgetItem(self.save_listWidget)
            item.setData(32, char)
            item.setText(fileName)

    def run_process(self, flag):
        self.mdsa.set_recive_function(self.recive_function)
        self.mdsa.process()
    
    def set_avatar_path_list(self, flag):
        folder_path = QtGui.QFileDialog.getExistingDirectory(None, "Avatar Folder", QtGui.QFileDialog.ShowDirsOnly)
        filter = self.mdsa.convert_qstring_to_py(str(raw_input(self.avatar_ext_comboBox.currentText())))
        print(filter)
        self.mdsa.set_avatar_folder(folder_path, filter)
        file_list = self.mdsa.open_avatar_file_list
        
        for char in file_list:
            fileInfo = QtCore.QFileInfo(char)
            fileName = fileInfo.fileName()
            item = QtGui.QListWidgetItem(self.avatar_listWidget)
            item.setData(32, char)
            item.setText(fileName)

    def refresh_avatar_list(self, flag):
        self.mdsa.open_avatar_file_list = []
        self.set_avatar_path_list(flag)

    def set_garment_path_list(self, flag):
        folder_path = QtGui.QFileDialog.getExistingDirectory(None, "Garment Folder", QtGui.QFileDialog.ShowDirsOnly)

        filter = self.mdsa.convert_qstring_to_py(str(raw_input(self.garment_ext_comboBox.currentText())))
        print(filter)
        self.mdsa.set_garment_folder(folder_path, filter)
        
        file_list = self.mdsa.open_garment_file_list
        print(file_list)
        for char in file_list:
            fileInfo = QtCore.QFileInfo(char)
            fileName = fileInfo.fileName()
            item = QtGui.QListWidgetItem(self.garment_listWidget)
            item.setData(32, char)
            item.setText(fileName)

    def refresh_garment_list(self, flag):
        self.mdsa.open_garment_file_list = []
        self.set_garment_path_list(flag)

    def set_animation_path_list(self, flag):
        folder_path = QtGui.QFileDialog.getExistingDirectory(None, "Animation Folder", QtGui.QFileDialog.ShowDirsOnly)
        
        filter = self.mdsa.convert_qstring_to_py(str(raw_input(self.animation_ext_comboBox.currentText())))
        print(filter)
        self.mdsa.set_animation_folder(folder_path, filter)

        file_list = self.mdsa.open_animation_file_list

        for char in file_list:
            fileInfo = QtCore.QFileInfo(char)
            fileName = fileInfo.fileName()
            item = QtGui.QListWidgetItem(self.animation_listWidget)
            item.setData(32, char)
            item.setText(fileName)

    def refresh_animation_list(self, flag):
        self.mdsa.open_animation_file_list = []
        self.set_animation_path_list(flag)

    def sync_file_list(self, flag):
        bigger_list = "garment"
        max_count = len(self.mdsa.open_garment_file_list)
        if max_count < len(self.mdsa.open_avatar_file_list):
            max_count = len(self.mdsa.open_avatar_file_list)
            bigger_list = "avatar"
            if max_count < len(self.mdsa.open_animation_file_list):
                bigger_list = "animation"

        self.mdsa.sync_file_lists(bigger_list)

    def set_save_path_list(self, flag):
        folder_path = QtGui.QFileDialog.getExistingDirectory(None, "Save Folder", QtGui.QFileDialog.ShowDirsOnly)
        filter = self.mdsa.convert_qstring_to_py(str(raw_input(self.save_ext_comboBox.currentText())))
        self.mdsa.set_save_folder_path(folder_path, filter)
        self.save_folder_path = folder_path





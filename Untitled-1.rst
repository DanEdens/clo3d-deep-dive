**API List**
############


EXPORT_API
***********
 
.. tabs::

	.. code-tab:: python

		def ExportZPac() -> str
		"""
		@brief Export ZPac file in the CLO temporary folder
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportZPac()
		/// @brief Export ZPac file in the CLO temporary folder
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportZPac(_filePath : str) -> str
		"""
		@brief Export ZPac file
		@param string _filePath : target file path in ASCII
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportZPac(const string& _filePath)
		/// @brief Export ZPac file
		/// @param string _filePath : target file path in ASCII
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportZPacW(_filePath : str) -> str
		"""
		@brief Export ZPac file
		@param wstring _filePath : target file path in UNICODE
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportZPacW(const wstring& _filePath)
		/// @brief Export ZPac file
		/// @param wstring _filePath : target file path in UNICODE
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportZPrj() -> str
		"""
		@brief Export ZPrj file 
		@return Output file path; output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportZPrj()
		/// @brief Export ZPrj file 
		/// @return Output file path; output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportZPrj(_filePath : str) -> str
		"""
		@brief Export ZPrj file 
		@param _filePath: output file path
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportZPrj(const string& _filePath)
		/// @brief Export ZPrj file 
		/// @param _filePath: output file path
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportZPrj(_filePath : str, _bCreateThumbnail : bool) -> str
		"""
		@brief Export ZPrj file 
		@param _filePath: output file path
		@param _bCreateThumbnail: if _bCreateThumbnail is true, 'png' file will be created along 'zprj' file.
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportZPrj(const string& _filePath, bool _bCreateThumbnail)
		/// @brief Export ZPrj file 
		/// @param _filePath: output file path
		/// @param _bCreateThumbnail: if _bCreateThumbnail is true, 'png' file will be created along 'zprj' file.
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportZPrjW(_filePath : str, _bCreateThumbnail : bool) -> str
		"""
		@brief Export ZPrj file 
		@param _filePath: output file path
		@param _bCreateThumbnail: if _bCreateThumbnail is true, 'png' file will be created along 'zprj' file.
		@return Output file path. If an error occurs, return empty wstring.
		"""

	.. code-tab:: c++

		 ExportZPrjW(const wstring& _filePath, bool _bCreateThumbnail)
		/// @brief Export ZPrj file 
		/// @param _filePath: output file path
		/// @param _bCreateThumbnail: if _bCreateThumbnail is true, 'png' file will be created along 'zprj' file.
		/// @return Output file path. If an error occurs, return empty wstring.


.. tabs::

	.. code-tab:: python

		def ExportOBJ() -> list[str]
		"""
		@brief Export OBJ file
		@param options If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportOBJ()
		/// @brief Export OBJ file
		/// @param options If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportOBJ(_filePath : str) -> list[str]
		"""
		@brief Export OBJ file
		@param _filePath: output file path
		@return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportOBJ()
		/// @brief Export OBJ file
		/// @param _filePath: output file path
		/// @return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportOBJ(_options : ImportExportOption) -> list[str]
		"""
		@brief Export OBJ file
		@param options: If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportOBJ(const Marvelous::ImportExportOption& _options)
		/// @brief Export OBJ file
		/// @param options: If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportOBJ(_filePath : str, _options : ImportExportOption) -> list[str]
		"""
		@brief Export OBJ file
		@param _filePath: output file path
		@param options: If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportOBJ(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Export OBJ file
		/// @param _filePath: output file path
		/// @param options: If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportOBJW(_filePath : str, _options : ImportExportOption) -> list[str]
		"""
		@brief Export OBJ file
		@param _filePath: output file path
		@param options: If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty wstring. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportOBJW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Export OBJ file
		/// @param _filePath: output file path
		/// @param options: If "options" is given, it exports OBJ according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. It outputs the file paths of an OBJ file and multiple MTL files for colorways. If the value "bSaveInZip" in ImportExportOption is true, it outputs a file path of a zipped file. If an error occurs, return empty wstring. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportGLTF(_filePath : str, _options : ImportExportOption, _bGLBinary : bool) -> list[str]
		"""
		@brief Export GLTF
		@param options: If "options" is given, it exports GLTF according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 ExportGLTF(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Export GLTF
		/// @param options: If "options" is given, it exports GLTF according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def ExportGLTFW(_filePath : str, _options : ImportExportOption, _bGLBinary : bool) -> list[str]
		"""
		@brief Export GLTFW
		@param options: If "options" is given, it exports GLTF according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 ExportGLTFW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Export GLTFW
		/// @param options: If "options" is given, it exports GLTF according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def ExportDXF() -> str
		"""
		@brief Export DXF file. This api call will display the dialog to set options
		@return Output file path. If an error occurs, return empty string. Output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportDXF()
		/// @brief Export DXF file. This api call will display the dialog to set options
		/// @return Output file path. If an error occurs, return empty string. Output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportDXF(_filePath : str) -> str
		"""
		@brief Export DXF file. This api call will display the dialog to set options
		@param _filePath: output file path to export dxf
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportDXF(const string& _filePath)
		/// @brief Export DXF file. This api call will display the dialog to set options
		/// @param _filePath: output file path to export dxf
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportDXF(_filePath : str, _exportOption : ExportDxfOption) -> str
		"""
		@brief Export DXF file without the option dialog. Param ExportDxfOption is applicable for the options.
		@param _filePath: output file path to export dxf
		@param _exportOption: options to export dxf file
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportDXF(const string& _filePath, const Marvelous::ExportDxfOption& _exportOption)
		/// @brief Export DXF file without the option dialog. Param ExportDxfOption is applicable for the options.
		/// @param _filePath: output file path to export dxf
		/// @param _exportOption: options to export dxf file
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportDXFW(_filePath : str, _exportOption : ExportDxfOption) -> str
		"""
		@brief Export DXF file without the option dialog. Param ExportDxfOption is applicable for the options.
		@param _filePath: output file path
		@param _exportOption: options to export dxf file
		@return Output file path. If an error occurs, return empty wstring. 
		"""

	.. code-tab:: c++

		 ExportDXF(const string& _filePath, const Marvelous::ExportDxfOption& _exportOption)
		/// @brief Export DXF file without the option dialog. Param ExportDxfOption is applicable for the options.
		/// @param _filePath: output file path
		/// @param _exportOption: options to export dxf file
		/// @return Output file path. If an error occurs, return empty wstring. 


.. tabs::

	.. code-tab:: python

		def ExportTechPack(_filePath : str, _exportOption : ExportTechpackOption) -> None
		"""
		@brief Export Tech Pack data in json file and associated image files.
		@param _filePath: output filepath; the filePath Should be given in "*.json" format
		@param _exportOption: options to export techpack(.json) file
		"""

	.. code-tab:: c++

		 ExportTechPack(const string& _filePath, const Marvelous::ExportTechpackOption& _exportOption)
		/// @brief Export Tech Pack data in json file and associated image files.
		/// @param _filePath: output filepath; the filePath Should be given in "*.json" format
		/// @param _exportOption: options to export techpack(.json) file


.. tabs::

	.. code-tab:: python

		def ExportTechPackW(_filepath : str, _exportOption : ExportTechpackOption) -> None
		"""
		@brief Export Tech Pack data in json file and associated image files.
		@param _filePath: output filepath; the filePath Should be given in "*.json" format
		@param _exportOption: options to export techpack(.json) file
		"""

	.. code-tab:: c++

		 ExportTechPackW(const wstring& _filepath, const Marvelous::ExportTechpackOption& _exportOption)
		/// @brief Export Tech Pack data in json file and associated image files.
		/// @param _filePath: output filepath; the filePath Should be given in "*.json" format
		/// @param _exportOption: options to export techpack(.json) file


.. tabs::

	.. code-tab:: python

		def ExportTechPackToStream(_outputImageFolderPath : str) -> str
		"""
		@brief Export Tech Pack data in string and associated image files.
		@param _outputImageFolderPath: get output folder path where the image files are located by ExportTechpack
		@return Output stream for JSON data with the output folder path at the first line. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportTechPackToStream(string& _outputImageFolderPath)
		/// @brief Export Tech Pack data in string and associated image files.
		/// @param _outputImageFolderPath: get output folder path where the image files are located by ExportTechpack
		/// @return Output stream for JSON data with the output folder path at the first line. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportTechPackToStreamW(_outputImageFolderPath : str) -> str
		"""
		@brief Export Tech Pack data in string and associated image files.
		@param _outputImageFolderPath: get output folder path where the image files are located by ExportTechpack
		@return Output stream for JSON data with the output folder path at the first line. If an error occurs, return empty wstring.
		"""

	.. code-tab:: c++

		 ExportTechPackToStreamW(wstring& _outputImageFolderPath)
		/// @brief Export Tech Pack data in string and associated image files.
		/// @param _outputImageFolderPath: get output folder path where the image files are located by ExportTechpack
		/// @return Output stream for JSON data with the output folder path at the first line. If an error occurs, return empty wstring.


.. tabs::

	.. code-tab:: python

		def ExportThumbnail3D() -> str
		"""
		@brief Export thumbnail of the current scene
		@return Output file path: output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportThumbnail3D()
		/// @brief Export thumbnail of the current scene
		/// @return Output file path: output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportThumbnail3D(_filePath : str) -> str
		"""
		@brief Export thumbnail of the current scene in the 3D Windows
		@param _filePath: output file path to save the screenshot
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportThumbnail3D(const string& _filePath)
		/// @brief Export thumbnail of the current scene in the 3D Windows
		/// @param _filePath: output file path to save the screenshot
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportThumbnail3DW(_filePath : str) -> str
		"""
		@brief Export thumbnail of the current scene in the 3D Windows
		@param _filePath: output file path to save the screenshot
		@return Output file path. If an error occurs, return empty wstring. 
		"""

	.. code-tab:: c++

		 ExportThumbnail3D(const string& _filePath)
		/// @brief Export thumbnail of the current scene in the 3D Windows
		/// @param _filePath: output file path to save the screenshot
		/// @return Output file path. If an error occurs, return empty wstring. 


.. tabs::

	.. code-tab:: python

		def ExportSnapshot3D(_filePath : str) -> list[ list [ str ] ]
		"""
		@brief Export snapshot images. This function displays the same dialog as CLO so that users can configure the snapshots. If user turns on the option "Save Separate Images", then series of images will be saved with the name followed by the postfix "_01", "_02", ...
		@param _filePath: output file path to save the screenshot
		@return Return the list of the path of output files per colorway. The first item of each array is the file path of the unified image. If filePath parameter is not given, output files will be created in CLO temporary folder.		
		"""

	.. code-tab:: c++

		 ExportSnapshot3D(const string& _filePath)
		/// @brief Export snapshot images. This function displays the same dialog as CLO so that users can configure the snapshots. If user turns on the option "Save Separate Images", then series of images will be saved with the name followed by the postfix "_01", "_02", ...
		/// @param _filePath: output file path to save the screenshot
		/// @return Return the list of the path of output files per colorway. The first item of each array is the file path of the unified image. If filePath parameter is not given, output files will be created in CLO temporary folder.		


.. tabs::

	.. code-tab:: python

		def ExportSnapshot3D() -> list[ list [ str ] ]
		"""
		@brief Export snapshot images. This function displays the same dialog as CLO so that users can configure the snapshots. If user turns on the option "Save Separate Images", then series of images will be saved with the name followed by the postfix "_01", "_02", ...				
		@return Return the list of the path of output files per colorway. The first item of each array is the file path of the unified image. If filePath parameter is not given, output files will be created in CLO temporary folder.		
		"""

	.. code-tab:: c++

		 ExportSnapshot3D()
		/// @brief Export snapshot images. This function displays the same dialog as CLO so that users can configure the snapshots. If user turns on the option "Save Separate Images", then series of images will be saved with the name followed by the postfix "_01", "_02", ...				
		/// @return Return the list of the path of output files per colorway. The first item of each array is the file path of the unified image. If filePath parameter is not given, output files will be created in CLO temporary folder.		


.. tabs::

	.. code-tab:: python

		def ExportSnapshot3DW(_filePath : str) -> list[ list [ str ] ]
		"""
		@brief Export snapshot images. This function displays the same dialog as CLO so that users can configure the snapshots. If user turns on the option "Save Separate Images", then series of images will be saved with the name followed by the postfix "_01", "_02", ...
		@param _filePath: output file path to save the screenshot
		@return Return the list of the path of output files per colorway. The first item of each array is the file path of the unified image. If filePath parameter is not given, output files will be created in CLO temporary folder.		
		"""

	.. code-tab:: c++

		 ExportSnapshot3DW(const wstring& _filePath)
		/// @brief Export snapshot images. This function displays the same dialog as CLO so that users can configure the snapshots. If user turns on the option "Save Separate Images", then series of images will be saved with the name followed by the postfix "_01", "_02", ...
		/// @param _filePath: output file path to save the screenshot
		/// @return Return the list of the path of output files per colorway. The first item of each array is the file path of the unified image. If filePath parameter is not given, output files will be created in CLO temporary folder.		


.. tabs::

	.. code-tab:: python

		def ExportCustomViewSnapshot(_targetFolderPath : str, _width : int, _height : int, _outputPrefix : str) -> list [ str ]
		"""
		@brief Export snapshot images of Custom View.
		@param _targetFolderPath: output folder path
		@param _width: image width for the snapshots
		@param _height: image height for the snapshots
		@param _outputPrefix: If you set the 'outputPrefix' as empty value - "", then the saved file names will start with the index in the custom view; or if you set the 'outputPrefix' as some letters, the saved file names will have it as the first letters.
		@return Return the list of the path of output files
		"""

	.. code-tab:: c++

		 ExportCustomViewSnapshot(const string& _targetFolderPath, unsigned int _width, unsigned int _height, string _outputPrefix = "")
		/// @brief Export snapshot images of Custom View.
		/// @param _targetFolderPath: output folder path
		/// @param _width: image width for the snapshots
		/// @param _height: image height for the snapshots
		/// @param _outputPrefix: If you set the 'outputPrefix' as empty value - "", then the saved file names will start with the index in the custom view; or if you set the 'outputPrefix' as some letters, the saved file names will have it as the first letters.
		/// @return Return the list of the path of output files


.. tabs::

	.. code-tab:: python

		def ExportCustomViewSnapshotW(_targetFolderPath : str, _width : int, _height : int, _outputPrefix : str) -> list [ str ]
		"""
		@brief Export snapshot images of Custom View.
		@param _targetFolderPath: output folder path
		@param _width: image width for the snapshots
		@param _height: image height for the snapshots
		@param _outputPrefix: If you set the 'outputPrefix' as empty value - "", then the saved file names will start with the index in the custom view; or if you set the 'outputPrefix' as some letters, the saved file names will have it as the first letters.
		@return Return the list of the path of output files
		"""

	.. code-tab:: c++

		 ExportCustomViewSnapshotW(const wstring& _targetFolderPath, unsigned int _width, unsigned int _height, wstring _outputPrefix = L"")
		/// @brief Export snapshot images of Custom View.
		/// @param _targetFolderPath: output folder path
		/// @param _width: image width for the snapshots
		/// @param _height: image height for the snapshots
		/// @param _outputPrefix: If you set the 'outputPrefix' as empty value - "", then the saved file names will start with the index in the custom view; or if you set the 'outputPrefix' as some letters, the saved file names will have it as the first letters.
		/// @return Return the list of the path of output files


.. tabs::

	.. code-tab:: python

		def ExportRenderingImage(_filePath : str) -> list[ list [ str ] ]
		"""
		@brief Export Rendering Image.
		@param _filePath: output file path
		@return Return the list of the path of output files per colorway. 
		"""

	.. code-tab:: c++

		 ExportRenderingImage(const string& _filePath)
		/// @brief Export Rendering Image.
		/// @param _filePath: output file path
		/// @return Return the list of the path of output files per colorway. 


.. tabs::

	.. code-tab:: python

		def ExportRenderingImage(_filePath : str, _bRenderAllColorways : bool) -> list[ list [ str ] ]
		"""
		@brief Export Rendering Image.
		@param _filePath: output file path
		@param _bRenderAllColorways: If true, output the images for all colorways. Otherwise, it returns the images for the current colorway specified by CLO user.
		@return Return the list of the path of output files per colorway. 
		"""

	.. code-tab:: c++

		 ExportRenderingImage(const string& _filePath, bool _bRenderAllColorways)
		/// @brief Export Rendering Image.
		/// @param _filePath: output file path
		/// @param _bRenderAllColorways: If true, output the images for all colorways. Otherwise, it returns the images for the current colorway specified by CLO user.
		/// @return Return the list of the path of output files per colorway. 


.. tabs::

	.. code-tab:: python

		def ExportRenderingImage(_bRenderAllColorways : bool) -> list[ list [ str ] ]
		"""
		@brief Export Rendering Image.
		@param _bRenderAllColorways: If true, output the images for all colorways. Otherwise, it returns the images for the current colorway specified by CLO user.
		@return Return the list of the path of output files per colorway. 
		"""

	.. code-tab:: c++

		 ExportRenderingImage(bool _bRenderAllColorways)
		/// @brief Export Rendering Image.
		/// @param _bRenderAllColorways: If true, output the images for all colorways. Otherwise, it returns the images for the current colorway specified by CLO user.
		/// @return Return the list of the path of output files per colorway. 


.. tabs::

	.. code-tab:: python

		def ExportRenderingImageW(_filePath : str, _bRenderAllColorways : bool) -> list[ list [ str ] ]
		"""
		@brief Export Rendering Image.
		@param _filePath: output file path
		@param _bRenderAllColorways: If true, output the images for all colorways. Otherwise, it returns the images for the current colorway specified by CLO user.
		@return Return the list of the path of output files per colorway. 
		"""

	.. code-tab:: c++

		 ExportRenderingImageW(const wstring& _filePath, bool _bRenderAllColorways)
		/// @brief Export Rendering Image.
		/// @param _filePath: output file path
		/// @param _bRenderAllColorways: If true, output the images for all colorways. Otherwise, it returns the images for the current colorway specified by CLO user.
		/// @return Return the list of the path of output files per colorway. 


.. tabs::

	.. code-tab:: python

		def ExportSingleColorwayRenderingImage(_filePath : str, _colorwayIndex : int) -> list [ str ]
		"""
		@brief Export Rendering Image for the colorway
		@param _filePath: output file path
		@param _colorwayIndex: colorway index to render the image
		@return Return the list of the path of output files
		"""

	.. code-tab:: c++

		 ExportSingleColorwayRenderingImage(const string& _filePath, unsigned int _colorwayIndex)
		/// @brief Export Rendering Image for the colorway
		/// @param _filePath: output file path
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Return the list of the path of output files


.. tabs::

	.. code-tab:: python

		def ExportSingleColorwayRenderingImage(_colorwayIndex : int) -> list [ str ]
		"""
		@brief Export Rendering Image for the colorway
		@param _colorwayIndex: colorway index to render the image
		@return Return the list of the path of output files; output files will be created in CLO temporary folder.		
		"""

	.. code-tab:: c++

		 ExportSingleColorwayRenderingImage(unsigned int _colorwayIndex)
		/// @brief Export Rendering Image for the colorway
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Return the list of the path of output files; output files will be created in CLO temporary folder.		


.. tabs::

	.. code-tab:: python

		def ExportSingleColorwayRenderingImageW(_filePath : str, _colorwayIndex : int) -> list [ str ]
		"""
		@brief Export Rendering Image for the colorway
		@param _filePath: output file path
		@param _colorwayIndex: colorway index to render the image
		@return Return the list of the path of output files		
		"""

	.. code-tab:: c++

		 ExportSingleColorwayRenderingImageW(const wstring& _filePath, unsigned int _colorwayIndex)
		/// @brief Export Rendering Image for the colorway
		/// @param _filePath: output file path
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Return the list of the path of output files		


.. tabs::

	.. code-tab:: python

		def GetTotalRenderImagePaths() -> list [ str ]
		"""
		@brief Get File name list for all the exported rendering images
		@return all the rendered image file paths
		"""

	.. code-tab:: c++

		 GetTotalRenderImagePaths()
		/// @brief Get File name list for all the exported rendering images
		/// @return all the rendered image file paths


.. tabs::

	.. code-tab:: python

		def GetTotalRenderImagePathsW() -> list [ str ]
		"""
		@brief Get File name list for all the exported rendering images
		@return all the rendered image file paths
		"""

	.. code-tab:: c++

		 GetTotalRenderImagePathsW()
		/// @brief Get File name list for all the exported rendering images
		/// @return all the rendered image file paths


.. tabs::

	.. code-tab:: python

		def GetCurrentRenderImagePaths() -> list [ str ]
		"""
		@brief Current Render Image paths
		@return all current renderded image files paths per colorways
		"""

	.. code-tab:: c++

		 GetCurrentRenderImagePaths()
		/// @brief Current Render Image paths
		/// @return all current renderded image files paths per colorways


.. tabs::

	.. code-tab:: python

		def GetCurrentRenderImagePathsW() -> list [ str ]
		"""
		@brief Current Render Image paths
		@return all current renderded image files paths per colorways
		"""

	.. code-tab:: c++

		 GetCurrentRenderImagePathsW()
		/// @brief Current Render Image paths
		/// @return all current renderded image files paths per colorways


.. tabs::

	.. code-tab:: python

		def GetFileNameOnRenderingProperty() -> str
		"""
		@return the output file names set on the Rendering Property in CLO
		"""

	.. code-tab:: c++

		 GetFileNameOnRenderingProperty()
		/// @return the output file names set on the Rendering Property in CLO


.. tabs::

	.. code-tab:: python

		def GetFileNameOnRenderingPropertyW() -> str
		"""
		@return the output file names set on the Rendering Property in CLO
		"""

	.. code-tab:: c++

		 GetFileNameOnRenderingPropertyW()
		/// @return the output file names set on the Rendering Property in CLO


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformation() -> str
		"""
		@brief Export garment information in json file. The information is the same as given in Garment Information Dialog in CLO (you can see this dialog by clicking File > Information > Garment menu in CLO)
		/@return Output file path. If an error occurs, return empty string; output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportGarmentInformation()
		/// @brief Export garment information in json file. The information is the same as given in Garment Information Dialog in CLO (you can see this dialog by clicking File > Information > Garment menu in CLO)
		//// @return Output file path. If an error occurs, return empty string; output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformation(_filePath : str) -> str
		"""
		@brief Export garment information in json file. The information is the same as given in Garment Information Dialog in CLO (you can see this dialog by clicking File > Information > Garment menu in CLO)
		@param _filePath output file path to export the garment information
		/@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportGarmentInformation(const string& _filePath)
		/// @brief Export garment information in json file. The information is the same as given in Garment Information Dialog in CLO (you can see this dialog by clicking File > Information > Garment menu in CLO)
		/// @param _filePath output file path to export the garment information
		//// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationW(_filePath : str) -> str
		"""
		@brief Export garment information in json file. The information is the same as given in Garment Information Dialog in CLO (you can see this dialog by clicking File > Information > Garment menu in CLO)
		@param _filePath output file path to export the garment information
		/@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportGarmentInformationW(const wstring& _filePath)
		/// @brief Export garment information in json file. The information is the same as given in Garment Information Dialog in CLO (you can see this dialog by clicking File > Information > Garment menu in CLO)
		/// @param _filePath output file path to export the garment information
		//// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationToStream() -> str
		"""
		@brief Export garment information in string
		@return Garment Information stream in sstring
		"""

	.. code-tab:: c++

		 ExportGarmentInformationToStream()
		/// @brief Export garment information in string
		/// @return Garment Information stream in sstring


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationToStreamW() -> str
		"""
		@brief Export garment information in string as well as json file
		@return Garment Information stream in wstring
		"""

	.. code-tab:: c++

		 ExportGarmentInformationToStreamW()
		/// @brief Export garment information in string as well as json file
		/// @return Garment Information stream in wstring


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationConfigData() -> str
		"""
		@brief Export garment information config data in json file. The information is the same as given in "Conf_Garment_Information.json" file via Preference
		@return Output file path; the output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportGarmentInformationConfigData()
		/// @brief Export garment information config data in json file. The information is the same as given in "Conf_Garment_Information.json" file via Preference
		/// @return Output file path; the output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationConfigData(_filePath : str) -> str
		"""
		@brief Export garment information config data in json file. The information is the same as given in "Conf_Garment_Information.json" file via Preference
		@param _filePath output file path to export the garment information configuration data
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportGarmentInformationConfigData(const string& _filePath)
		/// @brief Export garment information config data in json file. The information is the same as given in "Conf_Garment_Information.json" file via Preference
		/// @param _filePath output file path to export the garment information configuration data
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationConfigDataW(_filePath : str) -> str
		"""
		@brief Export garment information config data in json file. The information is the same as given in "Conf_Garment_Information.json" file via Preference
		@param _filePath output file path to export the garment information configuration data
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportGarmentInformationConfigDataW(const wstring& _filePath)
		/// @brief Export garment information config data in json file. The information is the same as given in "Conf_Garment_Information.json" file via Preference
		/// @param _filePath output file path to export the garment information configuration data
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationConfigDataToStream() -> str
		"""
		Export garment information configuration data in string
		@return Output stream for JSON data. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportGarmentInformationConfigDataToStream()
		Export garment information configuration data in string
		/// @return Output stream for JSON data. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportGarmentInformationConfigDataToStreamW() -> str
		"""
		Export garment information configuration data in string
		@return Output stream for JSON data. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportGarmentInformationConfigDataToStreamW()
		Export garment information configuration data in string
		/// @return Output stream for JSON data. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportTurntableVideo() -> str
		"""
		@brief Export turntable video. This function requires XVid Mpeg-4 codec installed on user's computer.
		@return Output file path; output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportTurntableVideo()
		/// @brief Export turntable video. This function requires XVid Mpeg-4 codec installed on user's computer.
		/// @return Output file path; output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportTurntableVideo(_filePath : str) -> str
		"""
		@brief Export turntable video. This function requires XVid Mpeg-4 codec installed on user's computer.
		@param _filePath 
		@return Output file path; output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportTurntableVideo(const string& _filePath)
		/// @brief Export turntable video. This function requires XVid Mpeg-4 codec installed on user's computer.
		/// @param _filePath 
		/// @return Output file path; output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportTurntableVideoW(_filePath : str) -> str
		"""
		@brief Export turntable video. This function requires XVid Mpeg-4 codec installed on user's computer.
		@return Output file path; output files will be created in CLO temporary folder. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportTurntableVideoW(const wstring& _filePath)
		/// @brief Export turntable video. This function requires XVid Mpeg-4 codec installed on user's computer.
		/// @return Output file path; output files will be created in CLO temporary folder. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportAnimationVideo() -> str
		"""
		@brief Export animation video. This function requires XVid Mpeg-4 codec installed on user's computer.
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportAnimationVideo()
		/// @brief Export animation video. This function requires XVid Mpeg-4 codec installed on user's computer.
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportAnimationVideo(_filePath : str) -> str
		"""
		@brief Export animation video. This function requires XVid Mpeg-4 codec installed on user's computer.
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportAnimationVideo()
		/// @brief Export animation video. This function requires XVid Mpeg-4 codec installed on user's computer.
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportAnimationVideoW(_filePath : str) -> str
		"""
		@brief Export animation video. This function requires XVid Mpeg-4 codec installed on user's computer.
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportAnimationVideo()
		/// @brief Export animation video. This function requires XVid Mpeg-4 codec installed on user's computer.
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def GetColorwayCount() -> int
		"""
		///////////////////////////////////////////////////////////////////
		@fn GetColorwayCount()
		@brief Get the number of colorways in the current garment loaded in CLO
		@return total count of colorways				
		"""

	.. code-tab:: c++

		
		///////////////////////////////////////////////////////////////////
		/// @fn GetColorwayCount()
		/// @brief Get the number of colorways in the current garment loaded in CLO
		/// @return total count of colorways				


.. tabs::

	.. code-tab:: python

		def GetCurrentColorwayIndex() -> int
		"""
		@brief Get the index of the current colorway in CLO
		@return the current colorway index
		"""

	.. code-tab:: c++

		 GetCurrentColorwayIndex()
		/// @brief Get the index of the current colorway in CLO
		/// @return the current colorway index


.. tabs::

	.. code-tab:: python

		def GetColorwayNameList() -> list[str]
		"""
		@brief Get all the colorway names for the current garment 
		@return the list of name of all colorways
		"""

	.. code-tab:: c++

		 GetColorwayNameList()
		/// @brief Get all the colorway names for the current garment 
		/// @return the list of name of all colorways


.. tabs::

	.. code-tab:: python

		def GetColorwayNameListW() -> list[str]
		"""
		@brief Get all the colorway names for the current garment 
		@return the list of name of all colorways
		"""

	.. code-tab:: c++

		 GetColorwayNameListW()
		/// @brief Get all the colorway names for the current garment 
		/// @return the list of name of all colorways


.. tabs::

	.. code-tab:: python

		def GetAvatarCount() -> int
		"""
		@brief Get the number of avatars loaded in CLO
		@return total count of avatars				
		"""

	.. code-tab:: c++

		 GetAvatarCount()
		/// @brief Get the number of avatars loaded in CLO
		/// @return total count of avatars				


.. tabs::

	.. code-tab:: python

		def GetAvatarNameList() -> list[str]
		"""
		@brief Get all the names of avatars loaded in CLO
		@return the list of name of all avatars
		"""

	.. code-tab:: c++

		 GetAvatarNameList()
		/// @brief Get all the names of avatars loaded in CLO
		/// @return the list of name of all avatars


.. tabs::

	.. code-tab:: python

		def GetAvatarNameListW() -> list[str]
		"""
		@brief Get all the names of avatars loaded in CLO
		@return the list of name of all avatars
		"""

	.. code-tab:: c++

		 GetAvatarNameListW()
		/// @brief Get all the names of avatars loaded in CLO
		/// @return the list of name of all avatars


.. tabs::

	.. code-tab:: python

		def GetAvatarGenderList() -> list[int]
		"""
		@brief Get all the genders of avatars loaded in CLO repectively
		@return the list of gender of all avatars. 0 : male, 1 : female, -1: unknown
		"""

	.. code-tab:: c++

		 GetAvatarGenderList()
		/// @brief Get all the genders of avatars loaded in CLO repectively
		/// @return the list of gender of all avatars. 0 : male, 1 : female, -1: unknown


.. tabs::

	.. code-tab:: python

		def GetSizeCount() -> int
		"""
		@brief Get the number of sizes/gradings
		@return total count of sizes/gradings
		"""

	.. code-tab:: c++

		 GetSizeCount()
		/// @brief Get the number of sizes/gradings
		/// @return total count of sizes/gradings


.. tabs::

	.. code-tab:: python

		def GetCurrentSizeIndex() -> int
		"""
		@brief Get the index of the current size/grading
		@return the current index of size/grading
		"""

	.. code-tab:: c++

		 GetCurrentSizeIndex()
		/// @brief Get the index of the current size/grading
		/// @return the current index of size/grading


.. tabs::

	.. code-tab:: python

		def GetSizeNameList() -> list[str]
		"""
		@brief Get the index of the current size/grading
		@return the list of name of all sizes/gradings
		"""

	.. code-tab:: c++

		 GetSizeNameList()
		/// @brief Get the index of the current size/grading
		/// @return the list of name of all sizes/gradings


.. tabs::

	.. code-tab:: python

		def GetSizeNameListW() -> list[str]
		"""
		@brief Get the index of the current size/grading
		@return the list of name of all sizes/gradings
		"""

	.. code-tab:: c++

		 GetSizeNameListW()
		/// @brief Get the index of the current size/grading
		/// @return the list of name of all sizes/gradings


.. tabs::

	.. code-tab:: python

		def ExportTurntableImages(_numberOfImages : int) -> list[str]
		"""
		@brief Export turntable images for current colorway.
		@param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		@return Output file path list; output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportTurntableImages(int _numberOfImages)
		/// @brief Export turntable images for current colorway.
		/// @param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		/// @return Output file path list; output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportTurntableImages(_filePath : str, _numberOfImages : int, _width : int, _height : int) -> list[str]
		"""
		@brief Export turntable images for current colorway.
		@param _filePath: the output file path to export the turntable snapshots
		@param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		@param _width: image width for the snapshots
		@param _height: image height for the snapshots
		@return Output file path list. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportTurntableImages(const string& _filePath, int _numberOfImages, int _width = 2500, int _height = 2500) 
		/// @brief Export turntable images for current colorway.
		/// @param _filePath: the output file path to export the turntable snapshots
		/// @param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		/// @param _width: image width for the snapshots
		/// @param _height: image height for the snapshots
		/// @return Output file path list. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportTurntableImagesW(_filePath : str, _numberOfImages : int, _width : int, _height : int) -> list[str]
		"""
		@brief Export turntable images for current colorway.
		@param _filePath: the output file path to export the turntable snapshots
		@param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		@param _width: image width for the snapshots
		@param _height: image height for the snapshots
		@return Output file path list. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportTurntableImagesW(const wstring& _filePath, int _numberOfImages, int _width = 2500, int _height = 2500)
		/// @brief Export turntable images for current colorway.
		/// @param _filePath: the output file path to export the turntable snapshots
		/// @param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		/// @param _width: image width for the snapshots
		/// @param _height: image height for the snapshots
		/// @return Output file path list. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportGLB(_filePath : str, _options : ImportExportOption) -> list[str]
		"""
		@brief Export GLB
		@param options: If "options" is given, it exports GLB according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 ExportGLB(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Export GLB
		/// @param options: If "options" is given, it exports GLB according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def ExportGLBW(_filePath : str, _options : ImportExportOption) -> list[str]
		"""
		@brief Export GLBW
		@param options: If "options" is given, it exports GLB according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 ExportGLBW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Export GLBW
		/// @param options: If "options" is given, it exports GLB according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def ExportGLTFAsFabric() -> list[str]
		"""
		@brief Export gltf/glb which cotains the fabric data selected in the object browser
		@return Output file path;output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportGLTFAsFabric()
		/// @brief Export gltf/glb which cotains the fabric data selected in the object browser
		/// @return Output file path;output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportGLTFAsFabric(_filePath : str) -> list[str]
		"""
		@brief Export gltf/glb which cotains the fabric data selected in the object browser
		@param _filePath: output file path
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportGLTFAsFabric(const string& _filePath)
		/// @brief Export gltf/glb which cotains the fabric data selected in the object browser
		/// @param _filePath: output file path
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportGLTFAsFabric(_filePath : str, index : int) -> list[str]
		"""
		@brief Export gltf/glb which cotains the fabric data in the index of the object browser
		@param _filePath: output file path
		@param index: target fabric index on the object browser to export
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportGLTFAsFabric(const string& _filePath, const int& index)
		/// @brief Export gltf/glb which cotains the fabric data in the index of the object browser
		/// @param _filePath: output file path
		/// @param index: target fabric index on the object browser to export
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportGLTFAsFabricW(_filePath : str, index : int) -> list[str]
		"""
		@brief Export gltf/glb file which cotains the fabric data in the index of the object browser
		@param _filePath: output file path
		@param index: target fabric index on the object browser to export
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportGLTFAsFabricW(const wstring& _filePath, const int& index)
		/// @brief Export gltf/glb file which cotains the fabric data in the index of the object browser
		/// @param _filePath: output file path
		/// @param index: target fabric index on the object browser to export
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportPOM() -> str
		"""
		@brief Export POM
		@return Output file path;output file will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportPOM(()
		/// @brief Export POM
		/// @return Output file path;output file will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportPOM(_filePath : str) -> str
		"""
		@brief Export POM
		@param _filePath: output file path
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportPOM(const string& _filePath)
		/// @brief Export POM
		/// @param _filePath: output file path
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportPOMW(_filePath : str) -> str
		"""
		@brief Export POM
		@param _filePath: output file path		
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportPOM(const wstring& _filePath)
		/// @brief Export POM
		/// @param _filePath: output file path		
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportPOM(_bInclude3DLength : bool) -> str
		"""
		@brief Export POM
		@param _bInclude3DLength, true: include 3D info, false: exclude 3D info 
		@return Output file path;output file will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportPOM(()
		/// @brief Export POM
		/// @param _bInclude3DLength, true: include 3D info, false: exclude 3D info 
		/// @return Output file path;output file will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportPOM(_bInclude3DLength : bool, _filePath : str) -> str
		"""
		@brief Export POM
		@param _filePath: output file path, _bInclude3DLength, true: include 3D info, false: exclude 3D info 
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportPOM(const string& _filePath)
		/// @brief Export POM
		/// @param _filePath: output file path, _bInclude3DLength, true: include 3D info, false: exclude 3D info 
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportPOMW(_bInclude3DLength : bool, _filePath : str) -> str
		"""
		@brief Export POM
		@param _filePath: output file path, _bInclude3DLength, true: include 3D info, false: exclude 3D info 		
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportPOM(const wstring& _filePath)
		/// @brief Export POM
		/// @param _filePath: output file path, _bInclude3DLength, true: include 3D info, false: exclude 3D info 		
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportGLTFWithDialog(_filePath : str, _bGLBinary : bool) -> list[str]
		"""
		@brief Export GLTF with Dialog
		@param _filePath: output file path
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 ExportGLTFWithDialog(const string& _filePath)
		/// @brief Export GLTF with Dialog
		/// @param _filePath: output file path
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def ExportGLBWithDialog(_filePath : str) -> list[str]
		"""
		@brief Export GLB with Dialog
		@param _filePath: output file path
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 ExportGLBWithDialog(const string& _filePath)
		/// @brief Export GLB with Dialog
		/// @param _filePath: output file path
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def ExportThumbnail3DByColorwayIndex(_colorwayIndex : int) -> str
		"""
		@brief Export thumbnail of the current scene
		@param _colorwayIndex: colorway index to render the image
		@return Output file path: output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportThumbnail3DByColorwayIndex(unsigned int _colorwayIndex)
		/// @brief Export thumbnail of the current scene
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Output file path: output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportThumbnail3DByColorwayIndex(_filePath : str, _colorwayIndex : int) -> str
		"""
		@brief Export thumbnail of the current scene in the 3D Windows
		@param _filePath: output file path to save the screenshot
		@param _colorwayIndex: colorway index to render the image
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportThumbnail3DByColorwayIndex(const string& _filePath, unsigned int _colorwayIndex)
		/// @brief Export thumbnail of the current scene in the 3D Windows
		/// @param _filePath: output file path to save the screenshot
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportThumbnail3DWByColorwayIndexW(_filePath : str, _colorwayIndex : int) -> str
		"""
		@brief Export thumbnail of the current scene in the 3D Windows
		@param _filePath: output file path to save the screenshot
		@param _colorwayIndex: colorway index to render the image
		@return Output file path. If an error occurs, return empty wstring. 
		"""

	.. code-tab:: c++

		 ExportThumbnail3DByColorwayIndexW(const wstring& _filePath, unsigned int _colorwayIndex)
		/// @brief Export thumbnail of the current scene in the 3D Windows
		/// @param _filePath: output file path to save the screenshot
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Output file path. If an error occurs, return empty wstring. 


.. tabs::

	.. code-tab:: python

		def ExportTurntableImagesByColorwayIndex(_numberOfImages : int, _colorwayIndex : int) -> list[str]
		"""
		@brief Export turntable images for colorway.
		@param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		@param _colorwayIndex: colorway index to render the image
		@return Output file path list; output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportTurntableImagesByColorwayIndex(int _numberOfImages, unsigned int _colorwayIndex)
		/// @brief Export turntable images for colorway.
		/// @param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		/// @param _colorwayIndex: colorway index to render the image
		/// @return Output file path list; output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportTurntableImagesByColorwayIndex(_filePath : str, _numberOfImages : int, _colorwayIndex : int, _width : int, _height : int) -> list[str]
		"""
		@brief Export turntable images for colorway.
		@param _filePath: the output file path to export the turntable snapshots
		@param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		@param _colorwayIndex: colorway index to render the image
		@param _width: image width for the snapshots
		@param _height: image height for the snapshots
		@return Output file path list. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportTurntableImagesByColorwayIndex(const string& _filePath, int _numberOfImages, unsigned int _colorwayIndex, int _width = 2500, int _height = 2500) 
		/// @brief Export turntable images for colorway.
		/// @param _filePath: the output file path to export the turntable snapshots
		/// @param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		/// @param _colorwayIndex: colorway index to render the image
		/// @param _width: image width for the snapshots
		/// @param _height: image height for the snapshots
		/// @return Output file path list. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportTurntableImagesByColorwayIndexW(_filePath : str, _numberOfImages : int, _colorwayIndex : int, _width : int, _height : int) -> list[str]
		"""
		@brief Export turntable images for colorway.
		@param _filePath: the output file path to export the turntable snapshots
		@param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		@param _colorwayIndex: colorway index to render the image
		@param _width: image width for the snapshots
		@param _height: image height for the snapshots
		@return Output file path list. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportTurntableImagesByColorwayIndexW(const wstring& _filePath, int _numberOfImages, unsigned int _colorwayIndex, int _width = 2500, int _height = 2500)
		/// @brief Export turntable images for colorway.
		/// @param _filePath: the output file path to export the turntable snapshots
		/// @param _numberOfImages: the number of images in 360 turn table. The turn table will turn by (360 / _numberOfImages) per an image each by each.
		/// @param _colorwayIndex: colorway index to render the image
		/// @param _width: image width for the snapshots
		/// @param _height: image height for the snapshots
		/// @return Output file path list. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportPose() -> str
		"""
		@brief Export ZPac file in the CLO temporary folder
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportPose()
		/// @brief Export ZPac file in the CLO temporary folder
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportPose(_filePath : str) -> str
		"""
		@brief Export ZPac file
		@param string _filePath : target file path in ASCII
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportPose(const string& _filePath)
		/// @brief Export ZPac file
		/// @param string _filePath : target file path in ASCII
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportPoseW(_filePath : str) -> str
		"""
		@brief Export ZPac file
		@param wstring _filePath : target file path in UNICODE
		@return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportPoseW(const wstring& _filePath)
		/// @brief Export ZPac file
		/// @param wstring _filePath : target file path in UNICODE
		/// @return Output file path. If an error occurs, return empty string. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportFBX(_options : ImportExportOption) -> list[str]
		"""
		@brief Export FBX file
		@param options: It exports FBX according to options, not allowing user for selecting options in Export Dialog.
		@return Output file paths. If filePath parameter is not given, output files will be created in CLO temporary folder.
		"""

	.. code-tab:: c++

		 ExportFBX(const Marvelous::ImportExportOption& _options)
		/// @brief Export FBX file
		/// @param options: It exports FBX according to options, not allowing user for selecting options in Export Dialog.
		/// @return Output file paths. If filePath parameter is not given, output files will be created in CLO temporary folder.


.. tabs::

	.. code-tab:: python

		def ExportFBX(_filePath : str, _options : ImportExportOption) -> list[str]
		"""
		@brief Export FBX file
		@param options: It exports FBX according to options, not allowing user for selecting options in Export Dialog.
		@param string _filePath : target file path in ASCII
		@return Output file paths.
		"""

	.. code-tab:: c++

		 ExportFBX(const Marvelous::ImportExportOption& _options)
		/// @brief Export FBX file
		/// @param options: It exports FBX according to options, not allowing user for selecting options in Export Dialog.
		/// @param string _filePath : target file path in ASCII
		/// @return Output file paths.


.. tabs::

	.. code-tab:: python

		def ExportFBXW(_filePath : str, _options : ImportExportOption) -> list[str]
		"""
		@brief Export FBX file
		@param options: It exports FBX according to options, not allowing user for selecting options in Export Dialog.
		@param string _filePath : target file path in UNICODE
		@return Output file paths.
		"""

	.. code-tab:: c++

		 ExportFBX(const Marvelous::ImportExportOption& _options)
		/// @brief Export FBX file
		/// @param options: It exports FBX according to options, not allowing user for selecting options in Export Dialog.
		/// @param string _filePath : target file path in UNICODE
		/// @return Output file paths.


.. tabs::

	.. code-tab:: python

		def ExportAVT(_filePath : str) -> str
		"""
		@brief Export AVT
		@param _filePath: output file path
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportAVT(const string& _filePath)
		/// @brief Export AVT
		/// @param _filePath: output file path
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportAVTW(_filePath : str) -> str
		"""
		@brief Export AVT
		@param _filePath: output file path		
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportAVTW(const wstring& _filePath)
		/// @brief Export AVT
		/// @param _filePath: output file path		
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportTrim(_filePath : str, _trimStyleIndex : int) -> str
		"""
		@brief Export trim file
		@param _filePath: the output file path to export trim
		@param _trimStyleIndex: trimstyle index to export trim style
		@return Output file path list. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportTrim(const std::string& _filePath, unsigned int _trimStyleIndex)
		/// @brief Export trim file
		/// @param _filePath: the output file path to export trim
		/// @param _trimStyleIndex: trimstyle index to export trim style
		/// @return Output file path list. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportStdViewImage(_viewIndex : int, _outputFolderPath : str, _colorwayIndex : int, _width : int, _height : int) -> str
		"""
		@brief ExportStdViewImage : Exports The Image based on the given Standard image view index for selected colorway.
		@param : 
		@return Output file path along with the selected colorway name. If an error occurs, return error message string. 
		"""

	.. code-tab:: c++

		 ExportStdViewImage(int _viewIndex, const std::string& _outputFolderPath, int _colorwayIndex, int _width, int _height)
		/// @brief ExportStdViewImage : Exports The Image based on the given Standard image view index for selected colorway.
		/// @param : 
		/// @return Output file path along with the selected colorway name. If an error occurs, return error message string. 


.. tabs::

	.. code-tab:: python

		def ExportStdViewImageForAllColorways(_viewIndex : int, _outputFolderPath : str, _width : int, _height : int) -> str
		"""
		@brief ExportStdViewImageForAllColorways : Exports The Image based on the given Standard image view index for all Colorways.
		@param : 
		@return Output file paths along with the colorway names. If an error occurs, return error message string. 
		"""

	.. code-tab:: c++

		 ExportStdViewImageForAllColorways(int _viewIndex, const std::string& _outputFolderPath, int _width, int _height)
		/// @brief ExportStdViewImageForAllColorways : Exports The Image based on the given Standard image view index for all Colorways.
		/// @param : 
		/// @return Output file paths along with the colorway names. If an error occurs, return error message string. 


.. tabs::

	.. code-tab:: python

		def ExportCustomViewImage(_zcmrFileUrl : str, _outputFolderPath : str, _colorwayIndex : int, _width : int, _height : int) -> str
		"""
		@brief ExportCustomViewImage : Exports The Custom image based on the given custom angles in ZCMR file for selected Colorway.
		@param : 
		@return Output file path along with the selected colorway name. If an error occurs, return error message string. 
		"""

	.. code-tab:: c++

		 ExportCustomViewImage((const std::string& _zcmrFileUrl, const std::string& _outputFolderPath, int _colorwayIndex, int _width, int _height)
		/// @brief ExportCustomViewImage : Exports The Custom image based on the given custom angles in ZCMR file for selected Colorway.
		/// @param : 
		/// @return Output file path along with the selected colorway name. If an error occurs, return error message string. 


.. tabs::

	.. code-tab:: python

		def ExportCustomViewImageForAllColorways(_zcmrFileUrl : str, _outputFolderPath : str, _width : int, _height : int) -> str
		"""
		@brief ExportCustomViewImageForAllColorways : Exports The Custom image based on the given custom angles in ZCMR file for all Colorways.
		@param : 
		@return Output file path along with the colorway names. If an error occurs, return error message string. 
		"""

	.. code-tab:: c++

		 ExportCustomViewImageForAllColorways((const std::string& _zcmrFileUrl, const std::string& _outputFolderPath, int _width, int _height)
		/// @brief ExportCustomViewImageForAllColorways : Exports The Custom image based on the given custom angles in ZCMR file for all Colorways.
		/// @param : 
		/// @return Output file path along with the colorway names. If an error occurs, return error message string. 


.. tabs::

	.. code-tab:: python

		def ExportMultiViewImages(_mvsFilePath : str, _outputFilePath : str, _colorwayIndex : int, _width : int, _height : int) -> str
		"""
		@brief ExportMultiViewImages : Exports The Multi View Images based on the given MVS File for selected Colorway.
		@param : 
		@return Output file path along with the selected colorway name. If an error occurs, return error message string. 
		"""

	.. code-tab:: c++

		 ExportMultiViewImages(const std::string& _mvsFilePath, const std::string& _outputFilePath, int _colorwayIndex, int _width, int _height)
		/// @brief ExportMultiViewImages : Exports The Multi View Images based on the given MVS File for selected Colorway.
		/// @param : 
		/// @return Output file path along with the selected colorway name. If an error occurs, return error message string. 


.. tabs::

	.. code-tab:: python

		def ExportMultiViewImagesForAllColorways(_mvsFilePath : str, _outputFilePath : str, _width : int, _height : int) -> str
		"""
		@brief ExportMultiViewImagesForAllColorways : Exports The Multi View Images based on the given MVS File for all Colorways.
		@param : 
		@return Output file path along with the colorway names. If an error occurs, return error message string. 
		"""

	.. code-tab:: c++

		 ExportMultiViewImagesForAllColorways(const std::string& _mvsFilePath, const std::string& _outputFilePath, int _width, int _height)
		/// @brief ExportMultiViewImagesForAllColorways : Exports The Multi View Images based on the given MVS File for all Colorways.
		/// @param : 
		/// @return Output file path along with the colorway names. If an error occurs, return error message string. 


.. tabs::

	.. code-tab:: python

		def ConvertZblcToZmod(_zblcFilePathList : list[str], _saveDirPath : str, _categoryName : str, _styleName : str) -> str
		"""
		@brief Convert .zblc file to .zmod file
		@param _zblcFilePathList: The path of the ZBLC files you want to convert
		@param _saveDirPath: Where to save the converted file
		@param _categoryName : Category name
		@param _styleName : Style name
		@return Output file path list. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ConvertZblcToZmod(const std::vector<std::wstring>& _zblcFilePathList, const std::wstring& _saveDirPath, const std::wstring& _categoryName, const std::wstring& _styleName)
		/// @brief Convert .zblc file to .zmod file
		/// @param _zblcFilePathList: The path of the ZBLC files you want to convert
		/// @param _saveDirPath: Where to save the converted file
		/// @param _categoryName : Category name
		/// @param _styleName : Style name
		/// @return Output file path list. If an error occurs, return empty string. 




IMPORT_API
***********
 
.. tabs::

	.. code-tab:: python

		def ImportFile(filePath : str) -> bool
		"""
		@brief Load File (zprj, zpac, avt, obj, fbx, zcmr). This function will show up the dialog per the file type.
		@param filePath: the input file path to load
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportFile(const string& filePath)
		/// @brief Load File (zprj, zpac, avt, obj, fbx, zcmr). This function will show up the dialog per the file type.
		/// @param filePath: the input file path to load
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportFileW(filePath : str) -> bool
		"""
		@brief Load File (zprj, zpac, avt, obj, fbx, zcmr). This function will show up the dialog per the file type.
		@param filePath: the input file path to load
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportFileW(const wstring& filePath)
		/// @brief Load File (zprj, zpac, avt, obj, fbx, zcmr). This function will show up the dialog per the file type.
		/// @param filePath: the input file path to load
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportZprj(filePath : str, loadOption : ImportZPRJOption) -> bool
		"""
		@brief Load zprj File without the dialog but the loadOption
		@param filePath: the input file path to load
		@param loadOption: the options to load the file
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportZprj(const string& filePath, const Marvelous::ImportZPRJOption& loadOption)
		/// @brief Load zprj File without the dialog but the loadOption
		/// @param filePath: the input file path to load
		/// @param loadOption: the options to load the file
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportZprjW(filePath : str, loadOption : ImportZPRJOption) -> bool
		"""
		@brief Load zprj File without the dialog but the loadOption
		@param filePath: the input file path to load
		@param loadOption: the options to load the file
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportZprjW(const wstring& filePath, const Marvelous::ImportZPRJOption& loadOption)
		/// @brief Load zprj File without the dialog but the loadOption
		/// @param filePath: the input file path to load
		/// @param loadOption: the options to load the file
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGarmentInformation(filePath : str) -> bool
		"""
		@brief Load Garment Information (json)
		@param filePath: the input file to load the garment information (.json)
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportGarmentInformation(const string& filePath)
		/// @brief Load Garment Information (json)
		/// @param filePath: the input file to load the garment information (.json)
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGarmentInformationW(filePath : str) -> bool
		"""
		@brief Load Garment Information (json)
		@param filePath: the input file to load the garment information (.json)
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportGarmentInformationW(const wstring& filePath)
		/// @brief Load Garment Information (json)
		/// @param filePath: the input file to load the garment information (.json)
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGarmentInformationConfigData(filePath : str) -> bool
		"""
		@brief Load Garment Information Configuration (json)				
		@param filePath: the input file to load the garment information configuration data(.json)
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportGarmentInformationConfigData(const string& filePath)
		/// @brief Load Garment Information Configuration (json)				
		/// @param filePath: the input file to load the garment information configuration data(.json)
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGarmentInformationConfigDataW(filePath : str) -> bool
		"""
		@brief Load Garment Information Configuration (json)				
		@param filePath: the input file to load the garment information configuration data(.json)
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportGarmentInformationConfigDataW(const wstring& filePath)
		/// @brief Load Garment Information Configuration (json)				
		/// @param filePath: the input file to load the garment information configuration data(.json)
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportOBJ(_filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Import OBJ file
		@param _filePath: input file path
		@param options: If "options" is given, it imports OBJ according to options, not allowing user for selecting options in Import Dialog.
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportOBJ(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Import OBJ file
		/// @param _filePath: input file path
		/// @param options: If "options" is given, it imports OBJ according to options, not allowing user for selecting options in Import Dialog.
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportOBJW(_filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Import OBJ file
		@param _filePath: input file path
		@param options: If "options" is given, it imports OBJ according to options, not allowing user for selecting options in Import Dialog.
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportOBJW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Import OBJ file
		/// @param _filePath: input file path
		/// @param options: If "options" is given, it imports OBJ according to options, not allowing user for selecting options in Import Dialog.
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportVMP(_filePath : str) -> bool
		"""
		@brief Import VMP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportVMP(const string& _filePath)
		/// @brief Import VMP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportVMPW(_filePath : str) -> bool
		"""
		@brief Import VMP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportVMP(const wstring& _filePath)
		/// @brief Import VMP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportCPT(_filePath : str) -> bool
		"""
		@brief Import CPT file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportCPT(const string& _filePath)
		/// @brief Import CPT file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportCPTW(_filePath : str) -> bool
		"""
		@brief Import CPT file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportCPT(const wstring& _filePath)
		/// @brief Import CPT file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportVLP(_filePath : str) -> bool
		"""
		@brief Import VLP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportVLP(const string& _filePath)
		/// @brief Import VLP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportVLPW(_filePath : str) -> bool
		"""
		@brief Import VLP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportVLP(const wstring& _filePath)
		/// @brief Import VLP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportVRP(_filePath : str) -> bool
		"""
		@brief Import VRP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportVRP(const string& _filePath)
		/// @brief Import VRP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportVRPW(_filePath : str) -> bool
		"""
		@brief Import VRP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportVRP(const wstring& _filePath)
		/// @brief Import VRP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportDXF(_filePath : str, loadOption : ImportDxfOption) -> bool
		"""
		@brief Import DXF file
		@param _filePath: input file path
		@param loadOption: the options to load the file
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportDXF(const string& _filePath, const Marvelous::ImportDxfOption& loadOption)
		/// @brief Import DXF file
		/// @param _filePath: input file path
		/// @param loadOption: the options to load the file
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportDXFW(_filePath : str, loadOption : ImportDxfOption) -> bool
		"""
		@brief Import DXF file
		@param _filePath: input file path
		@param loadOption: the options to load the file
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportDXF(const wstring& _filePath, const Marvelous::ImportDxfOption& loadOption)
		/// @brief Import DXF file
		/// @param _filePath: input file path
		/// @param loadOption: the options to load the file
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGraphicStyleFromImage(_filePath : str) -> bool
		"""
		@brief Import DXF file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportImageAsGraphicStyle(const string& _filePath)
		/// @brief Import DXF file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGraphicStyleFromImage(_filePath : str) -> bool
		"""
		@brief Import image file as graphic style
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportImageAsGraphicStyle(const wstring& _filePath)
		/// @brief Import image file as graphic style
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportAVAC(_filePath : str, _apfFilePath : str) -> bool
		"""
		@brief Import avac avatar file
		@param _filePath: input avatar file path
		@param _apfFilePath: input apf File path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportAvatar(const wstring& _filePath, const Marvelous::ImportExportOption& _importOption)
		/// @brief Import avac avatar file
		/// @param _filePath: input avatar file path
		/// @param _apfFilePath: input apf File path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportAVAC(_filePath : str, _apfFilePath : str) -> bool
		"""
		"""

	.. code-tab:: c++

		


.. tabs::

	.. code-tab:: python

		def ImportFile(filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Load File(obj, fbx, gltf) by obj type . This function will show up the dialog per the file type.
		@param filePath: the input file path to load, ImportExportOption - loadObjectType 0 : avater, 1 : trim
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportFile(const string& filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Load File(obj, fbx, gltf) by obj type . This function will show up the dialog per the file type.
		/// @param filePath: the input file path to load, ImportExportOption - loadObjectType 0 : avater, 1 : trim
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportFileW(filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Load File(obj, fbx, gltf) by obj type. This function will show up the dialog per the file type.
		@param filePath: the input file path to load, ImportExportOption - loadObjectType 0 : avater, 1 : trim
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportFileW(const wstring& filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Load File(obj, fbx, gltf) by obj type. This function will show up the dialog per the file type.
		/// @param filePath: the input file path to load, ImportExportOption - loadObjectType 0 : avater, 1 : trim
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportFBX(_filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Import FBX file
		@param _filePath: input file path
		@param options: If "options" is given, it imports FBX according to options, not allowing user for selecting options in Import Dialog.
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportFBX(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Import FBX file
		/// @param _filePath: input file path
		/// @param options: If "options" is given, it imports FBX according to options, not allowing user for selecting options in Import Dialog.
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportFBXW(_filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Import FBX file
		@param _filePath: input file path
		@param options: If "options" is given, it imports FBX according to options, not allowing user for selecting options in Import Dialog.
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportFBXW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Import FBX file
		/// @param _filePath: input file path
		/// @param options: If "options" is given, it imports FBX according to options, not allowing user for selecting options in Import Dialog.
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGLTF(_filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Import GLTF file
		@param _filePath: input file path
		@param options: If "options" is given, it imports GLTF according to options, not allowing user for selecting options in Import Dialog.
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportGLTF(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Import GLTF file
		/// @param _filePath: input file path
		/// @param options: If "options" is given, it imports GLTF according to options, not allowing user for selecting options in Import Dialog.
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportGLTFW(_filePath : str, _options : ImportExportOption) -> bool
		"""
		@brief Import GLTF file
		@param _filePath: input file path
		@param options: If "options" is given, it imports GLTF according to options, not allowing user for selecting options in Import Dialog.
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportGLTFW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Import GLTF file
		/// @param _filePath: input file path
		/// @param options: If "options" is given, it imports GLTF according to options, not allowing user for selecting options in Import Dialog.
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportSMP(_filePath : str) -> bool
		"""
		@brief Import SMP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportSMP(const string& _filePath)
		/// @brief Import SMP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportSMPW(_filePath : str) -> bool
		"""
		@brief Import SMP file
		@param _filePath: input file path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportSMPW(const wstring& _filePath)
		/// @brief Import SMP file
		/// @param _filePath: input file path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportAsGraphic(_filePath : str) -> None
		"""
		@brief Import an image file as Graphic.
		@param _filePath: input file path
		"""

	.. code-tab:: c++

		 ImportAsGraphic(const std::string& _filePath)
		/// @brief Import an image file as Graphic.
		/// @param _filePath: input file path


.. tabs::

	.. code-tab:: python

		def ImportAsGraphicW(_filePath : str) -> None
		"""
		@brief Import an image file as Graphic.
		@param _filePath: input file path
		"""

	.. code-tab:: c++

		 ImportAsGraphicW(const std::wstring& _filePath)
		/// @brief Import an image file as Graphic.
		/// @param _filePath: input file path


UTILITY_API
***********
 
.. tabs::

	.. code-tab:: python

		def GetCLOTemporaryFolderPath() -> str
		"""
		@brief Create and get the temporary folder path
		@return Get the temporary folder path to store temporary files used when exporting to server
		"""

	.. code-tab:: c++

		 GetCLOTemporaryFolderPath()
		/// @brief Create and get the temporary folder path
		/// @return Get the temporary folder path to store temporary files used when exporting to server


.. tabs::

	.. code-tab:: python

		def GetCLOTemporaryFolderPathW() -> str
		"""
		@brief Create and get the temporary folder path
		@return Get the temporary folder path to store temporary files used when exporting to server
		"""

	.. code-tab:: c++

		 GetCLOTemporaryFolderPathW()
		/// @brief Create and get the temporary folder path
		/// @return Get the temporary folder path to store temporary files used when exporting to server


.. tabs::

	.. code-tab:: python

		def DisplayMessageBox(str : str) -> None
		"""
		@brief Show a message with using the DialogBox implemented in CLO software
		@param str: message
		@return Display a message box to show input string on CLO. This can be used for debugging.
		"""

	.. code-tab:: c++

		 DisplayMessageBox(string str)
		/// @brief Show a message with using the DialogBox implemented in CLO software
		/// @param str: message
		/// @return Display a message box to show input string on CLO. This can be used for debugging.


.. tabs::

	.. code-tab:: python

		def DisplayMessageBoxW(str : str) -> None
		"""
		@brief Show a message with using the DialogBox implemented in CLO software
		@param str: message
		@return Display a message box to show input string on CLO. This can be used for debugging.
		"""

	.. code-tab:: c++

		 DisplayMessageBoxW(wstring str)
		/// @brief Show a message with using the DialogBox implemented in CLO software
		/// @param str: message
		/// @return Display a message box to show input string on CLO. This can be used for debugging.


.. tabs::

	.. code-tab:: python

		def GetProjectName() -> str
		"""
		@brief Get the current project name in CLO
		@return The current project name. When you opening "test.zprj" file at last, then the project name is given as "test"
		"""

	.. code-tab:: c++

		 GetProjectName()
		/// @brief Get the current project name in CLO
		/// @return The current project name. When you opening "test.zprj" file at last, then the project name is given as "test"


.. tabs::

	.. code-tab:: python

		def GetProjectNameW() -> str
		"""
		@brief Get the current project name in CLO
		@return The current project name. When you opening "test.zprj" file at last, then the project name is given as "test"
		"""

	.. code-tab:: c++

		 GetProjectNameW()
		/// @brief Get the current project name in CLO
		/// @return The current project name. When you opening "test.zprj" file at last, then the project name is given as "test"


.. tabs::

	.. code-tab:: python

		def GetProjectFilePath() -> str
		"""
		@brief Get the current profile file path
		@return The current project file path. If you load a project file saved in "c://download/default.zprj", this function returns the full path - "c://download/default.zprj". If you never load project files, then it returns "NULL".
		"""

	.. code-tab:: c++

		 GetProjectFilePath()
		/// @brief Get the current profile file path
		/// @return The current project file path. If you load a project file saved in "c://download/default.zprj", this function returns the full path - "c://download/default.zprj". If you never load project files, then it returns "NULL".


.. tabs::

	.. code-tab:: python

		def GetProjectFilePathW() -> str
		"""
		@brief Get the current profile file path
		@return The current project file path. If you load a project file saved in "c://download/default.zprj", this function returns the full path - "c://download/default.zprj". If you never load project files, then it returns "NULL".
		"""

	.. code-tab:: c++

		 GetProjectFilePathW()
		/// @brief Get the current profile file path
		/// @return The current project file path. If you load a project file saved in "c://download/default.zprj", this function returns the full path - "c://download/default.zprj". If you never load project files, then it returns "NULL".


.. tabs::

	.. code-tab:: python

		def GetMajorVersion() -> int
		"""
		@brief Get the major version of the CLO software
		@return Major version of SW. ex) 5 of 5.0.72
		"""

	.. code-tab:: c++

		 GetMajorVersion()
		/// @brief Get the major version of the CLO software
		/// @return Major version of SW. ex) 5 of 5.0.72


.. tabs::

	.. code-tab:: python

		def GetMinorVersion() -> int
		"""
		@brief Get the minor version of the CLO software
		@return Minor version of SW. ex) 0 of 5.0.72
		"""

	.. code-tab:: c++

		 GetMinorVersion()
		/// @brief Get the minor version of the CLO software
		/// @return Minor version of SW. ex) 0 of 5.0.72


.. tabs::

	.. code-tab:: python

		def GetPatchVersion() -> int
		"""
		@brief Get the patch version of the CLO software
		@return Patch version of SW. ex) 72 of 5.0.72
		"""

	.. code-tab:: c++

		 GetPatchVersion()
		/// @brief Get the patch version of the CLO software
		/// @return Patch version of SW. ex) 72 of 5.0.72


.. tabs::

	.. code-tab:: python

		def toUtf8(str : str) -> str
		"""
		@brief Convert and get the string encoded in UTF-8 from wstring
		@param str: target wstring to convert
		@return string in UTF8 from wstring encoded by UCS-2 in Windows or UTF-8 in Mac OS
		"""

	.. code-tab:: c++

		 toUtf8(const std::wstring &str)
		/// @brief Convert and get the string encoded in UTF-8 from wstring
		/// @param str: target wstring to convert
		/// @return string in UTF8 from wstring encoded by UCS-2 in Windows or UTF-8 in Mac OS


.. tabs::

	.. code-tab:: python

		def GetColorwayCount() -> int
		"""
		@brief Get the number of colorways in the current project
		@return The number of Colorways in the current project.
		"""

	.. code-tab:: c++

		 GetColorwayCount()
		/// @brief Get the number of colorways in the current project
		/// @return The number of Colorways in the current project.


.. tabs::

	.. code-tab:: python

		def GetCurrentColorwayIndex() -> int
		"""
		@brief Get the current colorway index
		@return The current colorway index.
		"""

	.. code-tab:: c++

		 GetCurrentColorwayIndex()
		/// @brief Get the current colorway index
		/// @return The current colorway index.


.. tabs::

	.. code-tab:: python

		def SetCurrentColorwayIndex(index : int) -> None
		"""
		@brief Change the current colorway
		@param index: the colorway index
		"""

	.. code-tab:: c++

		 SetCurrentColorwayIndex(unsigned int index)
		/// @brief Change the current colorway
		/// @param index: the colorway index


.. tabs::

	.. code-tab:: python

		def SetColorwayName(index : int, str : str) -> None
		"""
		@brief Change colorway name
		@param index: the target colorway index to change the name
		@param str: new name for the colorway
		"""

	.. code-tab:: c++

		 SetColorwayName(unsigned int index, const string& str)
		/// @brief Change colorway name
		/// @param index: the target colorway index to change the name
		/// @param str: new name for the colorway


.. tabs::

	.. code-tab:: python

		def SetColorwayNameW(index : int, wstr : str) -> None
		"""
		@brief Change colorway name
		@param index: the target colorway index to change the name
		@param str: new name for the colorway
		"""

	.. code-tab:: c++

		 SetColorwayNameW(unsigned int index, const wstring& wstr)
		/// @brief Change colorway name
		/// @param index: the target colorway index to change the name
		/// @param str: new name for the colorway


.. tabs::

	.. code-tab:: python

		def GetColorwayName(index : int) -> str
		"""
		@brief Get the colorway name for the colorway index
		@param index: colorway index to get the name
		@return the colorway name for the colorway index
		"""

	.. code-tab:: c++

		 GetColorwayName(unsigned int index)
		/// @brief Get the colorway name for the colorway index
		/// @param index: colorway index to get the name
		/// @return the colorway name for the colorway index


.. tabs::

	.. code-tab:: python

		def GetColorwayNameW(index : int) -> str
		"""
		@brief Get the colorway name for the colorway index
		@param index: colorway index to get the name
		@return the colorway name for the colorway index
		"""

	.. code-tab:: c++

		 GetColorwayNameW(unsigned int index)
		/// @brief Get the colorway name for the colorway index
		/// @param index: colorway index to get the name
		/// @return the colorway name for the colorway index


.. tabs::

	.. code-tab:: python

		def CopyColorway(index : int) -> int
		"""
		@brief Copy the colorway in the index and create a new one
		@param index: the source colorway index to copy
		@return index for the created colorway
		"""

	.. code-tab:: c++

		 CopyColorway(unsigned int index)
		/// @brief Copy the colorway in the index and create a new one
		/// @param index: the source colorway index to copy
		/// @return index for the created colorway


.. tabs::

	.. code-tab:: python

		def GetCustomViewInformation() -> str
		"""
		@brief Get the custom view information				
		{
		"customViewList": [
		{
		"cameraMatrix": [ // row vector 0, 1, 2 of "local to world camera matrix"
		1.0,
		0.000166,
		-0.001024,
		0.352125,
		0.0,
		0.987069,
		0.160306,
		2592.8,
		0.001039,
		-0.160306,
		0.987068,
		7973.05
		],
		"fov": 40.0
		}
		]
		}				
		@return Json stream including the data of Custom View such as Camera Matrix, FOV, and so on.
		"""

	.. code-tab:: c++

		 GetCustomViewInformation()
		/// @brief Get the custom view information				
		{
		"customViewList": [
		{
		"cameraMatrix": [ // row vector 0, 1, 2 of "local to world camera matrix"
		1.0,
		0.000166,
		-0.001024,
		0.352125,
		0.0,
		0.987069,
		0.160306,
		2592.8,
		0.001039,
		-0.160306,
		0.987068,
		7973.05
		],
		"fov": 40.0
		}
		]
		}				
		/// @return Json stream including the data of Custom View such as Camera Matrix, FOV, and so on.


.. tabs::

	.. code-tab:: python

		def GetCustomViewInformationW() -> str
		"""
		@brief Get the custom view information				
		{
		"customViewList": [
		{
		"cameraMatrix": [ // row vector 0, 1, 2 of "local to world camera matrix"
		1.0,
		0.000166,
		-0.001024,
		0.352125,
		0.0,
		0.987069,
		0.160306,
		2592.8,
		0.001039,
		-0.160306,
		0.987068,
		7973.05
		],
		"fov": 40.0
		}
		]
		}				
		@return Json stream including the data of Custom View such as Camera Matrix, FOV, and so on.
		"""

	.. code-tab:: c++

		 GetCustomViewInformationW()
		/// @brief Get the custom view information				
		{
		"customViewList": [
		{
		"cameraMatrix": [ // row vector 0, 1, 2 of "local to world camera matrix"
		1.0,
		0.000166,
		-0.001024,
		0.352125,
		0.0,
		0.987069,
		0.160306,
		2592.8,
		0.001039,
		-0.160306,
		0.987068,
		7973.05
		],
		"fov": 40.0
		}
		]
		}				
		/// @return Json stream including the data of Custom View such as Camera Matrix, FOV, and so on.


.. tabs::

	.. code-tab:: python

		def GetClothPositions(positions : list[float]) -> None
		"""
		@brief Get the position array of cloth shape. Each three array has x, y, z position of each vertex. 
		@param positions: the output position list for the cloth shape
		"""

	.. code-tab:: c++

		 GetClothPositions(vector<float>& positions)
		/// @brief Get the position array of cloth shape. Each three array has x, y, z position of each vertex. 
		/// @param positions: the output position list for the cloth shape


.. tabs::

	.. code-tab:: python

		def ResetClothArrangement() -> None
		"""
		@brief Restore the shape of cloth to when the cloth was loaded
		"""

	.. code-tab:: c++

		 ResetClothArrangement()
		/// @brief Restore the shape of cloth to when the cloth was loaded


.. tabs::

	.. code-tab:: python

		def GetThumbnailInCLOFile(filePath : str, thumbnailIndex : int, fileSize : int) -> char*
		"""
		@brief Get Preview thumbnail file buffer(png type) from the CLO file format(.zprj, .zpac, .zfab, .sst, and so on)
		@param filePath: the source file path to retrieve the thumbnail buffer
		@param thumbnailIndex: the index of the thumbnails in the CLO file format(the number of thumbnails differs by the format)
		@param fileSize: get the size of the thumbnail buffer
		@return thumbnail(png) buffer
		"""

	.. code-tab:: c++

		 GetThumbnailInCLOFile(std::string filePath, unsigned int thumbnailIndex, unsigned int& fileSize)
		/// @brief Get Preview thumbnail file buffer(png type) from the CLO file format(.zprj, .zpac, .zfab, .sst, and so on)
		/// @param filePath: the source file path to retrieve the thumbnail buffer
		/// @param thumbnailIndex: the index of the thumbnails in the CLO file format(the number of thumbnails differs by the format)
		/// @param fileSize: get the size of the thumbnail buffer
		/// @return thumbnail(png) buffer


.. tabs::

	.. code-tab:: python

		def GetAssetIconInCLOFile(filePath : str, fileSize : int) -> char*
		"""
		@brief Get Asset Icon thumbnail file buffer(png type) from the CLO file format(.zprj, .zpac, .zfab, .sst, and so on)
		@param filePath: the source file path to retrieve the thumbnail buffer				
		@param fileSize: get the size of the thumbnail buffer
		@return thumbnail(png) buffer
		"""

	.. code-tab:: c++

		 GetAssetIconInCLOFile(std::string filePath, unsigned int& fileSize)
		/// @brief Get Asset Icon thumbnail file buffer(png type) from the CLO file format(.zprj, .zpac, .zfab, .sst, and so on)
		/// @param filePath: the source file path to retrieve the thumbnail buffer				
		/// @param fileSize: get the size of the thumbnail buffer
		/// @return thumbnail(png) buffer


.. tabs::

	.. code-tab:: python

		def GetMetaDataForCurrentGarment() -> str
		"""
		@brief Get Meta data for the current Garment
		@return the meta data for the current garment
		"""

	.. code-tab:: c++

		 GetMetaDataForCurrentGarment()
		/// @brief Get Meta data for the current Garment
		/// @return the meta data for the current garment


.. tabs::

	.. code-tab:: python

		def GetMetaDataForCurrentGarmentW() -> str
		"""
		@brief Get Meta data for the current Garment
		@return the meta data for the current garment
		"""

	.. code-tab:: c++

		 GetMetaDataForCurrentGarmentW()
		/// @brief Get Meta data for the current Garment
		/// @return the meta data for the current garment


.. tabs::

	.. code-tab:: python

		def SetMetaDataForCurrentGarment(metaDataStr : str) -> None
		"""
		@brief Overwrite Meta data for the current Garment
		@param metaDataStr: the new meata data to set to the current garment
		"""

	.. code-tab:: c++

		 SetMetaDataForCurrentGarment(const string& metaDataStr)
		/// @brief Overwrite Meta data for the current Garment
		/// @param metaDataStr: the new meata data to set to the current garment


.. tabs::

	.. code-tab:: python

		def ChangeMetaDataValueForCurrentGarment(metaDataKey : str, metaDataValue : str) -> None
		"""
		@brief Change Meta Data Value for the current Garment
		@metaDataKey: target Key
		@metaDataValue: the new value for the key
		"""

	.. code-tab:: c++

		 ChangeMetaDataValueForCurrentGarment(const string& metaDataKey, const string& metaDataValue)
		/// @brief Change Meta Data Value for the current Garment
		/// @metaDataKey: target Key
		/// @metaDataValue: the new value for the key


.. tabs::

	.. code-tab:: python

		def CreateProgressBar() -> None
		"""
		@brief Create Progress Bar to show progress. This function should be called before using SetProgress function				
		"""

	.. code-tab:: c++

		 CreateProgressBar()
		/// @brief Create Progress Bar to show progress. This function should be called before using SetProgress function				


.. tabs::

	.. code-tab:: python

		def SetProgress(title : str, progress : int) -> None
		"""
		@brief Set progress on the Progress Bar
		"""

	.. code-tab:: c++

		 SetProgress(const string& title, int progress)
		/// @brief Set progress on the Progress Bar


.. tabs::

	.. code-tab:: python

		def SetProgressW(title : str, progress : int) -> None
		"""
		@brief Set progress on the Progress Bar
		"""

	.. code-tab:: c++

		 SetProgress(const string& title, int progress)
		/// @brief Set progress on the Progress Bar


.. tabs::

	.. code-tab:: python

		def DeleteProgressBar(bForce : bool) -> None
		"""
		@brief Delete the current Progress Bar. This function should be called after using the SetProgress funtion
		@param bForce: true - retry to delete progress bar; false - try only once to delete progress bar
		"""

	.. code-tab:: c++

		 DeleteProgressBar(bool bForce)
		/// @brief Delete the current Progress Bar. This function should be called after using the SetProgress funtion
		/// @param bForce: true - retry to delete progress bar; false - try only once to delete progress bar


.. tabs::

	.. code-tab:: python

		def stringToMD5(str : str) -> str
		"""
		@brief Create MD5 hashing string from string
		@param str: the source string to hash 
		@return MD5 hashed string
		"""

	.. code-tab:: c++

		 stringToMD5(const string& str)
		/// @brief Create MD5 hashing string from string
		/// @param str: the source string to hash 
		/// @return MD5 hashed string


.. tabs::

	.. code-tab:: python

		def AddColorSwatch(plmIDtoNameList : map[str, str], plmIDtoColorList : map[str, CloApiRgb], plmIDtoApiMetaDataList : map[str, str], swatchName : str) -> str
		"""
		@brief Add Color Swatch
		@param plmIDtoNameList: the list for map of PLM ID to Color Name
		@param plmIDtoColorList: list for map of PLM ID to color name
		@param plmIDtoApiMetaDataList: list for map of PLM ID to Api Meta Data
		@param swatchName: swatchName which will be shown in the color palette and the swatch file name to save
		@return added swatch file name(.aco) inside the asset folder for the current version of CLO
		"""

	.. code-tab:: c++

		 AddColorSwatch(const map<string, string>& plmIDtoNameList, const map<string, Marvelous::CloApiRgb>& plmIDtoColorList, const map<string, string>& plmIDtoApiMetaDataList, const string& swatchName)
		/// @brief Add Color Swatch
		/// @param plmIDtoNameList: the list for map of PLM ID to Color Name
		/// @param plmIDtoColorList: list for map of PLM ID to color name
		/// @param plmIDtoApiMetaDataList: list for map of PLM ID to Api Meta Data
		/// @param swatchName: swatchName which will be shown in the color palette and the swatch file name to save
		/// @return added swatch file name(.aco) inside the asset folder for the current version of CLO


.. tabs::

	.. code-tab:: python

		def AddColorSwatchW(plmIDtoNameList : map[str, str], plmIDtoColorList : map[str, CloApiRgb], plmIDtoApiMetaDataList : map[str, str], swatchName : str) -> str
		"""
		@brief Add Color Swatch
		@param plmIDtoNameList: the list for map of PLM ID to Color Name
		@param plmIDtoColorList: list for map of PLM ID to color name
		@param plmIDtoApiMetaDataList: list for map of PLM ID to Api Meta Data
		@param swatchName: swatchName which will be shown in the color palette and the swatch file name to save
		@return added swatch file name(.aco) inside the asset folder for the current version of CLO
		"""

	.. code-tab:: c++

		 AddColorSwatchW(const map<wstring, wstring>& plmIDtoNameList, const map<wstring, Marvelous::CloApiRgb>& plmIDtoColorList, const map<wstring, wstring>& plmIDtoApiMetaDataList, const wstring& swatchName)
		/// @brief Add Color Swatch
		/// @param plmIDtoNameList: the list for map of PLM ID to Color Name
		/// @param plmIDtoColorList: list for map of PLM ID to color name
		/// @param plmIDtoApiMetaDataList: list for map of PLM ID to Api Meta Data
		/// @param swatchName: swatchName which will be shown in the color palette and the swatch file name to save
		/// @return added swatch file name(.aco) inside the asset folder for the current version of CLO


.. tabs::

	.. code-tab:: python

		def NewProject() -> None
		"""
		@brief Clear the current garment and begin a new garment
		"""

	.. code-tab:: c++

		 NewProject()
		/// @brief Clear the current garment and begin a new garment


.. tabs::

	.. code-tab:: python

		def IsReadableImageFormat(filePath : str) -> bool
		"""
		- IsReadableImageFormatFromExtension / IsReadableImageFormatFromExtensionW
		: Check if the file stream loaded from the filepath used in Library Windows Implementations can be displayed on Library Windows for item thumbnail and/or preview dialog.
		(The files should not contain image data over 8bits per channel for 1 ~ 4 channels image.)
		- IsCLOFileFormatWithThumbnailExtension / IsCLOFileFormatWithThumbnailExtensionW
		: Check if the CLO file format has the thumbnail memory.
		
		- IsCLOFileFormatWithTripleThumbnailExtension / IsCLOFileFormatWithTripleThumbnailExtensionW
		: Check if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		@fn IsReadableImageFormat(const string& filePath)
		@brief Check if the file stream loaded from the filepath used in Library Windows Implementations can be displayed on Library Windows for item thumbnail and/or preview dialog.
		@return true if the file can be displayed on Library Windows for item thumbnail and/or preview dialog
		"""

	.. code-tab:: c++

		
		- IsReadableImageFormatFromExtension / IsReadableImageFormatFromExtensionW
		: Check if the file stream loaded from the filepath used in Library Windows Implementations can be displayed on Library Windows for item thumbnail and/or preview dialog.
		(The files should not contain image data over 8bits per channel for 1 ~ 4 channels image.)
		- IsCLOFileFormatWithThumbnailExtension / IsCLOFileFormatWithThumbnailExtensionW
		: Check if the CLO file format has the thumbnail memory.
		
		- IsCLOFileFormatWithTripleThumbnailExtension / IsCLOFileFormatWithTripleThumbnailExtensionW
		: Check if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		/// @fn IsReadableImageFormat(const string& filePath)
		/// @brief Check if the file stream loaded from the filepath used in Library Windows Implementations can be displayed on Library Windows for item thumbnail and/or preview dialog.
		/// @return true if the file can be displayed on Library Windows for item thumbnail and/or preview dialog


.. tabs::

	.. code-tab:: python

		def IsReadableImageFormatW(filePath : str) -> bool
		"""
		@brief Check if the file stream loaded from the filepath used in Library Windows Implementations can be displayed on Library Windows for item thumbnail and/or preview dialog.
		@return true if the file can be displayed on Library Windows for item thumbnail and/or preview dialog
		"""

	.. code-tab:: c++

		 IsReadableImageFormatW(const wstring& filePath)
		/// @brief Check if the file stream loaded from the filepath used in Library Windows Implementations can be displayed on Library Windows for item thumbnail and/or preview dialog.
		/// @return true if the file can be displayed on Library Windows for item thumbnail and/or preview dialog


.. tabs::

	.. code-tab:: python

		def IsCLOFileFormatWithThumbnail(filePath : str) -> bool
		"""
		@brief Check if the CLO file format has the thumbnail memory.
		@return true if the file is the CLO format file and contains the thumbnail memory which can be displayed on Library Windows for item thumbnail and/or preview dialog
		"""

	.. code-tab:: c++

		 IsCLOFileFormatWithThumbnail(const string& filePath)
		/// @brief Check if the CLO file format has the thumbnail memory.
		/// @return true if the file is the CLO format file and contains the thumbnail memory which can be displayed on Library Windows for item thumbnail and/or preview dialog


.. tabs::

	.. code-tab:: python

		def IsCLOFileFormatWithThumbnailW(filePath : str) -> bool
		"""
		@brief Check if the CLO file format has the thumbnail memory.
		@return true if the file is the CLO format file and contains the thumbnail memory which can be displayed on Library Windows for item thumbnail and/or preview dialog
		"""

	.. code-tab:: c++

		 IsCLOFileFormatWithThumbnailW(const wstring& filePath)
		/// @brief Check if the CLO file format has the thumbnail memory.
		/// @return true if the file is the CLO format file and contains the thumbnail memory which can be displayed on Library Windows for item thumbnail and/or preview dialog


.. tabs::

	.. code-tab:: python

		def IsCLOFileFormatWithTripleThumbnail(filePath : str) -> bool
		"""
		@brief Check if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		@return true if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		"""

	.. code-tab:: c++

		 IsCLOFileFormatWithTripleThumbnail(const string& filePath)
		/// @brief Check if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		/// @return true if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.


.. tabs::

	.. code-tab:: python

		def IsCLOFileFormatWithTripleThumbnailW(filePath : str) -> bool
		"""
		@brief Check if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		@return true if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		"""

	.. code-tab:: c++

		 IsCLOFileFormatWithTripleThumbnailW(const wstring& filePath)
		/// @brief Check if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.
		/// @return true if the CLO file format has the three images memory for preview thumbnail for the Library Preview Dialog.


.. tabs::

	.. code-tab:: python

		def GetCLOExecutableFolderPath(bLinuxTypePathDelimeter : bool) -> str
		"""
		@brief Get the executable folder path where the current version of CLO is located
		@param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		@return Get the executable folder path for the current version of CLO software
		"""

	.. code-tab:: c++

		 GetCLOExecutableFolderPath(bool bLinuxTypePathDelimeter = true)
		/// @brief Get the executable folder path where the current version of CLO is located
		/// @param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		/// @return Get the executable folder path for the current version of CLO software


.. tabs::

	.. code-tab:: python

		def GetCLOExecutableFolderPathW(bLinuxTypePathDelimeter : bool) -> str
		"""
		@brief Get the executable folder path where the current version of CLO is located
		@param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		@return Get the executable folder path for the current version of CLO software
		"""

	.. code-tab:: c++

		 GetCLOExecutableFolderPathW(bool bLinuxTypePathDelimeter = true)
		/// @brief Get the executable folder path where the current version of CLO is located
		/// @param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		/// @return Get the executable folder path for the current version of CLO software


.. tabs::

	.. code-tab:: python

		def GetCLOAssetFolderPath(bLinuxTypePathDelimeter : bool) -> str
		"""
		@brief Get the folder path where the CLO asset files are distributed
		@param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		@return Get the asset folder path where the CLO asset files are located in
		"""

	.. code-tab:: c++

		 GetCLOAssetFolderPath(bool bLinuxTypePathDelimeter = true)
		/// @brief Get the folder path where the CLO asset files are distributed
		/// @param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		/// @return Get the asset folder path where the CLO asset files are located in


.. tabs::

	.. code-tab:: python

		def GetCLOAssetFolderPathW(bLinuxTypePathDelimeter : bool) -> str
		"""
		@brief Get the folder path where the CLO asset files are distributed
		@param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		@return Get the asset folder path where the CLO asset files are located in
		"""

	.. code-tab:: c++

		 GetCLOAssetFolderPathW(bool bLinuxTypePathDelimeter = true)
		/// @brief Get the folder path where the CLO asset files are distributed
		/// @param bLinuxTypePathDelimeter: if true, set path delimiter to '/', false: set path delimiter to '\'
		/// @return Get the asset folder path where the CLO asset files are located in


.. tabs::

	.. code-tab:: python

		def GetAPIMetaData(filePath : str) -> str
		"""
		@brief Get API meta data for the file
		@param filePath: CLO file path
		@return json string for meta data [key - value] list				
		"""

	.. code-tab:: c++

		 GetAPIMetaData(const string& filePath)
		/// @brief Get API meta data for the file
		/// @param filePath: CLO file path
		/// @return json string for meta data [key - value] list				


.. tabs::

	.. code-tab:: python

		def GetAPIMetaDataW(filePath : str) -> str
		"""
		@brief Get API meta data for the file
		@param filePath: CLO file path
		@return json string for meta data [key - value] list
		"""

	.. code-tab:: c++

		 GetAPIMetaDataW(const wstring& filePath)
		/// @brief Get API meta data for the file
		/// @param filePath: CLO file path
		/// @return json string for meta data [key - value] list


.. tabs::

	.. code-tab:: python

		def SetAPIMetaData(filePath : str, jsonStr : str) -> bool
		"""
		@brief Set API meta data to the file
		@param filePath: target file path
		@param jsonStr: api meta data in string format
		@return if it succeeds, return true
		"""

	.. code-tab:: c++

		 SetAPIMetaData(const string& filePath, string jsonStr)
		/// @brief Set API meta data to the file
		/// @param filePath: target file path
		/// @param jsonStr: api meta data in string format
		/// @return if it succeeds, return true


.. tabs::

	.. code-tab:: python

		def SetAPIMetaDataW(filePath : str, jsonStr : str) -> bool
		"""
		@brief Set API meta data to the file
		@param filePath: target file path
		@param jsonStr: api meta data in string format
		@return if it succeeds, return true
		"""

	.. code-tab:: c++

		 SetAPIMetaDataW(const wstring& filePath, wstring jsonStr)
		/// @brief Set API meta data to the file
		/// @param filePath: target file path
		/// @param jsonStr: api meta data in string format
		/// @return if it succeeds, return true


.. tabs::

	.. code-tab:: python

		def Set3DWindowTitle(title : str) -> bool
		"""
		@brief Set 3D Window Title
		@param title: desired text in 3D window
		@return if it succeeds, return true
		"""

	.. code-tab:: c++

		 Set3DWindowTitle(const string& title)
		/// @brief Set 3D Window Title
		/// @param title: desired text in 3D window
		/// @return if it succeeds, return true


.. tabs::

	.. code-tab:: python

		def Set3DWindowTitleW(title : str) -> bool
		"""
		@brief Set 3D Window Title
		@param title: desired text in 3D window
		@return if it succeeds, return true
		"""

	.. code-tab:: c++

		 Set3DWindowTitleW(const wstring& title) 
		/// @brief Set 3D Window Title
		/// @param title: desired text in 3D window
		/// @return if it succeeds, return true


.. tabs::

	.. code-tab:: python

		def GetColorListForColorWay(_colorWayIndex : int) -> list[CloApiRgba]
		"""
		@brief Get Color List for ColorWay
		@param _colorwayIndex: the colorway index to get the result
		@return the color list in CloAgiRgba for the target ColorWay
		"""

	.. code-tab:: c++

		 GetColorListForColorWay(unsigned int _colorWayIndex) 
		/// @brief Get Color List for ColorWay
		/// @param _colorwayIndex: the colorway index to get the result
		/// @return the color list in CloAgiRgba for the target ColorWay


.. tabs::

	.. code-tab:: python

		def SetShowHideAvatar(_bShow : bool) -> None
		"""
		@brief Set all avatars' show/hide status
		@param _bShow: true for show, false for hide
		"""

	.. code-tab:: c++

		 SetShowHideAvatar(bool _bShow) 
		/// @brief Set all avatars' show/hide status
		/// @param _bShow: true for show, false for hide


.. tabs::

	.. code-tab:: python

		def SetShowHideAvatar(_bShow : bool, _avatarIdex : int) -> None
		"""
		@brief Set show/hide status of avatar that matches the index
		@param _bShow: true for show, false for hide
		"""

	.. code-tab:: c++

		 SetShowHideAvatar(bool _bShow, int _avatarIndex) 
		/// @brief Set show/hide status of avatar that matches the index
		/// @param _bShow: true for show, false for hide


.. tabs::

	.. code-tab:: python

		def IsShowAvatar(_avatarIndex : int) -> bool
		"""
		@brief Get show status of avatar that matches the index
		@param _avatarIndex: the avatar index to get the result.
		@return if avatar is shown, return true. if avatar is hidden, return false.
		"""

	.. code-tab:: c++

		 IsShowAvatar(int _avatarIndex) 
		/// @brief Get show status of avatar that matches the index
		/// @param _avatarIndex: the avatar index to get the result.
		/// @return if avatar is shown, return true. if avatar is hidden, return false.


.. tabs::

	.. code-tab:: python

		def SetSchematicRender(_bSet : bool) -> None
		"""
		@brief Set Schematic Render status
		@param _bSet: true for enable, false for disable
		"""

	.. code-tab:: c++

		 SetSchematicRender(bool _bSet) 
		/// @brief Set Schematic Render status
		/// @param _bSet: true for enable, false for disable


.. tabs::

	.. code-tab:: python

		def UpdateColorways(bUpdateSnapshot : bool) -> None
		"""
		@brief Update Colorways in the CLO software
		@param bUpdateSnapshot: put the value to true to update the colorway's snapshot
		"""

	.. code-tab:: c++

		 UpdateColorways(bool bUpdateSnapshot = true)	
		/// @brief Update Colorways in the CLO software
		/// @param bUpdateSnapshot: put the value to true to update the colorway's snapshot


.. tabs::

	.. code-tab:: python

		def DeleteColorwayItem(_index : int) -> None
		"""
		@brief Delete the colorway in the index
		@param index: the source colorway index to delete
		"""

	.. code-tab:: c++

		 DeleteColorwayItem(unsigned int _index)
		/// @brief Delete the colorway in the index
		/// @param index: the source colorway index to delete


.. tabs::

	.. code-tab:: python

		def ReplaceGraphicStyleFromImage(_graphicstyleIndex : int, _imagePath : str) -> bool
		"""
		@brief replace graphic style in index 
		@param _imagePath: input file path
		@param _graphicstyleindex: index of the style to be replaced
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ReplaceGraphicTextureFromImage(int graphicstyleIndex, const string& _imagePath)
		/// @brief replace graphic style in index 
		/// @param _imagePath: input file path
		/// @param _graphicstyleindex: index of the style to be replaced
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ReplaceGraphicStyleFromImage(_graphicstyleIndex : int, _imagePath : str) -> bool
		"""
		@brief replace graphic style in index
		@param _imagePath: input file path
		@param _graphicstyleindex: index of the style to be replaced
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ReplaceGraphicTextureFromImage((int graphicstyleIndex, const wstring& _imagePath)
		/// @brief replace graphic style in index
		/// @param _imagePath: input file path
		/// @param _graphicstyleindex: index of the style to be replaced
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def Simulate(_steps : int) -> bool
		"""
		@brief Simulate the garment in multi steps. All dynamics properties (time step, CG iteration count, ...) follow the current simulation properties
		@param _steps: how many steps(=frames) to simulate
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 Simulate(unsigned int _steps)
		/// @brief Simulate the garment in multi steps. All dynamics properties (time step, CG iteration count, ...) follow the current simulation properties
		/// @param _steps: how many steps(=frames) to simulate
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def SetSimulationQuality(_quality : int) -> None
		"""
		@brief Set simulation quality preset
		@param _quality: input simulation preset (0: Normal(Default), 1: Animation(Stable), 2: Fitting(Accurate Fabric), 3: FAST(GPU))
		"""

	.. code-tab:: c++

		 SetSimulationQuality(int _quality)
		/// @brief Set simulation quality preset
		/// @param _quality: input simulation preset (0: Normal(Default), 1: Animation(Stable), 2: Fitting(Accurate Fabric), 3: FAST(GPU))


.. tabs::

	.. code-tab:: python

		def SetSimulationTimeStep(_timeStep : float) -> None
		"""
		@brief Set simulation time step
		@param _timeStep: time step in second (Default : 0.03333, Min value: 0.001)
		"""

	.. code-tab:: c++

		 SetSimulationTimeStep(int _timeStep)
		/// @brief Set simulation time step
		/// @param _timeStep: time step in second (Default : 0.03333, Min value: 0.001)


.. tabs::

	.. code-tab:: python

		def SetSimulationNumberOfSimulation(_numberOfSimulation : int) -> None
		"""
		@brief Set simulation substeps in one time step
		@param _numberOfSimulation: the number of substeps in one time step (Default : 1, Min/Max Range : 1~50)
		"""

	.. code-tab:: c++

		 SetSimulationNumberOfSimulation(int _numberOfSimulation)
		/// @brief Set simulation substeps in one time step
		/// @param _numberOfSimulation: the number of substeps in one time step (Default : 1, Min/Max Range : 1~50)


.. tabs::

	.. code-tab:: python

		def SetSimulationCGFinishCondition(_cgFinishCondition : int) -> None
		"""
		@brief Set simulation finish condition
		@param _cgFinishCondition : Conjugate Gradient finish condition (0: iteration, 1: residual)
		"""

	.. code-tab:: c++

		 SetSimulationCGFinishCondition(int _cgFinishCondition)
		/// @brief Set simulation finish condition
		/// @param _cgFinishCondition : Conjugate Gradient finish condition (0: iteration, 1: residual)


.. tabs::

	.. code-tab:: python

		def SetSimulationCGIterationCount(_cgIterationCount : int) -> None
		"""
		@brief Set Conjugate Gradient iteration count per one step.
		@param _cgIterationCount : iteration count (Default : 50, Min/Max Range 1~1000)
		"""

	.. code-tab:: c++

		 SetSimulationCGIterationCount(int _cgIterationCount)
		/// @brief Set Conjugate Gradient iteration count per one step.
		/// @param _cgIterationCount : iteration count (Default : 50, Min/Max Range 1~1000)


.. tabs::

	.. code-tab:: python

		def SetSimulationCGResidual(_cgResidual : float) -> None
		"""
		@brief Set Conjugate Gradient relative residual value for finishing
		@param _cgResidual : relative residual value for finishing (0.0001 in Normal, 0.00001 in Animation and Fitting)
		"""

	.. code-tab:: c++

		 SetSimulationCGResidual(int _cgResidual)
		/// @brief Set Conjugate Gradient relative residual value for finishing
		/// @param _cgResidual : relative residual value for finishing (0.0001 in Normal, 0.00001 in Animation and Fitting)


.. tabs::

	.. code-tab:: python

		def SetSimulationSelfCollisionIterationCount(_selfCollisionIterationCount : int) -> None
		"""
		@brief Set self collision iteration count
		@param _selfCollisionIterationCount : self collision iteration count (Default: 1)
		"""

	.. code-tab:: c++

		 SetSimulationSelfCollisionIterationCount(int _selfCollisionIterationCount)
		/// @brief Set self collision iteration count
		/// @param _selfCollisionIterationCount : self collision iteration count (Default: 1)


.. tabs::

	.. code-tab:: python

		def SetSimulationAirDamping(_airDamping : float) -> None
		"""
		@brief Set air damping value
		@param _airDamping : air damping(Default: 1.0)
		"""

	.. code-tab:: c++

		 SetSimulationAirDamping(int _airDamping)
		/// @brief Set air damping value
		/// @param _airDamping : air damping(Default: 1.0)


.. tabs::

	.. code-tab:: python

		def SetSimulationGravity(_gravity : float) -> None
		"""
		@brief Set gravity value in y-axis
		@param _gravity : gravity  (Default: -9800.0 mm/s^2)
		"""

	.. code-tab:: c++

		 SetSimulationGravity(int _gravity)
		/// @brief Set gravity value in y-axis
		/// @param _gravity : gravity  (Default: -9800.0 mm/s^2)


.. tabs::

	.. code-tab:: python

		def SetSimulationNumberOfCPUInUse(_numberOfSimulationInUse : int) -> None
		"""
		@brief Set the number of CPUs for simulation
		@param _numberOfSimulationInUse : the number of CPUs (Default: total number of logical threads - 1, Min/Max Range : 1~total number of logical threads)
		"""

	.. code-tab:: c++

		 SetSimulationNumberOfCPUInUse(int _numberOfSimulationInUse)
		/// @brief Set the number of CPUs for simulation
		/// @param _numberOfSimulationInUse : the number of CPUs (Default: total number of logical threads - 1, Min/Max Range : 1~total number of logical threads)


.. tabs::

	.. code-tab:: python

		def SetSimulationNonlinearSimulation(_bNonlinearSimulation : bool) -> None
		"""
		@brief Set nonlinear simulation
		@param _bNonlinearSimulation : true for enable, false for disable
		"""

	.. code-tab:: c++

		 SetSimulationNonlinearSimulation(int _bNonlinearSimulation)
		/// @brief Set nonlinear simulation
		/// @param _bNonlinearSimulation : true for enable, false for disable


.. tabs::

	.. code-tab:: python

		def SetSimulationGroundCollision(_bGroundCollision : bool) -> None
		"""
		@brief Set ground collision
		@param _bGroundCollision : true for enable, false for disable
		"""

	.. code-tab:: c++

		 SetSimulationGroundCollision(int _bGroundCollision)
		/// @brief Set ground collision
		/// @param _bGroundCollision : true for enable, false for disable


.. tabs::

	.. code-tab:: python

		def SetSimulationGroundHeight(_groundHeight : float) -> None
		"""
		@brief Set ground height value
		@param _groundHeight : ground height in y-axis (Default: 0.0)
		"""

	.. code-tab:: c++

		 SetSimulationGroundHeight(int _groundHeight)
		/// @brief Set ground height value
		/// @param _groundHeight : ground height in y-axis (Default: 0.0)


.. tabs::

	.. code-tab:: python

		def SetSimulationSelfCollisionAvoidanceStiffness(_avoidanceStiffness : float) -> None
		"""
		@brief Set stiffness of the inserted spring to avoid self collision
		@param _avoidanceStiffness : (Default: 0.001)
		"""

	.. code-tab:: c++

		 SetSimulationSelfCollisionAvoidanceStiffness(int _avoidanceStiffness)
		/// @brief Set stiffness of the inserted spring to avoid self collision
		/// @param _avoidanceStiffness : (Default: 0.001)


.. tabs::

	.. code-tab:: python

		def SetSimulationLayerBasedCollisionDetection(_bUseLayer : bool) -> None
		"""
		@brief Set layer based collision detection 
		@param _bUseLayer : true for enable, false for disable
		"""

	.. code-tab:: c++

		 SetSimulationLayerBasedCollisionDetection(int _bUseLayer)
		/// @brief Set layer based collision detection 
		/// @param _bUseLayer : true for enable, false for disable


.. tabs::

	.. code-tab:: python

		def StartNesting() -> None
		"""
		@brief Start Nesting Simulation
		"""

	.. code-tab:: c++

		 StartNesting()
		/// @brief Start Nesting Simulation


.. tabs::

	.. code-tab:: python

		def GetNestingBufferSpacing() -> float
		"""
		@brief Get Nesting Buffer Space 
		"""

	.. code-tab:: c++

		 GetNestingBufferSpacing()
		/// @brief Get Nesting Buffer Space 


.. tabs::

	.. code-tab:: python

		def SetNestingBufferSpacing(_mm : float) -> None
		"""
		@brief Set Nesting Buffer Space 
		@param _mm : Buffer Space 
		"""

	.. code-tab:: c++

		 SetNestingBufferSpacing(float _mm)
		/// @brief Set Nesting Buffer Space 
		/// @param _mm : Buffer Space 


.. tabs::

	.. code-tab:: python

		def SetNestingTargetColorway(_colorwayList : list[int]) -> None
		"""
		@brief Colorway index to apply nesting result
		@param _colorwayList : Colorway index to apply nesting result
		"""

	.. code-tab:: c++

		 SetNestingTargetColorway(std::vector<int> _colorwayList)
		/// @brief Colorway index to apply nesting result
		/// @param _colorwayList : Colorway index to apply nesting result


.. tabs::

	.. code-tab:: python

		def GetNestingTargetColorway() -> list[int]
		"""
		@brief Gets the colorway index to apply nesting to.
		"""

	.. code-tab:: c++

		 GetNestingTargetColorway()
		/// @brief Gets the colorway index to apply nesting to.


.. tabs::

	.. code-tab:: python

		def SetAvatarMeshTexture(_matShapeName : str, _matMeshIndex : int, _textureImagePath : str) -> bool
		"""
		@brief Import AvtarTexture Body Part(face, body, arm, leg)
		@param _bodyShapeName: input avatar shape name(find object browser)
		@param _matShapeIndex: mat shape index (0: face, 1:body, 2:arm, 3:leg)
		@param _textureImagePath: change texture full path
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 SetAvatarBodyTexture(const wstring& _bodyShapeName, int _matShapeIndex, const wstring& _textureImagePath)
		/// @brief Import AvtarTexture Body Part(face, body, arm, leg)
		/// @param _bodyShapeName: input avatar shape name(find object browser)
		/// @param _matShapeIndex: mat shape index (0: face, 1:body, 2:arm, 3:leg)
		/// @param _textureImagePath: change texture full path
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def SetAnimationRecording(_bStart : bool) -> None
		"""
		@brief set animation recording
		@param _bStart: true for recording start, false for recording stop
		"""

	.. code-tab:: c++

		 SetAnimationRecording(bool _bStart)
		/// @brief set animation recording
		/// @param _bStart: true for recording start, false for recording stop


.. tabs::

	.. code-tab:: python

		def SetCurrentAnimationFrame(_frame : double) -> None
		"""
		@brief set current animation frame
		@param _frame: Value for setting current frame
		"""

	.. code-tab:: c++

		 SetCurrentAnimationFrame(double _frame)
		/// @brief set current animation frame
		/// @param _frame: Value for setting current frame


.. tabs::

	.. code-tab:: python

		def GetCurrentAnimationFrame() -> double
		"""
		@brief get current animation frame
		"""

	.. code-tab:: c++

		 GetCurrentAnimationFrame()
		/// @brief get current animation frame


.. tabs::

	.. code-tab:: python

		def SetStartAnimationFrame(_frame : double) -> None
		"""
		@brief set start animation frame
		@param _frame: Value for setting start frame
		"""

	.. code-tab:: c++

		 SetStartAnimationFrame(double _frame)
		/// @brief set start animation frame
		/// @param _frame: Value for setting start frame


.. tabs::

	.. code-tab:: python

		def GetStartAnimationFrame() -> double
		"""
		@brief get start animation frame
		"""

	.. code-tab:: c++

		 GetStartAnimationFrame()
		/// @brief get start animation frame


.. tabs::

	.. code-tab:: python

		def SetEndAnimationFrame(_frame : double) -> None
		"""
		@brief set end animation frame
		@param _frame: Value for setting end frame
		"""

	.. code-tab:: c++

		 SetEndAnimationFrame(double _frame)
		/// @brief set end animation frame
		/// @param _frame: Value for setting end frame


.. tabs::

	.. code-tab:: python

		def GetEndAnimationFrame() -> double
		"""
		@brief get end animation frame
		"""

	.. code-tab:: c++

		 GetEndAnimationFrame()
		/// @brief get end animation frame


.. tabs::

	.. code-tab:: python

		def GetStressMapStatus() -> bool
		"""
		@brief return current rendered status of the stress map (false = Off | true = On)
		"""

	.. code-tab:: c++

		 GetStressMapStatus()
		/// @brief return current rendered status of the stress map (false = Off | true = On)


.. tabs::

	.. code-tab:: python

		def SetStressMapStatus(_bOn : bool) -> None
		"""
		@brief set the rendered status of stress map
		@param _bOn: false = Off | true = On
		"""

	.. code-tab:: c++

		 SetStressMapStatus(bool _bOn)
		/// @brief set the rendered status of stress map
		/// @param _bOn: false = Off | true = On


.. tabs::

	.. code-tab:: python

		def GetStrainMapStatus() -> bool
		"""
		@brief return current rendered status of the strain map (false = Off | true = On)
		"""

	.. code-tab:: c++

		 GetStrainMapStatus()
		/// @brief return current rendered status of the strain map (false = Off | true = On)


.. tabs::

	.. code-tab:: python

		def SetStrainMapStatus(_bOn : bool) -> None
		"""
		@brief set the rendered status of strain map
		@param _bOn: false = Off | true = On
		"""

	.. code-tab:: c++

		 SetStrainMapStatus(bool _bOn)
		/// @brief set the rendered status of strain map
		/// @param _bOn: false = Off | true = On


.. tabs::

	.. code-tab:: python

		def GetSchematicRender() -> bool
		"""
		@brief Get Show Schematic Render Status
		"""

	.. code-tab:: c++

		 GetSchematicRender(bool _bSet)
		/// @brief Get Show Schematic Render Status


.. tabs::

	.. code-tab:: python

		def RefreshPlugIns() -> None
		"""
		@brief Refresh all PlugIns
		"""

	.. code-tab:: c++

		 RefreshPlugIns()
		/// @brief Refresh all PlugIns


.. tabs::

	.. code-tab:: python

		def SetCamViewPoint(_viewPointIndex : int) -> None
		"""
		@brief set camera view point
		@param _viewPointIndex: Value for setting camera view point index
		"""

	.. code-tab:: c++

		 SetCamViewPoint(int _viewPointIndex)
		/// @brief set camera view point
		/// @param _viewPointIndex: Value for setting camera view point index


.. tabs::

	.. code-tab:: python

		def StopNesting() -> None
		"""
		@brief Stop Nesting process
		"""

	.. code-tab:: c++

		 StopNesting()
		/// @brief Stop Nesting process


.. tabs::

	.. code-tab:: python

		def CreateModularCategory(_title : str, _folderPath : str) -> None
		"""
		@brief create modular category
		@param _title : category title, _folderPath: folder
		"""

	.. code-tab:: c++

		 CreateModularCategory(const std::wstring& _title, const std::wstring& _folderPath)
		/// @brief create modular category
		/// @param _title : category title, _folderPath: folder


.. tabs::

	.. code-tab:: python

		def DeleteModularCategory(_title : str) -> None
		"""
		@brief delete modular category
		@param _title : category title
		"""

	.. code-tab:: c++

		 DeleteModularCategory(const std::wstring& _title, const std::wstring& _folderPath)
		/// @brief delete modular category
		/// @param _title : category title


.. tabs::

	.. code-tab:: python

		def GetNestingTime() -> int
		"""
		@brief Get Nesting duration Time (milliseconds)
		"""

	.. code-tab:: c++

		 GetNestingTime()
		/// @brief Get Nesting duration Time (milliseconds)


.. tabs::

	.. code-tab:: python

		def SetSchematicSilhouetteLineWidth(_value : int) -> None
		"""
		@brief set schematic silhouette line width
		@param _value: Value for setting schematic silhouette line width
		"""

	.. code-tab:: c++

		 SetSchematicSilhouetteLineWidth(int _value)
		/// @brief set schematic silhouette line width
		/// @param _value: Value for setting schematic silhouette line width


.. tabs::

	.. code-tab:: python

		def SetSchematicSeamLineWidth(_value : int) -> None
		"""
		@brief set schematic seamline width
		@param _value: Value for setting schematic seamline width
		"""

	.. code-tab:: c++

		 SetSchematicSeamLineWidth(int _value)
		/// @brief set schematic seamline width
		/// @param _value: Value for setting schematic seamline width


.. tabs::

	.. code-tab:: python

		def SetSchematicInternalLineWidth(_value : int) -> None
		"""
		@brief set schematic internal line width
		@param _value: Value for setting chematic internal line width
		"""

	.. code-tab:: c++

		 SetSchematicInternalLineWidth(int _value)
		/// @brief set schematic internal line width
		/// @param _value: Value for setting chematic internal line width


.. tabs::

	.. code-tab:: python

		def SetSchematicTopstitchLineScalePercent(_value : int) -> None
		"""
		@brief set schematic topstitch line scale percent
		@param _value: Value for setting schematic topstitch line scale percent
		"""

	.. code-tab:: c++

		 SetSchematicTopstitchLineScalePercent(int _value)
		/// @brief set schematic topstitch line scale percent
		/// @param _value: Value for setting schematic topstitch line scale percent


.. tabs::

	.. code-tab:: python

		def SetSchematicBrightness(_value : int) -> None
		"""
		@brief set schematic brightness
		@param _value: Value for setting schematic brightness
		"""

	.. code-tab:: c++

		 SetSchematicBrightness(int _value)
		/// @brief set schematic brightness
		/// @param _value: Value for setting schematic brightness


.. tabs::

	.. code-tab:: python

		def SetShowSchematicSilhouetteLine(_bOn : bool) -> None
		"""
		@brief set show schematic silhouetteline
		@param _bOn: Value for setting showschematic silhouetteline
		"""

	.. code-tab:: c++

		 SetShowSchematicSilhouetteLine(bool _bOn)
		/// @brief set show schematic silhouetteline
		/// @param _bOn: Value for setting showschematic silhouetteline


.. tabs::

	.. code-tab:: python

		def SetShowSchematicSeamLine(_bOn : bool) -> None
		"""
		@brief set show schematic seamline
		@param _bOn: Value for setting show schematic seamline
		"""

	.. code-tab:: c++

		 SetShowSchematicSeamLine(int _bOn)
		/// @brief set show schematic seamline
		/// @param _bOn: Value for setting show schematic seamline


.. tabs::

	.. code-tab:: python

		def SetShowSchematicInternalLine(_bOn : bool) -> None
		"""
		@brief set show schematic internal line
		@param _bOn: Value for setting show schematic internalline
		"""

	.. code-tab:: c++

		 SetShowSchematicInternalLine(bool _bOn)
		/// @brief set show schematic internal line
		/// @param _bOn: Value for setting show schematic internalline


.. tabs::

	.. code-tab:: python

		def SetShowSchematicTopstitchLine(_bOn : bool) -> None
		"""
		@brief set show schematic topstitch line
		@param _bOn: Value for setting show schematic topstitchline
		"""

	.. code-tab:: c++

		 SetShowSchematicTopstitchLine(bool _bOn)
		/// @brief set show schematic topstitch line
		/// @param _bOn: Value for setting show schematic topstitchline


.. tabs::

	.. code-tab:: python

		def SetSchematicClothRenderType(_bTexture : bool) -> None
		"""
		@brief set schematic cloth render type
		@param _bTexture: Value for setting schematic cloth render type
		"""

	.. code-tab:: c++

		 SetSchematicClothRenderType(bool _bTexture)
		/// @brief set schematic cloth render type
		/// @param _bTexture: Value for setting schematic cloth render type


.. tabs::

	.. code-tab:: python

		def SetStyleLineColor(_r : int, _g : int, _b : int) -> None
		"""
		@brief set style line color
		@param int _r, int _g, int _b: Value for setting style line color
		Red: 0 ~ 255
		Green: 0 ~ 255
		Blue: 0 ~ 255
		"""

	.. code-tab:: c++

		 SetStyleLineColor(int _r, int _g, int _b)
		/// @brief set style line color
		/// @param int _r, int _g, int _b: Value for setting style line color
		Red: 0 ~ 255
		Green: 0 ~ 255
		Blue: 0 ~ 255


.. tabs::

	.. code-tab:: python

		def SetSchematicClothColor(_r : int, _g : int, _b : int) -> None
		"""
		@brief set schematic cloth color
		@param int _r, int _g, int _b: Value for setting schematic cloth color
		Red: 0 ~ 255
		Green: 0 ~ 255
		Blue: 0 ~ 255
		"""

	.. code-tab:: c++

		 SetSchematicClothColor(int _r, int _g, int _b)
		/// @brief set schematic cloth color
		/// @param int _r, int _g, int _b: Value for setting schematic cloth color
		Red: 0 ~ 255
		Green: 0 ~ 255
		Blue: 0 ~ 255


.. tabs::

	.. code-tab:: python

		def SetQualityRender(_bSet : bool) -> None
		"""
		@brief Set Quality Render status
		@param _bSet: true for enable, false for disable 
		"""

	.. code-tab:: c++

		 SetQualityRender(bool _bSet)
		/// @brief Set Quality Render status
		/// @param _bSet: true for enable, false for disable 


.. tabs::

	.. code-tab:: python

		def GetQualityRenderStatus() -> bool
		"""
		@brief Get Current Quality Render Status
		"""

	.. code-tab:: c++

		 GetQualityRenderStatus(bool _bSet)
		/// @brief Get Current Quality Render Status


.. tabs::

	.. code-tab:: python

		def BakeUVTexture(_filePath : str, _options : ImportExportOption, _bAll : bool) -> list[str]
		"""
		@brief Bake textures on UV editor
		@param _filePath: File path to be saved.
		@param _options: It bakes textures according to options, not allowing user for selecting options in Bake Textures Dialog.
		@param _bAll: true for all UV tiles, false for only 0-1 tile
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 BakeUVTexture(const string& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Bake textures on UV editor
		/// @param _filePath: File path to be saved.
		/// @param _options: It bakes textures according to options, not allowing user for selecting options in Bake Textures Dialog.
		/// @param _bAll: true for all UV tiles, false for only 0-1 tile
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def BakeUVTextureW(_filePath : str, _options : ImportExportOption, _bAll : bool) -> list[str]
		"""
		@brief Bake textures on UV editor
		@param _filePath: File path to be saved.
		@param _options: It bakes textures according to options, not allowing user for selecting options in Bake Textures Dialog.
		@param _bAll: true for all UV tiles, false for only 0-1 tile
		@return Output file paths. 
		"""

	.. code-tab:: c++

		 BakeUVTextureW(const wstring& _filePath, const Marvelous::ImportExportOption& _options)
		/// @brief Bake textures on UV editor
		/// @param _filePath: File path to be saved.
		/// @param _options: It bakes textures according to options, not allowing user for selecting options in Bake Textures Dialog.
		/// @param _bAll: true for all UV tiles, false for only 0-1 tile
		/// @return Output file paths. 


.. tabs::

	.. code-tab:: python

		def UVPacking(_bAll : bool, _bFixScaleRatio : bool, _textureFillSeam : float, _imgSize : int, _roationAngleOptions : list[int]) -> bool
		"""
		@brief Packing patterns in UV editor
		@param _bAll: true for all patterns, false for selected patterns
		@param _bFixScaleRatio: true - preserve current patterns size; false - rescale patterns
		@param _textureFillSeam, _imgSize: related values for fill texture seams
		@param _roationAngleOptions: rotation angle(degree) options for packing, default value is 0 degree ex) {0, 180} can rotate up side down
		@return If packing succeeds, return true.
		"""

	.. code-tab:: c++

		 UVPacking(bool _bAll, float _textureFillSeam, int _imgSize)
		/// @brief Packing patterns in UV editor
		/// @param _bAll: true for all patterns, false for selected patterns
		/// @param _bFixScaleRatio: true - preserve current patterns size; false - rescale patterns
		/// @param _textureFillSeam, _imgSize: related values for fill texture seams
		/// @param _roationAngleOptions: rotation angle(degree) options for packing, default value is 0 degree ex) {0, 180} can rotate up side down
		/// @return If packing succeeds, return true.


.. tabs::

	.. code-tab:: python

		def SetTrimWeight(_trimStyleIndex : int, _mass : float) -> None
		"""
		@brief Change weight of the trim style
		@param _trimStyleIndex: trimstyle index to change weight of trim style
		@param _mass: value to set weight of trim
		"""

	.. code-tab:: c++

		 SetTrimWeight(unsigned int _trimStyleIndex, float _mass)
		/// @brief Change weight of the trim style
		/// @param _trimStyleIndex: trimstyle index to change weight of trim style
		/// @param _mass: value to set weight of trim


.. tabs::

	.. code-tab:: python

		def SetColorwayColorItem(_colorwayIndex : int, _colorItemIndex : int, _plmId : str, _colorName : str, _rgb : CloApiRgb) -> None
		"""
		@brief Changes the color of the color item in colorway
		@param _colorwayIndex: colorway index to change color of color item
		@param _colorItemIndex: color item index to change color of colorway
		@param _plmId: plm id of color
		@param _colorName: name of color
		@param _rgb: rgb value of color
		"""

	.. code-tab:: c++

		 SetColorwayColorItem(int _colorwayIndex, int _colorItemIndex, std::string _plmId, std::string _colorName, Marvelous::CloApiRgb _rgb)
		/// @brief Changes the color of the color item in colorway
		/// @param _colorwayIndex: colorway index to change color of color item
		/// @param _colorItemIndex: color item index to change color of colorway
		/// @param _plmId: plm id of color
		/// @param _colorName: name of color
		/// @param _rgb: rgb value of color


.. tabs::

	.. code-tab:: python

		def GetColorwayColorItemRGB(_colorwayIndex : int, _colorItemIndex : int) -> CloApiRgb
		"""
		@brief Get rgb color value of the color item in colorway
		@param _colorwayIndex: colorway index to get rgb color value of color item
		@param _colorItemIndex: color item index to get rgb color value color of colorway
		@return a rgb color value if the indices are valid, (0, 0, 0) otherwise.
		"""

	.. code-tab:: c++

		 GetColorwayColorItemRGB(int _colorwayIndex, int _colorItemIndex)
		/// @brief Get rgb color value of the color item in colorway
		/// @param _colorwayIndex: colorway index to get rgb color value of color item
		/// @param _colorItemIndex: color item index to get rgb color value color of colorway
		/// @return a rgb color value if the indices are valid, (0, 0, 0) otherwise.


.. tabs::

	.. code-tab:: python

		def GetColorwayColorItemPlmId(_colorwayIndex : int, _colorItemIndex : int) -> str
		"""
		@brief Get plm id of the color item in colorway
		@param _colorwayIndex: colorway index to get plm id of color item
		@param _colorItemIndex: color item index to get plm id of colorway
		@return a plm id if the indices are valid, empty string otherwise.
		"""

	.. code-tab:: c++

		 GetColorwayColorItemPlmId(int _colorwayIndex, int _colorItemIndex)
		/// @brief Get plm id of the color item in colorway
		/// @param _colorwayIndex: colorway index to get plm id of color item
		/// @param _colorItemIndex: color item index to get plm id of colorway
		/// @return a plm id if the indices are valid, empty string otherwise.


.. tabs::

	.. code-tab:: python

		def GetColorwayColorItemName(_colorwayIndex : int, _colorItemIndex : int) -> str
		"""
		@brief Get color name of the color item in colorway
		@param _colorwayIndex: colorway index to get color name of color item
		@param _colorItemIndex: color item index to get color name of colorway
		@return color name if the indices are valid, empty string otherwise.
		"""

	.. code-tab:: c++

		 GetColorwayColorItemName(int _colorwayIndex, int _colorItemIndex)
		/// @brief Get color name of the color item in colorway
		/// @param _colorwayIndex: colorway index to get color name of color item
		/// @param _colorItemIndex: color item index to get color name of colorway
		/// @return color name if the indices are valid, empty string otherwise.


.. tabs::

	.. code-tab:: python

		def Refresh3DWindow() -> None
		"""
		@brief Refresh 3D Garment Window
		"""

	.. code-tab:: c++

		 Refresh3DWindow()
		/// @brief Refresh 3D Garment Window


.. tabs::

	.. code-tab:: python

		def RemovePlugInFromList(_pluginListIndex : int) -> None
		"""
		@brief Remove Plug In From PluginList
		@param _pluginListIndex: PluginList index to delete the plugin
		"""

	.. code-tab:: c++

		 RemovePlugInFromList(unsigned int _pluginListIndex)
		/// @brief Remove Plug In From PluginList
		/// @param _pluginListIndex: PluginList index to delete the plugin


.. tabs::

	.. code-tab:: python

		def AddPlugInFromFile(_filePath : str) -> None
		"""
		@brief Add Plug In From Filepath
		@param _filePath: File path to be added plugin.
		"""

	.. code-tab:: c++

		 AddPlugInFromFile(const std::string& _filePath)
		/// @brief Add Plug In From Filepath
		/// @param _filePath: File path to be added plugin.


.. tabs::

	.. code-tab:: python

		def UsePlugInFromList(_pluginListIndex : int) -> None
		"""
		@brief Use Plug In From PluginList
		@param _pluginListIndex: PluginList index to use the plugin
		"""

	.. code-tab:: c++

		 UsePlugInFromList(unsigned int _pluginListIndex)
		/// @brief Use Plug In From PluginList
		/// @param _pluginListIndex: PluginList index to use the plugin


.. tabs::

	.. code-tab:: python

		def TerminatePlugInFromList(_pluginListIndex : int) -> None
		"""
		@brief Terminate Plug In From PluginList
		@param _pluginListIndex: PluginList index to use the plugin
		"""

	.. code-tab:: c++

		 TerminatePlugInFromList(unsigned int _pluginListIndex)
		/// @brief Terminate Plug In From PluginList
		/// @param _pluginListIndex: PluginList index to use the plugin


FABRIC_API
***********
 
.. tabs::

	.. code-tab:: python

		def GetFabricCount() -> int
		"""
		@brief Get the number of fabrics
		@return the number of fabric in object browser for the current project.
		"""

	.. code-tab:: c++

		 GetFabricCount()
		/// @brief Get the number of fabrics
		/// @return the number of fabric in object browser for the current project.


.. tabs::

	.. code-tab:: python

		def GetCurrentFabricIndex() -> int
		"""
		@brief Get the index of the selected Fabric
		@return the index of selected fabric in object browser for the current project..
		"""

	.. code-tab:: c++

		 GetCurrentFabricIndex()
		/// @brief Get the index of the selected Fabric
		/// @return the index of selected fabric in object browser for the current project..


.. tabs::

	.. code-tab:: python

		def ExportZFab() -> str
		"""
		@brief Export ZFab which cotains the fabric data selected in the object browser
		@return Output file path;output files will be created in CLO temporary folder. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportZFab()
		/// @brief Export ZFab which cotains the fabric data selected in the object browser
		/// @return Output file path;output files will be created in CLO temporary folder. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportZFab(filePath : str) -> str
		"""
		@brief Export Zfab which cotains the fabric data selected in the object browser
		@param filePath: output file path
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportZFab(const string& filePath)
		/// @brief Export Zfab which cotains the fabric data selected in the object browser
		/// @param filePath: output file path
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportZFab(filePath : str, index : int) -> str
		"""
		@brief Export ZFab which cotains the fabric data in the index of the object browser
		@param filePath: output file path
		@param index: target fabric index on the object browser to export
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportZFab(const string& filePath, const int& index)
		/// @brief Export ZFab which cotains the fabric data in the index of the object browser
		/// @param filePath: output file path
		/// @param index: target fabric index on the object browser to export
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportZFabW(filePath : str, index : int) -> str
		"""
		@brief Export ZFab file which cotains the fabric data in the index of the object browser
		@param filePath: output file path
		@param index: target fabric index on the object browser to export
		@return Output file path. If an error occurs, return empty string. 
		"""

	.. code-tab:: c++

		 ExportZFabW(const wstring& filePath, const int& index)
		/// @brief Export ZFab file which cotains the fabric data in the index of the object browser
		/// @param filePath: output file path
		/// @param index: target fabric index on the object browser to export
		/// @return Output file path. If an error occurs, return empty string. 


.. tabs::

	.. code-tab:: python

		def ExportFabric(filePath : str) -> str
		"""
		@brief Export the selected fabric to the file(.jfab or .zfab)				
		@param filePath: output file path				
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportFabric(const string& filePath)
		/// @brief Export the selected fabric to the file(.jfab or .zfab)				
		/// @param filePath: output file path				
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportFabric(filePath : str, index : int) -> str
		"""
		@brief Export the selected fabric to the file(.jfab or .zfab)				
		@param filePath: output file path				
		@param index: target fabric index on the object browser to export
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportFabric(const string& filePath, const int& index)
		/// @brief Export the selected fabric to the file(.jfab or .zfab)				
		/// @param filePath: output file path				
		/// @param index: target fabric index on the object browser to export
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def ExportFabricW(filePath : str, index : int) -> str
		"""
		@brief Export the selected fabric to the file(.jfab or .zfab)				
		@param filePath: output file path				
		@param index: target fabric index on the object browser to export
		@return Output file path. If an error occurs, return empty string.
		"""

	.. code-tab:: c++

		 ExportFabricW(const wstring& filePath, const int& index)
		/// @brief Export the selected fabric to the file(.jfab or .zfab)				
		/// @param filePath: output file path				
		/// @param index: target fabric index on the object browser to export
		/// @return Output file path. If an error occurs, return empty string.


.. tabs::

	.. code-tab:: python

		def AddFabric(inputFilePath : str) -> int
		"""
		@brief Add Fabric into the Object Browser
		@param inputFilePath: 'zfab'(clo file) path or 'jfab'(json) path
		@return the index of added fabric in object browser for the current project. .
		"""

	.. code-tab:: c++

		 AddFabric(const string& inputFilePath)
		/// @brief Add Fabric into the Object Browser
		/// @param inputFilePath: 'zfab'(clo file) path or 'jfab'(json) path
		/// @return the index of added fabric in object browser for the current project. .


.. tabs::

	.. code-tab:: python

		def AddFabricW(inputFilePath : str) -> int
		"""
		@brief Add Fabric into the Object Browser
		@param inputFilePath: 'zfab'(clo file) path or 'jfab'(json) path
		@return the index of added fabric in object browser for the current project. .
		"""

	.. code-tab:: c++

		 AddFabricW(const wstring& inputFilePath)
		/// @brief Add Fabric into the Object Browser
		/// @param inputFilePath: 'zfab'(clo file) path or 'jfab'(json) path
		/// @return the index of added fabric in object browser for the current project. .


.. tabs::

	.. code-tab:: python

		def GetFirstFabricTextureName() -> str
		"""
		@brief Get the main image file name for the first fabric in the object browser for the current colorway index
		@return the name of the image file name without folder path and extension.
		"""

	.. code-tab:: c++

		 GetFirstFabricTextureName()
		/// @brief Get the main image file name for the first fabric in the object browser for the current colorway index
		/// @return the name of the image file name without folder path and extension.


.. tabs::

	.. code-tab:: python

		def GetFirstFabricTextureNameW() -> str
		"""
		@brief Get the main image file name for the first fabric in the object browser for the current colorway index
		@return the name of the image file name without folder path and extension.
		"""

	.. code-tab:: c++

		 GetFirstFabricTextureNameW()
		/// @brief Get the main image file name for the first fabric in the object browser for the current colorway index
		/// @return the name of the image file name without folder path and extension.


.. tabs::

	.. code-tab:: python

		def GetFirstFabricTextureName(colorwayIndex : int) -> str
		"""
		@brief Get the main image file name for the first fabric in the object browser for a colorway index
		@param colorwayIndex: colorway index
		@return the name of the image file name without folder path and extension.
		"""

	.. code-tab:: c++

		 GetFirstFabricTextureName(unsigned int colorwayIndex)
		/// @brief Get the main image file name for the first fabric in the object browser for a colorway index
		/// @param colorwayIndex: colorway index
		/// @return the name of the image file name without folder path and extension.


.. tabs::

	.. code-tab:: python

		def GetFirstFabricTextureNameW(colorwayIndex : int) -> str
		"""
		@brief Get the main image file name for the first fabric in the object browser for a colorway index
		@param colorwayIndex: colorway index
		@return the name of the image file name without folder path and extension.
		"""

	.. code-tab:: c++

		 GetFirstFabricTextureNameW(unsigned int colorwayIndex)
		/// @brief Get the main image file name for the first fabric in the object browser for a colorway index
		/// @param colorwayIndex: colorway index
		/// @return the name of the image file name without folder path and extension.


.. tabs::

	.. code-tab:: python

		def ChangeFabricWithJson(fabricIndex : int, inputJsonFilePath : str) -> bool
		"""
		@brief Overwrite all the properties of a fabric with json file(.jfab) 
		@param fabricIndex: target fabric index in the object browser
		@param inputJsonFilePath: the jfab file path to load on to the fabric in the fabricIndex
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ChangeFabricWithJson(unsigned int fabricIndex, const string& inputJsonFilePath)
		/// @brief Overwrite all the properties of a fabric with json file(.jfab) 
		/// @param fabricIndex: target fabric index in the object browser
		/// @param inputJsonFilePath: the jfab file path to load on to the fabric in the fabricIndex
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ChangeFabricWithJsonW(fabricIndex : int, inputJsonFilePath : str) -> bool
		"""
		@brief Overwrite all the properties of a fabric with json file(.jfab) 
		@param fabricIndex: target fabric index in the object browser
		@param inputJsonFilePath: the jfab file path to load on to the fabric in the fabricIndex
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ChangeFabricWithJsonW(unsigned int fabricIndex, const wstring& inputJsonFilePath)
		/// @brief Overwrite all the properties of a fabric with json file(.jfab) 
		/// @param fabricIndex: target fabric index in the object browser
		/// @param inputJsonFilePath: the jfab file path to load on to the fabric in the fabricIndex
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def AssignFabricToPattern(fabricIndex : int, patternIndex : int) -> bool
		"""
		@brief Assign a fabric to a pattern. 
		@param fabricIndex: the source fabric index in the object browser to apply to the target pattern
		@param patternIndex: the tagert pattern index to apply the fabric in the fabricIndex
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 AssignFabricToPattern(unsigned int fabricIndex, unsigned int patternIndex)
		/// @brief Assign a fabric to a pattern. 
		/// @param fabricIndex: the source fabric index in the object browser to apply to the target pattern
		/// @param patternIndex: the tagert pattern index to apply the fabric in the fabricIndex
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportXtexFile(fabricIndex : int, xTexFilePath : str) -> bool
		"""
		@brief Import xtex to a fabric. Overwrite all the values described in the xtex file into the Fabric
		@parm fabricIndex: the target fabric index in the object browser to import xTex file onto
		@parm xTexFilePath: the xTex file path to import
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportXtexFile(unsigned int fabricIndex, const string& xTexFilePath)		
		/// @brief Import xtex to a fabric. Overwrite all the values described in the xtex file into the Fabric
		/// @parm fabricIndex: the target fabric index in the object browser to import xTex file onto
		/// @parm xTexFilePath: the xTex file path to import
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportXtexFileW(fabricIndex : int, xTexFilePath : str) -> bool
		"""
		@brief Import xtex to a fabric. Overwrite all the values described in the xtex file into the Fabric
		@parm fabricIndex: the target fabric index in the object browser to import xTex file onto
		@parm xTexFilePath: the xTex file path to import
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportXtexFileW(unsigned int fabricIndex, const wstring& xTexFilePath)
		/// @brief Import xtex to a fabric. Overwrite all the values described in the xtex file into the Fabric
		/// @parm fabricIndex: the target fabric index in the object browser to import xTex file onto
		/// @parm xTexFilePath: the xTex file path to import
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ApplyXtexFile(fabricIndex : int, xTexFilePath : str) -> bool
		"""
		@brief Apply xtex to a fabric. Only set the values described in the xtex file into the Fabric.
		@parm fabricIndex: the target fabric index in the object browser to apply xTex file onto
		@parm xTexFilePath: the xTex file path to apply
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ApplyXtexFile(unsigned int fabricIndex, const string& xTexFilePath)
		/// @brief Apply xtex to a fabric. Only set the values described in the xtex file into the Fabric.
		/// @parm fabricIndex: the target fabric index in the object browser to apply xTex file onto
		/// @parm xTexFilePath: the xTex file path to apply
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ApplyXtexFileW(fabricIndex : int, xTexFilePath : str) -> bool
		"""
		@brief Apply xtex to a fabric. Only set the values described in the xtex file into the Fabric.
		@parm fabricIndex: the target fabric index in the object browser to apply xTex file onto
		@parm xTexFilePath: the xTex file path to apply
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ApplyXtexFile(unsigned int fabricIndex, const string& xTexFilePath)
		/// @brief Apply xtex to a fabric. Only set the values described in the xtex file into the Fabric.
		/// @parm fabricIndex: the target fabric index in the object browser to apply xTex file onto
		/// @parm xTexFilePath: the xTex file path to apply
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def DeleteFabric(fabricIndex : int) -> bool
		"""
		@brief Delete a fabric. If the fabric was assigned on Patterns, the patterns will have the default fabric
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 DeleteFabric(unsigned int fabricIndex)
		/// @brief Delete a fabric. If the fabric was assigned on Patterns, the patterns will have the default fabric
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def GetAPIMetaData(fabricIndex : int) -> str
		"""
		@brief Get API meta data for the fabric
		@parm fabricIndex: target fabric index on the Object Browser
		@return json string for meta data [key - value] list
		"""

	.. code-tab:: c++

		 GetAPIMetaData(unsigned int fabricIndex)
		/// @brief Get API meta data for the fabric
		/// @parm fabricIndex: target fabric index on the Object Browser
		/// @return json string for meta data [key - value] list


.. tabs::

	.. code-tab:: python

		def GetAPIMetaDataW(fabricIndex : int) -> str
		"""
		@brief Get API meta data for the fabric
		@parm fabricIndex: target fabric index on the Object Browser
		@return json string for meta data [key - value] list
		"""

	.. code-tab:: c++

		 GetAPIMetaDataW(unsigned int fabricIndex)
		/// @brief Get API meta data for the fabric
		/// @parm fabricIndex: target fabric index on the Object Browser
		/// @return json string for meta data [key - value] list


.. tabs::

	.. code-tab:: python

		def SetAPIMetaData(fabricIndex : int, jsonStr : str) -> bool
		"""
		@brief Set API meta data for the fabric
		@param fabricIndex: target fabric index on the Object Browser
		@param jsonStr: api meta data in string format 
		@return if it succeeds, return true
		"""

	.. code-tab:: c++

		 SetAPIMetaData(unsigned int fabricIndex, string jsonStr)
		/// @brief Set API meta data for the fabric
		/// @param fabricIndex: target fabric index on the Object Browser
		/// @param jsonStr: api meta data in string format 
		/// @return if it succeeds, return true


.. tabs::

	.. code-tab:: python

		def SetAPIMetaDataW(fabricIndex : int, jsonStr : str) -> bool
		"""
		@brief Set API meta data for the fabric
		@param fabricIndex: target fabric index on the Object Browser
		@param jsonStr: api meta data in string format 
		@return if it succeeds, return true
		"""

	.. code-tab:: c++

		 SetAPIMetaData(unsigned int fabricIndex, string jsonStr)
		/// @brief Set API meta data for the fabric
		/// @param fabricIndex: target fabric index on the Object Browser
		/// @param jsonStr: api meta data in string format 
		/// @return if it succeeds, return true


.. tabs::

	.. code-tab:: python

		def ChangeMetaDataValueForFabric(fabricIndex : int, metaDataKey : str, metaDataValue : str) -> None
		"""
		@brief Change or add Meta Data Value for the fabric with the index
		@param fabricIndex: target Fabric 
		@param metaDataKey: target Key
		@param metaDataValue: the new value for the key
		"""

	.. code-tab:: c++

		 ChangeMetaDataValueForFabric(unsigned int fabricIndex, const string& metaDataKey, const string& metaDataValue)
		/// @brief Change or add Meta Data Value for the fabric with the index
		/// @param fabricIndex: target Fabric 
		/// @param metaDataKey: target Key
		/// @param metaDataValue: the new value for the key


.. tabs::

	.. code-tab:: python

		def ChangeMetaDataValueForFabricW(fabricIndex : int, metaDataKey : str, metaDataValue : str) -> None
		"""
		@brief Change or add Meta Data Value for the fabric with the index
		@param fabricIndex: target Fabric 
		@param metaDataKey: target Key
		@param metaDataValue: the new value for the key
		"""

	.. code-tab:: c++

		 ChangeMetaDataValueForFabric(unsigned int fabricIndex, const wstring& metaDataKey, const wstring& metaDataValue)
		/// @brief Change or add Meta Data Value for the fabric with the index
		/// @param fabricIndex: target Fabric 
		/// @param metaDataKey: target Key
		/// @param metaDataValue: the new value for the key


.. tabs::

	.. code-tab:: python

		def GetFabricSize() -> int
		"""
		@brief Get the number of fabrics on the Object Browser
		@return return the number of fabrics on the object browser
		"""

	.. code-tab:: c++

		 GetFabricSize()
		/// @brief Get the number of fabrics on the Object Browser
		/// @return return the number of fabrics on the object browser


.. tabs::

	.. code-tab:: python

		def GetFabricIndexForPattern(patternIndex : int) -> int
		"""
		@brief Get the fabric index which is assigned on the pattern with the pattern index
		@param patternIndex: the input pattern index to get the fabric index
		@return fabric index on the object browser for the pattern with the pattern index
		"""

	.. code-tab:: c++

		 GetFabricIndexForPattern(int patternIndex)
		/// @brief Get the fabric index which is assigned on the pattern with the pattern index
		/// @param patternIndex: the input pattern index to get the fabric index
		/// @return fabric index on the object browser for the pattern with the pattern index


.. tabs::

	.. code-tab:: python

		def GetFabricIndex(fabricName : str) -> int
		"""
		@brief Get the fabric index which is using the fabric name
		@param fabricName: the fabric name to get the fabric index
		@return fabric index
		"""

	.. code-tab:: c++

		 GetFabricIndex(const string& fabricName)
		/// @brief Get the fabric index which is using the fabric name
		/// @param fabricName: the fabric name to get the fabric index
		/// @return fabric index


.. tabs::

	.. code-tab:: python

		def GetFabricIndexW(fabricName : str) -> int
		"""
		@brief Get the fabric index which is using the fabric name
		@param fabricName: the fabric name to get the fabric index
		@return fabric index
		"""

	.. code-tab:: c++

		 GetFabricIndexW(const wstring& fabricName)
		/// @brief Get the fabric index which is using the fabric name
		/// @param fabricName: the fabric name to get the fabric index
		/// @return fabric index


.. tabs::

	.. code-tab:: python

		def GetFabricName(fabricIndex : int) -> str
		"""
		@brief Get the fabric name of the fabric in the fabricIndex on the object browser
		@parm fabricIndex: the fabric index to get the name
		@return fabric name
		"""

	.. code-tab:: c++

		 GetFabricName(int fabricIndex)
		/// @brief Get the fabric name of the fabric in the fabricIndex on the object browser
		/// @parm fabricIndex: the fabric index to get the name
		/// @return fabric name


.. tabs::

	.. code-tab:: python

		def GetFabricNameW(fabricIndex : int) -> str
		"""
		@brief Get the fabric name of the fabric in the fabricIndex on the object browser
		@parm fabricIndex: the fabric index to get the name
		@return fabric name
		"""

	.. code-tab:: c++

		 GetFabricNameW(int fabricIndex)
		/// @brief Get the fabric name of the fabric in the fabricIndex on the object browser
		/// @parm fabricIndex: the fabric index to get the name
		/// @return fabric name


.. tabs::

	.. code-tab:: python

		def GetColorwayFabricInfo(colorwayIndex : int, fabricIndex : int) -> str
		"""
		@brief Get a fabric information for a colorway
		@param colorwayIndex: the colorway index for the fabric to get the fabric info
		@param fabricIndex: the fabricIndex for the fabric to get the fabric info
		@return json string for fabric information
		"""

	.. code-tab:: c++

		 GetColorwayFabricInfo(int colorwayIndex, int fabricIndex)
		/// @brief Get a fabric information for a colorway
		/// @param colorwayIndex: the colorway index for the fabric to get the fabric info
		/// @param fabricIndex: the fabricIndex for the fabric to get the fabric info
		/// @return json string for fabric information


.. tabs::

	.. code-tab:: python

		def GetColorwayFabricInfoW(colorwayIndex : int, fabricIndex : int) -> str
		"""
		@brief Get a fabric information for a colorway
		@param colorwayIndex: the colorway index for the fabric to get the fabric info
		@param fabricIndex: the fabricIndex for the fabric to get the fabric info
		@return json string for fabric information
		"""

	.. code-tab:: c++

		 GetColorwayFabricInfoW(int colorwayIndex, int fabricIndex)
		/// @brief Get a fabric information for a colorway
		/// @param colorwayIndex: the colorway index for the fabric to get the fabric info
		/// @param fabricIndex: the fabricIndex for the fabric to get the fabric info
		/// @return json string for fabric information


.. tabs::

	.. code-tab:: python

		def GetAPIMetaDataFromFile(filePath : str) -> str
		"""
		@brief Get API meta data for the fabric
		@param filePath: filepath (.zfab / .jfab)
		@return json string for meta data [key - value] list
		"""

	.. code-tab:: c++

		 GetAPIMetaDataFromFile(const string& filePath)
		/// @brief Get API meta data for the fabric
		/// @param filePath: filepath (.zfab / .jfab)
		/// @return json string for meta data [key - value] list


.. tabs::

	.. code-tab:: python

		def GetAPIMetaDataFromFileW(filePath : str) -> str
		"""
		@brief Get API meta data for the fabric
		@param filePath: filepath (.zfab / .jfab)
		@return json string for meta data [key - value] list
		"""

	.. code-tab:: c++

		 GetAPIMetaDataFromFileW(const wstring& filePath)
		/// @brief Get API meta data for the fabric
		/// @param filePath: filepath (.zfab / .jfab)
		/// @return json string for meta data [key - value] list


.. tabs::

	.. code-tab:: python

		def SetFabricInformation(_fabricIndex : int, _infoMap : map[str, str]) -> None
		"""
		@brief Set Fabric Information to fabric
		@param _fabricIndex: the fabricIndex for the fabric to set the fabric info
		@param _infoMap: Fabric Information (etc. Classification, Content, SupplierName, Owner)
		"""

	.. code-tab:: c++

		 SetFabricInformation(int _fabricIndex, const std::map<string, string> _infoMap)
		/// @brief Set Fabric Information to fabric
		/// @param _fabricIndex: the fabricIndex for the fabric to set the fabric info
		/// @param _infoMap: Fabric Information (etc. Classification, Content, SupplierName, Owner)


.. tabs::

	.. code-tab:: python

		def SetFabricInformationW(_fabricIndex : int, _infoMap : map[str, str]) -> None
		"""
		@brief Set Fabric Information to fabric
		@param _fabricIndex: the fabricIndex for the fabric to set the fabric info
		@param _infoMap: Fabric Information (etc. Classification, Content, SupplierName, Owner)
		"""

	.. code-tab:: c++

		 SetFabricInformationW(int _fabricIndex, const std::map<wstring, wstring> _infoMap)
		/// @brief Set Fabric Information to fabric
		/// @param _fabricIndex: the fabricIndex for the fabric to set the fabric info
		/// @param _infoMap: Fabric Information (etc. Classification, Content, SupplierName, Owner)


.. tabs::

	.. code-tab:: python

		def GetFabricInformation(_fabricIndex : int) -> map[str, str]
		"""
		@brief Get Fabric Information for fabric
		@param _fabricIndex: the fabricIndex for the fabric to get the fabric info
		@return Fabric Information
		"""

	.. code-tab:: c++

		 GetFabricInformation(int _fabricIndex)
		/// @brief Get Fabric Information for fabric
		/// @param _fabricIndex: the fabricIndex for the fabric to get the fabric info
		/// @return Fabric Information


.. tabs::

	.. code-tab:: python

		def GetFabricInformationW(_fabricIndex : int) -> map[str, str]
		"""
		@brief Get Fabric Information for fabric
		@param _fabricIndex: the fabricIndex for the fabric to get the fabric info
		@return Fabric Information
		"""

	.. code-tab:: c++

		 GetFabricInformationW(int _fabricIndex)
		/// @brief Get Fabric Information for fabric
		/// @param _fabricIndex: the fabricIndex for the fabric to get the fabric info
		/// @return Fabric Information


.. tabs::

	.. code-tab:: python

		def SetCustomImage(_fabricIndex : int, _filePath : str) -> None
		"""
		@brief Set Custom Image to fabric
		@param _fabricIndex: the fabricIndex for the fabric
		@param _filePath: filepath  (.png / .jpeg)
		"""

	.. code-tab:: c++

		 SetCustomImage(int _fabricIndex, const string& _filePath)
		/// @brief Set Custom Image to fabric
		/// @param _fabricIndex: the fabricIndex for the fabric
		/// @param _filePath: filepath  (.png / .jpeg)


.. tabs::

	.. code-tab:: python

		def SetCustomImageW(_fabricIndex : int, _filePath : str) -> None
		"""
		@brief Set Custom Image to fabric
		@param _fabricIndex: the fabricIndex for the fabric
		@param _filePath: filepath  (.png / .jpeg)
		"""

	.. code-tab:: c++

		 SetCustomImageW(int _fabricIndex, const wstring& _filePath)
		/// @brief Set Custom Image to fabric
		/// @param _fabricIndex: the fabricIndex for the fabric
		/// @param _filePath: filepath  (.png / .jpeg)


.. tabs::

	.. code-tab:: python

		def GetPrimaryFabric() -> int
		"""
		@brief Return the fabric index used for a major number of the patterns
		"""

	.. code-tab:: c++

		 GetPrimaryFabric()
		/// @brief Return the fabric index used for a major number of the patterns


.. tabs::

	.. code-tab:: python

		def SetFabricName(index : int, str : str) -> None
		"""
		@brief Change fabric name
		@param index: the target fabric index to change the name
		@param str: new name for the fabric
		"""

	.. code-tab:: c++

		 SetFabricName(unsigned int index, const string& str)
		/// @brief Change fabric name
		/// @param index: the target fabric index to change the name
		/// @param str: new name for the fabric


.. tabs::

	.. code-tab:: python

		def SetFabricNameW(index : int, wstr : str) -> None
		"""
		@brief Change fabric name
		@param index: the target fabric index to change the name
		@param str: new name for the fabric
		"""

	.. code-tab:: c++

		 SetColorwayNameW(unsigned int index, const wstring& wstr)
		/// @brief Change fabric name
		/// @param index: the target fabric index to change the name
		/// @param str: new name for the fabric


.. tabs::

	.. code-tab:: python

		def GetFabricStyleNameList() -> list[str]
		"""
		@brief Return all fabric style name
		"""

	.. code-tab:: c++

		 GetFabricStyleNameList()
		/// @brief Return all fabric style name


.. tabs::

	.. code-tab:: python

		def ImportSubstanceFile(fabricIndex : int, substanceFilePath : str) -> bool
		"""
		@brief Import substance to a fabric. 
		@parm fabricIndex: the target fabric index in the object browser to import substance file onto
		@parm substanceFilePath: the substance file path to import
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportSubstanceFile(unsigned int fabricIndex, const string& substanceFilePath)
		/// @brief Import substance to a fabric. 
		/// @parm fabricIndex: the target fabric index in the object browser to import substance file onto
		/// @parm substanceFilePath: the substance file path to import
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportSubstanceFileW(fabricIndex : int, substanceFilePath : str) -> bool
		"""
		@brief Import substance to a fabric. 
		@parm fabricIndex: the target fabric index in the object browser to import substance file onto
		@parm substanceFilePath: the substance file path to import
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportSubstanceFileW(unsigned int fabricIndex, const wstring& substanceFilePath)
		/// @brief Import substance to a fabric. 
		/// @parm fabricIndex: the target fabric index in the object browser to import substance file onto
		/// @parm substanceFilePath: the substance file path to import
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def GetFabricWidth(fabricIndex : int) -> float
		"""
		@brief Get Fabric width (mm)
		@parm fabricIndex: the target fabric index in the object browser
		@return fabric width
		"""

	.. code-tab:: c++

		 GetFabricWidth(int fabricIndex)
		/// @brief Get Fabric width (mm)
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @return fabric width


.. tabs::

	.. code-tab:: python

		def SetFabricWidth(fabricIndex : int, mm : float) -> None
		"""
		@brief Set Fabric width (mm)
		@parm fabricIndex: the target fabric index in the object browser
		@parm mm: Fabric width
		@return void
		"""

	.. code-tab:: c++

		 SetFabricWidth(int fabricIndex, float mm)
		/// @brief Set Fabric width (mm)
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @parm mm: Fabric width
		/// @return void


.. tabs::

	.. code-tab:: python

		def GetFabricLength(fabricIndex : int) -> float
		"""
		@brief Get Fabric Length (mm)
		@parm fabricIndex: the target fabric index in the object browser
		@return Fabric Length
		"""

	.. code-tab:: c++

		 GetFabricLength(int fabricIndex)
		/// @brief Get Fabric Length (mm)
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @return Fabric Length


.. tabs::

	.. code-tab:: python

		def SetTextureMapping(fabricIndex : int, mappingType : int) -> None
		"""
		@brief Set Texture Mapping Type (Repeat or Unified)
		@parm fabricIndex: the target fabric index in the object browser
		@parm mapping type: the target mapping type to set. 0: "Repeat", 1: "Unified"
		@return void
		"""

	.. code-tab:: c++

		 SetTextureMapping(unsigned int fabricIndex, int materialFace, int mappingType)
		/// @brief Set Texture Mapping Type (Repeat or Unified)
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @parm mapping type: the target mapping type to set. 0: "Repeat", 1: "Unified"
		/// @return void


.. tabs::

	.. code-tab:: python

		def SetSubstancePreset(fabricIndex : int, materialFace : int, presetIndex : int) -> None
		"""
		@brief Set Texture Mapping Type (Repeat or Unified)
		@parm fabricIndex: the target fabric index in the object browser
		@parm materialFace: the target material index in the property editor. 0: "Front", 1: "Back", 2: "Side"
		@parm presetIndex: the preset index to set
		@return void
		"""

	.. code-tab:: c++

		 SetSubstancePreset(unsigned int fabricIndex, int materialFace, int preset)
		/// @brief Set Texture Mapping Type (Repeat or Unified)
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @parm materialFace: the target material index in the property editor. 0: "Front", 1: "Back", 2: "Side"
		/// @parm presetIndex: the preset index to set
		/// @return void


.. tabs::

	.. code-tab:: python

		def SetSubstanceResolution(fabricIndex : int, materialFace : int, resolutionIndex : int) -> None
		"""
		@brief Set Texture Mapping Type (Repeat or Unified)
		@parm fabricIndex: the target fabric index in the object browser
		@parm materialFace: the target material index in the property editor. 0: "Front", 1: "Back", 2: "Side"
		@parm resolutionIndex: the resolution index to set
		@return void
		"""

	.. code-tab:: c++

		 SetSubstanceResolution(unsigned int fabricIndex, int materialFace, int resolution)
		/// @brief Set Texture Mapping Type (Repeat or Unified)
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @parm materialFace: the target material index in the property editor. 0: "Front", 1: "Back", 2: "Side"
		/// @parm resolutionIndex: the resolution index to set
		/// @return void


.. tabs::

	.. code-tab:: python

		def ImportSubstanceFileAsFaceType(_fabricIndex : int, _substanceFilePath : str, _faceType : str) -> bool
		"""
		@brief Import substance to a fabric as facetype. 
		@parm _fabricIndex: the target fabric index in the object browser to import substance file onto
		@parm _substanceFilePath: the substance file path to import
		@parm _facetype :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportSubstanceFileAsFaceType(unsigned int _fabricIndex, const string& _substanceFilePath, const string& _faceType)
		/// @brief Import substance to a fabric as facetype. 
		/// @parm _fabricIndex: the target fabric index in the object browser to import substance file onto
		/// @parm _substanceFilePath: the substance file path to import
		/// @parm _facetype :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def ImportSubstanceFileAsFaceTypeW(_fabricIndex : int, _substanceFilePath : str, _faceType : str) -> bool
		"""
		@brief Import substance to a fabric. 
		@parm _fabricIndex: the target fabric index in the object browser to import substance file onto
		@parm _substanceFilePath: the substance file path to import
		@parm _facetype :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 ImportSubstanceFileAsFaceTypeW(unsigned int _fabricIndex, const wstring& _substanceFilePath, const string& _faceType)
		/// @brief Import substance to a fabric. 
		/// @parm _fabricIndex: the target fabric index in the object browser to import substance file onto
		/// @parm _substanceFilePath: the substance file path to import
		/// @parm _facetype :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def SetUseSameMaterialAsFront(fabricIndex : int, materialFace : int, _useSameMaterial : bool) -> None
		"""
		@brief Set use same material as front. 
		@parm fabricIndex: the target fabric index in the object browser
		@parm materialFace: the target material index in the property editor. 1: "Back", 2: "Side"
		@parm _useSameMaterial: use same material as front
		@return void
		"""

	.. code-tab:: c++

		 SetUseSameMaterialAsFront(unsigned int fabricIndex, int materialFace, bool _useSameMaterial)
		/// @brief Set use same material as front. 
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @parm materialFace: the target material index in the property editor. 1: "Back", 2: "Side"
		/// @parm _useSameMaterial: use same material as front
		/// @return void


.. tabs::

	.. code-tab:: python

		def SetUseSameColorAsFront(fabricIndex : int, materialFace : int, _useSameColor : bool) -> None
		"""
		@brief Set use same color as front. 
		@parm fabricIndex: the target fabric index in the object browser
		@parm materialFace: the target material index in the property editor. 1: "Back", 2: "Side"
		@parm _useSameColor: use same color as front
		@return void
		"""

	.. code-tab:: c++

		 SetUseSameColorAsFront(unsigned int fabricIndex, int materialFace, bool _useSameMaterial)
		/// @brief Set use same color as front. 
		/// @parm fabricIndex: the target fabric index in the object browser
		/// @parm materialFace: the target material index in the property editor. 1: "Back", 2: "Side"
		/// @parm _useSameColor: use same color as front
		/// @return void


.. tabs::

	.. code-tab:: python

		def SetFabricPBRMaterialBaseColor(colorwayIndex : int, fabricIndex : int, materialFace : int, r : float, g : float, b : float, a : float) -> bool
		"""
		@brief Set a base color of PBR material in a fabric using given RGBA values.
		@parm colorwayIndex: colorway index
		@parm fabricIndex: the target fabric index in the object browser to import substance file onto
		@parm materialFace :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		@parm r : To be set as red value
		@parm g : To be set as green value
		@parm b : To be set as blue value
		@parm a : To be set as alpha value
		@return if it succeeds, return true.
		"""

	.. code-tab:: c++

		 SetFabricPBRMaterialBaseColor(unsigned int colorwayIndex, unsigned int fabricIndex, unsigned int materialFace, float r, float g, float b, float a)
		/// @brief Set a base color of PBR material in a fabric using given RGBA values.
		/// @parm colorwayIndex: colorway index
		/// @parm fabricIndex: the target fabric index in the object browser to import substance file onto
		/// @parm materialFace :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		/// @parm r : To be set as red value
		/// @parm g : To be set as green value
		/// @parm b : To be set as blue value
		/// @parm a : To be set as alpha value
		/// @return if it succeeds, return true.


.. tabs::

	.. code-tab:: python

		def GetFabricPBRMaterialBaseColor(colorwayIndex : int, fabricIndex : int, materialFace : int) -> tuple[float, float, float, float]
		"""
		@brief Get a base color of PBR material in a fabric.
		@parm colorwayIndex: colorway index
		@parm fabricIndex: the target fabric index in the object browser to import substance file onto
		@parm materialFace :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		@return RGBA float tuple
		"""

	.. code-tab:: c++

		 GetFabricPBRMaterialBaseColor(unsigned int colorwayIndex, unsigned int fabricIndex, unsigned int materialFace)
		/// @brief Get a base color of PBR material in a fabric.
		/// @parm colorwayIndex: colorway index
		/// @parm fabricIndex: the target fabric index in the object browser to import substance file onto
		/// @parm materialFace :ï¿½ï¿½Frontï¿½ï¿½, ï¿½ï¿½Backï¿½ï¿½, ï¿½ï¿½Sideï¿½ï¿½ 
		/// @return RGBA float tuple


.. tabs::

	.. code-tab:: python

		def SetCurrentFabricIndex(_index : int) -> bool
		"""
		@brief Set Current Fabric Index
		@parm _index: Fabric Index
		@return Fabric setting success or failure return
		"""

	.. code-tab:: c++

		 SetCurrentFabricIndex(int _index)
		/// @brief Set Current Fabric Index
		/// @parm _index: Fabric Index
		/// @return Fabric setting success or failure return


.. tabs::

	.. code-tab:: python

		def CreateZfabFromTextures(_filePath : str, _baseTexturePath : str, _normalTexturePath : str, _disPlacementTexturePath : str, _opacityTexturePath : str, _roughnessTexturePath : str, _metalnessTexturePath : str) -> bool
		"""
		@brief Create Zfab From Textures
		@param _filePath: created filepath (.zfab)
		@parm _baseTexturePath: the baseTexture file path to create zfab
		@parm _normalTexturePath: the normalTexturePath file path to create zfab
		@parm _disPlacementTexturePath :the disPlacementTexturePath file path to create zfab
		@parm _opacityTexturePath :the opacityTexturePath file path to create zfab
		@parm _roughnessTexturePath :the roughnessTexturePath file path to create zfab
		@parm _metalnessTexturePath :the metalnessTexturePath file path to create zfab
		@return zfab file creating success or failure return
		"""

	.. code-tab:: c++

		 CreateZfabFromTextures(const std::string& _filePath, const std::string& _baseTexturePath, const std::string& _normalTexturePath, const std::string& _disPlacementTexturePath, const std::string& _opacityTexturePath)
		/// @brief Create Zfab From Textures
		/// @param _filePath: created filepath (.zfab)
		/// @parm _baseTexturePath: the baseTexture file path to create zfab
		/// @parm _normalTexturePath: the normalTexturePath file path to create zfab
		/// @parm _disPlacementTexturePath :the disPlacementTexturePath file path to create zfab
		/// @parm _opacityTexturePath :the opacityTexturePath file path to create zfab
		/// @parm _roughnessTexturePath :the roughnessTexturePath file path to create zfab
		/// @parm _metalnessTexturePath :the metalnessTexturePath file path to create zfab
		/// @return zfab file creating success or failure return


.. tabs::

	.. code-tab:: python

		def CombineZfab(_filePath : str, _baseZfabPath : str, _targetZfabPath : str) -> None
		"""
		@brief Combining two zfab files into one
		@param _filePath: created filepath (.zfab)
		@parm _baseZfabPath: the Path to the zfab file on which the physical properties will be based
		@parm _targetZfabPath: the path to the zfab file on which the image will be based
		"""

	.. code-tab:: c++

		 CombineZfab(const std::string& _filePath, const std::string& _baseZfabPath, const std::string& _targetZfabPath)
		/// @brief Combining two zfab files into one
		/// @param _filePath: created filepath (.zfab)
		/// @parm _baseZfabPath: the Path to the zfab file on which the physical properties will be based
		/// @parm _targetZfabPath: the path to the zfab file on which the image will be based


.. tabs::

	.. code-tab:: python

		def GetRoughnessType(_index : int, _materialFace : int) -> int
		"""
		@brief Get Material RoughnessType
		@parm _index: Fabric Index, _materialFace : Fabric Material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		@return Return fabric's mateiral Roughness Type. ( 0 : Intensity, 1 : Map )
		"""

	.. code-tab:: c++

		 int GetRoughnessType()
		/// @brief Get Material RoughnessType
		/// @parm _index: Fabric Index, _materialFace : Fabric Material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		/// @return Return fabric's mateiral Roughness Type. ( 0 : Intensity, 1 : Map )


.. tabs::

	.. code-tab:: python

		def SetRoughnessType(_index : int, _materialFace : int, _roughnessType : int) -> None
		"""
		@brief Set Current Fabric's mateiral roughnessType
		@parm _index: Fabric Index, _materialFace : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE), _roughnessType : roughnessType to be set ( 0 : Intensity, 1 : Map )
		@return Fabric setting success or failure return
		"""

	.. code-tab:: c++

		 SetRoughnessType(int _index, int _materialFace, int _roughnessType)
		/// @brief Set Current Fabric's mateiral roughnessType
		/// @parm _index: Fabric Index, _materialFace : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE), _roughnessType : roughnessType to be set ( 0 : Intensity, 1 : Map )
		/// @return Fabric setting success or failure return


.. tabs::

	.. code-tab:: python

		def GetRoughnessValueIntensity(_index : int, _face : int) -> int
		"""
		@brief Get fabric material's Roughness Intensity values.
		@parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		@return Fabric material's Roughness Intensity values.
		"""

	.. code-tab:: c++

		 float GetRoughnessValueIntensity(int _index, int _face)
		/// @brief Get fabric material's Roughness Intensity values.
		/// @parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		/// @return Fabric material's Roughness Intensity values.


.. tabs::

	.. code-tab:: python

		def GetRoughnessValueMapIntensity(_index : int, _face : int) -> int
		"""
		@brief Get fabric material's map type roughness intensity values.
		@parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		@return Fabric material's map type roughness Intensity values.
		"""

	.. code-tab:: c++

		 float GetRoughnessValueMapIntensity(int _index, int _face)
		/// @brief Get fabric material's map type roughness intensity values.
		/// @parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		/// @return Fabric material's map type roughness Intensity values.


.. tabs::

	.. code-tab:: python

		def SetRoughnessValueMapIntensity(_index : int, _face : int, _value : int) -> None
		"""
		@brief Set fabric material's map type roughness intensity values.
		@parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE), _value : intensity value to be set.
		"""

	.. code-tab:: c++

		 SetRoughnessValueMapIntensity(int _index, int _face, int _value)
		/// @brief Set fabric material's map type roughness intensity values.
		/// @parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE), _value : intensity value to be set.


.. tabs::

	.. code-tab:: python

		def IsRoughnessValueMapInvert(_index : int, _face : int) -> bool
		"""
		@brief Return whether roughness map is inverted.
		@parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		@Return whether roughness map is inverted.
		"""

	.. code-tab:: c++

		 bool IsRoughnessValueMapInvert(int _index, int _face)
		/// @brief Return whether roughness map is inverted.
		/// @parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE)
		/// @Return whether roughness map is inverted.


.. tabs::

	.. code-tab:: python

		def SetRoughnessValueMapInvert(_index : int, _face : int, _bInvert : bool) -> None
		"""
		@brief SetS whether roughness map is inverted
		@parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE), bInvert : Whether roughness map is inverted.
		"""

	.. code-tab:: c++

		 bool SetRoughnessValueMapInvert(int _index, int _face, bool _bInvert)
		/// @brief SetS whether roughness map is inverted
		/// @parm _index: Fabric Index, _face : target material Face Type (0 : Front , 1 : BACK , 2 : SIDE), bInvert : Whether roughness map is inverted.


.. tabs::

	.. code-tab:: python

		def SetPBRMaterialDisplacementMap(_colorwayIndex : int, _fabricIndex : int, _path : str) -> rtual bool
		"""
		@brief Set fabric's displacement map using given image path.
		@parm _colorwayIndex: index of colorway
		@parm _fabricIndex: index of fabric
		@parm _path: path of the image file
		@Return true if succeed, false othrewise.
		"""

	.. code-tab:: c++

		 bool SetFabricDisplacementMap(unsigned int colorwayIndex, unsigned int fabricIndex, const std::string &path)
		/// @brief Set fabric's displacement map using given image path.
		/// @parm _colorwayIndex: index of colorway
		/// @parm _fabricIndex: index of fabric
		/// @parm _path: path of the image file
		/// @Return true if succeed, false othrewise.


.. tabs::

	.. code-tab:: python

		def GetPBRMaterialDisplacementMapValue(_colorwayIndex : int, _fabricIndex : int) -> rtual tuple[float, float, float, float, bool]
		"""
		@brief Get fabric's displacement map values.
		@parm _index: _colorwayIndex: index of colorway
		@parm _fabricIndex: index of fabric
		@Return [Amount, Shift, Clipping, Particle Distance, Keep(bool)] tuple if succeed, [0, 0, 0, 0, false] otherwise.
		"""

	.. code-tab:: c++

		 std::tuple<float, float, float, float, bool> GetPBRMaterialDisplacementMapValue(unsigned int _colorwayIndex, unsigned int _fabricIndex)
		/// @brief Get fabric's displacement map values.
		/// @parm _index: _colorwayIndex: index of colorway
		/// @parm _fabricIndex: index of fabric
		/// @Return [Amount, Shift, Clipping, Particle Distance, Keep(bool)] tuple if succeed, [0, 0, 0, 0, false] otherwise.


.. tabs::

	.. code-tab:: python

		def SetPBRMaterialDisplacementMapValue(_colorwayIndex : int, _fabricIndex : int, _amount : float, _shift : float, _clipping : float, _particleDist : float, _keep : bool) -> rtual bool
		"""
		@brief Set fabric's displacement map values.
		@parm _colorwayIndex: index of colorway
		@parm _fabricIndex: index of fabric
		@parm _amount: Amount value to be set (mm)
		@parm _shift: Shift value to be set (mm)
		@parm _clipping: Clipping value to be set (mm)
		@parm _particleDist: Particle distance value to be set (mm)
		@parm _keep: Keep Continuity value to be set
		@Return true if succeed, false othrewise.
		"""

	.. code-tab:: c++

		 bool SetPBRMaterialDisplacementMapValue(unsigned int _colorwayIndex, unsigned int _fabricIndex, float _amount, float _shift, float _clipping, float _particleDist, bool _keep)
		/// @brief Set fabric's displacement map values.
		/// @parm _colorwayIndex: index of colorway
		/// @parm _fabricIndex: index of fabric
		/// @parm _amount: Amount value to be set (mm)
		/// @parm _shift: Shift value to be set (mm)
		/// @parm _clipping: Clipping value to be set (mm)
		/// @parm _particleDist: Particle distance value to be set (mm)
		/// @parm _keep: Keep Continuity value to be set
		/// @Return true if succeed, false othrewise.




PATTERN_API
***********
 
.. tabs::

	.. code-tab:: python

		def GetPatternSize() -> int
		"""
		@brief Get the number of patterns
		@return return the number of patterns on the pattern editor and avatar window
		"""

	.. code-tab:: c++

		 GetPatternSize()
		/// @brief Get the number of patterns
		/// @return return the number of patterns on the pattern editor and avatar window


.. tabs::

	.. code-tab:: python

		def GetPatternIndex(patternName : str) -> int
		"""
		@brief Get the pattern index which is using the pattern name
		@param patternName: the input pattern name to get the pattern index
		@return pattern index
		"""

	.. code-tab:: c++

		 GetPatternIndex(const string& patternName)
		/// @brief Get the pattern index which is using the pattern name
		/// @param patternName: the input pattern name to get the pattern index
		/// @return pattern index


.. tabs::

	.. code-tab:: python

		def GetPatternIndexW(patternName : str) -> int
		"""
		@brief Get the pattern index which is using the pattern name
		@param patternName: the pattern name to get the pattern index
		@return pattern index
		"""

	.. code-tab:: c++

		 GetPatternIndexW(const wstring& patternName)
		/// @brief Get the pattern index which is using the pattern name
		/// @param patternName: the pattern name to get the pattern index
		/// @return pattern index


.. tabs::

	.. code-tab:: python

		def GetPatternInformation(patternIndex : int) -> str
		"""
		@brief Get the pattern information which is using for pattern index
		@param patternIndex: the pattern index to get the pattern information
		@return json string for pattern information
		"""

	.. code-tab:: c++

		 GetPatternInformation(int patternIndex)
		/// @brief Get the pattern information which is using for pattern index
		/// @param patternIndex: the pattern index to get the pattern information
		/// @return json string for pattern information


.. tabs::

	.. code-tab:: python

		def GetPatternInformationW(patternIndex : int) -> str
		"""
		@brief Get the pattern information which is using for pattern index
		@param patternIndex: the pattern index to get the pattern information
		@return json string for pattern information
		"""

	.. code-tab:: c++

		 GetPatternInformationW(int patternIndex)
		/// @brief Get the pattern information which is using for pattern index
		/// @param patternIndex: the pattern index to get the pattern information
		/// @return json string for pattern information


.. tabs::

	.. code-tab:: python

		def GetPatternCount() -> int
		"""
		@brief Get the number of patterns
		@return return the number of patterns on the pattern editor and avatar window
		"""

	.. code-tab:: c++

		 GetPatternCount()
		/// @brief Get the number of patterns
		/// @return return the number of patterns on the pattern editor and avatar window


.. tabs::

	.. code-tab:: python

		def GetPatternInputInformation(_patternIndex : int) -> str
		"""
		@brief Get the pattern input information which is using for pattern index
		@param patternIndex: the pattern index to get the pattern input information
		@return json string for pattern input information
		"""

	.. code-tab:: c++

		 GetPatternInputInformation(int patternIndex)
		/// @brief Get the pattern input information which is using for pattern index
		/// @param patternIndex: the pattern index to get the pattern input information
		/// @return json string for pattern input information


.. tabs::

	.. code-tab:: python

		def GetPatternInputInformationW(_patternIndex : int) -> str
		"""
		@brief Get the pattern input information which is using for pattern index
		@param patternIndex: the pattern index to get the pattern input information
		@return json string for pattern input information
		"""

	.. code-tab:: c++

		 GetPatternInputInformationW(int patternIndex)
		/// @brief Get the pattern input information which is using for pattern index
		/// @param patternIndex: the pattern index to get the pattern input information
		/// @return json string for pattern input information


.. tabs::

	.. code-tab:: python

		def GetPatternInputInformation() -> str
		"""
		@brief Get the pattern input information which is using for pattern index
		@param patternIndex: the pattern index to get the pattern input information
		@return json string for pattern input information
		"""

	.. code-tab:: c++

		 GetPatternInputInformation()
		/// @brief Get the pattern input information which is using for pattern index
		/// @param patternIndex: the pattern index to get the pattern input information
		/// @return json string for pattern input information


.. tabs::

	.. code-tab:: python

		def GetPatternInputInformationW() -> str
		"""
		@brief Get the pattern input information which is using for pattern index
		@param patternIndex: the pattern index to get the pattern input information
		@return json string for pattern input information
		"""

	.. code-tab:: c++

		 GetPatternInputInformationW()
		/// @brief Get the pattern input information which is using for pattern index
		/// @param patternIndex: the pattern index to get the pattern input information
		/// @return json string for pattern input information


.. tabs::

	.. code-tab:: python

		def GetPatternPieceArea(_patternIndex : int) -> float
		"""
		@brief Get the pattern piece area which is using for pattern index
		@return return pattern piece
		"""

	.. code-tab:: c++

		 GetPatternPieceArea()
		/// @brief Get the pattern piece area which is using for pattern index
		/// @return return pattern piece


.. tabs::

	.. code-tab:: python

		def GetLineLength(_patternIndex : int, _lineIndex : int) -> float
		"""
		@brief Get the pattern line length which is using for pattern index and line index
		@return return line length
		"""

	.. code-tab:: c++

		 GetLineLength()
		/// @brief Get the pattern line length which is using for pattern index and line index
		/// @return return line length


.. tabs::

	.. code-tab:: python

		def GetLineLength(_patternIndex : int, _childrenIndex : int, _lineIndex : int) -> float
		"""
		@brief Get the pattern line length which is using for pattern index and children shape index and line index
		@return return line length
		"""

	.. code-tab:: c++

		 GetLineLengthForInnerShape()
		/// @brief Get the pattern line length which is using for pattern index and children shape index and line index
		/// @return return line length


.. tabs::

	.. code-tab:: python

		def GetParticleDistanceOfPattern(_patternIndex : int) -> float
		"""
		@brief Get particle distance which is using pattern index
		@param patternIndex: the pattern index to get the pattern particle distance
		@return Output particle distance; If an error occurs, return MIN_PARTICLE_DISTANCE, 0.8f.
		"""

	.. code-tab:: c++

		 GetParticleDistanceOfPattern(int _patternIndex)
		/// @brief Get particle distance which is using pattern index
		/// @param patternIndex: the pattern index to get the pattern particle distance
		/// @return Output particle distance; If an error occurs, return MIN_PARTICLE_DISTANCE, 0.8f.


.. tabs::

	.. code-tab:: python

		def GetParticleDistanceOfPattern(_patternName : str) -> float
		"""
		@brief Get particle distance which is using the pattern name
		@param patternName: the pattern name to get the pattern particle distance
		@return Output particle distance; If an error occurs, return MIN_PARTICLE_DISTANCE, 0.8f.
		"""

	.. code-tab:: c++

		 GetParticleDistanceOfPattern(const string& _patternName)
		/// @brief Get particle distance which is using the pattern name
		/// @param patternName: the pattern name to get the pattern particle distance
		/// @return Output particle distance; If an error occurs, return MIN_PARTICLE_DISTANCE, 0.8f.


.. tabs::

	.. code-tab:: python

		def GetParticleDistanceOfPatternW(_patternName : str) -> float
		"""
		@brief Get particle distance which is using the pattern name
		@param patternName: the pattern name to get the pattern particle distance
		@return Output particle distance; If an error occurs, return MIN_PARTICLE_DISTANCE, 0.8f.
		"""

	.. code-tab:: c++

		 GetParticleDistanceOfPatternW(const wstring& _patternName)
		/// @brief Get particle distance which is using the pattern name
		/// @param patternName: the pattern name to get the pattern particle distance
		/// @return Output particle distance; If an error occurs, return MIN_PARTICLE_DISTANCE, 0.8f.


.. tabs::

	.. code-tab:: python

		def GetMeshCountByType(_patternIndex : int) -> map[str, str]
		"""
		@brief Get mesh face, vertex count by mesh type which is using pattern index
		@param patternIndex: the pattern index to get the pattern mesh face, vertex count
		@return Output map string mesh face,vertex count, mesh type; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetMeshCountByType(int _patternIndex)
		/// @brief Get mesh face, vertex count by mesh type which is using pattern index
		/// @param patternIndex: the pattern index to get the pattern mesh face, vertex count
		/// @return Output map string mesh face,vertex count, mesh type; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetMeshCountByType(_patternName : str) -> map[str, str]
		"""
		@brief Get mesh face, vertex count by mesh type which is using the pattern name
		@param patternName: the pattern name to get the pattern mesh face, vertex count
		@return Output map string mesh face,vertex count, mesh type; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetMeshCountByType(const string& _patternName)
		/// @brief Get mesh face, vertex count by mesh type which is using the pattern name
		/// @param patternName: the pattern name to get the pattern mesh face, vertex count
		/// @return Output map string mesh face,vertex count, mesh type; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetMeshCountByTypeW(_patternName : str) -> map[str, str]
		"""
		@brief Get mesh face, vertex count by mesh type which is using the pattern name
		@param patternName: the pattern name to get the pattern mesh face, vertex count
		@return Output map string mesh face,vertex count, mesh type; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetMeshCountByTypeW(const wstring& _patternName)
		/// @brief Get mesh face, vertex count by mesh type which is using the pattern name
		/// @param patternName: the pattern name to get the pattern mesh face, vertex count
		/// @return Output map string mesh face,vertex count, mesh type; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetShrinkagePercentage(_patternIndex : int) -> map[str, str]
		"""
		@brief Get ShrinkagePercentage each width, height which is using pattern index
		@param patternIndex: the pattern index to get the pattern shrinkagePercentage each width, height
		@return Output map string shrinkagePercentage width, height; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetShrinkagePercentage(int _patternIndex)
		/// @brief Get ShrinkagePercentage each width, height which is using pattern index
		/// @param patternIndex: the pattern index to get the pattern shrinkagePercentage each width, height
		/// @return Output map string shrinkagePercentage width, height; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetShrinkagePercentage(_patternName : str) -> map[str, str]
		"""
		@brief Get ShrinkagePercentage each width, height which is using the pattern name
		@param patternName: the pattern name to get the pattern shrinkagePercentage each width, height
		@return Output map string shrinkagePercentage width, height; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetShrinkagePercentage(const string& _patternName)
		/// @brief Get ShrinkagePercentage each width, height which is using the pattern name
		/// @param patternName: the pattern name to get the pattern shrinkagePercentage each width, height
		/// @return Output map string shrinkagePercentage width, height; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetShrinkagePercentageW(_patternName : str) -> map[str, str]
		"""
		@brief Get ShrinkagePercentage each width, height which is using the pattern name
		@param patternName: the pattern name to get the pattern shrinkagePercentage each width, height
		@return Output map string shrinkagePercentage width, height; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetShrinkagePercentageW(const wstring& _patternName)
		/// @brief Get ShrinkagePercentage each width, height which is using the pattern name
		/// @param patternName: the pattern name to get the pattern shrinkagePercentage each width, height
		/// @return Output map string shrinkagePercentage width, height; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetBoundingBoxOfPattern() -> list[map[str, str]]
		"""
		@brief Get patterns BoundingBox Size each width, height
		@param none
		@return Output vector map string patterns BoundingBox Size width, height, pattern index, pattern count; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetBoundingBoxOfPattern()
		/// @brief Get patterns BoundingBox Size each width, height
		/// @param none
		/// @return Output vector map string patterns BoundingBox Size width, height, pattern index, pattern count; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetBoundingBoxOfPattern(_patternIndex : int) -> map[str, str]
		"""
		@brief Get BoundingBox Size each width, height which is using pattern index
		@param patternIndex: the pattern index to get the pattern BoundingBox Size each width, height
		@return Output map string BoundingBox Size width, height; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetBoundingBoxOfPattern(int _patternIndex)
		/// @brief Get BoundingBox Size each width, height which is using pattern index
		/// @param patternIndex: the pattern index to get the pattern BoundingBox Size each width, height
		/// @return Output map string BoundingBox Size width, height; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetBoundingBoxOfPattern(_patternName : str) -> map[str, str]
		"""
		@brief Get BoundingBox Size each width, height which is using the pattern name
		@param patternName: the pattern name to get the pattern BoundingBox Size each width, height
		@return Output map string BoundingBox Size width, height, pattern index; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetBoundingBoxOfPattern(const string& _patternName)
		/// @brief Get BoundingBox Size each width, height which is using the pattern name
		/// @param patternName: the pattern name to get the pattern BoundingBox Size each width, height
		/// @return Output map string BoundingBox Size width, height, pattern index; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetBoundingBoxOfPatternW(_patternName : str) -> map[str, str]
		"""
		@brief Get BoundingBox Size each width, height which is using the pattern name
		@param patternName: the pattern name to get the pattern BoundingBox Size each width, height
		@return Output map string BoundingBox Size width, height, pattern index; If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetBoundingBoxOfPatternW(const wstring& _patternName)
		/// @brief Get BoundingBox Size each width, height which is using the pattern name
		/// @param patternName: the pattern name to get the pattern BoundingBox Size each width, height
		/// @return Output map string BoundingBox Size width, height, pattern index; If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def SetParticleDistanceOfPattern(_patternIndex : int, _length : float) -> None
		"""
		@brief Set particle distance using pattern index, length
		@param		patternIndex: the pattern index to set the pattern particle distance,
		length: the length value to determine particle distance
		"""

	.. code-tab:: c++

		 SetParticleDistanceOfPattern(int _patternIndex, float _length)
		/// @brief Set particle distance using pattern index, length
		/// @param		patternIndex: the pattern index to set the pattern particle distance,
		length: the length value to determine particle distance


.. tabs::

	.. code-tab:: python

		def SetParticleDistanceOfPatterns(_length : float) -> None
		"""
		@brief Set patterns particle distance using length
		@param length: the length value to determine particle distance
		"""

	.. code-tab:: c++

		 SetParticleDistanceOfPatterns()
		/// @brief Set patterns particle distance using length
		/// @param length: the length value to determine particle distance


.. tabs::

	.. code-tab:: python

		def SetMeshType(_patternIndex : int, _meshType : str) -> None
		"""
		@brief Set mesh type to get mesh count information
		@param		patternIndex: the pattern index to set the pattern mesh type,
		meshType: the mesh type to set the pattern mesh type "Triangle", "Quad" Other types not allowed
		"""

	.. code-tab:: c++

		 SetMeshType(int _patternIndex, const string& _meshType)
		/// @brief Set mesh type to get mesh count information
		/// @param		patternIndex: the pattern index to set the pattern mesh type,
		meshType: the mesh type to set the pattern mesh type "Triangle", "Quad" Other types not allowed


.. tabs::

	.. code-tab:: python

		def SetMeshTypeW(_patternIndex : int, _meshType : str) -> None
		"""
		@brief Set mesh type to get mesh count information
		@param		patternIndex: the pattern index to set the pattern mesh type,
		meshType: the mesh type to set the pattern mesh type "Triangle", "Quad" Other types not allowed
		"""

	.. code-tab:: c++

		 SetMeshType(int _patternIndex, const wstring& _meshType)
		/// @brief Set mesh type to get mesh count information
		/// @param		patternIndex: the pattern index to set the pattern mesh type,
		meshType: the mesh type to set the pattern mesh type "Triangle", "Quad" Other types not allowed


.. tabs::

	.. code-tab:: python

		def SetWidthShrinkagePercentage(_patternIndex : int, _width : float) -> None
		"""
		@brief Set Width Shrinkage Percentage using pattern index, width
		@param		patternIndex: the pattern index to set the pattern width shrinkage percentage,
		width: the width value to determine width shrinkage percentage
		"""

	.. code-tab:: c++

		 SetWidthShrinkagePercentage (int _patternIndex, float _width)
		/// @brief Set Width Shrinkage Percentage using pattern index, width
		/// @param		patternIndex: the pattern index to set the pattern width shrinkage percentage,
		width: the width value to determine width shrinkage percentage


.. tabs::

	.. code-tab:: python

		def SetHeightShrinkagePercentage(_patternIndex : int, _height : float) -> None
		"""
		@brief Set Height Shrinkage Percentage using pattern index, height
		@param		patternIndex: the pattern index to set the pattern height shrinkage percentage,
		height: the height value to determine width shrinkage percentage
		"""

	.. code-tab:: c++

		 SetHeightShrinkagePercentage (int _patternIndex, float _height)
		/// @brief Set Height Shrinkage Percentage using pattern index, height
		/// @param		patternIndex: the pattern index to set the pattern height shrinkage percentage,
		height: the height value to determine width shrinkage percentage


.. tabs::

	.. code-tab:: python

		def GetArrangementList() -> list[map[str, str]]
		"""
		@brief Get all ArrangementList
		@param		none
		@return Output vector map string Arrangement information of avatar arrangementlist (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return vector infoMap
		"""

	.. code-tab:: c++

		 GetArrangementList()
		/// @brief Get all ArrangementList
		/// @param		none
		/// @return Output vector map string Arrangement information of avatar arrangementlist (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return vector infoMap


.. tabs::

	.. code-tab:: python

		def GetArrangementOfPattern() -> list[map[str, str]]
		"""
		@brief Get Arrangement of patterns
		@param		none
		@return Output vector map string Arrangement information of patterns (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return vector infoMap
		"""

	.. code-tab:: c++

		 GetArrangementOfPattern()
		/// @brief Get Arrangement of patterns
		/// @param		none
		/// @return Output vector map string Arrangement information of patterns (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return vector infoMap


.. tabs::

	.. code-tab:: python

		def GetArrangementOfPattern(_patternIndex : int) -> map[str, str]
		"""
		@brief Get Arrangement of pattern which is using pattern index
		@param patternIndex: the pattern index to get the pattern arrangement information
		@return Output map string Arrangement information of pattern (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetArrangementOfPattern(int _patternIndex)
		/// @brief Get Arrangement of pattern which is using pattern index
		/// @param patternIndex: the pattern index to get the pattern arrangement information
		/// @return Output map string Arrangement information of pattern (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetArrangementOfPattern(_patternName : str) -> map[str, str]
		"""
		@brief Get Arrangement of pattern which is using the pattern name
		@param patternName: the pattern name to get the pattern arrangement information
		@return Output map string Arrangement information of pattern (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetArrangementOfPattern(const string& _patternName)
		/// @brief Get Arrangement of pattern which is using the pattern name
		/// @param patternName: the pattern name to get the pattern arrangement information
		/// @return Output map string Arrangement information of pattern (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def GetArrangementOfPatternW(_patternName : str) -> map[str, str]
		"""
		@brief Get Arrangement of pattern which is using the pattern name
		@param patternName: the pattern name to get the pattern arrangement information
		@return Output map string Arrangement information of pattern (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return infoMap
		"""

	.. code-tab:: c++

		 GetArrangementOfPatternW(const wstring& _patternName)
		/// @brief Get Arrangement of pattern which is using the pattern name
		/// @param patternName: the pattern name to get the pattern arrangement information
		/// @return Output map string Arrangement information of pattern (Arrangement Name,Type, Offset x,y,z, Orientation); If an error occurs, return infoMap


.. tabs::

	.. code-tab:: python

		def SetArrangementShapeStyle(_patternIndex : int, _shapeStyle : str) -> None
		"""
		@brief Set Arrangement ShapeStyle to set Arrangement ShapeStyle
		@param		patternIndex: the pattern index to set the pattern Arrangement shapeStyle,
		shapeStyle: the shapeStyle to set the pattern shapeStyle "Flat", "Curved" Other types not allowed
		"""

	.. code-tab:: c++

		 SetArrangementShapeStyle(int _patternIndex, const string& _shapeStyle)
		/// @brief Set Arrangement ShapeStyle to set Arrangement ShapeStyle
		/// @param		patternIndex: the pattern index to set the pattern Arrangement shapeStyle,
		shapeStyle: the shapeStyle to set the pattern shapeStyle "Flat", "Curved" Other types not allowed


.. tabs::

	.. code-tab:: python

		def SetArrangementShapeStyleW(_patternIndex : int, _shapeStyle : str) -> None
		"""
		@brief Set Arrangement ShapeStyle to set Arrangement ShapeStyle
		@param		patternIndex: the pattern index to set the pattern arrangement ShapeStyle,
		shapeStyle: the shapeStyle to set the pattern shapeStyle "Flat", "Curved" Other types not allowed
		"""

	.. code-tab:: c++

		 SetArrangementShapeStyleW(int _patternIndex, const wstring& _shapeStyle)
		/// @brief Set Arrangement ShapeStyle to set Arrangement ShapeStyle
		/// @param		patternIndex: the pattern index to set the pattern arrangement ShapeStyle,
		shapeStyle: the shapeStyle to set the pattern shapeStyle "Flat", "Curved" Other types not allowed


.. tabs::

	.. code-tab:: python

		def SetArrangementPosition(_patternIndex : int, _positionX : int, _positionY : int, _offset : int) -> None
		"""
		@brief Set Arrangement Position using positionX, positionY, offset
		@param		patternIndex: the pattern index to set the pattern arrangement position,
		positionX, positionY, offset : the value to determine pattern arrangement positionX, positionY, offset
		"""

	.. code-tab:: c++

		 SetArrangementPosition(int _patternIndex, int _positionX, int _positionY, int _offset)
		/// @brief Set Arrangement Position using positionX, positionY, offset
		/// @param		patternIndex: the pattern index to set the pattern arrangement position,
		positionX, positionY, offset : the value to determine pattern arrangement positionX, positionY, offset


.. tabs::

	.. code-tab:: python

		def SetArrangementOrientation(_patternIndex : int, _orientation : int) -> None
		"""
		@brief Set Arrangement Orientation using pattern arrangement Orientation
		@param		patternIndex: the pattern index to set the pattern arrangement orientation,
		Orientation: the value to determine pattern arrangement orientation
		"""

	.. code-tab:: c++

		 SetArrangementOrientation(int _patternIndex, int _orientation)
		/// @brief Set Arrangement Orientation using pattern arrangement Orientation
		/// @param		patternIndex: the pattern index to set the pattern arrangement orientation,
		Orientation: the value to determine pattern arrangement orientation


.. tabs::

	.. code-tab:: python

		def SetArrangement(_patternIndex : int, _arrangementIndex : int) -> None
		"""
		@brief Set Arrangement using arrangementlist Index
		@param		patternIndex: the pattern index to set the arrangement
		ArrangementIndex: the value to determine arrangement information
		"""

	.. code-tab:: c++

		 SetArrangement(int _patternIndex, int _arrangementIndex)
		/// @brief Set Arrangement using arrangementlist Index
		/// @param		patternIndex: the pattern index to set the arrangement
		ArrangementIndex: the value to determine arrangement information


.. tabs::

	.. code-tab:: python

		def CopyPatternPiecePos(_patternPieceIndex : int, _x : float, _y : float) -> int
		"""
		@brief Copy Pattern using the pattern index and x,y position
		@param		patternIndex: the pattern index for copying pattern
		positionX, positionY : the value to determine pattern copy position
		"""

	.. code-tab:: c++

		 CopyPatternPiecePos(int _patternPieceIndex, float _x, float _y)
		/// @brief Copy Pattern using the pattern index and x,y position
		/// @param		patternIndex: the pattern index for copying pattern
		positionX, positionY : the value to determine pattern copy position


.. tabs::

	.. code-tab:: python

		def CopyPatternPieceMove(_patternPieceIndex : int, _offsetX : float, _offsetY : float) -> int
		"""
		@brief Copy Pattern using the pattern index and x,y offset distance
		@param		patternIndex: the pattern index for copying pattern
		_offsetX, _offsetY : the value to determine pattern copy offset distance,
		@return return copy pattern index
		"""

	.. code-tab:: c++

		 CopyPatternPiecePos(int _patternPieceIndex, float _offsetX, float _offsetY)
		/// @brief Copy Pattern using the pattern index and x,y offset distance
		/// @param		patternIndex: the pattern index for copying pattern
		_offsetX, _offsetY : the value to determine pattern copy offset distance,
		/// @return return copy pattern index


.. tabs::

	.. code-tab:: python

		def DeletePatternPiece(_patternIndex : int) -> None
		"""
		@brief Delete Pattern using the pattern index
		@param		patternIndex: the pattern index for delete pattern
		@return return copy pattern index
		"""

	.. code-tab:: c++

		 DeletePatternPiece(int _patternPieceIndex)
		/// @brief Delete Pattern using the pattern index
		/// @param		patternIndex: the pattern index for delete pattern
		/// @return return copy pattern index


.. tabs::

	.. code-tab:: python

		def DeleteLine(_patternIndex : int, _lineIndex : int) -> None
		"""
		@brief Delete Pattern using the pattern index
		@param		patternIndex: the pattern index for delete pattern
		@param		lineIndex: the line index for delete line
		"""

	.. code-tab:: c++

		 DeletePatternPiece(int _patternPieceIndex)
		/// @brief Delete Pattern using the pattern index
		/// @param		patternIndex: the pattern index for delete pattern
		/// @param		lineIndex: the line index for delete line


.. tabs::

	.. code-tab:: python

		def DeletePoint(_patternIndex : int, _poinIndex : int) -> None
		"""
		@brief Delete Pattern using the pattern index
		@param		patternIndex: the pattern index for delete pattern
		@param		poinIndex: the point index for delete point
		"""

	.. code-tab:: c++

		 DeletePatternPiece(int _patternPieceIndex)
		/// @brief Delete Pattern using the pattern index
		/// @param		patternIndex: the pattern index for delete pattern
		/// @param		poinIndex: the point index for delete point


.. tabs::

	.. code-tab:: python

		def FlipPatternPiece(_patternIndex : int, _bHorizontally : bool, _bEach : bool) -> None
		"""
		@brief Flip Pattern using the pattern index
		@param		patternIndex: the pattern index for flip pattern
		_bHorizontally : the value is in the flip direction
		_bEach : the value is based on the pattern local matrix
		"""

	.. code-tab:: c++

		 FlipPatternPiece(int _patternIndex, bool _bHorizontally, bool _bEach)
		/// @brief Flip Pattern using the pattern index
		/// @param		patternIndex: the pattern index for flip pattern
		_bHorizontally : the value is in the flip direction
		_bEach : the value is based on the pattern local matrix


.. tabs::

	.. code-tab:: python

		def LayerClonePatternPiecePos(_patternIndex : int, _x : float, _y : float, _bUnder : bool) -> None
		"""
		@brief Layer Clone Pattern using the pattern index and x,y position
		@param		patternIndex: the pattern index for layer clone copying pattern
		positionX, positionY : the value to determine pattern copy position
		_bUnder : the value to 3D phase pattern position
		"""

	.. code-tab:: c++

		 LayerClonePatternPiecePos(int _patternIndex, float _x, float _y, bool _bUnder)
		/// @brief Layer Clone Pattern using the pattern index and x,y position
		/// @param		patternIndex: the pattern index for layer clone copying pattern
		positionX, positionY : the value to determine pattern copy position
		_bUnder : the value to 3D phase pattern position


.. tabs::

	.. code-tab:: python

		def LayerClonePatternPieceMove(_patternIndex : int, _offsetX : float, _offsetY : float, _bUnder : bool) -> None
		"""
		@brief Layer Clone Pattern using the pattern index and x,y offset distance
		@param		patternIndex: the pattern index for layer clone copying pattern
		_offsetX, _offsetY : the value to determine pattern copy offset distance,
		_bUnder : the value to 3D phase pattern position
		"""

	.. code-tab:: c++

		 LayerClonePatternPiecePos(int _patternIndex, float _offsetX, float _offsetY, bool _bUnder)
		/// @brief Layer Clone Pattern using the pattern index and x,y offset distance
		/// @param		patternIndex: the pattern index for layer clone copying pattern
		_offsetX, _offsetY : the value to determine pattern copy offset distance,
		_bUnder : the value to 3D phase pattern position


.. tabs::

	.. code-tab:: python

		def OffsetAsInternalLine(_patternIndex : int, _lineIndex : int, _number : int, _distance : float, _bReverseDirection : bool, _bExtend : bool) -> None
		"""
		@brief OffsetAsInternalLine using the pattern index and offset option
		@param		patternIndex: the pattern index for OffsetAsInternalLine pattern
		_lineIndex: the line index for Offset line
		_number: the value for number of offset internalLines,
		_distance: the value to offset distance,
		_bReverseDirection: the value to offset reverse direction,		
		_bExtend: the value to offset internalLines extend,
		"""

	.. code-tab:: c++

		 OffsetAsInternalLine(int _patternIndex, int _lineIndex, int _number, float _distance, bool _bReverse, bool _bDirection, bool _bExtend)
		/// @brief OffsetAsInternalLine using the pattern index and offset option
		/// @param		patternIndex: the pattern index for OffsetAsInternalLine pattern
		_lineIndex: the line index for Offset line
		_number: the value for number of offset internalLines,
		_distance: the value to offset distance,
		_bReverseDirection: the value to offset reverse direction,		
		_bExtend: the value to offset internalLines extend,


.. tabs::

	.. code-tab:: python

		def UnfoldPatternPiece(_patternIndex : int, _lineIndex : int, _bHalfSymmetry : bool) -> None
		"""
		@brief Unfold Pattern using the pattern index and line index and halfSymmetry option
		@param		patternIndex: the pattern index for delete pattern
		lineIndex: the line index for unfold line
		halfSymmetry: the value to make halfSymmetry pattern
		"""

	.. code-tab:: c++

		 UnfoldPatternPiece(int _patternIndex, int _lineIndex, bool _bHalfSymmetry)
		/// @brief Unfold Pattern using the pattern index and line index and halfSymmetry option
		/// @param		patternIndex: the pattern index for delete pattern
		lineIndex: the line index for unfold line
		halfSymmetry: the value to make halfSymmetry pattern


.. tabs::

	.. code-tab:: python

		def GetPatternPieceName(_patternIndex : int) -> str
		"""
		@brief Get Pattern name using the pattern index
		@param		_patternIndex: the pattern index for get name
		"""

	.. code-tab:: c++

		 GetPatternPieceName(int _patternIndex)
		/// @brief Get Pattern name using the pattern index
		/// @param		_patternIndex: the pattern index for get name


.. tabs::

	.. code-tab:: python

		def SetPatternPieceName(_patternIndex : int, _patternName : str) -> None
		"""
		@brief Set Pattern name using the pattern index
		@param		_patternIndex: the pattern index to set
		_patternName: the value to set as pattern name
		"""

	.. code-tab:: c++

		 SetPatternPieceName(int _patternIndex)
		/// @brief Set Pattern name using the pattern index
		/// @param		_patternIndex: the pattern index to set
		_patternName: the value to set as pattern name


.. tabs::

	.. code-tab:: python

		def GetPatternPieceFabricIndex(_patternPieceIndex : int) -> int
		"""
		@brief Get Pattern fabric index using the pattern index
		@param		_patternIndex: the pattern index to get
		"""

	.. code-tab:: c++

		 GetPatternPieceFabricIndex(int _patternIndex)
		/// @brief Get Pattern fabric index using the pattern index
		/// @param		_patternIndex: the pattern index to get


.. tabs::

	.. code-tab:: python

		def SetPatternPieceFabricIndex(_patternPieceIndex : int, _fabricIndex : int) -> None
		"""
		@brief Set Pattern fabric index using the pattern index
		@param		_patternIndex: the pattern index to set
		_fabricIndex: the value to set as gabric index
		"""

	.. code-tab:: c++

		 SetPatternPieceFabricIndex(int _patternPieceIndex, int _fabricIndex)
		/// @brief Set Pattern fabric index using the pattern index
		/// @param		_patternIndex: the pattern index to set
		_fabricIndex: the value to set as gabric index


.. tabs::

	.. code-tab:: python

		def GetPatternPieceGrainDirection(_patternPieceIndex : int) -> float
		"""
		@brief Get Pattern Grain direction info using the pattern index
		@param		_patternIndex: the pattern index to get
		"""

	.. code-tab:: c++

		 GetPatternPieceGrainDirection(int _patternPieceIndex)
		/// @brief Get Pattern Grain direction info using the pattern index
		/// @param		_patternIndex: the pattern index to get


.. tabs::

	.. code-tab:: python

		def SetPatternPieceGrainDirection(_patternPieceIndex : int, _degree : float) -> None
		"""
		@brief Set Pattern grain direction value using the pattern index
		@param		_patternIndex: the pattern index to set
		_degree: the value to set as grain direction
		"""

	.. code-tab:: c++

		 SetPatternPieceGrainDirection(int _patternPieceIndex, float _degree)
		/// @brief Set Pattern grain direction value using the pattern index
		/// @param		_patternIndex: the pattern index to set
		_degree: the value to set as grain direction


.. tabs::

	.. code-tab:: python

		def IsPatternPieceGrainLinkAllColorways(_patternPieceIndex : int) -> bool
		"""
		@brief Check if Pattern link all color ways value using the pattern index
		@param		_patternIndex: the pattern index to set
		"""

	.. code-tab:: c++

		 IsPatternPieceGrainLinkAllColorways(int patternPieceIndex)
		/// @brief Check if Pattern link all color ways value using the pattern index
		/// @param		_patternIndex: the pattern index to set


.. tabs::

	.. code-tab:: python

		def SetPatternPieceGrainLinkAllColorways(_patternPieceIndex : int, _isOn : bool) -> None
		"""
		@brief Set Pattern link all color ways value using the pattern index
		@param		_patternIndex: the pattern index to set
		_isOn: the value to set as link all color ways
		"""

	.. code-tab:: c++

		  SetPatternPieceGrainLinkAllColorways(int _patternPieceIndex, bool _isOn)
		/// @brief Set Pattern link all color ways value using the pattern index
		/// @param		_patternIndex: the pattern index to set
		_isOn: the value to set as link all color ways


.. tabs::

	.. code-tab:: python

		def GetPatternPieceCategory(_patternPieceIndex : int) -> int
		"""
		@brief Get Pattern category number using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		"""

	.. code-tab:: c++

		 GetPatternPieceCategory(int _patternPieceIndex)
		/// @brief Get Pattern category number using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get


.. tabs::

	.. code-tab:: python

		def SetPatternPieceCategory(_patternPieceIndex : int, _category : int) -> None
		"""
		@brief Set Pattern category number using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		_category: the value to set category value
		"""

	.. code-tab:: c++

		 SetPatternPieceCategory(int _patternPieceIndex, int _category)
		/// @brief Set Pattern category number using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get
		_category: the value to set category value


.. tabs::

	.. code-tab:: python

		def GetPatternPieceClassification(_patternPieceIndex : int) -> str
		"""
		@brief Get Pattern classification using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		"""

	.. code-tab:: c++

		 GetPatternPieceClassification(int _patternPieceIndex)
		/// @brief Get Pattern classification using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get


.. tabs::

	.. code-tab:: python

		def SetPatternPieceClassification(_patternPieceIndex : int, _classification : str) -> None
		"""
		@brief Set Pattern classification using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		_classification: the value to set classification
		"""

	.. code-tab:: c++

		 SetPatternPieceClassification(int _patternPieceIndex, string _classificatio)
		/// @brief Set Pattern classification using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get
		_classification: the value to set classification


.. tabs::

	.. code-tab:: python

		def IsPatternPieceSolidify(_patternPieceIndex : int) -> bool
		"""
		@brief Check if Pattern Solidify using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		"""

	.. code-tab:: c++

		 IsPatternPieceSolidify(int _patternPieceIndex)
		/// @brief Check if Pattern Solidify using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get


.. tabs::

	.. code-tab:: python

		def SetPatternPieceSolidify(_patternPieceIndex : int, _isOn : bool) -> None
		"""
		@brief Set Pattern Solidify using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		_isOn: the value to set Solidify On/Off
		"""

	.. code-tab:: c++

		 SetPatternPieceSolidify(int _patternPieceIndex, bool _isOn);
		/// @brief Set Pattern Solidify using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get
		_isOn: the value to set Solidify On/Off


.. tabs::

	.. code-tab:: python

		def GetPatternPieceSolidifyStrengthen(_patternPieceIndex : int) -> float
		"""
		@brief Get Pattern Solidify using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		"""

	.. code-tab:: c++

		 GetPatternPieceSolidifyStrengthen(int _patternPieceIndex)
		/// @brief Get Pattern Solidify using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get


.. tabs::

	.. code-tab:: python

		def SetPatternPieceSolidifyStrengthen(_patternPieceIndex : int, _strengthen : float) -> None
		"""
		@brief Get Pattern Solidify using the pattern index
		@param		_patternPieceIndex: the pattern index to get
		_strengthen : strengthen value to set
		"""

	.. code-tab:: c++

		  SetPatternPieceSolidifyStrengthen(int _patternPieceIndex, float _strengthen);
		/// @brief Get Pattern Solidify using the pattern index
		/// @param		_patternPieceIndex: the pattern index to get
		_strengthen : strengthen value to set


.. tabs::

	.. code-tab:: python

		def ConvertToBaseLine(_patternIndex : int, _childrenIndex : int) -> None
		"""
		@brief Convert To BaseLine using the pattern index and children index
		@param		patternIndex: the pattern index for convert pattern
		children Index: the children index for convert children
		"""

	.. code-tab:: c++

		 ConvertToBaseLine(int _patternIndex, int _childrenIndex)
		/// @brief Convert To BaseLine using the pattern index and children index
		/// @param		patternIndex: the pattern index for convert pattern
		children Index: the children index for convert children


.. tabs::

	.. code-tab:: python

		def ConvertToInternalLine(_patternIndex : int, _childrenIndex : int) -> None
		"""
		@brief Convert To InternalLine using the pattern index and children index
		@param		patternIndex: the pattern index for convert pattern
		children Index: the children index for convert children
		"""

	.. code-tab:: c++

		 ConvertToInternalLine(int _patternPieceIndex)
		/// @brief Convert To InternalLine using the pattern index and children index
		/// @param		patternIndex: the pattern index for convert pattern
		children Index: the children index for convert children


.. tabs::

	.. code-tab:: python

		def DistribueInternalLinesbetweenSegments(_patternIndex : int, _lineIndexs : list[int], _number : int, _bStraightLine : bool, _bPerpendicularDirection : bool, _bGraduateSegmentLengths : bool) -> None
		"""
		@brief Distribue Internal Lines betweenSegments using the pattern index and line indexs and option
		@param		patternIndex: the pattern index for taget pattern
		lineIndexs: the line indexs for taget lines
		number: the number of internal shapes to be created
		straightLine: create an internal figure with straight lines
		perpendicularDirection: target line reversal
		GraduateSegmentLengths: extend to the outline of the pattern
		"""

	.. code-tab:: c++

		 DistribueInternalLinesbetweenSegments(int _patternIndex, vector<int> _indexs, int _number, bool _bStraightLine, bool _bPerpendicularDirection, bool _bGraduateSegmentLengths)
		/// @brief Distribue Internal Lines betweenSegments using the pattern index and line indexs and option
		/// @param		patternIndex: the pattern index for taget pattern
		lineIndexs: the line indexs for taget lines
		number: the number of internal shapes to be created
		straightLine: create an internal figure with straight lines
		perpendicularDirection: target line reversal
		GraduateSegmentLengths: extend to the outline of the pattern


.. tabs::

	.. code-tab:: python

		def GetPatternPiecePos(_patternIndex : int) -> list[float]
		"""
		@brief		Get Pattern piece's world position
		@param		_patternIndex: The pattern index to get the world position
		@return		The world position of pattern is given in order (x, y). If an error occurs, return empty vector
		"""

	.. code-tab:: c++

				GetPatternPiecePos(int _patternIndex)
		/// @brief		Get Pattern piece's world position
		/// @param		_patternIndex: The pattern index to get the world position
		/// @return		The world position of pattern is given in order (x, y). If an error occurs, return empty vector


.. tabs::

	.. code-tab:: python

		def SetPatternPiecePos(_patternIndex : int, _x : float, _y : float) -> None
		"""
		@brief		Set Pattern piece's world position to (_x, _y)
		@param		_patternIndex: The pattern index to move
		_x: The X position of pattern want to move
		_y: The Y position of pattern want to move
		"""

	.. code-tab:: c++

				SetPatternPiecePos(int _patternIndex)
		/// @brief		Set Pattern piece's world position to (_x, _y)
		/// @param		_patternIndex: The pattern index to move
		_x: The X position of pattern want to move
		_y: The Y position of pattern want to move


.. tabs::

	.. code-tab:: python

		def SetPatternPieceMove(_patternIndex : int, _offsetX : float, _offsetY : float) -> None
		"""
		@brief		Set Pattern piece's world position to (CurrentPosition.x + _offsetX, CurrentPosition.y + _offsetY)
		@param		_patternIndex: The pattern index to move
		_x: The X position offset of pattern want to move
		_y: The Y position offset of pattern want to move
		"""

	.. code-tab:: c++

				SetPatternPieceMove(int _patternIndex)
		/// @brief		Set Pattern piece's world position to (CurrentPosition.x + _offsetX, CurrentPosition.y + _offsetY)
		/// @param		_patternIndex: The pattern index to move
		_x: The X position offset of pattern want to move
		_y: The Y position offset of pattern want to move


.. tabs::

	.. code-tab:: python

		def SetPatternPieceElastic(_patternIndex : int, _lineIndex : int, _bElastic : bool) -> None
		"""
		@brief		Set Pattern piece's elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply elastic
		_lineIndex: The line index to apply elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bElastic: Whether to apply elastic
		"""

	.. code-tab:: c++

				SetPatternPieceElastic(int _patternIndex, int _lineIndex, bool _bElastic)
		/// @brief		Set Pattern piece's elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply elastic
		_lineIndex: The line index to apply elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bElastic: Whether to apply elastic


.. tabs::

	.. code-tab:: python

		def SetPatternPieceElasticStrength(_patternIndex : int, _lineIndex : int, _strength : float) -> None
		"""
		@brief		Set Pattern piece's elastic strength. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply elastic strength
		_lineIndex: The line index to apply elastic strength. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_strength: The strength of elastic
		"""

	.. code-tab:: c++

				SetPatternPieceElasticStrength(int _patternIndex, int _lineIndex, float _strength)
		/// @brief		Set Pattern piece's elastic strength. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply elastic strength
		_lineIndex: The line index to apply elastic strength. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_strength: The strength of elastic


.. tabs::

	.. code-tab:: python

		def SetPatternPieceElasticStrengthRatio(_patternIndex : int, _lineIndex : int, _ratio : int) -> None
		"""
		@brief		Set Pattern piece's elastic strength ratio. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply elastic strength ratio
		_lineIndex: The line index to apply elastic strength ratio. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_ratio: The strength ratio of elastic
		"""

	.. code-tab:: c++

				SetPatternPieceElasticStrengthRatio(int _patternIndex, int _lineIndex, int _ratio)
		/// @brief		Set Pattern piece's elastic strength ratio. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply elastic strength ratio
		_lineIndex: The line index to apply elastic strength ratio. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_ratio: The strength ratio of elastic


.. tabs::

	.. code-tab:: python

		def SetPatternPieceElasticSegmentLength(_patternIndex : int, _lineIndex : int, _segmentLength : float) -> None
		"""
		@brief		Set Pattern piece's segment length of elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply segment length
		_lineIndex: The line index to apply segment length. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_segmentLength: The segment length of elastic 
		"""

	.. code-tab:: c++

				SetPatternPieceElasticSegmentLength(int _patternIndex, int _lineIndex, float _segmentLength)
		/// @brief		Set Pattern piece's segment length of elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply segment length
		_lineIndex: The line index to apply segment length. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_segmentLength: The segment length of elastic 


.. tabs::

	.. code-tab:: python

		def SetPatternPieceElasticTotalLength(_patternIndex : int, _lineIndex : int, _totalLength : float) -> None
		"""
		@brief		Set Pattern piece's total length of elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply total length 
		_lineIndex: The line index to apply total length. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_totalLength: The total length of elasitc
		"""

	.. code-tab:: c++

				SetPatternPieceElasticTotalLength(int _patternIndex, int _lineIndex, float _totalLength)
		/// @brief		Set Pattern piece's total length of elastic. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply total length 
		_lineIndex: The line index to apply total length. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_totalLength: The total length of elasitc


.. tabs::

	.. code-tab:: python

		def SetPatternPieceShirring(_patternIndex : int, _lineIndex : int, _bShirring : bool) -> None
		"""
		@brief		Set Pattern piece's shirring. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply shirring 
		_lineIndex: The line index to apply shirring. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bShirring: Whether to apply shirring
		"""

	.. code-tab:: c++

				SetPatternPieceShirring(int _patternIndex, int _lineIndex, bool _bShirring)
		/// @brief		Set Pattern piece's shirring. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply shirring 
		_lineIndex: The line index to apply shirring. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bShirring: Whether to apply shirring


.. tabs::

	.. code-tab:: python

		def SetPatternPieceShirringInterval(_patternIndex : int, _lineIndex : int, _interval : float) -> None
		"""
		@brief		Set Pattern piece's shirring interval. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply shirring interval
		_lineIndex: The line index to apply shirring interval. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_interval: The interval of shirring
		"""

	.. code-tab:: c++

				SetPatternPieceShirringInterval(int _patternIndex, int _lineIndex, float _interval)
		/// @brief		Set Pattern piece's shirring interval. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply shirring interval
		_lineIndex: The line index to apply shirring interval. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_interval: The interval of shirring


.. tabs::

	.. code-tab:: python

		def SetPatternPieceShirringHeight(_patternIndex : int, _lineIndex : int, _height : float) -> None
		"""
		@brief		Set Pattern piece's shirring height. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply shirring height
		_lineIndex: The line index to apply shirring height. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_height: The height of shirring
		"""

	.. code-tab:: c++

				SetPatternPieceShirringHeight(int _patternIndex, int _lineIndex, float _height)
		/// @brief		Set Pattern piece's shirring height. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply shirring height
		_lineIndex: The line index to apply shirring height. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_height: The height of shirring


.. tabs::

	.. code-tab:: python

		def SetPatternPieceShirringExtend(_patternIndex : int, _lineIndex : int, _bExtend : bool) -> None
		"""
		@brief		Set Pattern piece's shirring extend. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply shirring extend
		_lineIndex: The line index to apply shirring extend. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bExtend: Whether to apply shirring extend
		"""

	.. code-tab:: c++

				SetPatternPieceShirringExtend(int _patternIndex, int _lineIndex, bool _bExtend)
		/// @brief		Set Pattern piece's shirring extend. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply shirring extend
		_lineIndex: The line index to apply shirring extend. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bExtend: Whether to apply shirring extend


.. tabs::

	.. code-tab:: python

		def SetPatternPieceSeamtaping(_patternIndex : int, _lineIndex : int, _bSeamtaping : bool) -> None
		"""
		@brief		Set Pattern piece's seamtaping. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply seamtaping
		_lineIndex: The line index to apply seamtaping. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bSeamtaping: Whether to apply seamtaping
		"""

	.. code-tab:: c++

				SetPatternPieceSeamtaping(int _patternIndex, int _lineIndex, bool _bSeamtaping)
		/// @brief		Set Pattern piece's seamtaping. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply seamtaping
		_lineIndex: The line index to apply seamtaping. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_bSeamtaping: Whether to apply seamtaping


.. tabs::

	.. code-tab:: python

		def SetPatternPieceSametapingWidth(_patternIndex : int, _lineIndex : int, _width : float) -> None
		"""
		@brief		Set Pattern piece's seamtaping width. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		@param		_patternIndex: The pattern index to apply seamtaping width
		_lineIndex: The line index to apply seamtaping width. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_width: The width of seamtaping width
		"""

	.. code-tab:: c++

				SetPatternPieceSametapingWidth(int _patternIndex, int _lineIndex, int _width)
		/// @brief		Set Pattern piece's seamtaping width. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		/// @param		_patternIndex: The pattern index to apply seamtaping width
		_lineIndex: The line index to apply seamtaping width. When _lineIndex == -1, apply to all line, 0 <= _lineIndex, apply to line
		_width: The width of seamtaping width


.. tabs::

	.. code-tab:: python

		def CreatePatternWithPoints(_points : list[tuple[float, float, int]]) -> int
		"""
		@brief		Create a pattern using a set of vertices.
		@param		_points: set of vertices.
		tuple --> postion X, postion Y, VertexType  
		VertexType : 0, 2, 3 
		0 : Straight Point
		2 : Spline Curve Point
		3 : Bezier Curve Point
		"""

	.. code-tab:: c++

				CreatePatternWithPoints
		/// @brief		Create a pattern using a set of vertices.
		/// @param		_points: set of vertices.
		tuple --> postion X, postion Y, VertexType  
		VertexType : 0, 2, 3 
		0 : Straight Point
		2 : Spline Curve Point
		3 : Bezier Curve Point


.. tabs::

	.. code-tab:: python

		def CreateInternalShapeWithPoints(_patternIndex : int, _points : list[tuple[float, float, int]], _isClosed : bool) -> int
		"""
		@brief		Create a pattern's internal shape using a set of vertices.
		@param		_patternIndex: Parent Pattern Index
		tuple --> postion X, postion Y, VertexType  
		VertexType : 0, 2, 3 
		0 : Straight Point
		2 : Spline Curve Point
		3 : Bezier Curve Point
		_isClosed: If true, connect the last vertex to the first vertex.
		@return		PatternIndex
		"""

	.. code-tab:: c++

				CreateInternalShapeWithPoints
		/// @brief		Create a pattern's internal shape using a set of vertices.
		/// @param		_patternIndex: Parent Pattern Index
		tuple --> postion X, postion Y, VertexType  
		VertexType : 0, 2, 3 
		0 : Straight Point
		2 : Spline Curve Point
		3 : Bezier Curve Point
		_isClosed: If true, connect the last vertex to the first vertex.
		/// @return		PatternIndex


.. tabs::

	.. code-tab:: python

		def CreateBaseShapeWithPoints(_patternIndex : int, _points : list[tuple[float, float, int]], _isClosed : bool) -> int
		"""
		@brief		Create a pattern's base shape using a set of vertices.
		@param		_patternIndex: Parent Pattern Index
		_points: set of vertices.
		tuple --> postion X, postion Y, VertexType  
		VertexType : 0, 2, 3 
		0 : Straight Point
		2 : Spline Curve Point
		3 : Bezier Curve Point
		_isClosed: If true, connect the last vertex to the first vertex.
		@return		InternalShapeIndex
		"""

	.. code-tab:: c++

				CreateBaseShapeWithPoints
		/// @brief		Create a pattern's base shape using a set of vertices.
		/// @param		_patternIndex: Parent Pattern Index
		_points: set of vertices.
		tuple --> postion X, postion Y, VertexType  
		VertexType : 0, 2, 3 
		0 : Straight Point
		2 : Spline Curve Point
		3 : Bezier Curve Point
		_isClosed: If true, connect the last vertex to the first vertex.
		/// @return		InternalShapeIndex


.. tabs::

	.. code-tab:: python

		def SetPatternLayer(_patternIndex : int, _layer : int) -> None
		"""
		@brief Set Pattern Layer using pattern index, layer
		@param		patternIndex: the pattern index to set the pattern layer,
		layer: the layer value to determine pattern layer
		@return		BaseShapeIndex
		"""

	.. code-tab:: c++

		 SetPatternLayer(int _patternIndex, int _layer)
		/// @brief Set Pattern Layer using pattern index, layer
		/// @param		patternIndex: the pattern index to set the pattern layer,
		layer: the layer value to determine pattern layer
		/// @return		BaseShapeIndex


.. tabs::

	.. code-tab:: python

		def GetPatternLayer(_patternIndex : int) -> int
		"""
		@brief Get Pattern Layer using pattern index
		@param		patternIndex: the pattern index to get the pattern layer,
		"""

	.. code-tab:: c++

		 GetPatternLayer(int _patternIndex)
		/// @brief Get Pattern Layer using pattern index
		/// @param		patternIndex: the pattern index to get the pattern layer,


.. tabs::

	.. code-tab:: python

		def SetPatternFreeze(_patternIndex : int, _bFreeze : bool) -> None
		"""
		@brief Set Pattern Freeze using pattern index, freeze state
		@param		patternIndex: the pattern index to set the pattern freeze state,
		freeze: the freeze state to determine pattern freeze
		"""

	.. code-tab:: c++

		 SetPatternFreeze(int _patternIndex, int _bFreeze)
		/// @brief Set Pattern Freeze using pattern index, freeze state
		/// @param		patternIndex: the pattern index to set the pattern freeze state,
		freeze: the freeze state to determine pattern freeze


.. tabs::

	.. code-tab:: python

		def SetPatternStrengthen(_patternIndex : int, _bStrengthen : bool) -> None
		"""
		@brief Set Pattern Strengthen using pattern index, Active state
		@param		patternIndex: the pattern index to set the pattern Strengthen,
		Strengthen: the Active state to determine pattern Strengthen
		"""

	.. code-tab:: c++

		 SetPatternStrengthen(int _patternIndex, bool _bActive)
		/// @brief Set Pattern Strengthen using pattern index, Active state
		/// @param		patternIndex: the pattern index to set the pattern Strengthen,
		Strengthen: the Active state to determine pattern Strengthen


.. tabs::

	.. code-tab:: python

		def SetPatternLock(_patternIndex : int, _bLock : bool) -> None
		"""
		@brief Set Pattern Lock using pattern index, Lock state
		@param		patternIndex: the pattern index to set the pattern Lock,
		Lock: the Lock state to determine pattern Lock
		"""

	.. code-tab:: c++

		 SetPatternLock(int _patternIndex, bool _bLock)
		/// @brief Set Pattern Lock using pattern index, Lock state
		/// @param		patternIndex: the pattern index to set the pattern Lock,
		Lock: the Lock state to determine pattern Lock


.. tabs::

	.. code-tab:: python

		def SetPatternHide3D(_patternIndex : int, _bHide : bool) -> None
		"""
		@brief Set Pattern Hide 3d using pattern index, Hide state
		@param		patternIndex: the pattern index to set the pattern Hide 3d,
		Hide: the Hide state to determine pattern Lock
		"""

	.. code-tab:: c++

		 SetPatternHide3D(int _patternIndex, bool _bHide)
		/// @brief Set Pattern Hide 3d using pattern index, Hide state
		/// @param		patternIndex: the pattern index to set the pattern Hide 3d,
		Hide: the Hide state to determine pattern Lock


.. tabs::

	.. code-tab:: python

		def AddSegmentTopstitch(_patternIndex : int, _lineIndex : int, _topStitchStyleIndex : int) -> bool
		"""
		@brief Add Segment Topstitch to  Pattern using the pattern index, lineindex , topStitchStyleIndex
		@param		patternIndex: the pattern index for Add Segment Topstitch to pattern
		@param		lineIndex: the line index for topstitch added line
		@param		topStitchStyleIndex: the topstitch style index for topstitch
		"""

	.. code-tab:: c++

		 AddSegmentTopstitch(int _patternIndex, int _lineIndex)
		/// @brief Add Segment Topstitch to  Pattern using the pattern index, lineindex , topStitchStyleIndex
		/// @param		patternIndex: the pattern index for Add Segment Topstitch to pattern
		/// @param		lineIndex: the line index for topstitch added line
		/// @param		topStitchStyleIndex: the topstitch style index for topstitch


.. tabs::

	.. code-tab:: python

		def GetTopstitchStyleList() -> list[map[str, str]]
		"""
		@brief Get all GetTopstitchStyleList
		@param		none
		@return Output vector map string TopstitchStyleList information (Topstitch style Name, index); If an error occurs, return vector infoMap
		"""

	.. code-tab:: c++

		 GetTopstitchStyleList()
		/// @brief Get all GetTopstitchStyleList
		/// @param		none
		/// @return Output vector map string TopstitchStyleList information (Topstitch style Name, index); If an error occurs, return vector infoMap


.. tabs::

	.. code-tab:: python

		def GetPatternAssignedTopstitchCount(_patternIndex : int) -> int
		"""
		@brief Get Pattern Assigned Topstitch Count
		@param		none
		@return Output int Count Pattern Assigned Topstitch Count; If an error occurs, return -1
		"""

	.. code-tab:: c++

		 GetPatternAssignedTopstitchCount()
		/// @brief Get Pattern Assigned Topstitch Count
		/// @param		none
		/// @return Output int Count Pattern Assigned Topstitch Count; If an error occurs, return -1


.. tabs::

	.. code-tab:: python

		def GetPatternAssignedTopstitchStyle(_patternIndex : int) -> list[map[str, str]]
		"""
		@brief Get Pattern Assigned Topstitch style
		@param		none
		@return Output vector map string Pattern Assigned Topstitch Style (Topstitch style Name, Count); If an error occurs, return vector vMap
		"""

	.. code-tab:: c++

		 GetPatternAssignedTopstitchStyle(int _patternIndex)
		/// @brief Get Pattern Assigned Topstitch style
		/// @param		none
		/// @return Output vector map string Pattern Assigned Topstitch Style (Topstitch style Name, Count); If an error occurs, return vector vMap


.. tabs::

	.. code-tab:: python

		def GetPatternAssignedTopstitch(_patternIndex : int) -> list[map[str, str]]
		"""
		@brief Get Pattern Assigned Topstitch
		@param		patternIndex: the pattern index for Get Topstitch
		@return Output vector map string Pattern Assigned Topstitch (Topstitch Name, index); If an error occurs, return vector vMap
		"""

	.. code-tab:: c++

		 GetPatternAssignedTopstitch(int _patternIndex)
		/// @brief Get Pattern Assigned Topstitch
		/// @param		patternIndex: the pattern index for Get Topstitch
		/// @return Output vector map string Pattern Assigned Topstitch (Topstitch Name, index); If an error occurs, return vector vMap


.. tabs::

	.. code-tab:: python

		def GetPatternAssignedTopstitchStyleIndex(_patternIndex : int, _segmentStitchIndex : int) -> int
		"""
		@brief Get Pattern Assigned Topstitch Style
		@param		patternIndex: the pattern index for Get Topstitch Style
		@return Output int Pattern Assigned Topstitch Syle index; If an error occurs, return 0
		"""

	.. code-tab:: c++

		 GetPatternAssignedTopstitchStyleIndex(int _patternIndex, int _segmentStitchIndex)
		/// @brief Get Pattern Assigned Topstitch Style
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @return Output int Pattern Assigned Topstitch Syle index; If an error occurs, return 0


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchStyle(_patternIndex : int, _segmentStitchIndex : int, _stitchStyleIndex : int) -> None
		"""
		@brief Set Pattern Assigned Topstitch Style
		@param		patternIndex: the pattern index for Set Topstitch Style
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchStyle(int _patternIndex, int _segmentStitchIndex, int _stitchStyleIndex)
		/// @brief Set Pattern Assigned Topstitch Style
		/// @param		patternIndex: the pattern index for Set Topstitch Style


.. tabs::

	.. code-tab:: python

		def IsPatternAssignedTopstitchExtendStart(_patternIndex : int, _segmentStitchIndex : int) -> bool
		"""
		@brief  Get Pattern Assigned Topstitch Property Value ExtendStart
		@param		patternIndex: the pattern index for Get Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Get Topstitch property ExtendStart
		"""

	.. code-tab:: c++

		 IsPatternAssignedTopstitchExtendStart(int _patternIndex, int _segmentStitchIndex)
		/// @brief  Get Pattern Assigned Topstitch Property Value ExtendStart
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Get Topstitch property ExtendStart


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchExtendStart(_patternIndex : int, _segmentStitchIndex : int, _bStart : bool) -> None
		"""
		@brief Set Pattern Assigned Topstitch Property Value ExtendStart
		@param		patternIndex: the pattern index for Set Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Set Topstitch property ExtendStart
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchExtendStart(int _patternIndex, int _segmentStitchIndex, bool _bStart)
		/// @brief Set Pattern Assigned Topstitch Property Value ExtendStart
		/// @param		patternIndex: the pattern index for Set Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Set Topstitch property ExtendStart


.. tabs::

	.. code-tab:: python

		def IsPatternAssignedTopstitchExtendEnd(_patternIndex : int, _segmentStitchIndex : int) -> bool
		"""
		@brief  Get Pattern Assigned Topstitch Property Value ExtendEnd
		@param		patternIndex: the pattern index for Get Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Get Topstitch property ExtendEnd
		"""

	.. code-tab:: c++

		 IsPatternAssignedTopstitchExtendEnd(int _patternIndex, int _segmentStitchIndex)
		/// @brief  Get Pattern Assigned Topstitch Property Value ExtendEnd
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Get Topstitch property ExtendEnd


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchExtendEnd(_patternIndex : int, _segmentStitchIndex : int, _bEnd : bool) -> None
		"""
		@brief Set Pattern Assigned Topstitch Property Value ExtendEnd
		@param		patternIndex: the pattern index for Set Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Set Topstitch property ExtendEnd
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchExtendEnd(int _patternIndex, int _segmentStitchIndex, bool _bEnd)
		/// @brief Set Pattern Assigned Topstitch Property Value ExtendEnd
		/// @param		patternIndex: the pattern index for Set Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Set Topstitch property ExtendEnd


.. tabs::

	.. code-tab:: python

		def IsPatternAssignedTopstitchCurved(_patternIndex : int, _segmentStitchIndex : int) -> bool
		"""
		@brief  Get Pattern Assigned Topstitch Property Value Curved
		@param		patternIndex: the pattern index for Get Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Get Topstitch property Curved
		"""

	.. code-tab:: c++

		 IsPatternAssignedTopstitchCurved(int _patternIndex, int _segmentStitchIndex)
		/// @brief  Get Pattern Assigned Topstitch Property Value Curved
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Get Topstitch property Curved


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchCurved(_patternIndex : int, _segmentStitchIndex : int, _bCurved : bool) -> None
		"""
		@brief Set Pattern Assigned Topstitch Property Value Curved
		@param		patternIndex: the pattern index for Set Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Set Topstitch property Curved
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchCurved(int _patternIndex, int _segmentStitchIndex, bool _bCurved)
		/// @brief Set Pattern Assigned Topstitch Property Value Curved
		/// @param		patternIndex: the pattern index for Set Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Set Topstitch property Curved


.. tabs::

	.. code-tab:: python

		def GetPatternAssignedTopstitchCurvedLength(_patternIndex : int, _segmentStitchIndex : int) -> int
		"""
		@brief  Get Pattern Assigned Topstitch Property Value CurvedLength
		@param		patternIndex: the pattern index for Get Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Get Topstitch property CurvedLength
		"""

	.. code-tab:: c++

		 GetPatternAssignedTopstitchCurvedLength(int _patternIndex, int _segmentStitchIndex)
		/// @brief  Get Pattern Assigned Topstitch Property Value CurvedLength
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Get Topstitch property CurvedLength


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchCurvedLength(_patternIndex : int, _segmentStitchIndex : int, _length : int) -> None
		"""
		@brief Set Pattern Assigned Topstitch Property Value CurvedLength
		@param		patternIndex: the pattern index for Set Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Set Topstitch property CurvedLength
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchCurvedLength(int _patternIndex, int _segmentStitchIndex, int _length)
		/// @brief Set Pattern Assigned Topstitch Property Value CurvedLength
		/// @param		patternIndex: the pattern index for Set Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Set Topstitch property CurvedLength


.. tabs::

	.. code-tab:: python

		def IsPatternAssignedTopstitchCurvedRightAngled(_patternIndex : int, _segmentStitchIndex : int) -> bool
		"""
		@brief  Get Pattern Assigned Topstitch Property Value CurvedRightAngled
		@param		patternIndex: the pattern index for Get Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Get Topstitch property CurvedRightAngled
		"""

	.. code-tab:: c++

		 IsPatternAssignedTopstitchCurvedRightAngled(int _patternIndex, int _segmentStitchIndex)
		/// @brief  Get Pattern Assigned Topstitch Property Value CurvedRightAngled
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Get Topstitch property CurvedRightAngled


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchCurvedRightAngled(_patternIndex : int, _segmentStitchIndex : int, _bRightAngled : bool) -> None
		"""
		@brief Set Pattern Assigned Topstitch Property Value CurvedRightAngled
		@param		patternIndex: the pattern index for Set Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Set Topstitch property CurvedRightAngled
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchCurvedRightAngled(int _patternIndex, int _segmentStitchIndex, bool _bRightAngled)
		/// @brief Set Pattern Assigned Topstitch Property Value CurvedRightAngled
		/// @param		patternIndex: the pattern index for Set Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Set Topstitch property CurvedRightAngled


.. tabs::

	.. code-tab:: python

		def GetPatternAssignedTopstitchZOffset(_patternIndex : int, _segmentStitchIndex : int) -> float
		"""
		@brief  Get Pattern Assigned Topstitch Property Value ZOffset
		@param		patternIndex: the pattern index for Get Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Get Topstitch property ZOffset
		"""

	.. code-tab:: c++

		 GetPatternAssignedTopstitchZOffset(int _patternIndex, int _segmentStitchIndex)
		/// @brief  Get Pattern Assigned Topstitch Property Value ZOffset
		/// @param		patternIndex: the pattern index for Get Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Get Topstitch property ZOffset


.. tabs::

	.. code-tab:: python

		def SetPatternAssignedTopstitchZOffset(_patternIndex : int, _segmentStitchIndex : int, _zOffset : float) -> None
		"""
		@brief Set Pattern Assigned Topstitch Property Value ZOffset
		@param		patternIndex: the pattern index for Set Topstitch Style
		@param		segmentStitchIndex: the segmentStitch index for Set Topstitch property ZOffset
		"""

	.. code-tab:: c++

		 SetPatternAssignedTopstitchZOffset(int _patternIndex, int _segmentStitchIndex, float _zOffset)
		/// @brief Set Pattern Assigned Topstitch Property Value ZOffset
		/// @param		patternIndex: the pattern index for Set Topstitch Style
		/// @param		segmentStitchIndex: the segmentStitch index for Set Topstitch property ZOffset


.. tabs::

	.. code-tab:: python

		def ImportTopStitchStyle(_filePath : str) -> bool
		"""
		@brief Import TopStitch Style from file path
		@param		filePath: the .sst file path for Import TopStitch Style
		"""

	.. code-tab:: c++

		 ImportTopStitchStyle(const string& _filePath)
		/// @brief Import TopStitch Style from file path
		/// @param		filePath: the .sst file path for Import TopStitch Style


.. tabs::

	.. code-tab:: python

		def GetNestingPatternPieceGrainDirection(patternPieceIndex : int) -> int
		"""
		@brief Returns the index of the graindirection option widget for the pattern.
		@param		patternPieceIndex: PatternIndex
		"""

	.. code-tab:: c++

		 GetNestingPatternPieceGrainDirection(int patternPieceIndex)
		/// @brief Returns the index of the graindirection option widget for the pattern.
		/// @param		patternPieceIndex: PatternIndex


.. tabs::

	.. code-tab:: python

		def SetNestingPatternPieceGrainDirection(patternPieceIndex : int, menuIndex : int) -> None
		"""
		@brief Set the index of the graindirection option widget for the pattern.
		@param		patternPieceIndex: PatternIndex
		@param		menuIndex: graindirection option widget index, 0 : 1-way, 1 : 2-way , 2 : 4-way
		"""

	.. code-tab:: c++

		 SetNestingPatternPieceGrainDirection(int patternPieceIndex, int menuIndex)
		/// @brief Set the index of the graindirection option widget for the pattern.
		/// @param		patternPieceIndex: PatternIndex
		/// @param		menuIndex: graindirection option widget index, 0 : 1-way, 1 : 2-way , 2 : 4-way


.. tabs::

	.. code-tab:: python

		def GetNestingFixedPatternPiecePos(patternPieceIndex : int) -> std::pair[int, int]
		"""
		@brief When the pattern is fixed in print layout mode, the coordinates of the fixed position are returned. If not, it returns {0, 0}.
		@param		patternPieceIndex: PatternIndex
		"""

	.. code-tab:: c++

		 GetNestingFixedPatternPiecePos(int patternPieceIndex)
		/// @brief When the pattern is fixed in print layout mode, the coordinates of the fixed position are returned. If not, it returns {0, 0}.
		/// @param		patternPieceIndex: PatternIndex


.. tabs::

	.. code-tab:: python

		def SetNestingFixedPatternPiecePos(patternPieceIndex : int, x : int, y : int) -> None
		"""
		@brief Fix the pattern in print layout mode.
		@param		patternPieceIndex: PatternIndex
		@param		x: fixed position x
		@param		y: fixed position y
		"""

	.. code-tab:: c++

		 SetNestingFixedPatternPiecePos(int patternPieceIndex, int x, int y)
		/// @brief Fix the pattern in print layout mode.
		/// @param		patternPieceIndex: PatternIndex
		/// @param		x: fixed position x
		/// @param		y: fixed position y


.. tabs::

	.. code-tab:: python

		def AddPatternAnnotation(patternIndex : int, posX : float, posY : float, annotation : str) -> None
		"""
		@brief Add Annotation in pattern
		@param		patternPieceIndex: PatternIndex
		@param		posX: annotation position x
		@param		posY: annotation position y
		"""

	.. code-tab:: c++

		 AddPatternAnnotation(int patternIndex, float posX, float posY, std::string annotation)
		/// @brief Add Annotation in pattern
		/// @param		patternPieceIndex: PatternIndex
		/// @param		posX: annotation position x
		/// @param		posY: annotation position y


.. tabs::

	.. code-tab:: python

		def EditPatternAnnotation(patternIndex : int, posX : float, posY : float, annotationIndex : int, annotation : str) -> None
		"""
		@brief Edit Annotation
		@param		patternPieceIndex: PatternIndex
		@param		posX: annotation position x
		@param		posY: annotation position y
		@param		annotationIndex: annotation Index
		"""

	.. code-tab:: c++

		 EditPatternAnnotation(int patternIndex, float posX, float posY, int annotationIndex, std::string annotation)
		/// @brief Edit Annotation
		/// @param		patternPieceIndex: PatternIndex
		/// @param		posX: annotation position x
		/// @param		posY: annotation position y
		/// @param		annotationIndex: annotation Index


.. tabs::

	.. code-tab:: python

		def GetPatternAnnotation(patternIndex : int) -> list[tuple[str, float, float]]
		"""
		@brief Returns all annotations the pattern has.
		@param		patternPieceIndex: PatternIndex
		"""

	.. code-tab:: c++

		 vector<string GetPatternAnnotation(int patternIndex)
		/// @brief Returns all annotations the pattern has.
		/// @param		patternPieceIndex: PatternIndex


.. tabs::

	.. code-tab:: python

		def GetLinkedPatternIndex(patternIndex : int) -> list[int]
		"""
		@brief Get the pattern index information connected to the pattern. 
		@param patternIndex: Tartget Pattern Index
		"""

	.. code-tab:: c++

		 std::vector<int> GetLinkedPatternIndex(int patternIndex)
		/// @brief Get the pattern index information connected to the pattern. 
		/// @param patternIndex: Tartget Pattern Index


.. tabs::

	.. code-tab:: python

		def GetTopstitchStyleModelType(_topStitchStyleIndex : int) -> int
		"""
		@brief Get topstitch style's model type (Type value: OBJ = 0, Texture = 1, Fail = -1)
		@param		_topStitchStyleIndex: the topstitch style index for topstitch
		"""

	.. code-tab:: c++

		 GetTopstitchStyleModelType(int _topStitchStyleIndex)
		/// @brief Get topstitch style's model type (Type value: OBJ = 0, Texture = 1, Fail = -1)
		/// @param		_topStitchStyleIndex: the topstitch style index for topstitch


.. tabs::

	.. code-tab:: python

		def SetTopstitchStyleModelType(_topStitchStyleIndex : int, _modelType : int) -> bool
		"""
		@brief Set topstitch style's model type. If it succeeds, return true
		@param		_topStitchStyleIndex: the topstitch style index for topstitch
		@param		_modelType:  the topstitch style model type (Type value: OBJ = 0, Texture = 1)
		"""

	.. code-tab:: c++

		 SetTopstitchStyleModelType(int _topStitchStyleIndex, int _modelType)
		/// @brief Set topstitch style's model type. If it succeeds, return true
		/// @param		_topStitchStyleIndex: the topstitch style index for topstitch
		/// @param		_modelType:  the topstitch style model type (Type value: OBJ = 0, Texture = 1)


.. tabs::

	.. code-tab:: python

		def ExportObjectBrowserMaterialsList() -> str
		"""
		@brief Get the material name used in the garment 
		@return json string for pattern input information
		"""

	.. code-tab:: c++

		 ExportObjectBrowserMaterialUsedList( )
		/// @brief Get the material name used in the garment 
		/// @return json string for pattern input information


.. tabs::

	.. code-tab:: python

		def GetPinList() -> list[str]
		"""
		@brief Get all pins from patterns as list
		@return list of pins with their uuid
		"""

	.. code-tab:: c++

		 GetPinList()
		/// @brief Get all pins from patterns as list
		/// @return list of pins with their uuid


.. tabs::

	.. code-tab:: python

		def RemovePinByIndex(_index : int) -> bool
		"""
		@brief Remove the index-wise selected pin 
		@param index of pin
		"""

	.. code-tab:: c++

		 RemovePinByIndex(int _index)
		/// @brief Remove the index-wise selected pin 
		/// @param index of pin


.. tabs::

	.. code-tab:: python

		def GetValidGradingSizeGroupInformation() -> list[str]
		"""
		@brief Gets the names of the grading size groups that are valid for the patterns currently loaded in the scene.
		@return names of the grading size groups
		"""

	.. code-tab:: c++

		 GetVaildGradingSizeGroupNameList()
		/// @brief Gets the names of the grading size groups that are valid for the patterns currently loaded in the scene.
		/// @return names of the grading size groups


.. tabs::

	.. code-tab:: python

		def GetValidGradingSizeGroupCount() -> int
		"""
		@brief Get the size of the grading size grouplist that is valid for the patterns currently loaded in the scene.
		@return size of the grading size groups
		"""

	.. code-tab:: c++

		 GetVaildGradingSizeGroupCount()
		/// @brief Get the size of the grading size grouplist that is valid for the patterns currently loaded in the scene.
		/// @return size of the grading size groups


.. tabs::

	.. code-tab:: python

		def GetGradingSizeGroupInformation() -> list[str]
		"""
		@brief Get the names of all existing grading size groups.
		@return names of the grading size groups
		"""

	.. code-tab:: c++

		 GetGradingSizeGroupNameList()
		/// @brief Get the names of all existing grading size groups.
		/// @return names of the grading size groups


.. tabs::

	.. code-tab:: python

		def GetGradingSizeGroupCount() -> int
		"""
		@brief Get the size of all existing grading size groups.
		@return size of the grading size groups
		"""

	.. code-tab:: c++

		 GetGradingSizeGroupCount()
		/// @brief Get the size of all existing grading size groups.
		/// @return size of the grading size groups


.. tabs::

	.. code-tab:: python

		def GetGradingSizeTotalCount() -> int
		"""
		@brief Get the number of sizes/gradings
		@return total count of sizes/gradings
		"""

	.. code-tab:: c++

		 GetGradingSizeTotalCount()
		/// @brief Get the number of sizes/gradings
		/// @return total count of sizes/gradings


.. tabs::

	.. code-tab:: python

		def GetCurrentGradingSizeIndex() -> int
		"""
		@brief Get the index of the current size/grading
		@return the current index of size/grading
		"""

	.. code-tab:: c++

		 GetCurrentGradingSizeIndex()
		/// @brief Get the index of the current size/grading
		/// @return the current index of size/grading


.. tabs::

	.. code-tab:: python

		def GetGradingSizeListFromRuleTable(_gradingSizeGroupName : str) -> list[str]
		"""
		@brief Get the list of name about the grading size from grading size group;
		@return the list of name of all sizes/gradings
		"""

	.. code-tab:: c++

		 GetGradingSizeListFromRuleTable()
		/// @brief Get the list of name about the grading size from grading size group;
		/// @return the list of name of all sizes/gradings


.. tabs::

	.. code-tab:: python

		def GetGradingSizeListFromRuleTable(_gradingSizeGroupIndex : int) -> list[str]
		"""
		"""

	.. code-tab:: c++

		


.. tabs::

	.. code-tab:: python

		def GetGradingSizeNameList() -> list[str]
		"""
		@brief Get the name of the current size/grading
		@return the list of name of all sizes/gradings
		"""

	.. code-tab:: c++

		 GetGradingSizeNameList()
		/// @brief Get the name of the current size/grading
		/// @return the list of name of all sizes/gradings


.. tabs::

	.. code-tab:: python

		def GetGradingSizeNameListW() -> list[str]
		"""
		@brief Get the index of the current size/grading
		@return the list of name of all sizes/gradings
		"""

	.. code-tab:: c++

		 GetSizeNameListW()
		/// @brief Get the index of the current size/grading
		/// @return the list of name of all sizes/gradings


.. tabs::

	.. code-tab:: python

		def ChangeGradingSizeInformation(_gradingSizeGroupName : str, _gradingSizeName : str) -> bool
		"""
		@brief Change Grading Size information
		@return Successful grading size change
		@param _gradingSizeGroupName: sizegroup name
		@param _gradingSizeName: grading size name 
		"""

	.. code-tab:: c++

		 GetGradingSizeInforamtionFromSizeGroup(const std::wstring& _sizeGroupName)
		/// @brief Change Grading Size information
		/// @return Successful grading size change
		/// @param _gradingSizeGroupName: sizegroup name
		/// @param _gradingSizeName: grading size name 


.. tabs::

	.. code-tab:: python

		def ChangeGradingSizeInformation(_gradingSizeGroupIndex : int, _gradingSizeIndex : int) -> bool
		"""
		@brief Change Grading Size information
		@return Successful grading size change
		@param _gradingSizeGroupIndex: sizegroup name
		@param _gradingSizeIndex: grading size name 
		"""

	.. code-tab:: c++

		 GetGradingSizeInforamtionFromSizeGroup(const std::wstring& _sizeGroupName)
		/// @brief Change Grading Size information
		/// @return Successful grading size change
		/// @param _gradingSizeGroupIndex: sizegroup name
		/// @param _gradingSizeIndex: grading size name 




REST_API
********
 

.. tabs::

	.. code-tab:: python

		def CallRESTGet(url : str, headerNameAndValueList : list[std::pair[str, str]], progressBarText : str) -> str
		"""
		@brief HTTP GET Method
		@param url : e.g. https://api.clo3d.com/customers?version=2.5.9999.299999&userid=clo
		@param headerNameAndValueList : pair list of input HTTP request header parameters
		@param progressBarText : text for the progress bar
		@return string = HTTP Response header + "\r\n\r\n" + HTTP Response body				
		"""

	.. code-tab:: c++

		 CallRESTGet(const string& url, const vector<pair<string, string>>& headerNameAndValueList, const string& progressBarText)
		/// @brief HTTP GET Method
		/// @param url : e.g. https://api.clo3d.com/customers?version=2.5.9999.299999&userid=clo
		/// @param headerNameAndValueList : pair list of input HTTP request header parameters
		/// @param progressBarText : text for the progress bar
		/// @return string = HTTP Response header + "\r\n\r\n" + HTTP Response body				


.. tabs::

	.. code-tab:: python

		def CallRESTPost(url : str, postField : str, headerNameAndValueList : list[std::pair[str, str]], progressBarText : str) -> str
		"""
		@brief HTTP POST Method
		@param url : the full URL for REST API call
		@param postField HTTP Post Body parameter		e.g. "{"parameter1":20,"parameter2":100,"date":"2017-12-13T00:00:00"}"
		@param headerNameAndValueList : pair list of input HTTP request header parameters
		@param progressBarText : text for the progress bar
		@return string = HTTP Response header + "\r\n\r\n" + HTTP Response body
		"""

	.. code-tab:: c++

		 CallRESTPost(const string& url, string *postField, const vector<pair<string, string>>& headerNameAndValueList, const string& progressBarText)
		/// @brief HTTP POST Method
		/// @param url : the full URL for REST API call
		/// @param postField HTTP Post Body parameter		e.g. "{"parameter1":20,"parameter2":100,"date":"2017-12-13T00:00:00"}"
		/// @param headerNameAndValueList : pair list of input HTTP request header parameters
		/// @param progressBarText : text for the progress bar
		/// @return string = HTTP Response header + "\r\n\r\n" + HTTP Response body


.. tabs::

	.. code-tab:: python

		def CallRESTPost2(url : str, postField : char, sizeInByte : int, headerNameAndValueList : list[std::pair[str, str]], progressBarText : str) -> str
		"""
		@brief HTTP POST Method 2
		@param url : the full URL for REST API call
		@param postField HTTP Post Body parameter
		@param sizeInByte The size of postField in bytes
		@param headerNameAndValueList : pair list of input HTTP request header parameters
		@param progressBarText : text for the progress bar
		@return string = HTTP Response header + "\r\n\r\n" + HTTP Response body
		"""

	.. code-tab:: c++

		 CallRESTPost2(const string& url, unsigned char *postField, unsigned int& sizeInByte, const vector<pair<string, string>>& headerNameAndValueList, const string& progressBarText)
		/// @brief HTTP POST Method 2
		/// @param url : the full URL for REST API call
		/// @param postField HTTP Post Body parameter
		/// @param sizeInByte The size of postField in bytes
		/// @param headerNameAndValueList : pair list of input HTTP request header parameters
		/// @param progressBarText : text for the progress bar
		/// @return string = HTTP Response header + "\r\n\r\n" + HTTP Response body


.. tabs::

	.. code-tab:: python

		def CallRESTPostWithMultipartFormData(url : str, filePath : str, headerNameAndValueList : list[std::pair[str, str]], progressBarText : str) -> str
		"""
		@brief HTTP POST with multipart/form-data Method
		@param url : the full URL for REST API call
		@param filePath : path of file to send via REST API
		@param headerNameAndValueList : pair list of input HTTP request header parameters
		@param progressBarText : text for the progress bar
		@return string = HTTP Response header + "\r\n\r\n" + HTTP Response body
		"""

	.. code-tab:: c++

		 CallRESTPostWithMultipartFormData(const string& url, const string& filePath, const vector<pair<string, string>>& headerNameAndValueList, const string& progressBarText)
		/// @brief HTTP POST with multipart/form-data Method
		/// @param url : the full URL for REST API call
		/// @param filePath : path of file to send via REST API
		/// @param headerNameAndValueList : pair list of input HTTP request header parameters
		/// @param progressBarText : text for the progress bar
		/// @return string = HTTP Response header + "\r\n\r\n" + HTTP Response body


.. tabs::

	.. code-tab:: python

		def CallRESTPostWithMultipartFormData(url : str, filePathList : list[str], headerNameAndValueList : list[std::pair[str, str]], progressBarText : str) -> str
		"""
		@brief HTTP POST with multipart/form-data Method
		@param url : the full URL for REST API call
		@param filePathList : path list of files to send via REST API
		@param headerNameAndValueList : pair list of input HTTP request header parameters
		@param progressBarText : text for the progress bar
		@return string = HTTP Response header + "\r\n\r\n" + HTTP Response body
		"""

	.. code-tab:: c++

		 CallRESTPostWithMultipartFormData(const string& url, const vector<string>& filePathList, const vector<pair<string, string>>& headerNameAndValueList, const string& progressBarText) 
		/// @brief HTTP POST with multipart/form-data Method
		/// @param url : the full URL for REST API call
		/// @param filePathList : path list of files to send via REST API
		/// @param headerNameAndValueList : pair list of input HTTP request header parameters
		/// @param progressBarText : text for the progress bar
		/// @return string = HTTP Response header + "\r\n\r\n" + HTTP Response body






 
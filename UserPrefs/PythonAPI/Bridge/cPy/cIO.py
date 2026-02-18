from __future__ import annotations
import cPy.cTypes
import cPy.cImage
#cIO
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class cFileDisk():
	'''
			
		Class for direct disk file Input/Output operations.
		* This class wraps standard C file operations (fopen, fread, fwrite)
		to provide a convenient interface for reading and writing files directly to disk.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def OpenRead(self, FilePn: str) -> bool:
		pass # cpp source

	def CreateWrite(self, FilePn: str) -> bool:
		pass # cpp source

	def OpenAppend(self, FilePn: str) -> bool:
		pass # cpp source

	def GetSizeBytes(self) -> any:
		pass # cpp source

	def GetPos(self) -> any:
		pass # cpp source

	def SetPos(self, Pos: any):
		'''
			
		Sets the file pointer to a specific absolute position.
		
		'''
		pass # cpp source

	def SeekCur(self, Offset: any):
		'''
			
		Moves the file pointer relative to the current position.
		
		'''
		pass # cpp source

	def SeekEnd(self):
		'''
			
		Moves the file pointer to the end of the file.
		
		'''
		pass # cpp source

	def IsEof(self) -> bool:
		'''
			
		Checks if the file pointer is at the end of the file.
		
		'''
		pass # cpp source

	def ReadBytes(self, To: any, MaxSize: int) -> int:
		pass # cpp source

	def WriteBytes(self, From: any, SizeBytes: int):
		pass # cpp source

	def Close(self):
		pass # cpp source

	def GetFILE(self) -> any:
		'''
			
		Returns the underlying standard FILE pointer.
		
		'''
		pass # cpp source



class cFile():
	'''
			
		Class representing an in-memory file or data buffer.
		* Allows reading and writing various data types to a memory block similarly to a file stream.
		* Handles endianness swapping if configured.
		
	'''

	def __init__(self):
		pass # CPP source

	def Copy(self, Src: any, Size: int, FilePn: str = None):
		'''
			
		Copies data from a raw pointer into the internal buffer.
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		Clears the internal data buffer and resets position.
		
		'''
		pass # cpp source

	def GetFilePn(self) -> cPy.cTypes.cStr:
		pass # cpp source

	def SetFilePn(self, FilePn: str):
		pass # cpp source

	def IsEof(self) -> bool:
		pass # cpp source

	def Size(self) -> int:
		pass # cpp source

	def GetPos(self) -> int:
		pass # cpp source

	def SeekCur(self, Offset: int) -> int:
		pass # cpp source

	def SeekEnd(self, Offset: int) -> int:
		'''
			
		Moves the data position pointer relative to the end of the data.

		Args:
			Offset (int): The offset in bytes (usually negative or zero).

		Returns:
			int: The new absolute position.
		
		'''
		pass # cpp source

	def SetPos(self, Pos: int) -> int:
		'''
			
		Sets the data position pointer to an absolute value.

		Args:
			Pos (int): The new position.

		Returns:
			int: The actual new position (clamped to valid range).
		
		'''
		pass # cpp source

	def SetPosMutable(self, Pos: int) -> int:
		'''
			
		Sets the data position pointer, enlarging the file with zeros if "Pos" lies after EOF.

		Args:
			Pos (int): The new position.

		Returns:
			int: The new position.
		
		'''
		pass # cpp source

	def ReadBytes(self, To: any, MaxSize: int) -> int:
		'''
			
		Reads raw bytes from the buffer.
		* Warning: only bytes reading / writing are endian independent.

		Args:
			To : Destination buffer.
			MaxSize (int): Maximum bytes to read.

		Returns:
			int: The number of bytes actually read.
		
		'''
		pass # cpp source

	def WriteBytes(self, Fm: any, Size: int):
		'''
			
		Inserts raw bytes at the current position.
		
		'''
		pass # cpp source

	def ReplaceBytes(self, Fm: any, MaxSize: int) -> int:
		'''
			
		Replaces existing bytes at the current position without inserting new space.
		
		'''
		pass # cpp source

	def ToPtr(self) -> any:
		'''
			
		Returns a constant pointer to the internal data.
		
		'''
		pass # cpp source

	def ToPtr(self) -> any:
		pass # cpp source

	def ToCharPtr(self) -> str:
		pass # cpp source

	def ReadByte(self) -> any:
		pass # cpp source

	def ReadByte(self, b: any) -> bool:
		pass # cpp source

	def WriteByte(self, b: any):
		pass # cpp source

	def ReadShort(self) -> int:
		pass # cpp source

	def ReadShort(self, s: int) -> bool:
		pass # cpp source

	def WriteShort(self, s: int):
		pass # cpp source

	def ReadWord(self) -> int:
		pass # cpp source

	def ReadWord(self, w: int) -> bool:
		pass # cpp source

	def WriteWord(self, w: int):
		pass # cpp source

	def ReadInt(self) -> int:
		pass # cpp source

	def ReadInt(self, i: int) -> bool:
		pass # cpp source

	def WriteInt(self, i: int):
		pass # cpp source

	def ReadDword(self) -> int:
		pass # cpp source

	def ReadDword(self, dw: int) -> bool:
		pass # cpp source

	def WriteDword(self, dw: int):
		pass # cpp source

	def ReadFloat(self) -> float:
		pass # cpp source

	def ReadFloat(self, f: float) -> bool:
		pass # cpp source

	def WriteFloat(self, f: float):
		pass # cpp source

	def ReadDouble(self) -> float:
		pass # cpp source

	def ReadDouble(self, d: float) -> bool:
		pass # cpp source

	def WriteDouble(self, d: float):
		pass # cpp source

	def ReadString(self, _0: cPy.cTypes.cStr, Terminators: str = "\r\n") -> bool:
		'''
			
		Reads a string until a terminator is found.
		
		'''
		pass # cpp source

	def WriteString(self, _0: str):
		'''
			
		Writes a string without a trailing zero.
		
		'''
		pass # cpp source

	def ReadVec2(self, u: cPy.cTypes.cVec2) -> bool:
		pass # cpp source

	def WriteVec2(self, u: cPy.cTypes.cVec2):
		pass # cpp source

	def ReadVec3(self, u: cPy.cTypes.cVec3) -> bool:
		pass # cpp source

	def WriteVec3(self, u: cPy.cTypes.cVec3):
		pass # cpp source

	def ReadRect(self, r: cPy.cTypes.cRect) -> bool:
		pass # cpp source

	def WriteRect(self, r: cPy.cTypes.cRect):
		pass # cpp source

	def ReadVec2i(self, u: any) -> bool:
		pass # cpp source

	def WriteVec2i(self, u: any):
		pass # cpp source



class cImageCodec():
	'''
			
		Abstract base class for image decoding and encoding.
		* Implement this interface to add support for new image formats.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self) -> any:
		pass # CPP source

	def Decode(self, Src: cFile, To: cPy.cImage.cImage) -> bool:
		pass # cpp source

	def Encode(self, Image: cPy.cImage.cImage, To: cFile) -> bool:
		'''
			
		Encodes an image into a file buffer.

		Args:
			Image (cImage): The source image to encode.
			To (cFile): The destination file buffer.

		Returns:
			bool: true if encoding was successful, false otherwise.
		
		'''
		pass # cpp source

	def CheckMagic(self, Magic: int, ext: str) -> int:
		'''
			
		Checks if the file magic number matches this codec.

		Args:
			Magic (int): The magic number (usually the first 4 bytes of the file).
			ext (str): The file extension.

		Returns:
			int: 1 if magic is correct, 0 if incorrect, -1 if this format has no magic number.
		
		'''
		pass # cpp source



class cIO():
	'''
			
		Main Input/Output utility class.
		* Provides static methods for file manipulation, path handling, ZIP archives,
		system dialogs, and image loading/saving.
		
	'''

	@staticmethod
	def AddSourceZip(ZipFilePn: str, DataFolderWithinZip: str = None):
		'''
			
		Mounts a ZIP file as a data source.

		Args:
			ZipFilePn (str): Path to the zip file.
			DataFolderWithinZip (str): Optional subfolder within the zip to treat as root.
		
		'''
		pass # cpp source

	@staticmethod
	def SearchZipSources(DataFolderWithinZip: str = None):
		'''
			
		Searches for ZIP files to add as sources.

		Args:
			DataFolderWithinZip (str): Optional subfolder check.
		
		'''
		pass # cpp source

	@staticmethod
	def ZipInflateRaw(SrcCompressed: any, CompressedSize: int, ToMemory: cFile) -> bool:
		'''
			
		Inflates a raw deflated chunk into memory.

		Args:
			SrcCompressed : Pointer to compressed data.
			CompressedSize (int): Size of compressed data.
			ToMemory (cFile): Destination file buffer.

		Returns:
			bool: true if successful.
		
		'''
		pass # cpp source

	@staticmethod
	def ZipInflateRaw_Debug():
		pass # cpp source

	@staticmethod
	def LoadFile(FilePn: str, To: cFile, ShowWarning: bool = True) -> bool:
		'''
			
		Loads a file into memory.

		Args:
			FilePn (str): Path to the file.
			To (cFile): Destination cFile object.
			ShowWarning (bool): If true, shows a warning if loading fails.

		Returns:
			bool: true if successful.
		
		'''
		pass # cpp source

	@staticmethod
	def SaveFile(FilePn: str, Src: any, Size: int, Append: bool = False, ShowWarning: bool = True) -> bool:
		'''
			
		Saves raw memory to a file.

		Args:
			FilePn (str): Path to the file.
			Src : Source memory pointer.
			Size (int): Size to write.
			Append (bool): If true, appends to the file.
			ShowWarning (bool): If true, shows a warning on failure.

		Returns:
			bool: true if successful.
		
		'''
		pass # cpp source

	@staticmethod
	def SaveFile(FilePn: str, Src: cFile, Append: bool = False, ShowWarning: bool = True) -> bool:
		'''
			
		Saves a cFile object to disk.

		Args:
			FilePn (str): Path to the file. If nullptr, uses Src.GetFilePn().
			Src (cFile): Source cFile object.
			Append (bool): If true, appends to the file.
			ShowWarning (bool): If true, shows a warning on failure.

		Returns:
			bool: true if successful.
		
		'''
		pass # cpp source

	@staticmethod
	def SetFileDialogInitialFolder(PrefKey: str, Folder: str):
		'''
			
		Sets the initial folder for a specific preference key (can be absolute or relative).
		
		'''
		pass # cpp source

	@staticmethod
	def GetFileDialogInitialFolder(PrefKey: str) -> cPy.cTypes.cStr:
		'''
			
		Returns the initial folder for the given key. Returns "GetDefaultSourceFolder" if key is new.
		
		'''
		pass # cpp source

	@staticmethod
	def GetFileDialogPrefExists(PrefKey: str) -> bool:
		'''
			
		Returns false if there is no custom initial folder stored for this PrefKey.
		
		'''
		pass # cpp source

	@staticmethod
	def SelectFolderDialog(Title: str, SelectedFolder: cPy.cTypes.cStr, InitialFolder: str = None) -> bool:
		'''
			
		Opens a dialog to select a folder.

		Args:
			Title (str): Dialog title.
			SelectedFolder (cStr): Output for selected folder path.
			InitialFolder (str): Optional start folder (absolute or relative).

		Returns:
			bool: true if a folder was selected.
		
		'''
		pass # cpp source

	@staticmethod
	def AddCodec(FileExtension: str, Codec: cImageCodec) -> bool:
		'''
			
		Registers a new image codec for a specific extension.
		
		'''
		pass # cpp source

	@staticmethod
	def LoadImage(FilePn: str, To: cPy.cImage.cImage) -> bool:
		'''
			
		Loads an image from file.
		
		'''
		pass # cpp source

	@staticmethod
	def SaveImage(FilePn: str, Src: cPy.cImage.cImage) -> bool:
		'''
			
		Saves an image to file.
		
		'''
		pass # cpp source

	@staticmethod
	def FindImageCodec(FileExtension: str) -> cImageCodec:
		'''
			
		Finds a codec responsible for the given extension.
		
		'''
		pass # cpp source

	@staticmethod
	def GetActualFileExtensionByMagic(FilePn: str, ext: cPy.cTypes.cStr) -> bool:
		'''
			
		Checks magic bytes to determine actual file extension. Returns true if original extension matches.
		
		'''
		pass # cpp source

	@staticmethod
	def GetActualFileExtensionByMagic(Magic: int, ext: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	@staticmethod
	def LastOpenedResource() -> cPy.cTypes.cStr:
		'''
			
		Returns the path of the last opened resource.
		
		'''
		pass # cpp source

	@staticmethod
	def LoadImageDialog(ImageFilePn: cPy.cTypes.cStr) -> bool:
		'''
			
		*
		
		'''
		pass # cpp source

	@staticmethod
	def SaveImageDialog(ImageFilePn: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	@staticmethod
	def SetImageDialogInitialPath(InitialPath: str):
		pass # cpp source

	@staticmethod
	def SetImageDialogInitialFile(InitialFile: str):
		'''
			
		Sets initial file for image dialog. Overrides initial path if not nullptr.
		
		'''
		pass # cpp source

	@staticmethod
	def GetImageDialogInitialPath() -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def GetImageDialogInitialFile() -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def SaveScreenShot(I: cPy.cImage.cImage, OptionalSuffix: str = None):
		'''
			
		Saves a screenshot of the given image, optionally adding a suffix.
		
		'''
		pass # cpp source

	@staticmethod
	def MakeAndSaveScreenShot():
		'''
			
		Captures the current screen and saves it.
		
		'''
		pass # cpp source

	@staticmethod
	def LoadXmlDialog(XmlFilePn: cPy.cTypes.cStr) -> bool:
		'''
			
		*
		
		'''
		pass # cpp source

	@staticmethod
	def SaveXmlDialog(XmlFilePn: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	@staticmethod
	def SetXmlDialogInitialPath(InitialPath: str):
		pass # cpp source

	@staticmethod
	def SetXmlDialogInitialFile(InitialFile: str):
		pass # cpp source

	@staticmethod
	def GetXmlDialogInitialPath() -> cPy.cTypes.cStr:
		'''
			
		 If not nullptr, it will override initial path
		
		'''
		pass # cpp source

	@staticmethod
	def GetXmlDialogInitialFile() -> cPy.cTypes.cStr:
		'''
			
		Returns last loaded/saved XML file or the one set via SetXmlDialogInitialFile.
		
		'''
		pass # cpp source

	@staticmethod
	def SetModelAnimCameraBspDialogsInitialPath(InitialPath: str):
		'''
			
		 Model, Animation, Camera, and Bsp dialogs have common initial path, because they are in the same folder
		
		'''
		pass # cpp source

	@staticmethod
	def GetModelAnimCameraBspDialogsInitialPath() -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def SetModelDialogInitialFile(InitialFile: str):
		'''
			
		 decoding general formats for preview takes a lot of time
		
		'''
		pass # cpp source

	@staticmethod
	def SetAnimDialogInitialFile(InitialFile: str):
		pass # cpp source

	@staticmethod
	def SetBspDialogInitialFile(InitialFile: str):
		pass # cpp source

	@staticmethod
	def SetCameraDialogInitialFile(InitialFile: str):
		pass # cpp source

	@staticmethod
	def PathIsAbsolute(Path: str) -> bool:
		'''
			
		Returns "true" if path is absolute local or network (contains drive letter or starts from two (back)slashes).
		
		'''
		pass # cpp source

	@staticmethod
	def MakeRelativePath(Path: cPy.cTypes.cStr) -> bool:
		'''
			
		Converts the path to relative. Returns true if shortening happened successfully.
		
		'''
		pass # cpp source

	@staticmethod
	def EnsureAbsolutePath(Path: str) -> cPy.cTypes.cStr:
		'''
			
		Builds an absolute path relative to the default source folder if "Path" is relative.
		Also ensures correct (back)slashes.
		
		'''
		pass # cpp source

	@staticmethod
	def GetDefaultSourceFolder() -> cPy.cTypes.cStr:
		'''
			
		Returns folder of the first (default) source.
		usually program folder or its parent if running in Debug/Release.
		
		'''
		pass # cpp source

	@staticmethod
	def SetDefaultSourceWriteFolder(WriteFolder: str):
		'''
			
		Defines alternative write path for source folder.
		
		'''
		pass # cpp source

	@staticmethod
	def ReplaceReadPath(Path: cPy.cTypes.cStr) -> bool:
		'''
			
		Updates path to point to the write folder if applicable.
		Returns "true" if:
		1. "WriteFolder" is defined;
		2. "Path" lies within default source folder;
		3. The argument "Path" has been altered and contains absolute path including "WriteFolder".
		
		'''
		pass # cpp source

	@staticmethod
	def ReplaceReadPathForExistingFile(Path: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	@staticmethod
	def CheckReadPath(Path: str) -> bool:
		'''
			
		Checks if path is within the default source folder structure.
		Returns "true" if:
		1. "WriteFolder" is defined;
		2. "Path" lies within default source folder.
		
		'''
		pass # cpp source

	@staticmethod
	def RestartThisApplication():
		'''
			
		Exits this application and launches this executable again.
		
		'''
		pass # cpp source

	@staticmethod
	def GetThisFilePathName() -> cPy.cTypes.cStr:
		'''
			
		Returns absolute path to this executable file including its name.
		
		'''
		pass # cpp source

	@staticmethod
	def GetDocumentsFolder() -> cPy.cTypes.cStr:
		'''
			
		Returns documents folder. Linux: /home/USER/Documents/, macOS: /Users/USER/Documents/, Windows: C:/Users/USER/Documents/
		
		'''
		pass # cpp source

	@staticmethod
	def GetSystemDocumentsFolder() -> cPy.cTypes.cStr:
		pass # cpp source

	@staticmethod
	def GetDownloadsFolder() -> cPy.cTypes.cStr:
		'''
			
		Returns downloads folder.
		
		'''
		pass # cpp source

	@staticmethod
	def GetDesktopFolder() -> cPy.cTypes.cStr:
		'''
			
		Returns desktop folder (Windows only).
		
		'''
		pass # cpp source

	@staticmethod
	def SetFilePermissions(FilePn: str):
		'''
			
		Corrects file attributes to ensure read/write rights.
		
		'''
		pass # cpp source

	@staticmethod
	def SetFolderPermissions(Folder: str):
		pass # cpp source

	@staticmethod
	def CreatePath(PathOrFilePn: str, inUserDocuments: bool = True) -> bool:
		'''
			
		Checks existence of all intermediate directories and creates them if necessary.
		* "PathOrFilePn" can be absolute / relative path or file name without path.
		Examples:
		- `cIO::CreatePath("1/2/3");`
		- Windows: `cIO::CreatePath("c:/A/B\\C\\File.txt")`
		- MacOS: `cIO::CreatePath("/A/B\\C")`

		Args:
			PathOrFilePn (str): The path to create.
			inUserDocuments (bool): If true, tries to create in user documents folder.

		Returns:
			bool: "true" if all intermediate directories exist or have been created.
		
		'''
		pass # cpp source

	@staticmethod
	def Exec(FilePn: str, Args: str = None, Wait: bool = False, Hide: bool = False) -> bool:
		'''
			
		Executes an external file or program.
		* Usage examples:
		1. Document pathname:
		- `cIO::Exec(cIO::EnsureAbsolutePath("~/Scripts/Scripting.pdf"))`
		2. Program with absolute path and optional arguments:
		- Windows: `cIO::Exec("C:\\...\\maya.exe", "D:\\...\\Logo.mb")`
		- Linux: `cIO::Exec("/usr/bin/env python", "-V")`
		3. URL with protocol:
		- `cIO::Exec("http://3d-coat.com/")`
		*

		Args:
			FilePn (str): Path to file, program, or URL.
			Args (str): Optional arguments.
			Wait (bool): If true, waits for process to finish.
			Hide (bool): If true, hides the window.

		Returns:
			bool: true if execution started successfully.
		
		'''
		pass # cpp source

	@staticmethod
	def CheckProcessInMemory(ProcName: str) -> bool:
		'''
			
		Checks if a process with the given name is running.

		Args:
			ProcName (str): Process name (case-insensitive partial match).

		Returns:
			bool: true if process exists.
		
		'''
		pass # cpp source

	@staticmethod
	def Explore(Folder: str) -> bool:
		'''
			
		Opens a folder in the system file explorer.
		Examples: `cIO::Explore("Shaders")`

		Args:
			Folder (str): Absolute or relative path.

		Returns:
			bool: true on success.
		
		'''
		pass # cpp source

	@staticmethod
	def CompareFileChangeTimes(FilePn0: str, FilePn1: str) -> bool:
		'''
			
		Compares file modification times.

		Args:
			FilePn0 (str): First file path.
			FilePn1 (str): Second file path.

		Returns:
			bool: "true" when "FilePn0" is older than "FilePn1".
		
		'''
		pass # cpp source

	@staticmethod
	def NeedUpdateFile(FileToUpdate: str, SourceFile: str) -> bool:
		'''
			
		Returns true if FileToUpdate does not exist or is older than SourceFile.
		
		'''
		pass # cpp source

	@staticmethod
	def CombineImages(File1: str, File2: str, FileOut: str) -> bool:
		'''
			
		Combines two images into an output image with the same format.

		Returns:
			bool: true if successful.
		
		'''
		pass # cpp source

	@staticmethod
	def CheckDifferentDisks(PathName0: str, PathName1: str) -> bool:
		'''
			
		Returns "true" when files/folders "PathName0" and "PathName1" reside on different disks.
		Note: paths could be non-existent.
		
		'''
		pass # cpp source

	@staticmethod
	def CopyToClipboard(Src: str):
		pass # cpp source

	@staticmethod
	def CopyFromClipboard(To: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	@staticmethod
	def CopyToClipboard(Src: cPy.cImage.cImage):
		pass # cpp source

	@staticmethod
	def CopyFromClipboard(To: cPy.cImage.cImage) -> bool:
		pass # cpp source

	@staticmethod
	def RemoveFolder(Folder: str, Recursive: bool = True) -> bool:
		'''
			
		Removes a directory.

		Args:
			Folder (str): Directory path.
			Recursive (bool): If true, deletes content recursively.
		
		'''
		pass # cpp source

	@staticmethod
	def RemoveFile(FilePn: str) -> bool:
		'''
			
		Deletes a file.
		
		'''
		pass # cpp source

	@staticmethod
	def CheckIfPathWritable(path: str) -> bool:
		'''
			
		Checks if the path is writable.
		
		'''
		pass # cpp source

	@staticmethod
	def GetDiskFreeSpace() -> float:
		'''
			
		Returns number of free megabytes on the disk containing this program.
		
		'''
		pass # cpp source

	@staticmethod
	def FileExists(filename: str) -> bool:
		'''
			
		Returns true if file exists.

		Args:
			filename (str): The filename. Relative and absolute paths are supported. Documents folder placement taken into account. Checked in both install and documents folders.

		Returns:
			bool: true if file exists.
		
		'''
		pass # cpp source

	@staticmethod
	def FileCopy(Src: str, Dst: str, overwrite: bool = True) -> bool:
		'''
			
		Copy file from Src to Dst.

		Args:
			Src (str): The source file.
			Dst (str): The destination file. If file is in install folder, it will be copied to the documents folder.
			overwrite (bool): If true, overwrites existing file.

		Returns:
			bool: true if file copied successfully.
		
		'''
		pass # cpp source

	@staticmethod
	def GetDiskSerialNumber() -> cPy.cTypes.cStr:
		'''
			
		Returns serial number of bootable hard disk.
		Examples: MacOS "6RY57LG3", Windows "1490395c", Linux "49cb4cde".

		Returns:
			cPy.cTypes.cStr: Serial number or empty string on failure.
		
		'''
		pass # cpp source

	@staticmethod
	def GetMACAddress() -> cPy.cTypes.cStr:
		'''
			
		Returns primary MAC address.
		Format: "xx:xx:xx:xx:xx:xx".

		Returns:
			cPy.cTypes.cStr: MAC address or empty string on failure.
		
		'''
		pass # cpp source

	@staticmethod
	def ShowString(OptionalInit: cPy.cTypes.cStr = None, dx: int = 0, dy: int = 0, center_x: bool = True, center_y: bool = True):
		pass # cpp source

	@staticmethod
	def GetString(S: cPy.cTypes.cStr) -> bool:
		'''
			
		Returns "true" when the string is visible.
		
		'''
		pass # cpp source

	@staticmethod
	def InputString(X: int, Y: int, S: cPy.cTypes.cStr, EditWidthPixels: int = 100) -> bool:
		pass # cpp source

	@staticmethod
	def InputString(S: cPy.cTypes.cStr) -> bool:
		pass # cpp source

	@staticmethod
	def StopStringInput():
		pass # cpp source

	@staticmethod
	def GetInputPixelsHeight() -> int:
		pass # cpp source

	@staticmethod
	def ReturnPressed() -> bool:
		pass # cpp source

	@staticmethod
	def GetUserFolder() -> cPy.cTypes.cStr:
		'''
			
		Deprecated. Use "cIO::GetDocumentsFolder".
		
		'''
		pass # cpp source

	@staticmethod
	def GetCacheFolder() -> cPy.cTypes.cStr:
		'''
			
		Returns cache folder path. Could be empty.
		
		'''
		pass # cpp source

	@staticmethod
	def GetEnvironmentVariable(VarName: str) -> cPy.cTypes.cStr:
		'''
			
		Returns value of environment variable or empty string if the variable is not defined.
		
		'''
		pass # cpp source


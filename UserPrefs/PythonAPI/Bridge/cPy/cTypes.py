from __future__ import annotations
#cTypes
import Coat_CPP
import typing
from typing import ClassVar
from typing import TypeAlias
from typing import Any
from enum import Enum


class cStr():
	'''
			
		A custom string class optimized for performance and ease of use.
		 *
		This class provides a wide range of string manipulation functions, including
		dynamic resizing, formatting, path handling, and type conversions.
		It is designed to work with standard C-style strings and provides
		safe memory management.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, Src: cStr):
		pass # CPP source

	def __init__(self, Src: cStr, StartIndex: int, Count: int):
		pass # CPP source

	def __init__(self, Src: str):
		pass # CPP source

	def __init__(self, Src: str, StartIndex: int, Count: int):
		pass # CPP source

	def __init__(self, Src: any):
		pass # CPP source

	def __init__(self, Length: int, Fill: any):
		pass # CPP source

	def __init__(self):
		pass # CPP source

	def Copy(self, Src: cStr):
		'''
			
		 \brief Copies content from another cStr object.
		
		'''
		pass # cpp source

	def Copy(self, Src: cStr, StartIndex: int, Count: int):
		'''
			
		 \brief Copies a substring from another cStr object.
		
		'''
		pass # cpp source

	def Copy(self, Src: str):
		'''
			
		 \brief Copies content from a C-style string.
		
		'''
		pass # cpp source

	def Copy(self, Src: str, StartIndex: int, Count: int):
		'''
			
		 \brief Copies a substring from a C-style string.
		
		'''
		pass # cpp source

	def Copy(self, _0: any):
		'''
			
		 \brief Copies content from a wide character string.
		
		'''
		pass # cpp source

	def __assign__(self, Src: cStr):
		return super().__assign__(Src)

	def __assign__(self, Src: str):
		return super().__assign__(Src)

	def __assign__(self, x: int):
		return super().__assign__(x)

	def ToCharPtr(self) -> str:
		'''
			
		Returns a pointer to the internal character buffer.

		Returns:
			str: A const char pointer to the string data. Returns a pointer to an empty string if null.
		
		'''
		pass # cpp source

	def __str__(self) -> str:
		'''
			
		 \brief Python-style string representation.
		
		'''
		pass # cpp source

	def __repr__(self) -> str:
		pass # cpp source

	def ToNonConstCharPtr(self) -> str:
		pass # cpp source

	def __getitem__(self, CharIndex: int) -> any:
		return super().__getitem__(CharIndex)

	def __setitem__(self, CharIndex: int) -> any:
		return super().__setitem__(CharIndex)

	def Length(self) -> int:
		'''
			
		 \brief Gets the length of the string.
		
		'''
		pass # cpp source

	def SetLength(self, Length: int, Fill: any):
		'''
			
		Ensures needed capacity and sets a specified length.

		Args:
			Length (int): The new length of the string.
			Fill : The character to fill new space with if expanding.
		
		'''
		pass # cpp source

	def CalcLength(self):
		'''
			
		Recalculates the length based on the actual null terminator position.
		Useful after direct buffer manipulation via ToCharPtr().
		
		'''
		pass # cpp source

	def Fill(self, c: any):
		'''
			
		 \brief Fills the entire string with a specified character.
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		 \brief Checks if the string is empty.
		
		'''
		pass # cpp source

	def empty(self) -> bool:
		'''
			
		 \brief Checks if the string length is 0 (STL compatibility).
		
		'''
		pass # cpp source

	def Clear(self):
		'''
			
		 \brief Clears the string content (sets length to 0).
		
		'''
		pass # cpp source

	Empty: cStr = Coat_CPP.cStr.Empty #: static const cStr (T)  \brief A static constant representing an empty string. 
	@staticmethod
	def Equals(l: str, r: str) -> bool:
		'''
			
		 \brief Checks equality of two strings.
		
		'''
		pass # cpp source

	@staticmethod
	def Equals(l: str, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def Equals(l: cStr, r: str) -> bool:
		pass # cpp source

	@staticmethod
	def Equals(l: cStr, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def Equals(l: cStr, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: str, r: str) -> bool:
		'''
			
		 \brief Checks equality ignoring case sensitivity.
		
		'''
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: str, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: cStr, r: str) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: cStr, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: cStr, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: str, r: str, MaxLength: int) -> bool:
		'''
			
		 \brief Checks equality ignoring case sensitivity with length limit.
		
		'''
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: str, r: cStr, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: cStr, r: str, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsNoCase(l: cStr, r: cStr, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def Compare(l: str, r: str) -> int:
		'''
			
		Compares two strings.

		Returns:
			int: < 0 if l < r, 0 if l == r, > 0 if l > r.
		
		'''
		pass # cpp source

	@staticmethod
	def Compare(l: str, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def Compare(l: cStr, r: str) -> int:
		pass # cpp source

	@staticmethod
	def Compare(l: cStr, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def Compare(l: cStr, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def Compare(l: str, r: str, MaxLength: int) -> int:
		'''
			
		 \brief Compares two strings with length limit.
		
		'''
		pass # cpp source

	@staticmethod
	def Compare(l: str, r: cStr, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def Compare(l: cStr, r: str, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def Compare(l: cStr, r: cStr, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: str, r: str) -> int:
		'''
			
		 \brief Compares two strings ignoring case.
		
		'''
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: str, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: cStr, r: str) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: cStr, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: cStr, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: str, r: str, MaxLength: int) -> int:
		'''
			
		 \brief Compares two strings ignoring case with length limit.
		
		'''
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: str, r: cStr, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: cStr, r: str, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def CompareNoCase(l: cStr, r: cStr, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: str, r: str) -> bool:
		'''
			
		Checks if two file paths are equal.
		Considers '\\' and '/' as equivalent and ignores case.
		
		'''
		pass # cpp source

	@staticmethod
	def EqualsPath(l: str, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: cStr, r: str) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: cStr, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: cStr, r: cStr) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: str, r: str, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: str, r: cStr, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: cStr, r: str, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def EqualsPath(l: cStr, r: cStr, MaxLength: int) -> bool:
		pass # cpp source

	@staticmethod
	def ComparePath(l: str, r: str) -> int:
		'''
			
		Compares two file paths.
		Considers '\\' and '/' as equivalent, ignores case, and compares according to folder depth.
		
		'''
		pass # cpp source

	@staticmethod
	def ComparePath(l: str, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: cStr, r: str) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: cStr, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: cStr, r: cStr) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: str, r: str, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: str, r: cStr, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: cStr, r: str, MaxLength: int) -> int:
		pass # cpp source

	@staticmethod
	def ComparePath(l: cStr, r: cStr, MaxLength: int) -> int:
		pass # cpp source

	def StartsWith(self, Str: str, NoCase: bool = False) -> bool:
		'''
			
		Determines whether the beginning of this instance matches the specified string.

		Args:
			Str (str): The string to compare.
			NoCase (bool): If true, ignores case.

		Returns:
			bool: True if it starts with Str or if Str is empty.
		
		'''
		pass # cpp source

	def EndsWith(self, Str: str, NoCase: bool = False) -> bool:
		'''
			
		Determines whether the end of this instance matches the specified string.

		Args:
			Str (str): The string to compare.
			NoCase (bool): If true, ignores case.

		Returns:
			bool: True if it ends with Str or if Str is empty.
		
		'''
		pass # cpp source

	@staticmethod
	def ToString(Src: bool) -> cStr:
		'''
			
		Converts various types to a string representation.
		Used internally for Append/Insert and stream operators.
		
		'''
		pass # cpp source

	@staticmethod
	def ToString(Src: int) -> cStr:
		pass # cpp source

	@staticmethod
	def ToString(Src: int, Prec: int) -> cStr:
		pass # cpp source

	@staticmethod
	def ToString(IntArray: int, Count: int, Separator: str = " ") -> cStr:
		pass # cpp source

	@staticmethod
	def ToString(Src: float, Prec: int = 2) -> cStr:
		pass # cpp source

	@staticmethod
	def ToString(FloatArray: float, Count: int, Prec: int = 2, Separator: str = " ") -> cStr:
		pass # cpp source

	@staticmethod
	def ToString(Src: float, Prec: int = 6) -> cStr:
		pass # cpp source

	@staticmethod
	def ToString(DoubleArray: float, Count: int, Prec: int = 6, Separator: str = " ") -> cStr:
		pass # cpp source

	@staticmethod
	def ToHex(dw: int) -> cStr:
		'''
			
		 \brief Converts dword to hex string.
		
		'''
		pass # cpp source

	@staticmethod
	def ToHex(qw: any) -> cStr:
		'''
			
		 \brief Converts qword to hex string.
		
		'''
		pass # cpp source

	@staticmethod
	def ToHex(Ptr: any) -> cStr:
		'''
			
		 \brief Converts pointer address to hex string.
		
		'''
		pass # cpp source

	def Append(self, Src: cStr):
		'''
			
		 \brief Appends a string to the end of this instance.
		
		'''
		pass # cpp source

	def Append(self, Src: cStr, StartIndex: int, Count: int):
		pass # cpp source

	def Append(self, Src: str):
		pass # cpp source

	def Append(self, Src: any):
		pass # cpp source

	def Append(self, Src: str, StartIndex: int, Count: int):
		pass # cpp source

	def Append(self, Src: any):
		pass # cpp source

	def Append(self, Src: any, Count: int):
		pass # cpp source

	def Append(self, Src: bool):
		pass # cpp source

	def Append(self, Src: int):
		pass # cpp source

	def Append(self, Src: float, Prec: int = 2):
		pass # cpp source

	def Append(self, Src: float, Prec: int = 6):
		pass # cpp source

	def AppendWithEndLn(self, Src: cStr):
		'''
			
		 \brief Appends a string followed by a newline.
		
		'''
		pass # cpp source

	EndLn: cStr = Coat_CPP.cStr.EndLn #: static const cStr (T)  \brief Static newline constant. 
	def __iadd__(self, Src: cStr):
		return super().__iadd__(Src)

	def __iadd__(self, Src: str):
		return super().__iadd__(Src)

	def __iadd__(self, Src: any):
		return super().__iadd__(Src)

	def __iadd__(self, Src: any):
		return super().__iadd__(Src)

	def __iadd__(self, Src: bool):
		return super().__iadd__(Src)

	def __iadd__(self, Src: int):
		return super().__iadd__(Src)

	def __iadd__(self, Src: float):
		return super().__iadd__(Src)

	def __iadd__(self, Src: float):
		return super().__iadd__(Src)

	def AppendPath(self, Path: str):
		'''
			
		 \brief Appends a path segment, automatically adding a slash or backslash.
		
		'''
		pass # cpp source

	def Insert(self, Index: int, Src: cStr):
		'''
			
		 \brief Inserts a string or value at a specified index.
		
		'''
		pass # cpp source

	def Insert(self, Index: int, Src: cStr, StartIndex: int, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Src: str):
		pass # cpp source

	def Insert(self, Index: int, Src: str, StartIndex: int, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Src: any):
		pass # cpp source

	def Insert(self, Index: int, Src: any, Count: int):
		pass # cpp source

	def Insert(self, Index: int, Src: bool):
		pass # cpp source

	def Insert(self, Index: int, Src: int):
		pass # cpp source

	def Insert(self, Index: int, Src: float, Prec: int = 2):
		pass # cpp source

	def Insert(self, Index: int, Src: float, Prec: int = 6):
		pass # cpp source

	def Remove(self, StartIndex: int):
		'''
			
		Deletes characters from the string.

		Args:
			StartIndex (int): Position to start removing.
		
		'''
		pass # cpp source

	def Remove(self, StartIndex: int, Count: int):
		'''
			
		Deletes a specific number of characters.

		Args:
			StartIndex (int): Position to start removing.
			Count (int): Number of characters to remove.
		
		'''
		pass # cpp source

	def Replace(self, Char: any, WithChar: any):
		'''
			
		 \brief Replaces all occurrences of a character with another.
		
		'''
		pass # cpp source

	def ReplaceCommaWithDot(self):
		'''
			
		 \brief Utility to replace commas with dots (e.g. for localization fixing).
		
		'''
		pass # cpp source

	def Replace(self, Char: any, WithChar: any, StartIndex: int, Count: int):
		pass # cpp source

	def Replace(self, String: str, WithString: str, NoCase: bool = False) -> int:
		'''
			
		Replaces all occurrences of a string with another string.

		Returns:
			int: Number of replacements made.
		
		'''
		pass # cpp source

	def Replace(self, String: str, WithString: str, StartIndex: int, NoCase: bool = False) -> int:
		pass # cpp source

	def Replace(self, String: str, WithString: str, StartIndex: int, Count: int, NoCase: bool = False) -> int:
		pass # cpp source

	def ReplaceFirst(self, String: str, WithString: str, NoCase: bool = False) -> int:
		'''
			
		 \brief Replaces only the first occurrence of a string.
		
		'''
		pass # cpp source

	def ReplaceFirst(self, String: str, WithString: str, StartIndex: int, Count: int, NoCase: bool = False) -> int:
		pass # cpp source

	def ReplaceAny(self, Chars: str, WithChar: any):
		'''
			
		Replaces all occurrences of any character in the 'Chars' list with 'WithChar'.
		Example: S.ReplaceAny(",;\t", ' ');
		
		'''
		pass # cpp source

	def ReplaceAny(self, Chars: str, WithChar: any, StartIndex: int, Count: int):
		pass # cpp source

	def Substring(self, StartIndex: int) -> cStr:
		'''
			
		 \brief Retrieves a substring starting from StartIndex to the end.
		
		'''
		pass # cpp source

	def Substring(self, StartIndex: int, Count: int) -> cStr:
		'''
			
		 \brief Retrieves a substring of specified length.
		
		'''
		pass # cpp source

	def TrimStart(self, TrimChars: str):
		'''
			
		 \brief Removes specified characters from the start of the string.
		
		'''
		pass # cpp source

	def TrimEnd(self, TrimChars: str):
		'''
			
		 \brief Removes specified characters from the end of the string.
		
		'''
		pass # cpp source

	def Trim(self, TrimChars: str):
		'''
			
		 \brief Removes specified characters from both start and end.
		
		'''
		pass # cpp source

	def PadLeft(self, TotalWidth: int, PaddingChar: any):
		'''
			
		 \brief Right-aligns characters, padding on the left.
		
		'''
		pass # cpp source

	def PadRight(self, TotalWidth: int, PaddingChar: any):
		'''
			
		 \brief Left-aligns characters, padding on the right.
		
		'''
		pass # cpp source

	def Contains(self, c: any) -> bool:
		'''
			
		 \brief Checks if the string contains a character.
		
		'''
		pass # cpp source

	def Contains(self, Str: str, NoCase: bool = False) -> bool:
		'''
			
		 \brief Checks if the string contains a substring.
		
		'''
		pass # cpp source

	def IndexOf(self, c: any) -> int:
		'''
			
		 \brief Returns the index of the first occurrence of a character, or -1.
		
		'''
		pass # cpp source

	def IndexOfAny(self, Chars: str) -> int:
		'''
			
		 \brief Returns the index of the first occurrence of any character from the list, or -1.
		
		'''
		pass # cpp source

	def IndexOfAny(self, Chars: str, StartIndex: int) -> int:
		pass # cpp source

	def IndexOfAny(self, Chars: str, StartIndex: int, Count: int) -> int:
		pass # cpp source

	def LastIndexOf(self, c: any) -> int:
		'''
			
		 \brief Returns the index of the last occurrence of a character, or -1.
		
		'''
		pass # cpp source

	def LastIndexOf(self, c: any, StartIndex: int) -> int:
		pass # cpp source

	def LastIndexOf(self, c: any, StartIndex: int, Count: int) -> int:
		pass # cpp source

	def LastIndexOf(self, Str: str, NoCase: bool = False) -> int:
		'''
			
		 \brief Returns the index of the last occurrence of a string, or -1.
		
		'''
		pass # cpp source

	def LastIndexOf(self, Str: str, StartIndex: int, NoCase: bool = False) -> int:
		pass # cpp source

	def LastIndexOf(self, Str: str, StartIndex: int, Count: int, NoCase: bool = False) -> int:
		pass # cpp source

	def LastIndexOfAny(self, Chars: str) -> int:
		'''
			
		 \brief Returns the index of the last occurrence of any character from the list, or -1.
		
		'''
		pass # cpp source

	def LastIndexOfAny(self, Chars: str, StartIndex: int) -> int:
		pass # cpp source

	def LastIndexOfAny(self, Chars: str, StartIndex: int, Count: int) -> int:
		pass # cpp source

	@staticmethod
	def ToLower(c: any) -> any:
		'''
			
		 \brief Static helper to convert char to lower case.
		
		'''
		pass # cpp source

	@staticmethod
	def ToUpper(c: any) -> any:
		'''
			
		 \brief Static helper to convert char to upper case.
		
		'''
		pass # cpp source

	def MakeLower(self, start: int = 0):
		'''
			
		 \brief Converts this string instance to lowercase in place.
		
		'''
		pass # cpp source

	def MakeUpper(self, start: int = 0):
		'''
			
		 \brief Converts this string instance to uppercase in place.
		
		'''
		pass # cpp source

	@staticmethod
	def Formatv(Format: str, Args: any) -> cStr:
		'''
			
		Creates a formatted string (printf style).

		Args:
			Format (str): The format string.

		Returns:
			cStr: A new formatted cStr.
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsLower(c: int) -> bool:
		'''
			
		 \brief Helper: Is character lowercase?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsUpper(c: int) -> bool:
		'''
			
		 \brief Helper: Is character uppercase?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsAlpha(c: int) -> bool:
		'''
			
		 \brief Helper: Is character alphabetical?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsNumeric(c: int) -> bool:
		'''
			
		 \brief Helper: Is character a digit?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsHexadecimal(c: int) -> bool:
		'''
			
		 \brief Helper: Is character hexadecimal digit?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsNewLine(c: int) -> bool:
		'''
			
		 \brief Helper: Is character a newline type?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsTab(c: int) -> bool:
		'''
			
		 \brief Helper: Is character a tab?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsWhitespace(c: int) -> bool:
		'''
			
		 \brief Helper: Is character whitespace?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsDecimalPoint(c: int) -> bool:
		'''
			
		 \brief Helper: Is character a decimal point (. or ,)?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsSign(c: int) -> bool:
		'''
			
		 \brief Helper: Is character a sign (+ or -)?
		
		'''
		pass # cpp source

	@staticmethod
	def CharIsExponent(c: int) -> bool:
		'''
			
		 \brief Helper: Is character part of exponent notation (e, E, d, D)?
		
		'''
		pass # cpp source

	@staticmethod
	def ToInt(Str: str, Value: int) -> bool:
		'''
			
		 \brief Parses string to integer.
		
		'''
		pass # cpp source

	@staticmethod
	def ToFloat(Str: str, Value: float) -> bool:
		'''
			
		 \brief Parses string to float.
		
		'''
		pass # cpp source

	def GetHashCode(self, NoCase: bool = False) -> int:
		'''
			
		 \brief Calculates a hash code for the string.
		
		'''
		pass # cpp source

	def GetFileExtension(self) -> cStr:
		'''
			
		 \brief Extracts file extension from path.
		
		'''
		pass # cpp source

	def GetFileName(self) -> cStr:
		'''
			
		 \brief Extracts file name (with extension) from path.
		
		'''
		pass # cpp source

	def GetFileBase(self) -> cStr:
		'''
			
		 \brief Extracts file base name (no path, no extension).
		
		'''
		pass # cpp source

	def GetFilePath(self) -> cStr:
		'''
			
		 \brief Extracts directory path (excluding filename).
		
		'''
		pass # cpp source

	def RemoveFileExtension(self):
		'''
			
		 \brief Removes extension from the string (in place).
		
		'''
		pass # cpp source

	def RemoveFileName(self):
		'''
			
		 \brief Removes filename, leaving only path (in place).
		
		'''
		pass # cpp source

	def RemoveFilePath(self):
		'''
			
		 \brief Removes path, leaving only filename (in place).
		
		'''
		pass # cpp source

	def RemoveFileAbsPath(self, AbsPath: str):
		'''
			
		 \brief Removes absolute path prefix if present.
		
		'''
		pass # cpp source

	def AppendFileRelPath(self, RelPath: str):
		'''
			
		 \brief Appends a relative path correctly.
		
		'''
		pass # cpp source

	def SetFileExtension(self, Extension: str):
		'''
			
		 \brief Sets or replaces file extension.
		
		'''
		pass # cpp source

	def SetFileDefaultExtension(self, DefaultExtension: str):
		'''
			
		 \brief Sets extension only if none exists.
		
		'''
		pass # cpp source

	def SetFilePath(self, Path: str):
		'''
			
		 \brief Sets or replaces the directory path.
		
		'''
		pass # cpp source

	def SetFileDefaultPath(self, DefaultPath: str):
		'''
			
		 \brief Sets path only if none exists.
		
		'''
		pass # cpp source

	def EnsureTrailingBackslash(self):
		'''
			
		 \brief Ensures string ends with a backslash.
		
		'''
		pass # cpp source

	def EnsureTrailingSlash(self):
		'''
			
		 \brief Ensures string ends with a forward slash.
		
		'''
		pass # cpp source

	def EnsureTrailingPlatformSlash(self):
		'''
			
		 \brief Ensures trailing slash based on current platform (Windows/Linux/Mac).
		
		'''
		pass # cpp source

	def SlashesToBackSlashes(self):
		pass # cpp source

	def BackSlashesToSlashes(self):
		'''
			
		 \brief Converts all backslashes to forward slashes.
		
		'''
		pass # cpp source

	def MakePlatformSlashes(self):
		'''
			
		 \brief Normalizes slashes based on current platform.
		
		'''
		pass # cpp source

	def CalcUTF8Length(self, StartIndex: int) -> int:
		pass # cpp source

	def Init(self):
		'''
			
		 \brief Resets internal state to empty.
		
		'''
		pass # cpp source

	def Free(self):
		'''
			
		 \brief Frees memory and resets state.
		
		'''
		pass # cpp source

	def __init__(self, Src: any):
		pass # CPP source

	def __init__(self, Src: str):
		pass # CPP source

	def Copy(self, _0: any):
		pass # cpp source

	def Copy(self, _0: any):
		pass # cpp source

	def __assign__(self, _0: any):
		return super().__assign__(_0)

	def __assign__(self, _0: any):
		return super().__assign__(_0)

	def toWstring(self, ws: any):
		pass # cpp source

	def toWstring(self) -> any:
		pass # cpp source

	def Append(self, _0: str):
		pass # cpp source

	def Append(self, _0: any):
		pass # cpp source

	def __iadd__(self, _0: str):
		return super().__iadd__(_0)

	def __iadd__(self, _0: any):
		return super().__iadd__(_0)



class cVec2():
	'''
			
		A 2D vector class providing linear algebra operations and geometry functions.
		 *
		This class represents a 2-component vector (x, y) and includes methods for
		arithmetic, geometric transformations (dot, cross, normalize), matrix multiplication,
		and various utility functions (lerp, clamp, reflect).
		 *
		Refer to it as coat::vec2 in the Core API.
		
	'''

	x: float #: float (T)  The X component of the vector. 
	y: float #: float (T)  The Y component of the vector. 
	def __init__(self):
		pass # CPP source

	def __init__(self, S: float) -> any:
		pass # CPP source

	def __init__(self, X: float, Y: float):
		pass # CPP source

	def __init__(self, v: cVec2):
		pass # CPP source

	def Copy(self, Src: float):
		pass # cpp source

	def SetZero(self):
		'''
			
		Sets the vector to (0, 0).
		
		'''
		pass # cpp source

	def SetOne(self):
		'''
			
		Sets the vector to (1, 1).
		
		'''
		pass # cpp source

	def Set(self, S: float):
		'''
			
		Sets both components to scalar S.
		
		'''
		pass # cpp source

	def Set(self, X: float, Y: float):
		'''
			
		Sets components to specific X and Y values.
		
		'''
		pass # cpp source

	def __getitem__(self, index: int) -> float:
		return super().__getitem__(index)

	def __setitem__(self, index: int) -> float:
		return super().__setitem__(index)

	def __neg__(self) -> cVec2:
		return super().__neg__()

	def __iadd__(self, _0: cVec2) -> cVec2:
		return super().__iadd__(_0)

	def __isub__(self, _0: cVec2) -> cVec2:
		return super().__isub__(_0)

	def __imul__(self, _0: cVec2) -> cVec2:
		return super().__imul__(_0)

	def __imul__(self, _0: float) -> cVec2:
		return super().__imul__(_0)

	def __itruediv__(self, _0: cVec2) -> cVec2:
		return super().__itruediv__(_0)

	def __itruediv__(self, _0: float) -> cVec2:
		return super().__itruediv__(_0)

	def Transform(self, _0: any):
		'''
			
		Transforms the vector by a 3x3 matrix.
		
		Treats the vector as a direction (x, y, 0).
		
		'''
		pass # cpp source

	def __imul__(self, _0: any):
		return super().__imul__(_0)

	def TransformCoordinate(self, _0: any):
		'''
			
		Transforms the vector by a 4x4 matrix treating it as a point.
		
		Implicitly extends to (x, y, 0, 1) and projects the result back 
		by dividing by w (Perspective divide).
		
		'''
		pass # cpp source

	def TransformNormal(self, _0: any):
		'''
			
		Transforms the vector by a 4x4 matrix treating it as a normal/direction.
		
		Implicitly extends to (x, y, 0, 0), ignoring translation.
		
		'''
		pass # cpp source

	def __add__(self, _0: cVec2) -> cVec2:
		return super().__add__(_0)

	def __sub__(self, _0: cVec2) -> cVec2:
		return super().__sub__(_0)

	def __mul__(self, _0: cVec2) -> cVec2:
		return super().__mul__(_0)

	def __mul__(self, _0: float) -> cVec2:
		return super().__mul__(_0)

	def __truediv__(self, _0: cVec2) -> cVec2:
		return super().__truediv__(_0)

	def __truediv__(self, _0: float) -> cVec2:
		return super().__truediv__(_0)

	def __mul__(self, _0: any) -> cVec2:
		return super().__mul__(_0)

	def __eq__(self, _0: cVec2) -> bool:
		return super().__eq__(_0)

	def __ne__(self, _0: cVec2) -> bool:
		return super().__ne__(_0)

	@staticmethod
	def Equals(_0: cVec2, _1: cVec2, Eps: float) -> bool:
		'''
			
		Checks if two vectors are equal within a given epsilon tolerance.
		
		'''
		pass # cpp source

	def Length(self) -> float:
		'''
			
		Returns the length (magnitude) of the vector.
		
		'''
		pass # cpp source

	def LengthSq(self) -> float:
		'''
			
		Returns the squared length of the vector (faster than Length).
		
		'''
		pass # cpp source

	def Normalize(self) -> float:
		'''
			
		Normalizes the vector in place. Returns the previous length.
		
		'''
		pass # cpp source

	def NormalizeSafe(self, Fallback: cVec2) -> float:
		'''
			
		Normalizes the vector safely.

		Args:
			Fallback (cVec2): The value to assign if the vector length is zero.

		Returns:
			float: The previous length, or 0.0f if the vector was zero.
		
		'''
		pass # cpp source

	def IsValid(self) -> bool:
		'''
			
		Checks if the vector components are valid numbers (not NaN/Inf).
		
		'''
		pass # cpp source

	def IsNormalized(self, Eps: float) -> bool:
		'''
			
		Checks if the vector is normalized (length == 1) within tolerance.
		
		'''
		pass # cpp source

	def IsZero(self, Eps: float) -> bool:
		'''
			
		Checks if the vector is zero (length == 0) within tolerance.
		
		'''
		pass # cpp source

	@staticmethod
	def Round(_0: cVec2) -> cVec2:
		'''
			
		Returns a new vector with components rounded to the nearest integer.
		
		'''
		pass # cpp source

	def ToRound(self) -> cVec2:
		'''
			
		Returns a new vector with this vector's components rounded.
		
		'''
		pass # cpp source

	@staticmethod
	def Abs(_0: cVec2) -> cVec2:
		'''
			
		Returns a vector containing the absolute values of the components.
		
		'''
		pass # cpp source

	@staticmethod
	def Fract(_0: cVec2) -> cVec2:
		'''
			
		Returns the fractional part of the components.
		
		'''
		pass # cpp source

	@staticmethod
	def Angle(_0: cVec2, _1: cVec2) -> float:
		'''
			
		Returns the angle in degrees between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def AreaSigned(t0: cVec2, t1: cVec2, t2: cVec2) -> float:
		'''
			
		Returns the signed area of the triangle formed by t0, t1, t2.
		
		'''
		pass # cpp source

	@staticmethod
	def Ccw(_0: cVec2, _1: cVec2) -> float:
		'''
			
		"Counter-Clockwise" or 2D Cross Product.

		Returns:
			float: The magnitude of the Z component of the cross product (u.x*v.y - u.y*v.x).
		
		'''
		pass # cpp source

	@staticmethod
	def Clamp(Value: cVec2, Lo: cVec2, Hi: cVec2) -> cVec2:
		'''
			
		Clamps a vector between a Low and High range (component-wise).
		
		'''
		pass # cpp source

	@staticmethod
	def Distance(_0: cVec2, _1: cVec2) -> float:
		'''
			
		Calculates the distance between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def DistanceSq(_0: cVec2, _1: cVec2) -> float:
		'''
			
		Calculates the squared distance between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Dot(_0: cVec2, _1: cVec2) -> float:
		'''
			
		Calculates the Dot Product of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp(_0: cVec2, _1: cVec2, _2: float) -> cVec2:
		'''
			
		Linearly interpolates between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp05(_0: cVec2, _1: cVec2) -> cVec2:
		'''
			
		Linearly interpolates between two vectors with factor 0.5.
		
		'''
		pass # cpp source

	@staticmethod
	def Max(_0: cVec2, _1: cVec2) -> cVec2:
		'''
			
		Returns the component-wise maximum of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Min(_0: cVec2, _1: cVec2) -> cVec2:
		'''
			
		Returns the component-wise minimum of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def PerpCw(_0: cVec2) -> cVec2:
		'''
			
		Returns a vector perpendicular to u (Clockwise rotation 90 deg).
		
		'''
		pass # cpp source

	@staticmethod
	def PerpCcw(_0: cVec2) -> cVec2:
		'''
			
		Returns a vector perpendicular to u (Counter-Clockwise rotation 90 deg).
		
		'''
		pass # cpp source

	@staticmethod
	def Reflect(RayDir: cVec2, Normal: cVec2) -> cVec2:
		'''
			
		Reflects a ray direction off a surface normal.
		
		'''
		pass # cpp source

	@staticmethod
	def Refract(RayDir: cVec2, Normal: cVec2, Eta: float) -> cVec2:
		'''
			
		Refracts a ray direction through a surface normal with index of refraction Eta.
		
		'''
		pass # cpp source

	@staticmethod
	def Truncate(u: cVec2, MaxLength: float) -> cVec2:
		'''
			
		Truncates the vector length to MaxLength. Returns a new vector.
		
		'''
		pass # cpp source

	@staticmethod
	def RandRange1() -> cVec2:
		'''
			
		Returns a random vector with components in range [0, 1].
		
		'''
		pass # cpp source

	@staticmethod
	def RandNormal() -> cVec2:
		'''
			
		Returns a random normalized vector.
		
		'''
		pass # cpp source

	@staticmethod
	def Rand(Lo: cVec2, Hi: cVec2) -> cVec2:
		'''
			
		Returns a random vector between Lo and Hi.
		
		'''
		pass # cpp source

	def distance2(self, _0: cVec2) -> float:
		'''
			
		Python-style distance squared.
		
		'''
		pass # cpp source

	def distance(self, _0: cVec2) -> float:
		'''
			
		Python-style distance.
		
		'''
		pass # cpp source

	def DistanceToLineSegSq(self, A: cVec2, B: cVec2, pScale: float = None) -> float:
		'''
			
		Squared distance from this point to a line segment AB.
		
		'''
		pass # cpp source

	@staticmethod
	def SegIntersection(L0: cVec2, L1: cVec2, R0: cVec2, R1: cVec2, l: float = None, r: float = None) -> bool:
		'''
			
		Calculates the intersection of two line segments.
		
		'''
		pass # cpp source

	@staticmethod
	def FromBaryCentric(t0: cVec2, t1: cVec2, t2: cVec2, u: float, v: float) -> cVec2:
		'''
			
		Calculates a position from Barycentric coordinates (u, v) on a triangle.
		
		'''
		pass # cpp source

	@staticmethod
	def FromPolar(Radius: float, Angle: float) -> cVec2:
		'''
			
		Creates a vector from Polar coordinates (Radius, Angle in degrees).
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		 Serialization helpers
		
		'''
		pass # cpp source

	def __repr__(self) -> str:
		pass # cpp source

	Zero: cVec2 = Coat_CPP.cVec2.Zero #: static const cVec2 (T)  
	One: cVec2 = Coat_CPP.cVec2.One #: static const cVec2 (T)  
	Infinity: cVec2 = Coat_CPP.cVec2.Infinity #: static const cVec2 (T)  
	AxisX: cVec2 = Coat_CPP.cVec2.AxisX #: static const cVec2 (T)  
	AxisY: cVec2 = Coat_CPP.cVec2.AxisY #: static const cVec2 (T)  
	AxisNegX: cVec2 = Coat_CPP.cVec2.AxisNegX #: static const cVec2 (T)  
	AxisNegY: cVec2 = Coat_CPP.cVec2.AxisNegY #: static const cVec2 (T)  
	def GetDimension(self) -> int:
		'''
			
		Returns the number of dimensions (2).
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a const pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToPolar(self, Radius: float, Angle: float):
		'''
			
		Converts Cartesian coordinates to Polar (Radius, Angle).
		
		'''
		pass # cpp source

	def ToBaryCentric(self, t0: cVec2, t1: cVec2, t2: cVec2, u: float, v: float) -> float:
		'''
			
		Calculates Barycentric coordinates of this point within triangle t0,t1,t2.
		
		'''
		pass # cpp source

	def IsInsideTri(self, t0: cVec2, t1: cVec2, t2: cVec2) -> bool:
		'''
			
		Checks if this point lies inside the triangle t0,t1,t2.
		
		'''
		pass # cpp source

	def ToString(self, Prec: int = 2) -> cStr:
		'''
			
		Converts the vector to a formatted string.
		
		'''
		pass # cpp source

	def ToNormal(self) -> cVec2:
		'''
			
		Returns a normalized copy of this vector.
		
		'''
		pass # cpp source

	def ToPerpCw(self) -> cVec2:
		'''
			
		Returns a copy rotated 90 degrees Clockwise.
		
		'''
		pass # cpp source

	def ToPerpCcw(self) -> cVec2:
		'''
			
		Returns a copy rotated 90 degrees Counter-Clockwise.
		
		'''
		pass # cpp source

	def AddWithWeight(self, src: cVec2, weight: float):
		'''
			
		 for compatibility with OpenSubdiv ////
		
		'''
		pass # cpp source

	def SetPosition(self, aX: float, aY: float):
		pass # cpp source

	def GetPosition(self) -> float:
		pass # cpp source



class cVec3():
	'''
			
		The 3D-vector, refer it as coat::vec3 in the Core API.
		* This class represents a 3-dimensional vector with float precision components (x, y, z).
		It includes standard vector arithmetic, geometric operations, and transformation utilities.
		
	'''

	x: float #: float (T)  X component of the vector 
	y: float #: float (T)  Y component of the vector 
	z: float #: float (T)  Z component of the vector 
	def __init__(self):
		pass # CPP source

	def __init__(self, S: float) -> any:
		pass # CPP source

	def __init__(self, X: float, Y: float, Z: float):
		pass # CPP source

	def __init__(self, XY: cVec2, Z: float):
		pass # CPP source

	def __init__(self, v: any):
		pass # CPP source

	def __init__(self, v: cVec3):
		pass # CPP source

	def Copy(self, Src: float):
		pass # cpp source

	def SetZero(self):
		'''
			
		Sets the vector to (0, 0, 0).
		
		'''
		pass # cpp source

	def SetOne(self):
		'''
			
		Sets the vector to (1, 1, 1).
		
		'''
		pass # cpp source

	def SetRandRange1(self):
		'''
			
		Sets components to random values in the range [0, 1].
		
		'''
		pass # cpp source

	def Set(self, S: float):
		'''
			
		Sets all components to value S.
		
		'''
		pass # cpp source

	def Set(self, X: float, Y: float, Z: float):
		'''
			
		Sets components individually.
		
		'''
		pass # cpp source

	def Set(self, XY: cVec2, Z: float):
		'''
			
		Sets components from a 2D vector and a Z value.
		
		'''
		pass # cpp source

	def __setitem__(self, Index: int) -> float:
		return super().__setitem__(Index)

	def __getitem__(self, Index: int) -> float:
		return super().__getitem__(Index)

	def __neg__(self) -> cVec3:
		return super().__neg__()

	def __iadd__(self, _0: cVec3) -> cVec3:
		return super().__iadd__(_0)

	def __isub__(self, _0: cVec3) -> cVec3:
		return super().__isub__(_0)

	def __imul__(self, _0: cVec3) -> cVec3:
		return super().__imul__(_0)

	def __imul__(self, _0: float) -> cVec3:
		return super().__imul__(_0)

	def __itruediv__(self, _0: cVec3) -> cVec3:
		return super().__itruediv__(_0)

	def __itruediv__(self, _0: float) -> cVec3:
		return super().__itruediv__(_0)

	def TransformCoordinate(self, _0: any):
		'''
			
		Transforms the vector as a coordinate (position) using a 4x4 matrix.
		
		'''
		pass # cpp source

	def TransformNormal(self, _0: any):
		'''
			
		Transforms the vector as a normal using a 4x4 matrix.
		
		'''
		pass # cpp source

	def TransformNormalTransposed(self, _0: any):
		'''
			
		Transforms the vector as a normal using the transpose of a 4x4 matrix.
		
		'''
		pass # cpp source

	def Transform(self, _0: any):
		'''
			
		Transforms the vector using a 3x3 matrix.
		
		'''
		pass # cpp source

	def __imul__(self, _0: any) -> cVec3:
		return super().__imul__(_0)

	def Rotate(self, _0: any):
		'''
			
		Rotates the vector using a quaternion.
		
		'''
		pass # cpp source

	def __imul__(self, _0: any):
		return super().__imul__(_0)

	def Rotate(self, _0: any):
		'''
			
		Rotates the vector using a rotation object.
		
		'''
		pass # cpp source

	def __imul__(self, _0: any):
		return super().__imul__(_0)

	def __assign__(self, _0: any) -> cVec3:
		return super().__assign__(_0)

	def distance(self, u: cVec3) -> float:
		'''
			
		Calculates the Euclidean distance to another vector.
		
		'''
		pass # cpp source

	def distanceSq(self, u: cVec3) -> float:
		pass # cpp source

	def dot(self, u: cVec3) -> float:
		pass # cpp source

	def cross(self, u: cVec3, v: cVec3):
		pass # cpp source

	def AddWithWeight(self, src: cVec3, weight: float):
		'''
			
		Adds a weighted vector to this vector.
		
		'''
		pass # cpp source

	def SetPosition(self, aX: float, aY: float, aZ: float):
		pass # cpp source

	def GetPosition(self) -> float:
		pass # cpp source

	def __add__(self, _0: cVec3) -> cVec3:
		return super().__add__(_0)

	def __sub__(self, _0: cVec3) -> cVec3:
		return super().__sub__(_0)

	def __mul__(self, _0: cVec3) -> cVec3:
		return super().__mul__(_0)

	def __mul__(self, _0: float) -> cVec3:
		return super().__mul__(_0)

	def __truediv__(self, _0: cVec3) -> cVec3:
		return super().__truediv__(_0)

	def __truediv__(self, _0: float) -> cVec3:
		return super().__truediv__(_0)

	def __mul__(self, _0: any) -> cVec3:
		return super().__mul__(_0)

	def __mul__(self, _0: any) -> cVec3:
		return super().__mul__(_0)

	def __mul__(self, _0: any) -> cVec3:
		return super().__mul__(_0)

	def __eq__(self, _0: cVec3) -> bool:
		return super().__eq__(_0)

	def __ne__(self, _0: cVec3) -> bool:
		return super().__ne__(_0)

	@staticmethod
	def Equals(_0: cVec3, _1: cVec3, Eps: float) -> bool:
		'''
			
		Checks if two vectors are equal within a given epsilon tolerance.
		
		'''
		pass # cpp source

	def Length(self) -> float:
		'''
			
		Returns the length (magnitude) of the vector.
		
		'''
		pass # cpp source

	def Length2(self) -> float:
		'''
			
		Returns the length using fast sqrt approximation.
		
		'''
		pass # cpp source

	def LengthSq(self) -> float:
		'''
			
		Returns the squared length of the vector.
		
		'''
		pass # cpp source

	def LengthM(self) -> float:
		'''
			
		Returns the Manhattan distance (sum of absolute components).
		
		'''
		pass # cpp source

	def Normalize(self) -> float:
		'''
			
		Normalizes the vector. Returns the original length.
		
		'''
		pass # cpp source

	def Normalize2(self) -> float:
		'''
			
		Normalizes the vector using fast sqrt. Returns the squared length.
		
		'''
		pass # cpp source

	def NormalizeSafe(self, Fallback: cVec3 = Coat_CPP.cVec3.AxisZ) -> float:
		'''
			
		Safely normalizes the vector. If length is zero, uses the Fallback vector.
		
		'''
		pass # cpp source

	def FixDegenerateNormal(self) -> bool:
		'''
			
		Fixes degenerate normal vectors (NaN or zero length). Returns true if fixed.
		
		'''
		pass # cpp source

	def FixDenormals(self) -> bool:
		'''
			
		Fixes denormalized floating point numbers in the vector.
		
		'''
		pass # cpp source

	def IsValid(self) -> bool:
		'''
			
		Checks if the vector contains valid numbers (not NaN or Inf).
		
		'''
		pass # cpp source

	def IsNormalized(self, Eps: float) -> bool:
		'''
			
		Checks if the vector is normalized (length is approximately 1).
		
		'''
		pass # cpp source

	def IsZero(self, Eps: float) -> bool:
		'''
			
		Checks if the vector is approximately zero.
		
		'''
		pass # cpp source

	def Round(self):
		'''
			
		Rounds components to the nearest integer.
		
		'''
		pass # cpp source

	@staticmethod
	def Abs(_0: cVec3) -> cVec3:
		'''
			
		Returns a vector with absolute values of the components.
		
		'''
		pass # cpp source

	@staticmethod
	def Angle(_0: cVec3, _1: cVec3) -> float:
		'''
			
		Returns the angle between two vectors in degrees.
		
		'''
		pass # cpp source

	@staticmethod
	def Angle(p1: cVec3, p2: cVec3, p3: cVec3, normal: cVec3) -> float:
		'''
			
		Returns the signed angle between (p1-p2) and (p3-p2) around a normal.
		
		'''
		pass # cpp source

	@staticmethod
	def AreaSigned(t0: cVec3, t1: cVec3, t2: cVec3) -> float:
		'''
			
		Returns the area of the triangle formed by t0, t1, t2.
		
		'''
		pass # cpp source

	@staticmethod
	def BaryCentric(t0: cVec3, t1: cVec3, t2: cVec3, f: float, g: float) -> cVec3:
		'''
			
		Computes a point using barycentric coordinates (f, g).
		
		'''
		pass # cpp source

	@staticmethod
	def Clamp(_0: cVec3, _1: cVec3, _2: cVec3) -> cVec3:
		'''
			
		Clamps a vector between a min and max vector (component-wise).
		
		'''
		pass # cpp source

	@staticmethod
	def Cross(_0: cVec3, _1: cVec3) -> cVec3:
		'''
			
		Computes the cross product of two vectors (static).
		
		'''
		pass # cpp source

	def SetCross(self, _0: cVec3, _1: cVec3):
		'''
			
		Computes the cross product of two vectors and sets the result to this.
		
		'''
		pass # cpp source

	@staticmethod
	def Distance(_0: cVec3, _1: cVec3) -> float:
		'''
			
		Computes the distance between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Distance2(_0: cVec3, _1: cVec3) -> float:
		'''
			
		Computes the distance between two vectors using fast sqrt.
		
		'''
		pass # cpp source

	@staticmethod
	def DistanceSq(_0: cVec3, _1: cVec3) -> float:
		'''
			
		Computes the squared distance between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Dot(_0: cVec3, _1: cVec3) -> float:
		'''
			
		Computes the dot product of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp(_0: cVec3, _1: cVec3, _2: float) -> cVec3:
		'''
			
		Linearly interpolates between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp05(_0: cVec3, _1: cVec3) -> cVec3:
		'''
			
		Linearly interpolates between two vectors with factor 0.5.
		
		'''
		pass # cpp source

	@staticmethod
	def Max(_0: cVec3, _1: cVec3) -> cVec3:
		'''
			
		Returns the component-wise maximum of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Min(_0: cVec3, _1: cVec3) -> cVec3:
		'''
			
		Returns the component-wise minimum of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Reflect(RayDir: cVec3, Normal: cVec3) -> cVec3:
		'''
			
		Reflects a ray direction off a surface with the given normal.
		
		'''
		pass # cpp source

	@staticmethod
	def Refract(RayDir: cVec3, Normal: cVec3, Eta: float) -> cVec3:
		'''
			
		Refracts a ray direction.

		Args:
			Eta (float): Ratio of indices of refraction at the surface interface.
		
		'''
		pass # cpp source

	@staticmethod
	def Slerp(n0: cVec3, n1: cVec3, s: float) -> cVec3:
		'''
			
		Spherical linear interpolation between two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Truncate(u: cVec3, MaxLen: float) -> cVec3:
		'''
			
		Truncates the vector u so its length does not exceed MaxLen.
		
		'''
		pass # cpp source

	@staticmethod
	def RandRange1() -> cVec3:
		'''
			
		Returns a vector with random components in range [0, 1].
		
		'''
		pass # cpp source

	@staticmethod
	def RandNormal() -> cVec3:
		'''
			
		Returns a random normalized vector.
		
		'''
		pass # cpp source

	@staticmethod
	def Rand(Lo: cVec3, Hi: cVec3) -> cVec3:
		'''
			
		Returns a vector with random components in the range [Lo, Hi].
		
		'''
		pass # cpp source

	@staticmethod
	def Project(v1: cVec3, v2: cVec3) -> cVec3:
		'''
			
		Projects vector v1 onto vector v2.
		
		'''
		pass # cpp source

	@staticmethod
	def Perpendicular(v1: cVec3) -> cVec3:
		'''
			
		Returns a vector perpendicular to v1 (arbitrary axis).
		
		'''
		pass # cpp source

	def TriProjectionSolidAngle(self, a: cVec3, b: cVec3, c: cVec3) -> float:
		'''
			
		Calculates the solid angle of the triangle (a, b, c) as seen from this point.
		
		'''
		pass # cpp source

	Zero: cVec3 = Coat_CPP.cVec3.Zero #: static const cVec3 (T)  Constants 
	One: cVec3 = Coat_CPP.cVec3.One #: static const cVec3 (T)  < (0, 0, 0) 
	Infinity: cVec3 = Coat_CPP.cVec3.Infinity #: static const cVec3 (T)  < (1, 1, 1) 
	AxisX: cVec3 = Coat_CPP.cVec3.AxisX #: static const cVec3 (T)  < (Inf, Inf, Inf) 
	AxisY: cVec3 = Coat_CPP.cVec3.AxisY #: static const cVec3 (T)  < (1, 0, 0) 
	AxisZ: cVec3 = Coat_CPP.cVec3.AxisZ #: static const cVec3 (T)  < (0, 1, 0) 
	AxisNegX: cVec3 = Coat_CPP.cVec3.AxisNegX #: static const cVec3 (T)  < (0, 0, 1) 
	AxisNegY: cVec3 = Coat_CPP.cVec3.AxisNegY #: static const cVec3 (T)  < (-1, 0, 0) 
	AxisNegZ: cVec3 = Coat_CPP.cVec3.AxisNegZ #: static const cVec3 (T)  < (0, -1, 0) 
	def GetDimension(self) -> int:
		'''
			
		Returns the dimension of the vector (3).
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a const pointer to the float data.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a pointer to the float data.
		
		'''
		pass # cpp source

	def ToVec2(self) -> cVec2:
		'''
			
		Casts to a const reference of a 2D vector (xy).
		
		'''
		pass # cpp source

	def ToVec2(self) -> cVec2:
		'''
			
		Casts to a reference of a 2D vector (xy).
		
		'''
		pass # cpp source

	def ToString(self, Prec: int = 2) -> cStr:
		'''
			
		Converts the vector to a formatted string.
		
		'''
		pass # cpp source

	def __repr__(self) -> str:
		'''
			
		Python-style representation string.
		
		'''
		pass # cpp source

	def ToAngles(self) -> any:
		'''
			
		Converts the vector to Euler angles (Pitch, Yaw, Roll).
		
		'''
		pass # cpp source

	def GetOrthonormal(self) -> cVec3:
		'''
			
		Returns an arbitrary vector orthonormal to this one.
		
		'''
		pass # cpp source

	def GetOrthonormalPair(self) -> list:
		'''
			
		Returns a pair of vectors orthonormal to this one and each other (forming a basis).
		
		'''
		pass # cpp source

	def MakeOrthonormalTo(self, vec: cVec3):
		'''
			
		Makes this vector orthonormal to the given vector.
		
		'''
		pass # cpp source

	def ToPolarXZ(self, Radius: float, Angle: float):
		'''
			
		Converts to Polar coordinates in the XZ plane.
		
		'''
		pass # cpp source

	@staticmethod
	def FromPolarXZ(Radius: float, Angle: float) -> cVec3:
		'''
			
		Creates a vector from Polar coordinates in the XZ plane.
		
		'''
		pass # cpp source

	def ToBaryCentric(self, t0: cVec3, t1: cVec3, t2: cVec3, f: float, g: float) -> float:
		'''
			
		Computes barycentric coordinates (f, g) of this point relative to triangle (t0, t1, t2).
		
		'''
		pass # cpp source

	def ToNormal(self) -> cVec3:
		'''
			
		Returns a normalized copy of this vector.
		
		'''
		pass # cpp source

	def ToPerps(self, X: cVec3, Y: cVec3):
		'''
			
		Computes two perpendicular vectors (X, Y) to this vector.
		
		'''
		pass # cpp source

	def ToPerp(self) -> cVec3:
		'''
			
		Returns a single perpendicular vector.
		
		'''
		pass # cpp source

	@staticmethod
	def RayTri(RayOrig: cVec3, RayDir: cVec3, t0: cVec3, t1: cVec3, t2: cVec3, u: float, v: float, t: float, BackFaceCull: bool = False) -> bool:
		'''
			
		Ray-Triangle intersection test.
		
		'''
		pass # cpp source

	@staticmethod
	def PointInTriangle(p: cVec3, t0: cVec3, t1: cVec3, t2: cVec3) -> bool:
		'''
			
		Checks if a point p lies within triangle (t0, t1, t2).
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		Serialization state getter.
		
		'''
		pass # cpp source



class cVec4():
	'''
			
		A 4-component vector class (x, y, z, w).
		* This class represents a 4D vector, often used for homogeneous coordinates in 3D graphics,
		colors (RGBA), or generic 4-value mathematical operations.
		Refer to it as coat::vec4 in the Core API.
		
	'''

	x: float #: float (T)  X component of the vector. 
	y: float #: float (T)  Y component of the vector. 
	z: float #: float (T)  Z component of the vector. 
	w: float #: float (T)  W component of the vector. 
	def __init__(self):
		pass # CPP source

	def __init__(self, S: float) -> any:
		pass # CPP source

	def __init__(self, X: float, Y: float, Z: float, W: float):
		pass # CPP source

	def __init__(self, XY: cVec2, Z: float, W: float):
		pass # CPP source

	def __init__(self, XY: cVec2, ZW: cVec2):
		pass # CPP source

	def __init__(self, XYZ: cVec3, W: float):
		pass # CPP source

	def __init__(self, v: cVec4):
		pass # CPP source

	def SetZero(self):
		pass # cpp source

	def Set(self, S: float):
		'''
			
		Sets all components to a scalar value.

		Args:
			S (float): The value to set.
		
		'''
		pass # cpp source

	def Set(self, X: float, Y: float, Z: float, W: float):
		'''
			
		Sets components explicitly.

		Args:
			X (float): The x component.
			Y (float): The y component.
			Z (float): The z component.
			W (float): The w component.
		
		'''
		pass # cpp source

	def Set(self, XY: cVec2, Z: float, W: float):
		'''
			
		Sets components from a 2D vector and scalars.

		Args:
			XY (cVec2): The vector containing x and y.
			Z (float): The z component.
			W (float): The w component.
		
		'''
		pass # cpp source

	def Set(self, XY: cVec2, ZW: cVec2):
		'''
			
		Sets components from two 2D vectors.

		Args:
			XY (cVec2): The vector containing x and y.
			ZW (cVec2): The vector containing z and w.
		
		'''
		pass # cpp source

	def Set(self, XYZ: cVec3, W: float):
		'''
			
		Sets components from a 3D vector and a scalar.

		Args:
			XYZ (cVec3): The vector containing x, y, and z.
			W (float): The w component.
		
		'''
		pass # cpp source

	def Copy(self, pSrc: float):
		'''
			
		Copies components from a raw float array.

		Args:
			pSrc (float): Pointer to an array of at least 4 floats.
		
		'''
		pass # cpp source

	def __setitem__(self, index: int) -> float:
		return super().__setitem__(index)

	def __getitem__(self, index: int) -> float:
		return super().__getitem__(index)

	def __neg__(self) -> cVec4:
		return super().__neg__()

	def __iadd__(self, _0: cVec4) -> cVec4:
		return super().__iadd__(_0)

	def __isub__(self, _0: cVec4) -> cVec4:
		return super().__isub__(_0)

	def __imul__(self, _0: cVec4) -> cVec4:
		return super().__imul__(_0)

	def __imul__(self, _0: float) -> cVec4:
		return super().__imul__(_0)

	def __itruediv__(self, _0: cVec4) -> cVec4:
		return super().__itruediv__(_0)

	def __itruediv__(self, _0: float) -> cVec4:
		return super().__itruediv__(_0)

	def Transform(self, mat: any):
		'''
			
		Transforms this vector by a 4x4 matrix.

		Args:
			mat : The matrix to transform by.
		
		'''
		pass # cpp source

	def __imul__(self, _0: any):
		return super().__imul__(_0)

	def __assign__(self, _0: cVec3) -> cVec4:
		return super().__assign__(_0)

	def __add__(self, _0: cVec4) -> cVec4:
		return super().__add__(_0)

	def __sub__(self, _0: cVec4) -> cVec4:
		return super().__sub__(_0)

	def __mul__(self, _0: cVec4) -> cVec4:
		return super().__mul__(_0)

	def __mul__(self, _0: float) -> cVec4:
		return super().__mul__(_0)

	def __truediv__(self, _0: cVec4) -> cVec4:
		return super().__truediv__(_0)

	def __truediv__(self, _0: float) -> cVec4:
		return super().__truediv__(_0)

	def __mul__(self, _0: any) -> cVec4:
		return super().__mul__(_0)

	def __eq__(self, _0: cVec4) -> bool:
		return super().__eq__(_0)

	def __ne__(self, _0: cVec4) -> bool:
		return super().__ne__(_0)

	@staticmethod
	def Equals(u: cVec4, v: cVec4, Eps: float) -> bool:
		'''
			
		Checks if two vectors are equal within a tolerance.

		Args:
			u (cVec4): First vector.
			v (cVec4): Second vector.
			Eps (float): Epsilon tolerance.
		
		'''
		pass # cpp source

	def Length(self) -> float:
		'''
			
		Calculates the length (magnitude) of the vector.
		
		'''
		pass # cpp source

	def LengthSq(self) -> float:
		'''
			
		Calculates the squared length of the vector (faster than Length).
		
		'''
		pass # cpp source

	def Normalize(self) -> float:
		'''
			
		Normalizes the vector to unit length.

		Returns:
			float: The original length of the vector.
		
		'''
		pass # cpp source

	def NormalizeSafe(self, Fallback: cVec4 = Coat_CPP.cVec4.AxisW) -> float:
		'''
			
		Safely normalizes the vector. If length is close to zero, sets to Fallback.

		Args:
			Fallback (cVec4): The vector to use if this vector is zero-length.

		Returns:
			float: The original length.
		
		'''
		pass # cpp source

	def IsNormalized(self, Eps: float) -> bool:
		'''
			
		Checks if the vector is normalized (length is ~1).
		
		'''
		pass # cpp source

	def IsZero(self, Eps: float) -> bool:
		'''
			
		Checks if the vector is zero (all components ~0).
		
		'''
		pass # cpp source

	@staticmethod
	def Abs(_0: cVec4) -> cVec4:
		'''
			
		Returns a vector containing the absolute values of the input components.
		
		'''
		pass # cpp source

	@staticmethod
	def Dot(_0: cVec4, _1: cVec4) -> float:
		'''
			
		Calculates the dot product of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp(u: cVec4, v: cVec4, s: float) -> cVec4:
		'''
			
		Linear interpolation between two vectors.

		Args:
			u (cVec4): Start vector.
			v (cVec4): End vector.
			s (float): Interpolation factor (0.0 to 1.0).

		Returns:
			cVec4: Interpolated vector.
		
		'''
		pass # cpp source

	@staticmethod
	def Max(_0: cVec4, _1: cVec4) -> cVec4:
		'''
			
		Returns a vector containing the maximum components of two vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def Min(_0: cVec4, _1: cVec4) -> cVec4:
		'''
			
		Returns a vector containing the minimum components of two vectors.
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		 Python binding helpers
		
		'''
		pass # cpp source

	def __repr__(self) -> str:
		pass # cpp source

	Zero: cVec4 = Coat_CPP.cVec4.Zero #: static const cVec4 (T)  
	One: cVec4 = Coat_CPP.cVec4.One #: static const cVec4 (T)  < (0, 0, 0, 0) 
	Infinity: cVec4 = Coat_CPP.cVec4.Infinity #: static const cVec4 (T)  < (1, 1, 1, 1) 
	AxisX: cVec4 = Coat_CPP.cVec4.AxisX #: static const cVec4 (T)  < (Inf, Inf, Inf, Inf) 
	AxisY: cVec4 = Coat_CPP.cVec4.AxisY #: static const cVec4 (T)  < (1, 0, 0, 0) 
	AxisZ: cVec4 = Coat_CPP.cVec4.AxisZ #: static const cVec4 (T)  < (0, 1, 0, 0) 
	AxisW: cVec4 = Coat_CPP.cVec4.AxisW #: static const cVec4 (T)  < (0, 0, 1, 0) 
	AxisNegX: cVec4 = Coat_CPP.cVec4.AxisNegX #: static const cVec4 (T)  < (0, 0, 0, 1) 
	AxisNegY: cVec4 = Coat_CPP.cVec4.AxisNegY #: static const cVec4 (T)  < (-1, 0, 0, 0) 
	AxisNegZ: cVec4 = Coat_CPP.cVec4.AxisNegZ #: static const cVec4 (T)  < (0, -1, 0, 0) 
	AxisNegW: cVec4 = Coat_CPP.cVec4.AxisNegW #: static const cVec4 (T)  < (0, 0, -1, 0) 
	def ToFloatPtr(self) -> float:
		'''
			
		Returns a const pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToVec2(self) -> cVec2:
		'''
			
		Casts this vector to a cVec2 (x, y).
		
		'''
		pass # cpp source

	def ToVec2(self) -> cVec2:
		'''
			
		Casts this vector to a cVec2 (x, y).
		
		'''
		pass # cpp source

	def ToVec3(self) -> cVec3:
		'''
			
		Casts this vector to a cVec3 (x, y, z).
		
		'''
		pass # cpp source

	def ToVec3(self) -> cVec3:
		'''
			
		Casts this vector to a cVec3 (x, y, z).
		
		'''
		pass # cpp source

	def GetDimension(self) -> int:
		'''
			
		Returns the number of dimensions (4).
		
		'''
		pass # cpp source

	def ToString(self, Prec: int = 2) -> cStr:
		'''
			
		Converts the vector to a formatted string.
		
		'''
		pass # cpp source

	def AddWithWeight(self, src: cVec4, weight: float):
		'''
			
		Clears the vector (sets all to 0). OpenSubdiv compat.
		
		'''
		pass # cpp source

	def SetPosition(self, aX: float, aY: float, aZ: float, aW: float):
		pass # cpp source

	def GetPosition(self) -> float:
		pass # cpp source



class cMat3():
	'''
			
		Represents a 3x3 Matrix.
		* Used for 3D linear algebra transformations, primarily rotation and scaling.
		* Stored in row-major order (array of 3 rows).
		* Supports interaction with cVec3, cQuat, and cAngles.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, _0: float, _1: float, _2: float, _3: float, _4: float, _5: float, _6: float, _7: float, _8: float):
		pass # CPP source

	def __init__(self, v: cMat3):
		pass # CPP source

	def Copy(self, Float9: float):
		pass # cpp source

	def CopyTransposed(self, Float9: float):
		'''
			
		Copies 9 floats into the matrix treating input as Column-Major (Transposes).
		
		'''
		pass # cpp source

	def SetZero(self):
		'''
			
		Sets all elements to zero.
		
		'''
		pass # cpp source

	def SetIdentity(self):
		'''
			
		Sets the matrix to Identity (diagonal 1.0, others 0.0).
		
		'''
		pass # cpp source

	def GetRow(self, Index: int) -> cVec3:
		'''
			
		Returns the specified row as a vector (0, 1, or 2).
		
		'''
		pass # cpp source

	def GetRow0(self) -> cVec3:
		pass # cpp source

	def GetRow1(self) -> cVec3:
		pass # cpp source

	def GetRow2(self) -> cVec3:
		pass # cpp source

	def Row(self, Index: int) -> cVec3:
		'''
			
		Returns a mutable reference to the specified row.
		
		'''
		pass # cpp source

	def Row0(self) -> cVec3:
		pass # cpp source

	def Row1(self) -> cVec3:
		pass # cpp source

	def Row2(self) -> cVec3:
		pass # cpp source

	def SetRow(self, Index: int, _1: cVec3):
		'''
			
		Sets the values of a specific row using a vector.
		
		'''
		pass # cpp source

	def SetRow0(self, _0: cVec3):
		pass # cpp source

	def SetRow1(self, _0: cVec3):
		pass # cpp source

	def SetRow2(self, _0: cVec3):
		pass # cpp source

	def SetRow(self, Index: int, X: float, Y: float, Z: float):
		'''
			
		Sets the values of a specific row using floats.
		
		'''
		pass # cpp source

	def SetRow0(self, X: float, Y: float, Z: float):
		pass # cpp source

	def SetRow1(self, X: float, Y: float, Z: float):
		pass # cpp source

	def SetRow2(self, X: float, Y: float, Z: float):
		pass # cpp source

	def GetCol(self, Index: int) -> cVec3:
		'''
			
		Constructs and returns a vector representing the specified column.
		
		'''
		pass # cpp source

	def GetCol0(self) -> cVec3:
		pass # cpp source

	def GetCol1(self) -> cVec3:
		pass # cpp source

	def GetCol2(self) -> cVec3:
		pass # cpp source

	def SetCol(self, Index: int, _1: cVec3):
		'''
			
		Sets the values of a specific column using a vector.
		
		'''
		pass # cpp source

	def SetCol0(self, _0: cVec3):
		pass # cpp source

	def SetCol1(self, _0: cVec3):
		pass # cpp source

	def SetCol2(self, _0: cVec3):
		pass # cpp source

	def SetCol(self, Index: int, X: float, Y: float, Z: float):
		'''
			
		Sets the values of a specific column using floats.
		
		'''
		pass # cpp source

	def SetCol0(self, X: float, Y: float, Z: float):
		pass # cpp source

	def SetCol1(self, X: float, Y: float, Z: float):
		pass # cpp source

	def SetCol2(self, X: float, Y: float, Z: float):
		pass # cpp source

	def SetElem(self, Row: int, Col: int, Value: float):
		'''
			
		Sets a specific element at (Row, Col).
		
		'''
		pass # cpp source

	def GetElem(self, Row: int, Col: int) -> float:
		'''
			
		Returns the value at (Row, Col).
		
		'''
		pass # cpp source

	def Elem(self, Row: int, Col: int) -> float:
		'''
			
		Returns a mutable reference to the element at (Row, Col).
		
		'''
		pass # cpp source

	def __getitem__(self, Row: int) -> cVec3:
		return super().__getitem__(Row)

	def __setitem__(self, Row: int) -> cVec3:
		return super().__setitem__(Row)

	def __call__(self, Row: int, Col: int) -> float:
		return super().__call__(Row, Col)

	def __call__(self, Row: int, Col: int) -> float:
		return super().__call__(Row, Col)

	def Trace(self) -> float:
		'''
			
		Calculates the sum of the diagonal elements.
		
		'''
		pass # cpp source

	def Determinant(self) -> float:
		'''
			
		Calculates the determinant of the matrix.
		
		'''
		pass # cpp source

	def __eq__(self, _0: cMat3) -> bool:
		return super().__eq__(_0)

	@staticmethod
	def Equals(_0: cMat3, _1: cMat3, Eps: float) -> bool:
		'''
			
		Checks equality with a tolerance (Epsilon).
		
		'''
		pass # cpp source

	def IsZero(self, Eps: float) -> bool:
		'''
			
		Checks if all elements are zero (within Eps).
		
		'''
		pass # cpp source

	def IsIdentity(self, Eps: float) -> bool:
		'''
			
		Checks if the matrix is Identity (within Eps).
		
		'''
		pass # cpp source

	def IsSymmetric(self, Eps: float) -> bool:
		'''
			
		Checks if the matrix is symmetric (Matrix == Transpose).
		
		'''
		pass # cpp source

	def IsOrthonormal(self, Eps: float) -> bool:
		'''
			
		Checks if rows are orthogonal and unit length (Pure rotation matrix).
		
		'''
		pass # cpp source

	def __neg__(self) -> cMat3:
		return super().__neg__()

	def __iadd__(self, R: cMat3) -> cMat3:
		return super().__iadd__(R)

	def __isub__(self, R: cMat3) -> cMat3:
		return super().__isub__(R)

	def __imul__(self, R: cMat3) -> cMat3:
		return super().__imul__(R)

	def __imul__(self, _0: float) -> cMat3:
		return super().__imul__(_0)

	def __itruediv__(self, _0: float) -> cMat3:
		return super().__itruediv__(_0)

	def __add__(self, R: cMat3) -> cMat3:
		return super().__add__(R)

	def __sub__(self, R: cMat3) -> cMat3:
		return super().__sub__(R)

	def __mul__(self, R: cMat3) -> cMat3:
		return super().__mul__(R)

	def __mul__(self, _0: float) -> cMat3:
		return super().__mul__(_0)

	def __truediv__(self, _0: float) -> cMat3:
		return super().__truediv__(_0)

	def Add(self, R: cMat3):
		'''
			
		Adds matrix R to this matrix.
		
		'''
		pass # cpp source

	def Sub(self, R: cMat3):
		'''
			
		Subtracts matrix R from this matrix.
		
		'''
		pass # cpp source

	def Mul(self, R: cMat3):
		'''
			
		Multiplies this matrix by matrix R (This = This * R).
		
		'''
		pass # cpp source

	def Mul(self, s: float):
		'''
			
		Multiplies all elements by scalar s.
		
		'''
		pass # cpp source

	Zero: cMat3 = Coat_CPP.cMat3.Zero #: static const cMat3 (T)  Zero matrix constant. 
	Identity: cMat3 = Coat_CPP.cMat3.Identity #: static const cMat3 (T)  Identity matrix constant. 
	@staticmethod
	def Transpose(_0: cMat3) -> cMat3:
		'''
			
		Returns the transpose of matrix M (swaps rows and columns).
		
		'''
		pass # cpp source

	@staticmethod
	def Invert(Fm: cMat3, To: cMat3) -> bool:
		'''
			
		Calculates the inverse of matrix Fm.

		Args:
			Fm (cMat3): Source matrix.
			To (cMat3): Pointer to destination matrix.

		Returns:
			bool: True if successful, False if determinant is too small (singular).
		
		'''
		pass # cpp source

	@staticmethod
	def OrthoNormalize(Src: cMat3) -> cMat3:
		'''
			
		Inverts this matrix in place. Returns false if singular.
		
		'''
		pass # cpp source

	@staticmethod
	def Rotation(Axis: cVec3, Angle: float) -> cMat3:
		'''
			
		Creates a rotation matrix around an arbitrary axis.
		
		'''
		pass # cpp source

	@staticmethod
	def RotationX(Angle: float) -> cMat3:
		'''
			
		Creates a rotation matrix around the X axis.
		
		'''
		pass # cpp source

	@staticmethod
	def RotationY(Angle: float) -> cMat3:
		'''
			
		Creates a rotation matrix around the Y axis.
		
		'''
		pass # cpp source

	@staticmethod
	def RotationZ(Angle: float) -> cMat3:
		'''
			
		Creates a rotation matrix around the Z axis.
		
		'''
		pass # cpp source

	@staticmethod
	def RotationXYZ(Pitch: float, Yaw: float, Roll: float) -> cMat3:
		'''
			
		Creates a rotation matrix from Euler angles (Pitch, Yaw, Roll).
		
		'''
		pass # cpp source

	@staticmethod
	def EulerZYX(eulerX: float, eulerY: float, eulerZ: float) -> cMat3:
		'''
			
		Creates a rotation matrix using ZYX order.
		
		'''
		pass # cpp source

	@staticmethod
	def Scaling(XYZ: float) -> cMat3:
		'''
			
		Creates a uniform scaling matrix.
		
		'''
		pass # cpp source

	@staticmethod
	def Scaling(X: float, Y: float) -> cMat3:
		'''
			
		Creates a 2D scaling matrix (Z scale = 1).
		
		'''
		pass # cpp source

	@staticmethod
	def Scaling(X: float, Y: float, Z: float) -> cMat3:
		'''
			
		Creates a non-uniform 3D scaling matrix.
		
		'''
		pass # cpp source

	@staticmethod
	def Scaling(XY: cVec2) -> cMat3:
		'''
			
		Creates a scaling matrix from a 2D vector.
		
		'''
		pass # cpp source

	@staticmethod
	def Scaling(XYZ: cVec3) -> cMat3:
		'''
			
		Creates a scaling matrix from a 3D vector.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns const pointer to raw data.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns mutable pointer to raw data.
		
		'''
		pass # cpp source

	def ToMat4(self) -> any:
		'''
			
		Converts to a 4x4 matrix (puts this in top-left, Identity elsewhere).
		
		'''
		pass # cpp source

	def ToQuat(self) -> any:
		'''
			
		Converts rotation matrix to Quaternion.
		
		'''
		pass # cpp source

	def ToVectors(self, Forward: cVec3, Right: cVec3 = None, Up: cVec3 = None):
		'''
			
		Extracts basis vectors (Forward, Right, Up) from the matrix.
		Typically assumes rows contain the basis vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def FromVectors(Forward: cVec3, Right: cVec3, Up: cVec3) -> cMat3:
		'''
			
		Constructs a matrix from basis vectors.
		
		'''
		pass # cpp source

	@staticmethod
	def FromForward(Forward: cVec3) -> cMat3:
		'''
			
		Constructs a rotation matrix looking in 'Forward' direction.
		
		'''
		pass # cpp source

	def ToForward(self) -> cVec3:
		'''
			
		Extracts the Forward vector (Row 0).
		
		'''
		pass # cpp source

	def ToRight(self) -> cVec3:
		'''
			
		Extracts the Right vector (Row 1).
		
		'''
		pass # cpp source

	def ToUp(self) -> cVec3:
		'''
			
		Extracts the Up vector (Row 2).
		
		'''
		pass # cpp source

	def ToAngles(self) -> any:
		'''
			
		Converts rotation matrix to Euler angles.
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		 Python serialization support
		
		'''
		pass # cpp source

	def __repr__(self) -> str:
		pass # cpp source



class cMat4():
	'''
			
		A 4x4 Matrix class designed for 3D graphics and linear algebra.
		 *
		This class uses row-major storage (cVec4 m_Rows[4]).
		It supports row-vector multiplication conventions (v' = v * M).
		Translation data is typically stored in the 4th row (Index 3).
		 *
		\note Refer to it as coat::mat4 in the Core API.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, Rotation: cMat3, Translation: cVec3):
		pass # CPP source

	def __init__(self, Scaling: cVec3, Translation: cVec3):
		pass # CPP source

	def __init__(self, _0: float, _1: float, _2: float, _3: float, _4: float, _5: float, _6: float, _7: float, _8: float, _9: float, _10: float, _11: float, _12: float, _13: float, _14: float, _15: float):
		pass # CPP source

	def __init__(self, v: cMat4):
		pass # CPP source

	def Copy(self, Float16: float):
		pass # cpp source

	def CopyTransposed(self, Float16: float):
		'''
			
		Copies data from a float array and transposes it.
		
		'''
		pass # cpp source

	def SetZero(self):
		'''
			
		Sets all elements to zero.
		
		'''
		pass # cpp source

	def SetIdentity(self):
		'''
			
		Sets the matrix to the identity matrix.
		
		'''
		pass # cpp source

	def GetRow(self, Index: int) -> cVec4:
		'''
			
		-
		
		'''
		pass # cpp source

	def GetRow0(self) -> cVec4:
		pass # cpp source

	def GetRow1(self) -> cVec4:
		pass # cpp source

	def GetRow2(self) -> cVec4:
		pass # cpp source

	def GetRow3(self) -> cVec4:
		pass # cpp source

	def Row(self, Index: int) -> cVec4:
		pass # cpp source

	def Row0(self) -> cVec4:
		pass # cpp source

	def Row1(self) -> cVec4:
		pass # cpp source

	def Row2(self) -> cVec4:
		pass # cpp source

	def Row3(self) -> cVec4:
		pass # cpp source

	def SetRow(self, Index: int, _1: cVec4):
		pass # cpp source

	def SetRow0(self, _0: cVec4):
		pass # cpp source

	def SetRow1(self, _0: cVec4):
		pass # cpp source

	def SetRow2(self, _0: cVec4):
		pass # cpp source

	def SetRow3(self, _0: cVec4):
		pass # cpp source

	def SetRow(self, Index: int, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetRow0(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetRow1(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetRow2(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetRow3(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def GetCol(self, Index: int) -> cVec4:
		'''
			
		-
		
		'''
		pass # cpp source

	def GetCol0(self) -> cVec4:
		pass # cpp source

	def GetCol1(self) -> cVec4:
		pass # cpp source

	def GetCol2(self) -> cVec4:
		pass # cpp source

	def GetCol3(self) -> cVec4:
		pass # cpp source

	def SetCol(self, Index: int, _1: cVec4):
		pass # cpp source

	def SetCol0(self, _0: cVec4):
		pass # cpp source

	def SetCol1(self, _0: cVec4):
		pass # cpp source

	def SetCol2(self, _0: cVec4):
		pass # cpp source

	def SetCol3(self, _0: cVec4):
		pass # cpp source

	def SetCol(self, Index: int, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetCol0(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetCol1(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetCol2(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetCol3(self, X: float, Y: float, Z: float, W: float):
		pass # cpp source

	def SetElem(self, Row: int, Col: int, Value: float):
		'''
			
		-
		
		'''
		pass # cpp source

	def GetElem(self, Row: int, Col: int) -> float:
		pass # cpp source

	def Elem(self, Row: int, Col: int) -> float:
		pass # cpp source

	def __getitem__(self, Row: int) -> cVec4:
		return super().__getitem__(Row)

	def __setitem__(self, Row: int) -> cVec4:
		return super().__setitem__(Row)

	def __call__(self, Row: int, Col: int) -> float:
		return super().__call__(Row, Col)

	def __call__(self, Row: int, Col: int) -> float:
		return super().__call__(Row, Col)

	def Trace(self) -> float:
		'''
			
		Calculates the trace (sum of diagonal elements).
		
		'''
		pass # cpp source

	def Determinant(self) -> float:
		'''
			
		Calculates the determinant of the matrix.
		
		'''
		pass # cpp source

	def __eq__(self, _0: cMat4) -> bool:
		return super().__eq__(_0)

	@staticmethod
	def Equals(_0: cMat4, _1: cMat4, Eps: float) -> bool:
		'''
			
		Checks equality with another matrix within a tolerance epsilon.
		
		'''
		pass # cpp source

	def IsZero(self, Eps: float) -> bool:
		'''
			
		Checks if this is a zero matrix.
		
		'''
		pass # cpp source

	def IsIdentity(self, Eps: float) -> bool:
		'''
			
		Checks if this is an identity matrix.
		
		'''
		pass # cpp source

	def IsSymmetric(self, Eps: float) -> bool:
		'''
			
		Checks if the matrix is symmetric (M == M^T).
		
		'''
		pass # cpp source

	def IsOrthonormal(self, Eps: float) -> bool:
		'''
			
		Checks if the matrix is orthonormal (Determinant is 1).
		
		'''
		pass # cpp source

	def __neg__(self) -> cMat4:
		return super().__neg__()

	def __iadd__(self, R: cMat4) -> cMat4:
		return super().__iadd__(R)

	def __isub__(self, R: cMat4) -> cMat4:
		return super().__isub__(R)

	def __imul__(self, R: cMat4) -> cMat4:
		return super().__imul__(R)

	def __imul__(self, _0: float) -> cMat4:
		return super().__imul__(_0)

	def __itruediv__(self, _0: float) -> cMat4:
		return super().__itruediv__(_0)

	def __add__(self, R: cMat4) -> cMat4:
		return super().__add__(R)

	def __sub__(self, R: cMat4) -> cMat4:
		return super().__sub__(R)

	def __mul__(self, R: cMat4) -> cMat4:
		return super().__mul__(R)

	def __mul__(self, _0: float) -> cMat4:
		return super().__mul__(_0)

	def __truediv__(self, _0: float) -> cMat4:
		return super().__truediv__(_0)

	def Add(self, R: cMat4):
		'''
			
		 In-place arithmetic operations
		
		'''
		pass # cpp source

	def Sub(self, R: cMat4):
		pass # cpp source

	def Mul(self, R: cMat4):
		pass # cpp source

	def Mul(self, s: float):
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		pass # cpp source

	def ToString(self, Prec: int = 2) -> cStr:
		'''
			
		Converts the matrix to a formatted string.
		
		'''
		pass # cpp source

	def ToMat3(self) -> cMat3:
		'''
			
		Extracts the upper-left 3x3 matrix.
		
		'''
		pass # cpp source

	def ToNormalMatrix(self) -> cMat3:
		'''
			
		Extracts the normal matrix (usually inverse transpose of upper 3x3).
		
		'''
		pass # cpp source

	def ToQuat(self) -> any:
		'''
			
		Converts the rotation component to a Quaternion.
		
		'''
		pass # cpp source

	def GetTranslation(self) -> cVec3:
		'''
			
		-
		
		'''
		pass # cpp source

	def SetTranslation(self, _0: cVec3):
		pass # cpp source

	def GetScaling(self) -> cVec3:
		pass # cpp source

	def SetScaling(self, _0: cVec3):
		pass # cpp source

	def GetRotation(self) -> any:
		pass # cpp source

	def SetRotation(self, _0: any):
		pass # cpp source

	@staticmethod
	def Transpose(_0: cMat4) -> cMat4:
		'''
			
		Returns the transpose of matrix M.
		
		'''
		pass # cpp source

	@staticmethod
	def Invert(Fm: cMat4, To: cMat4) -> bool:
		'''
			
		Calculates the inverse of Fm and stores it in To. Returns false if singular.
		
		'''
		pass # cpp source

	Zero: cMat4 = Coat_CPP.cMat4.Zero #: static const cMat4 (T)  Inverts this matrix in-place. Returns false if singular. 
	Identity: cMat4 = Coat_CPP.cMat4.Identity #: static const cMat4 (T)  
	@staticmethod
	def Translation(X: float, Y: float) -> cMat4:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Translation(X: float, Y: float, Z: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Translation(XY: cVec2) -> cMat4:
		pass # cpp source

	@staticmethod
	def Translation(XYZ: cVec3) -> cMat4:
		pass # cpp source

	@staticmethod
	def Rotation(Axis: cVec3, Angle: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def RotationX(Angle: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def RotationY(Angle: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def RotationZ(Angle: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def RotationXYZ(Pitch: float, Yaw: float, Roll: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def EulerZYX(eulerX: float, eulerY: float, eulerZ: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def RotationAt(Orig: cVec2, Angle: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def RotationAt(Orig: cVec3, Axis: cVec3, Angle: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Scaling(XYZ: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Scaling(X: float, Y: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Scaling(X: float, Y: float, Z: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Scaling(XY: cVec2) -> cMat4:
		pass # cpp source

	@staticmethod
	def Scaling(XYZ: cVec3) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(OrigX: float, OrigY: float, ScaleXY: float) -> cMat4:
		'''
			
		 Scaling with a pivot point
		
		'''
		pass # cpp source

	@staticmethod
	def ScalingAt(OrigX: float, OrigY: float, ScaleX: float, ScaleY: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec2, ScaleXY: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec2, ScaleX: float, ScaleY: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec2, Scale: cVec2) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec3, ScaleXYZ: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec3, ScaleX: float, ScaleY: float, ScaleZ: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec3, Scale: cVec3) -> cMat4:
		pass # cpp source

	@staticmethod
	def ScalingAt(Orig: cVec3, Dir: cVec3, Scale: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Perspective(YFov: float, AspectWtoH: float, Znear: float, Zfar: float) -> cMat4:
		'''
			
		Creates a perspective projection matrix.
		
		'''
		pass # cpp source

	@staticmethod
	def PerspectiveInf(YFov: float, AspectWtoH: float, Znear: float) -> cMat4:
		'''
			
		Creates an infinite perspective projection matrix (Zfar at infinity).
		
		'''
		pass # cpp source

	@staticmethod
	def Ortho(Width: float, Height: float, Znear: float, Zfar: float) -> cMat4:
		'''
			
		Creates an orthographic projection matrix.
		
		'''
		pass # cpp source

	@staticmethod
	def Ortho(Left: float, Right: float, Bottom: float, Top: float, Znear: float, Zfar: float) -> cMat4:
		pass # cpp source

	@staticmethod
	def Ortho(B: any) -> cMat4:
		pass # cpp source

	@staticmethod
	def CubeViewProjection(Pos: cVec3, Side: int, Radius: float, GL: bool) -> cMat4:
		'''
			
		Creates a view-projection matrix for a specific side of a cube map.
		
		'''
		pass # cpp source

	@staticmethod
	def LookAtViewProjection(LookFrom: cVec3, LookAt: cVec3, FovY: float, AspectYtoH: float, Znear: float, Zfar: float) -> cMat4:
		'''
			
		Creates a LookAt view matrix.
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		-
		
		'''
		pass # cpp source

	def __repr__(self) -> str:
		pass # cpp source



class cRect():
	'''
			
		Represents an axis-aligned 2D rectangle defined by Min and Max points.
		* Coordinate system note: This class typically assumes a standard mathematical 
		coordinate system where Y increases upwards (Top > Bottom), based on the implementation 
		of AlignTop/Bottom.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, v: cRect):
		pass # CPP source

	def __eq__(self, _0: cRect) -> bool:
		return super().__eq__(_0)

	def __ne__(self, _0: cRect) -> bool:
		return super().__ne__(_0)

	@staticmethod
	def Equals(_0: cRect, _1: cRect, Eps: float) -> bool:
		'''
			
		Checks if two rectangles are equal within a tolerance epsilon.

		Args:
			Eps (float): Tolerance for floating point comparison.
		
		'''
		pass # cpp source

	def Set(self, MinX: float, MinY: float, MaxX: float, MaxY: float):
		'''
			
		Sets the rectangle coordinates directly.
		
		'''
		pass # cpp source

	def Set(self, Min: cVec2, Max: cVec2):
		'''
			
		Sets the rectangle coordinates using vectors.
		
		'''
		pass # cpp source

	def x(self) -> float:
		pass # cpp source

	def y(self) -> float:
		pass # cpp source

	def width(self) -> float:
		pass # cpp source

	def height(self) -> float:
		pass # cpp source

	def SetLeft(self, Left: float):
		pass # cpp source

	def AlignLeft(self, X: float):
		pass # cpp source

	def SetTop(self, Top: float):
		'''
			
		Sets the top edge position (resizes height).
		
		'''
		pass # cpp source

	def AlignTop(self, Y: float):
		pass # cpp source

	def SetRight(self, Right: float):
		'''
			
		Sets the right edge position (resizes width).
		
		'''
		pass # cpp source

	def AlignRight(self, X: float):
		pass # cpp source

	def SetBottom(self, Bottom: float):
		'''
			
		Sets the bottom edge position (resizes height).
		
		'''
		pass # cpp source

	def AlignBottom(self, Y: float):
		pass # cpp source

	def AlignInside(self, Parent: cRect):
		'''
			
		Successively aligns right, bottom, left, and top edges to keep this rectangle inside the parent.
		
		'''
		pass # cpp source

	def GetTopLeft(self) -> cVec2:
		'''
			
		 TopLeft
		
		'''
		pass # cpp source

	def SetTopLeft(self, X: float, Y: float):
		pass # cpp source

	def SetTopLeft(self, TopLeft: cVec2):
		pass # cpp source

	def AlignTopLeft(self, X: float, Y: float):
		pass # cpp source

	def AlignTopLeft(self, TopLeft: cVec2):
		pass # cpp source

	def GetTopCenter(self) -> cVec2:
		pass # cpp source

	def AlignTopCenter(self, X: float, Y: float):
		pass # cpp source

	def AlignTopCenter(self, TopCenter: cVec2):
		pass # cpp source

	def GetTopRight(self) -> cVec2:
		pass # cpp source

	def SetTopRight(self, X: float, Y: float):
		pass # cpp source

	def SetTopRight(self, TopRight: cVec2):
		pass # cpp source

	def AlignTopRight(self, X: float, Y: float):
		pass # cpp source

	def AlignTopRight(self, TopRight: cVec2):
		pass # cpp source

	def GetMiddleLeft(self) -> cVec2:
		pass # cpp source

	def AlignMiddleLeft(self, X: float, Y: float):
		pass # cpp source

	def AlignMiddleLeft(self, MiddleLeft: cVec2):
		pass # cpp source

	def GetMiddleCenter(self) -> cVec2:
		pass # cpp source

	def AlignMiddleCenter(self, X: float, Y: float):
		pass # cpp source

	def AlignMiddleCenter(self, MiddleCenter: cVec2):
		pass # cpp source

	def GetMiddleRight(self) -> cVec2:
		pass # cpp source

	def AlignMiddleRight(self, X: float, Y: float):
		pass # cpp source

	def AlignMiddleRight(self, MiddleRight: cVec2):
		pass # cpp source

	def GetBottomLeft(self) -> cVec2:
		pass # cpp source

	def SetBottomLeft(self, X: float, Y: float):
		pass # cpp source

	def SetBottomLeft(self, BottomLeft: cVec2):
		pass # cpp source

	def AlignBottomLeft(self, X: float, Y: float):
		pass # cpp source

	def AlignBottomLeft(self, BottomLeft: cVec2):
		pass # cpp source

	def GetBottomCenter(self) -> cVec2:
		pass # cpp source

	def AlignBottomCenter(self, X: float, Y: float):
		pass # cpp source

	def AlignBottomCenter(self, BottomCenter: cVec2):
		pass # cpp source

	def GetBottomRight(self) -> cVec2:
		pass # cpp source

	def SetBottomRight(self, X: float, Y: float):
		pass # cpp source

	def SetBottomRight(self, BottomRight: cVec2):
		pass # cpp source

	def AlignBottomRight(self, X: float, Y: float):
		pass # cpp source

	def AlignBottomRight(self, BottomRight: cVec2):
		pass # cpp source

	def GetPoint(self, Align: int) -> cVec2:
		pass # cpp source

	def AlignPoint(self, Align: int, X: float, Y: float):
		'''
			
		Moves the rectangle so the point specified by Align is at X, Y.
		
		'''
		pass # cpp source

	def AlignPoint(self, Align: int, With: cVec2):
		pass # cpp source

	def AlignPoint(self, Align: int, Parent: cRect):
		pass # cpp source

	def GetDockingAlign(self, Child: cRect, DockingRegion: cRect = None, RelPos: cVec2 = None) -> int:
		'''
			
		Calculates the docking alignment of a child rectangle relative to this one.

		Args:
			Child (cRect): The inner rectangle to check.
			DockingRegion (cRect): Optional pointer to receive the calculated region.
			RelPos (cVec2): Optional pointer to receive the relative position [-1..1].

		Returns:
			int: A cAlign value indicating the best docking match.
		
		'''
		pass # cpp source

	def GetDockingRegion(self, Child: cRect, Align: int) -> cRect:
		'''
			
		Returns a sub-region rectangle corresponding to the given alignment flag.
		
		'''
		pass # cpp source

	def GetDockingAlign(self, Child: cVec2, DockingRegion: cRect = None, RelPos: cVec2 = None) -> int:
		pass # cpp source

	def GetDockingRegion(self, Child: cVec2, Align: int) -> cRect:
		pass # cpp source

	def GetLeft(self) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	def GetTop(self) -> float:
		pass # cpp source

	def GetRight(self) -> float:
		pass # cpp source

	def GetBottom(self) -> float:
		pass # cpp source

	def GetWidth(self) -> float:
		pass # cpp source

	def GetHeight(self) -> float:
		pass # cpp source

	def SetWidth(self, HoldPoint: int, Width: float):
		pass # cpp source

	def SetHeight(self, HoldPoint: int, Height: float):
		'''
			
		Sets the height, resizing relative to a specific hold point (cAlign).
		
		'''
		pass # cpp source

	def GetSize(self) -> cVec2:
		pass # cpp source

	def SetSize(self, MinX: float, MinY: float, Width: float, Height: float):
		pass # cpp source

	def SetSize(self, Min: cVec2, Size: cVec2):
		pass # cpp source

	def SetSize(self, HoldPoint: int, Width: float, Height: float):
		'''
			
		Sets size while anchoring a specific point of the rectangle.
		
		'''
		pass # cpp source

	def SetSize(self, HoldPoint: int, Size: cVec2):
		pass # cpp source

	def SetSize(self, HoldPoint: int, Side: float):
		pass # cpp source

	def GetCenterX(self) -> float:
		pass # cpp source

	def GetCenterY(self) -> float:
		pass # cpp source

	def AlignCenterX(self, X: float):
		pass # cpp source

	def AlignCenterY(self, Y: float):
		'''
			
		Moves the rectangle vertically to center at Y.
		
		'''
		pass # cpp source

	def Inflate(self, DeltaXY: float):
		'''
			
		Expands the rectangle by Delta in all directions.
		
		'''
		pass # cpp source

	def Inflate(self, DeltaX: float, DeltaY: float):
		'''
			
		Expands the rectangle independently in X and Y.
		
		'''
		pass # cpp source

	def Inflate(self, Delta: cVec2):
		pass # cpp source

	def SetToPoint(self, X: float, Y: float):
		pass # cpp source

	def SetToPoint(self, P: cVec2):
		pass # cpp source

	def ProjectPoint(self, _0: cVec2) -> cVec2:
		pass # cpp source

	def AddPoint(self, X: float, Y: float) -> bool:
		'''
			
		Expands the rectangle to include the given point.

		Returns:
			bool: true if the rectangle was expanded.
		
		'''
		pass # cpp source

	def AddPoint(self, P: cVec2) -> bool:
		pass # cpp source

	def AddRect(self, Rc: cRect) -> bool:
		pass # cpp source

	def Translate(self, DeltaX: float, DeltaY: float):
		'''
			
		Moves the rectangle by the specified delta.
		
		'''
		pass # cpp source

	def Translate(self, Delta: cVec2):
		pass # cpp source

	def Contains(self, X: float, Y: float) -> bool:
		pass # cpp source

	def Contains(self, P: cVec2) -> bool:
		pass # cpp source

	def Contains(self, Rc: cRect) -> bool:
		pass # cpp source

	@staticmethod
	def Union(l: cRect, r: cRect) -> cRect:
		'''
			
		Returns the smallest rectangle containing both inputs.
		
		'''
		pass # cpp source

	@staticmethod
	def Intersect(l: cRect, r: cRect) -> cRect:
		'''
			
		Returns the overlapping area of two rectangles.
		
		'''
		pass # cpp source

	def IntersectsWith(self, Rc: cRect) -> bool:
		'''
			
		Checks if this rectangle overlaps with Rc.
		
		'''
		pass # cpp source

	def Transform(self, R: cMat3):
		pass # cpp source

	def __imul__(self, R: cMat3):
		return super().__imul__(R)

	def Transform(self, T: cMat4):
		'''
			
		Applies a 3D transform (projecting back to w=1) to the rectangle.
		
		'''
		pass # cpp source

	def __imul__(self, T: cMat4):
		return super().__imul__(T)

	def __mul__(self, R: cMat3) -> cRect:
		return super().__mul__(R)

	def __mul__(self, T: cMat4) -> cRect:
		return super().__mul__(T)

	def ToRound(self) -> cRect:
		'''
			
		Returns a rectangle with integer coordinates (rounded).
		
		'''
		pass # cpp source

	def Round(self):
		'''
			
		Rounds the coordinates of this rectangle in place.
		
		'''
		pass # cpp source

	Zero: cRect = Coat_CPP.cRect.Zero #: static const cRect (T)  
	Empty: cRect = Coat_CPP.cRect.Empty #: static const cRect (T)  
	Unit: cRect = Coat_CPP.cRect.Unit #: static const cRect (T)  
	def IsEmpty(self) -> bool:
		'''
			
		Checks if the rectangle is invalid (Min > Max).
		
		'''
		pass # cpp source

	def SetEmpty(self):
		pass # cpp source

	def SetZero(self):
		pass # cpp source

	@staticmethod
	def Inscribe(What: cRect, Where: cRect) -> cRect:
		pass # cpp source



class cBounds():
	'''
			
		Represents an Axis-Aligned Bounding Box (AABB) in 3D space.
		* Defined by a minimum point (min x, min y, min z) and a maximum point (max x, max y, max z).
		Used for collision detection, visibility testing, and spatial partitioning.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, bMin: cVec3, bMax: cVec3):
		pass # CPP source

	def __init__(self, v: any):
		pass # CPP source

	def GetMin(self) -> cVec3:
		pass # cpp source

	def GetMax(self) -> cVec3:
		'''
			
		Returns the maximum corner of the box.
		
		'''
		pass # cpp source

	def GetMin(self) -> cVec3:
		'''
			
		Returns a mutable reference to the minimum corner.
		
		'''
		pass # cpp source

	def GetMax(self) -> cVec3:
		'''
			
		Returns a mutable reference to the maximum corner.
		
		'''
		pass # cpp source

	def Set(self, Min: cVec3, Max: cVec3):
		'''
			
		Sets the bounds using new min and max values.

		Args:
			Min (cVec3): New minimum corner.
			Max (cVec3): New maximum corner.
		
		'''
		pass # cpp source

	def SetMin(self, _0: cVec3):
		'''
			
		Sets the minimum corner.
		
		'''
		pass # cpp source

	def SetMax(self, _0: cVec3):
		'''
			
		Sets the maximum corner.
		
		'''
		pass # cpp source

	def GetSize(self) -> cVec3:
		'''
			
		Calculates the size vector (Max - Min).
		
		'''
		pass # cpp source

	def GetSizeX(self) -> float:
		'''
			
		Returns the width (X axis size).
		
		'''
		pass # cpp source

	def GetSizeY(self) -> float:
		'''
			
		Returns the height (Y axis size).
		
		'''
		pass # cpp source

	def GetSizeZ(self) -> float:
		'''
			
		Returns the depth (Z axis size).
		
		'''
		pass # cpp source

	def GetDiagonal(self) -> float:
		'''
			
		Calculates the length of the diagonal.
		
		'''
		pass # cpp source

	def GetCenter(self) -> cVec3:
		'''
			
		Calculates the center point of the bounds.
		
		'''
		pass # cpp source

	def GetLargestAxis(self) -> int:
		'''
			
		Returns the index of the longest axis.

		Returns:
			int: 0 for X, 1 for Y, 2 for Z.
		
		'''
		pass # cpp source

	def GetShortestAxis(self) -> int:
		'''
			
		Returns the index of the shortest axis.

		Returns:
			int: 0 for X, 1 for Y, 2 for Z.
		
		'''
		pass # cpp source

	def SetEmpty(self):
		'''
			
		Invalidates the bounds by setting Min to MaxValue and Max to -MaxValue.
		
		'''
		pass # cpp source

	def SetZero(self):
		'''
			
		Sets bounds to (0,0,0) -> (0,0,0).
		
		'''
		pass # cpp source

	def IsEmpty(self) -> bool:
		'''
			
		Checks if the bounds are empty (invalid or zero volume).
		
		'''
		pass # cpp source

	Empty: cBounds = Coat_CPP.cBounds.Empty #: static const cBounds (T)  Represents an invalid/empty bounding box. 
	Zero: cBounds = Coat_CPP.cBounds.Zero #: static const cBounds (T)  Represents a zero-sized bounding box at the origin. 
	One: cBounds = Coat_CPP.cBounds.One #: static const cBounds (T)  Represents a box from (-1,-1,-1) to (1,1,1). 
	def AddPoint(self, _0: cVec3) -> bool:
		'''
			
		Expands the bounds to include the given point.

		Returns:
			bool: True if the bounds were expanded.
		
		'''
		pass # cpp source

	def AddBounds(self, _0: any) -> bool:
		'''
			
		Expands the bounds to include another bounding box.

		Returns:
			bool: True if the bounds were expanded.
		
		'''
		pass # cpp source

	def Inflate(self, DeltaX: float, DeltaY: float, DeltaZ: float):
		'''
			
		Expands the bounds by a delta in each direction.
		* Subtracts delta from Min and adds delta to Max.
		
		'''
		pass # cpp source

	def Inflate(self, DeltaXYZ: float):
		'''
			
		Uniform inflation.
		
		'''
		pass # cpp source

	def Inflate(self, Delta: cVec3):
		pass # cpp source

	def Translate(self, _0: cVec2):
		pass # cpp source

	def Translate(self, _0: cVec3):
		'''
			
		Translates the bounds by a 3D vector.
		
		'''
		pass # cpp source

	def DistanceToPointSq(self, p: cVec2) -> float:
		'''
			
		Squared distance from a 2D point to the bounds (0 if inside). 
		\note Ignores Z axis.
		
		'''
		pass # cpp source

	def DistanceToPointSq(self, p: cVec3) -> float:
		'''
			
		Squared distance from a 3D point to the bounds (0 if inside).
		
		'''
		pass # cpp source

	def ContainsPoint(self, _0: cVec2) -> bool:
		'''
			
		Checks if a 2D point is inside the projected 2D bounds.
		
		'''
		pass # cpp source

	def ContainsCircle(self, Center: cVec2, Radius: float) -> bool:
		'''
			
		Checks if a 2D circle is contained within or overlaps the projected bounds.
		
		'''
		pass # cpp source

	def ContainsPoint(self, _0: cVec3) -> bool:
		'''
			
		Checks if a 3D point is inside the bounds.
		
		'''
		pass # cpp source

	def ContainsBounds(self, _0: any) -> bool:
		'''
			
		Checks if another bounding box is fully contained within this one.
		
		'''
		pass # cpp source

	def IntersectsBounds(self, _0: any) -> bool:
		'''
			
		Checks if this box intersects with another box.
		
		'''
		pass # cpp source

	def IntersectsSphere(self, _0: any) -> bool:
		'''
			
		Checks if this box intersects with a sphere.
		
		'''
		pass # cpp source

	def RayIntersection(self, RayOrig: cVec3, RayDir: cVec3, Scale: float) -> bool:
		'''
			
		Checks if a ray intersects the bounds.
		* The ray can intersect the bounds in both directions from the start point.
		If "RayOrig" is inside the bounds it is considered an intersection with "Scale == 0".
		Intersection point is "RayOrig + RayDir * Scale".
		*

		Args:
			RayOrig (cVec3): Ray origin point.
			RayDir (cVec3): Ray direction vector.
			Scale (float): [Out] Distance from origin to intersection.

		Returns:
			bool: True if intersecting.
		
		'''
		pass # cpp source

	def RayIntersection(self, RayOrig: cVec3, RayDir: cVec3, Cross: cVec3 = None) -> bool:
		'''
			
		Helper for RayIntersection that returns the intersection point.

		Args:
			RayOrig (cVec3): Ray origin.
			RayDir (cVec3): Ray direction.
			Cross (cVec3): [Out] Intersection point (optional).

		Returns:
			bool: True if intersecting.
		
		'''
		pass # cpp source

	def LineIntersection(self, RayOrig: cVec3, RayDir: cVec3, Scale: float) -> bool:
		pass # cpp source



class cRotation():
	'''
			
		Represents a rotation defined by an origin (pivot), an axis, and an angle.
		 *
		This class handles rotation logic including conversion to matrices, quaternions,
		and Euler angles. It includes an internal caching mechanism for the rotation matrix
		to optimize repeated access.
		
	'''

	def __init__(self):
		pass # CPP source

	def __init__(self, Orig: cVec3, Axis: cVec3, Angle: float):
		pass # CPP source

	def Set(self, Orig: cVec3, Axis: cVec3, Angle: float) -> cRotation:
		'''
			
		Sets new parameters for the rotation.
		* Invalidates the cached matrix.
		*

		Args:
			Orig (cVec3): The new origin.
			Axis (cVec3): The new axis.
			Angle (float): The new angle.

		Returns:
			cRotation: Reference to this cRotation object.
		
		'''
		pass # cpp source

	def GetOrig(self) -> cVec3:
		'''
			
		Gets the origin of the rotation.

		Returns:
			cVec3: Const reference to the origin vector.
		
		'''
		pass # cpp source

	def GetAxis(self) -> cVec3:
		'''
			
		Gets the axis of the rotation.

		Returns:
			cVec3: Const reference to the axis vector.
		
		'''
		pass # cpp source

	def GetAngle(self) -> float:
		'''
			
		Gets the angle of the rotation.

		Returns:
			float: The angle value.
		
		'''
		pass # cpp source

	def SetOrig(self, Orig: cVec3):
		'''
			
		Sets the origin of the rotation.

		Args:
			Orig (cVec3): The new origin vector.
		
		'''
		pass # cpp source

	def SetAxis(self, Axis: cVec3):
		'''
			
		Sets the axis of the rotation.
		* Invalidates the cached matrix.

		Args:
			Axis (cVec3): The new axis vector.
		
		'''
		pass # cpp source

	def SetAngle(self, Angle: float):
		'''
			
		Sets the angle of the rotation.
		* Invalidates the cached matrix.

		Args:
			Angle (float): The new angle value.
		
		'''
		pass # cpp source

	def ReCalcMatrix(self):
		'''
			
		Forces recalculation of the cached rotation matrix.
		
		'''
		pass # cpp source

	def __neg__(self) -> cRotation:
		return super().__neg__()

	def __imul__(self, s: float) -> cRotation:
		return super().__imul__(s)

	def __itruediv__(self, s: float) -> cRotation:
		return super().__itruediv__(s)

	def __mul__(self, s: float) -> cRotation:
		return super().__mul__(s)

	def __truediv__(self, s: float) -> cRotation:
		return super().__truediv__(s)

	def Normalize180(self) -> cRotation:
		'''
			
		Normalizes the angle to be within [-180, 180] degrees (or radians equivalent).

		Returns:
			cRotation: Reference to this object.
		
		'''
		pass # cpp source

	def Normalize360(self) -> cRotation:
		'''
			
		Normalizes the angle to be within [0, 360] degrees (or radians equivalent).

		Returns:
			cRotation: Reference to this object.
		
		'''
		pass # cpp source

	def ToAngles(self) -> any:
		'''
			
		Converts the rotation to Euler angles.

		Returns:
			any: A cAngles object representing the rotation.
		
		'''
		pass # cpp source

	def ToQuat(self) -> any:
		'''
			
		Converts the rotation to a Quaternion.

		Returns:
			any: A cQuat object representing the rotation.
		
		'''
		pass # cpp source

	def ToMat3(self) -> cMat3:
		'''
			
		Converts the rotation to a 3x3 Matrix.
		* Updates the internal cache if necessary.

		Returns:
			cMat3: Const reference to the cMat3 matrix.
		
		'''
		pass # cpp source

	def ToMat4(self) -> cMat4:
		'''
			
		Converts the rotation to a 4x4 Matrix.

		Returns:
			cMat4: A cMat4 object.
		
		'''
		pass # cpp source

	def ToAngularVelocity(self) -> cVec3:
		'''
			
		Calculates the angular velocity vector.

		Returns:
			cVec3: A cVec3 representing angular velocity.
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		Serialization helper for Python state (pickle support).

		Returns:
			list: A tuple containing the object state.
		
		'''
		pass # cpp source



class cAngles():
	'''
			
		Represents Euler angles for 3D rotations.
		* This class manages rotations using Pitch, Yaw, and Roll components.
		Commonly used for object orientation, camera control, and physics calculations.
		
	'''

	Pitch: float #: float (T)  Rotation around the X-axis (Up/Down) in degrees. 
	Yaw: float #: float (T)  Rotation around the Y-axis (Left/Right) in degrees. 
	Roll: float #: float (T)  Rotation around the Z-axis (Banking/Fall over) in degrees. 
	def __init__(self):
		pass # CPP source

	def __init__(self, Pitch: float, Yaw: float, Roll: float):
		pass # CPP source

	def Set(self, Pitch: float, Yaw: float, Roll: float):
		'''
			
		Sets the angles to new values.

		Args:
			Pitch (float): Rotation around X-axis.
			Yaw (float): Rotation around Y-axis.
			Roll (float): Rotation around Z-axis.
		
		'''
		pass # cpp source

	def SetZero(self):
		'''
			
		Resets all angles to zero.
		
		'''
		pass # cpp source

	def Copy(self, Src: float):
		'''
			
		Copies values from a float array.

		Args:
			Src (float): Pointer to an array of at least 3 floats [Pitch, Yaw, Roll].
		
		'''
		pass # cpp source

	def __setitem__(self, Index: int) -> float:
		return super().__setitem__(Index)

	def __getitem__(self, Index: int) -> float:
		return super().__getitem__(Index)

	def __neg__(self) -> cAngles:
		return super().__neg__()

	def __iadd__(self, _0: cAngles):
		return super().__iadd__(_0)

	def __isub__(self, _0: cAngles):
		return super().__isub__(_0)

	def __imul__(self, _0: float):
		return super().__imul__(_0)

	def __itruediv__(self, _0: float):
		return super().__itruediv__(_0)

	def __add__(self, _0: cAngles) -> cAngles:
		return super().__add__(_0)

	def __sub__(self, _0: cAngles) -> cAngles:
		return super().__sub__(_0)

	def __mul__(self, _0: float) -> cAngles:
		return super().__mul__(_0)

	def __truediv__(self, _0: float) -> cAngles:
		return super().__truediv__(_0)

	def __eq__(self, _0: cAngles) -> bool:
		return super().__eq__(_0)

	def __ne__(self, _0: cAngles) -> bool:
		return super().__ne__(_0)

	@staticmethod
	def Equals(_0: cAngles, _1: cAngles, Eps: float) -> bool:
		'''
			
		Checks if two angles are equal within a given epsilon tolerance.

		Args:
			Eps (float): Tolerance value (default is cMath::Epsilon).

		Returns:
			bool: True if components are within Eps of each other.
		
		'''
		pass # cpp source

	def Length(self) -> float:
		'''
			
		Calculates the length (magnitude) of the angle vector.

		Returns:
			float: Square root of sum of squares.
		
		'''
		pass # cpp source

	def LengthSq(self) -> float:
		'''
			
		Calculates the squared length of the angle vector.

		Returns:
			float: Sum of squares (Pitch^2 + Yaw^2 + Roll^2).
		
		'''
		pass # cpp source

	def Normalize360(self):
		'''
			
		Normalizes the angles to be within the range [0, 360).
		
		'''
		pass # cpp source

	def Normalize180(self):
		'''
			
		Normalizes the angles to be within the range [-180, 180).
		
		'''
		pass # cpp source

	def Round(self):
		'''
			
		Rounds each component to the nearest integer.
		
		'''
		pass # cpp source

	@staticmethod
	def Clamp(u: cAngles, Min: cAngles, Max: cAngles) -> cAngles:
		'''
			
		Clamps angle values between a minimum and maximum range.

		Args:
			u (cAngles): The angle to clamp.
			Min (cAngles): Minimum values.
			Max (cAngles): Maximum values.

		Returns:
			cAngles: The clamped cAngles object.
		
		'''
		pass # cpp source

	@staticmethod
	def Rand(Range: cAngles) -> cAngles:
		'''
			
		Generates random angles within the specified range.

		Args:
			Range (cAngles): Maximum magnitude for each component.

		Returns:
			cAngles: Random angles.
		
		'''
		pass # cpp source

	@staticmethod
	def Angle(l: cAngles, r: cAngles) -> float:
		'''
			
		Calculates the angular difference between two orientations.

		Args:
			l (cAngles): First angle.
			r (cAngles): Second angle.

		Returns:
			float: Angle in degrees.
		
		'''
		pass # cpp source

	@staticmethod
	def Distance(l: cAngles, r: cAngles) -> float:
		'''
			
		Calculates the "distance" between two angles (alias for Angle).

		Args:
			l (cAngles): First angle.
			r (cAngles): Second angle.

		Returns:
			float: Angle in degrees.
		
		'''
		pass # cpp source

	Zero: cAngles = Coat_CPP.cAngles.Zero #: static const cAngles (T)  
	def ToVectors(self, Forward: cVec3, Right: cVec3 = None, Up: cVec3 = None):
		'''
			
		Converts Euler angles to direction vectors (Forward, Right, Up).

		Args:
			Forward (cVec3): Pointer to store the forward vector.
			Right (cVec3): Pointer to store the right vector (optional).
			Up (cVec3): Pointer to store the up vector (optional).
		
		'''
		pass # cpp source

	def ToForward(self) -> cVec3:
		'''
			
		Converts to a forward direction vector.
		
		'''
		pass # cpp source

	def ToRight(self) -> cVec3:
		'''
			
		Converts to a right direction vector.
		
		'''
		pass # cpp source

	def ToUp(self) -> cVec3:
		'''
			
		Converts to an up direction vector.
		
		'''
		pass # cpp source

	def ToMat3(self) -> cMat3:
		'''
			
		Converts angles to a 3x3 rotation matrix.
		
		'''
		pass # cpp source

	def ToMat4(self) -> cMat4:
		'''
			
		Converts angles to a 4x4 rotation matrix.
		
		'''
		pass # cpp source

	def ToQuat(self) -> any:
		'''
			
		Converts angles to a Quaternion.
		
		'''
		pass # cpp source

	def GetDimension(self) -> int:
		'''
			
		Returns the number of components (3).
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToString(self, Prec: int = 2) -> cStr:
		'''
			
		Converts the angles to a string representation.

		Args:
			Prec (int): Decimal precision.

		Returns:
			cStr: String formatted as "Pitch Yaw Roll".
		
		'''
		pass # cpp source

	@staticmethod
	def EnsureShortestPath(l: cAngles, r: cAngles):
		'''
			
		Modifies angles to ensure the interpolation takes the shortest path.
		* Ensures that the difference between components is within [-180, 180].

		Args:
			l (cAngles): Pointer to start angles.
			r (cAngles): Pointer to end angles.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp(l: cAngles, r: cAngles, s: float) -> cAngles:
		'''
			
		Linearly interpolates between two angles.

		Args:
			l (cAngles): Start angle.
			r (cAngles): End angle.
			s (float): Interpolation factor (0.0 to 1.0).

		Returns:
			cAngles: Interpolated angle.
		
		'''
		pass # cpp source



class cQuat():
	'''
			
		Header file for the Quaternion class.
		* Implementation of quaternions for 3D rotations and orientation, 
		including arithmetic operations, interpolation (SLERP, SQUAD), 
		and conversions to/from matrices and Euler angles.
		
	'''

	x: float #: float (T)  
	y: float #: float (T)  < X component of the vector part. 
	z: float #: float (T)  < Y component of the vector part. 
	w: float #: float (T)  < Z component of the vector part. 
	def __init__(self):
		pass # CPP source

	def __init__(self, X: float, Y: float, Z: float, W: float):
		pass # CPP source

	def __init__(self, v: cQuat):
		pass # CPP source

	def SetIdentity(self):
		pass # cpp source

	def SetZero(self):
		'''
			
		Sets all components to zero.
		
		'''
		pass # cpp source

	def IsZero(self, Eps: float) -> bool:
		'''
			
		Checks if the quaternion is zero (within epsilon).

		Args:
			Eps (float): Tolerance for comparison.

		Returns:
			bool: true if all components are close to zero.
		
		'''
		pass # cpp source

	def Set(self, X: float, Y: float, Z: float, W: float):
		'''
			
		Sets the components of the quaternion.
		
		'''
		pass # cpp source

	def Set(self, XYZ: cVec3, W: float):
		'''
			
		Sets the components using a vector and a scalar.
		
		'''
		pass # cpp source

	def __setitem__(self, index: int) -> float:
		return super().__setitem__(index)

	def __getitem__(self, index: int) -> float:
		return super().__getitem__(index)

	def __neg__(self) -> cQuat:
		return super().__neg__()

	@staticmethod
	def Mul(_0: cQuat, _1: cQuat) -> cQuat:
		'''
			
		Multiplies two quaternions.
		* Represents combining two rotations (q0 applied then q1, depending on convention).
		
		'''
		pass # cpp source

	@staticmethod
	def Div(_0: cQuat, _1: cQuat) -> cQuat:
		'''
			
		Divides two quaternions.
		* Equivalent to q0 * Inverse(q1).
		
		'''
		pass # cpp source

	def __iadd__(self, _0: cQuat) -> cQuat:
		return super().__iadd__(_0)

	def __isub__(self, _0: cQuat) -> cQuat:
		return super().__isub__(_0)

	def __imul__(self, _0: cQuat) -> cQuat:
		return super().__imul__(_0)

	def __itruediv__(self, _0: cQuat) -> cQuat:
		return super().__itruediv__(_0)

	def __imul__(self, _0: float) -> cQuat:
		return super().__imul__(_0)

	def __itruediv__(self, _0: float) -> cQuat:
		return super().__itruediv__(_0)

	def __add__(self, _0: cQuat) -> cQuat:
		return super().__add__(_0)

	def __sub__(self, _0: cQuat) -> cQuat:
		return super().__sub__(_0)

	def __mul__(self, _0: cQuat) -> cQuat:
		return super().__mul__(_0)

	def __truediv__(self, _0: cQuat) -> cQuat:
		return super().__truediv__(_0)

	def __mul__(self, _0: float) -> cQuat:
		return super().__mul__(_0)

	def __truediv__(self, _0: float) -> cQuat:
		return super().__truediv__(_0)

	def __eq__(self, _0: cQuat) -> bool:
		return super().__eq__(_0)

	def __ne__(self, _0: cQuat) -> bool:
		return super().__ne__(_0)

	@staticmethod
	def Equals(_0: cQuat, _1: cQuat, Eps: float) -> bool:
		'''
			
		Checks if two quaternions are equal component-wise.
		
		'''
		pass # cpp source

	@staticmethod
	def EqualRotations(_0: cQuat, _1: cQuat, Eps: float) -> bool:
		'''
			
		Checks if two quaternions represent the same rotation.
		* Considers that q and -q represent the same orientation in 3D space.
		
		'''
		pass # cpp source

	@staticmethod
	def SameHemisphere(_0: cQuat, _1: cQuat) -> bool:
		'''
			
		Checks if two quaternions are in the same hemisphere.
		* Based on the dot product sign.
		
		'''
		pass # cpp source

	def Compress(self):
		'''
			
		Compresses the quaternion for storage (e.g., usually for network).
		* Ensures W is positive and then sets it to 0 (assuming reconstruction later).
		
		'''
		pass # cpp source

	def CalcW(self):
		'''
			
		Reconstructs W component assuming a unit quaternion.
		* w = sqrt(1 - x^2 - y^2 - z^2).
		
		'''
		pass # cpp source

	def Length(self) -> float:
		'''
			
		Returns the magnitude (length) of the quaternion.
		
		'''
		pass # cpp source

	def LengthSq(self) -> float:
		'''
			
		Returns the squared magnitude.
		
		'''
		pass # cpp source

	def Normalize(self) -> cQuat:
		'''
			
		Normalizes the quaternion to unit length.

		Returns:
			cQuat: Reference to this quaternion.
		
		'''
		pass # cpp source

	def IsNormalized(self, Eps: float) -> bool:
		'''
			
		Checks if the quaternion is normalized (length is close to 1).
		
		'''
		pass # cpp source

	@staticmethod
	def Conjugate(_0: cQuat) -> cQuat:
		'''
			
		Returns the conjugate of a quaternion (-x, -y, -z, w).
		
		'''
		pass # cpp source

	@staticmethod
	def Dot(_0: cQuat, _1: cQuat) -> float:
		'''
			
		Calculates the dot product of two quaternions.
		
		'''
		pass # cpp source

	@staticmethod
	def Exp(_0: cQuat) -> cQuat:
		'''
			
		Calculates the exponential map.
		
		'''
		pass # cpp source

	@staticmethod
	def Invert(_0: cQuat) -> cQuat:
		'''
			
		Calculates the inverse of the quaternion.
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp(q0: cQuat, q1: cQuat, s: float, ShortestPath: bool = True) -> cQuat:
		'''
			
		Linear Interpolation between two quaternions.

		Args:
			ShortestPath (bool): If true, flips signs to ensure shortest rotational path.
		
		'''
		pass # cpp source

	@staticmethod
	def Ln(_0: cQuat) -> cQuat:
		'''
			
		Calculates the natural logarithm map.
		
		'''
		pass # cpp source

	@staticmethod
	def LnDif(_0: cQuat, _1: cQuat) -> cQuat:
		'''
			
		Calculates the difference in log space.
		
		'''
		pass # cpp source

	@staticmethod
	def Slerp(q0: cQuat, q1: cQuat, s: float, ShortestPath: bool = True) -> cQuat:
		'''
			
		Spherical Linear Interpolation (SLERP).
		* Provides constant speed interpolation along the arc.
		
		'''
		pass # cpp source

	@staticmethod
	def Squad(q1: cQuat, A: cQuat, B: cQuat, C: cQuat, s: float) -> cQuat:
		'''
			
		Spherical Quadrangle Interpolation (SQUAD).
		* Used for smooth spline interpolation between quaternions.
		
		'''
		pass # cpp source

	@staticmethod
	def SquadSetup(q0: cQuat, q1: cQuat, q2: cQuat, q3: cQuat, A: cQuat, B: cQuat, C: cQuat):
		'''
			
		Helper function to calculate intermediate control points for SQUAD.
		
		'''
		pass # cpp source

	Identity: cQuat = Coat_CPP.cQuat.Identity #: static const cQuat (T)  
	Zero: cQuat = Coat_CPP.cQuat.Zero #: static const cQuat (T)  < Identity Quaternion (0, 0, 0, 1). 
	def GetDimension(self) -> int:
		'''
			
		Returns the dimensionality (4).
		
		'''
		pass # cpp source

	def ToAngles(self) -> cAngles:
		'''
			
		 Conversions
		
		'''
		pass # cpp source

	def ToRotation(self) -> cRotation:
		pass # cpp source

	def ToMat3(self) -> cMat3:
		pass # cpp source

	def ToMat4(self) -> cMat4:
		pass # cpp source

	def ToAngularVelocity(self) -> cVec3:
		pass # cpp source

	def ToFloatPtr(self) -> float:
		'''
			
		Returns a pointer to the raw float data.
		
		'''
		pass # cpp source

	def ToFloatPtr(self) -> float:
		pass # cpp source

	def ToStr(self, nPrec: int = 2) -> cStr:
		'''
			
		Converts quaternion to a string representation.
		
		'''
		pass # cpp source

	def __getstate__(self) -> list:
		'''
			
		 Serialization helpers (likely for Python bindings)
		
		'''
		pass # cpp source



class cPlane():
	'''
			
		Class representing a generic plane in 3D space.
		* The plane is defined by the equation: ax + by + cz + d = 0.
		The vector (a, b, c) represents the plane's normal, and d represents 
		the distance factor relative to the origin.
		
	'''

	a: float #: float (T)  \brief X component of the plane normal (A in the plane equation). 
	b: float #: float (T)  \brief Y component of the plane normal (B in the plane equation). 
	c: float #: float (T)  \brief Z component of the plane normal (C in the plane equation). 
	d: float #: float (T)  \brief Distance coefficient (D in the plane equation). 
	def __init__(self):
		pass # CPP source

	def __init__(self, A: float, B: float, C: float, D: float):
		pass # CPP source

	def __init__(self, t0: cVec3, t1: cVec3, t2: cVec3):
		pass # CPP source

	def __init__(self, Pt: cVec3, Normal: cVec3):
		pass # CPP source

	def __init__(self, Normal: cVec3, Offset: float):
		pass # CPP source

	def SetNormalize(self, A: float, B: float, C: float, D: float):
		'''
			
		Sets the plane coefficients and normalizes them.

		Args:
			A (float): X component.
			B (float): Y component.
			C (float): Z component.
			D (float): Distance coefficient.
		
		'''
		pass # cpp source

	def GetNormal(self) -> cVec3:
		'''
			
		Gets the normal vector of the plane.

		Returns:
			cVec3: Const reference to the normal vector (interpreted from a, b, c).
		
		'''
		pass # cpp source

	def SetNormal(self, _0: cVec3):
		'''
			
		Sets the normal vector of the plane.
		
		'''
		pass # cpp source

	def SetOffset(self, Offset: float):
		'''
			
		Sets the offset (distance to origin).
		* Note: Internal 'd' is stored as -Offset.

		Args:
			Offset (float): The distance from the origin.
		
		'''
		pass # cpp source

	def GetOffset(self) -> float:
		pass # cpp source

	def MutableNormal(self) -> cVec3:
		pass # cpp source

	def SetFromPoints(self, t0: cVec3, t1: cVec3, t2: cVec3) -> float:
		'''
			
		Defines the plane from three points.

		Args:
			t0 (cVec3): First point.
			t1 (cVec3): Second point.
			t2 (cVec3): Third point.

		Returns:
			float: The area of the triangle formed by the points (before normalization).
		
		'''
		pass # cpp source

	def SetFromPointAndNormal(self, Pt: cVec3, Normal: cVec3):
		'''
			
		Defines the plane from a point and a normal.

		Args:
			Pt (cVec3): A point on the plane.
			Normal (cVec3): The normal vector.
		
		'''
		pass # cpp source

	def MoveToPoint(self, p: cVec3):
		'''
			
		Moves the plane so that it passes through the specified point.
		* The normal vector remains unchanged.

		Args:
			p (cVec3): The point to move the plane to.
		
		'''
		pass # cpp source

	def Distance(self, p: cVec3) -> float:
		'''
			
		Calculates the signed distance from a point to the plane.

		Args:
			p (cVec3): The point to check.

		Returns:
			float: Positive value if in front, negative if behind, zero if on the plane.
		
		'''
		pass # cpp source

	def ProjectPoint(self, p: cVec3) -> cVec3:
		'''
			
		Projects a point onto the plane.

		Args:
			p (cVec3): The point to project.

		Returns:
			cVec3: The projected point on the plane surface.
		
		'''
		pass # cpp source

	def ProjectVector(self, u: cVec3) -> cVec3:
		'''
			
		Projects a vector onto the plane (removes the component parallel to the normal).

		Args:
			u (cVec3): The vector to project.

		Returns:
			cVec3: The projected vector.
		
		'''
		pass # cpp source

	def MirrorPoint(self, p: cVec3) -> cVec3:
		'''
			
		Mirrors a point across the plane.

		Args:
			p (cVec3): The point to mirror.

		Returns:
			cVec3: The mirrored point position.
		
		'''
		pass # cpp source

	def MirrorVector(self, u: cVec3) -> cVec3:
		'''
			
		Mirrors a vector across the plane.

		Args:
			u (cVec3): The vector to mirror.

		Returns:
			cVec3: The mirrored vector.
		
		'''
		pass # cpp source

	def MirrorOrient(self, q: cQuat) -> cQuat:
		'''
			
		Mirrors a quaternion (orientation) across the plane.

		Args:
			q (cQuat): The orientation to mirror.

		Returns:
			cQuat: The mirrored orientation.
		
		'''
		pass # cpp source

	def FlipNormal(self):
		'''
			
		Inverts the normal of the plane and the distance coefficient.
		* Effectively flips the front and back sides of the plane.
		
		'''
		pass # cpp source

	def BelowPlane(self, B: any, T: cMat4) -> bool:
		'''
			
		Checks if a bounding box is completely on the negative side of the plane.

		Args:
			B : The bounding box.
			T (cMat4): Transformation matrix applied to the bounds.

		Returns:
			bool: True if all vertices are on the back side.
		
		'''
		pass # cpp source

	def ClassifyPoint(self, p: cVec3, Eps: float) -> any:
		'''
			
		Classifies a point's position relative to the plane.

		Args:
			p (cVec3): The point to classify.
			Eps (float): Epsilon tolerance for "on the plane" check.

		Returns:
			any: S_FRONT, S_BACK, or S_ON.
		
		'''
		pass # cpp source

	def ClassifySphere(self, S: any, Eps: float) -> any:
		'''
			
		Classifies a sphere's position relative to the plane.

		Args:
			S : The sphere to classify.
			Eps (float): Epsilon tolerance.

		Returns:
			any: S_FRONT, S_BACK, or S_CROSS.
		
		'''
		pass # cpp source

	def IsFrontFacingTo(self, Dir: cVec3) -> bool:
		'''
			
		Checks if the plane is facing towards a specific direction.

		Args:
			Dir (cVec3): The direction vector.

		Returns:
			bool: True if the plane normal opposes the direction vector (dot product <= 0).
		
		'''
		pass # cpp source

	def RayIntersection(self, RayOrig: cVec3, RayDir: cVec3, pScale: float = None, pCross: cVec3 = None) -> bool:
		'''
			
		Intersects a ray with the plane.

		Args:
			RayOrig (cVec3): Origin of the ray.
			RayDir (cVec3): Direction of the ray.
			pScale (float): [out] Optional pointer to store the distance/scale along the ray.
			pCross (cVec3): [out] Optional pointer to store the intersection point.

		Returns:
			bool: True if an intersection occurs (ray is not parallel).
		
		'''
		pass # cpp source

	def SegIntersection(self, S0: cVec3, S1: cVec3, pCross: cVec3 = None) -> bool:
		'''
			
		Intersects a line segment with the plane.

		Args:
			S0 (cVec3): Start point of the segment.
			S1 (cVec3): End point of the segment.
			pCross (cVec3): [out] Optional pointer to store the intersection point.

		Returns:
			bool: True if the segment intersects the plane.
		
		'''
		pass # cpp source

	def PlaneIntersection(self, P: cPlane, pCross: cVec3 = None, pDir: cVec3 = None) -> bool:
		'''
			
		Intersects this plane with another plane.

		Args:
			P (cPlane): The other plane.
			pCross (cVec3): [out] A point on the intersection line.
			pDir (cVec3): [out] The direction of the intersection line.

		Returns:
			bool: True if planes intersect, False if they are parallel.
		
		'''
		pass # cpp source

	def ToPtr(self) -> float:
		'''
			
		Returns a raw pointer to the plane coefficients.

		Returns:
			float: Pointer to float array {a, b, c, d}.
		
		'''
		pass # cpp source

	def ToPtr(self) -> float:
		'''
			
		Returns a const raw pointer to the plane coefficients.

		Returns:
			float: Const pointer to float array {a, b, c, d}.
		
		'''
		pass # cpp source

	def ToVec4(self) -> cVec4:
		'''
			
		Casts the plane coefficients to a cVec4 reference.

		Returns:
			cVec4: Reference to cVec4.
		
		'''
		pass # cpp source

	def ToVec4(self) -> cVec4:
		'''
			
		Casts the plane coefficients to a const cVec4 reference.

		Returns:
			cVec4: Const reference to cVec4.
		
		'''
		pass # cpp source



class cMath():
	'''
			
		Static helper class providing a wide range of mathematical functions.
		 *
		This class includes constants, trigonometry, interpolation (Linear, Cosine, Hermite, TCB),
		geometric calculations, random number generation, and utility functions for
		floating-point and integer comparisons.
		
	'''

	Pi: float = Coat_CPP.cMath.Pi #: static const float (T)  - 
	TwoPi: float = Coat_CPP.cMath.TwoPi #: static const float (T)  < \brief Value of Pi (3.14159...) 
	HalfPi: float = Coat_CPP.cMath.HalfPi #: static const float (T)  < \brief Value of 2 * Pi 
	QuarterPi: float = Coat_CPP.cMath.QuarterPi #: static const float (T)  < \brief Value of Pi / 2 
	RadsPerDeg: float = Coat_CPP.cMath.RadsPerDeg #: static const float (T)  < \brief Value of Pi / 4 
	DegsPerRad: float = Coat_CPP.cMath.DegsPerRad #: static const float (T)  < \brief Multiplier to convert Degrees to Radians 
	Epsilon: float = Coat_CPP.cMath.Epsilon #: static const float (T)  < \brief Multiplier to convert Radians to Degrees 
	EpsilonSq: float = Coat_CPP.cMath.EpsilonSq #: static const float (T)  < \brief Standard small epsilon for float comparisons 
	SpaceEpsilon: float = Coat_CPP.cMath.SpaceEpsilon #: static const float (T)  < \brief Epsilon squared 
	MatrixEpsilon: float = Coat_CPP.cMath.MatrixEpsilon #: static const float (T)  < \brief Epsilon used for spatial calculations 
	MatrixInvertEpsilon: float = Coat_CPP.cMath.MatrixInvertEpsilon #: static const float (T)  < \brief Epsilon for matrix operations 
	dMatrixInvertEpsilon: float = Coat_CPP.cMath.dMatrixInvertEpsilon #: static const double (T)  < \brief Epsilon for matrix inversion checks (float) 
	dEpsilon: float = Coat_CPP.cMath.dEpsilon #: static const double (T)  < \brief Epsilon for matrix inversion checks (double) 
	Sqrt1Over2: float = Coat_CPP.cMath.Sqrt1Over2 #: static const float (T)  < \brief Standard small epsilon for double comparisons 
	Sqrt1Over3: float = Coat_CPP.cMath.Sqrt1Over3 #: static const float (T)  < \brief Square root of 1/2 
	SecsPerMs: float = Coat_CPP.cMath.SecsPerMs #: static const float (T)  < \brief Square root of 1/3 
	MsPerSec: float = Coat_CPP.cMath.MsPerSec #: static const float (T)  < \brief Seconds per Millisecond (0.001) 
	DoubleMinValue: float = Coat_CPP.cMath.DoubleMinValue #: static const double (T)  < \brief Milliseconds per Second (1000.0) 
	DoubleMaxValue: float = Coat_CPP.cMath.DoubleMaxValue #: static const double (T)  < \brief Minimum representable positive double (0x0010000000000000) 
	FloatMinValue: float = Coat_CPP.cMath.FloatMinValue #: static const float (T)  < \brief Maximum representable double (0x7fefffffffffffff) 
	FloatMaxValue: float = Coat_CPP.cMath.FloatMaxValue #: static const float (T)  < \brief Minimum representable positive float (0x00800000) 
	@staticmethod
	def IsInfinity(Value: float) -> bool:
		'''
			
		< \brief Maximum representable float (0x7f7fffff)
		
		'''
		pass # cpp source

	@staticmethod
	def IsPositiveInfinity(Value: float) -> bool:
		'''
			
		< \brief Checks if value is either positive or negative infinity
		
		'''
		pass # cpp source

	@staticmethod
	def IsNegativeInfinity(Value: float) -> bool:
		'''
			
		< \brief Checks if value is positive infinity
		
		'''
		pass # cpp source

	IntMinValue: int = Coat_CPP.cMath.IntMinValue #: static const int (T)  < \brief Checks if value is negative infinity 
	IntMaxValue: int = Coat_CPP.cMath.IntMaxValue #: static const int (T)  < \brief Minimum integer value (0x80000000) 
	@staticmethod
	def MulDiv(Number: int, Numerator: int, Denominator: int) -> int:
		'''
			
		Multiplies two 32-bit values and then divides the 64-bit result by a third 32-bit value.
		Equivalent to Win32 API "MulDiv".

		Args:
			Number (int): Multiplicand
			Numerator (int): Multiplier
			Denominator (int): Divisor

		Returns:
			int: (Number * Numerator) / Denominator
		
		'''
		pass # cpp source

	@staticmethod
	def Rad(Deg: float) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Deg(Rad: float) -> float:
		'''
			
		< \brief Converts Degrees to Radians (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Rad(Deg: float) -> float:
		'''
			
		< \brief Converts Radians to Degrees (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Deg(Rad: float) -> float:
		'''
			
		< \brief Converts Degrees to Radians (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Sec(Ms: float) -> float:
		'''
			
		< \brief Converts Radians to Degrees (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Ms(Sec: float) -> float:
		'''
			
		< \brief Converts Milliseconds to Seconds
		
		'''
		pass # cpp source

	@staticmethod
	def IsZero(f: float, Eps: float) -> bool:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def IsOne(f: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if float is close to zero
		
		'''
		pass # cpp source

	@staticmethod
	def IsOne(f: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if float is close to one
		
		'''
		pass # cpp source

	@staticmethod
	def IsMinusOne(f: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if double is close to one
		
		'''
		pass # cpp source

	@staticmethod
	def IsZeroToOneExact(f: float) -> bool:
		'''
			
		< \brief Checks if float is close to minus one
		
		'''
		pass # cpp source

	@staticmethod
	def IsZeroToOneEps(f: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if 0.0 <= f <= 1.0
		
		'''
		pass # cpp source

	@staticmethod
	def IsInRange(i: int, Lo: int, Hi: int) -> bool:
		'''
			
		< \brief Checks if -Eps <= f <= 1.0 + Eps
		
		'''
		pass # cpp source

	@staticmethod
	def IsInRangeExact(f: float, Lo: float, Hi: float) -> bool:
		'''
			
		< \brief Checks if Lo <= i <= Hi (integer)
		
		'''
		pass # cpp source

	@staticmethod
	def IsInRangeEps(f: float, Lo: float, Hi: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if Lo <= f <= Hi (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Equals(x: float, y: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if Lo - Eps <= f <= Hi + Eps
		
		'''
		pass # cpp source

	@staticmethod
	def IsValid(f: float) -> bool:
		'''
			
		< \brief Checks if two floats are equal within Epsilon
		
		'''
		pass # cpp source

	@staticmethod
	def IsValid(f: float) -> bool:
		'''
			
		< \brief Checks if float is a valid number (not infinite, inside bounds)
		
		'''
		pass # cpp source

	@staticmethod
	def IsZero(d: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if double is a valid number
		
		'''
		pass # cpp source

	@staticmethod
	def Equals(x: float, y: float, Eps: float) -> bool:
		'''
			
		< \brief Checks if double is close to zero
		
		'''
		pass # cpp source

	@staticmethod
	def Clamp01(f: float) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def ClampRange1(f: float) -> float:
		'''
			
		< \brief Clamps value between 0.0 and 1.0
		
		'''
		pass # cpp source

	@staticmethod
	def ClampRange(f: float, l: float) -> float:
		'''
			
		< \brief Clamps value between -1.0 and 1.0
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp(a: float, b: float, s: float) -> float:
		'''
			
		< \brief Clamps value between -l and l
		
		'''
		pass # cpp source

	@staticmethod
	def Cerp(a: float, b: float, s: float) -> float:
		'''
			
		< \brief Linear Interpolation: a + s * (b - a)
		
		'''
		pass # cpp source

	@staticmethod
	def Lerp05(a: float, b: float) -> float:
		'''
			
		< \brief Cosine Interpolation
		
		'''
		pass # cpp source

	@staticmethod
	def Lerper(Fm: float, To: float, x: float) -> float:
		'''
			
		< \brief Returns midpoint (a + b) * 0.5
		
		'''
		pass # cpp source

	@staticmethod
	def LerperClamp01(Lo: float, Hi: float, x: float) -> float:
		'''
			
		< \brief Inverse Lerp: Returns factor given value x
		
		'''
		pass # cpp source

	@staticmethod
	def MidPointLerp(Start: float, Mid: float, End: float, s: float) -> float:
		'''
			
		< \brief Inverse Lerp clamped to [0, 1]
		
		'''
		pass # cpp source

	@staticmethod
	def Abs(n: int) -> int:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Abs(x: float) -> float:
		'''
			
		< \brief Absolute value (int)
		
		'''
		pass # cpp source

	@staticmethod
	def Abs(x: float) -> float:
		'''
			
		< \brief Absolute value (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Round(x: float) -> float:
		'''
			
		< \brief Absolute value (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Round(x: float) -> float:
		'''
			
		< \brief Round to nearest integer (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Sqrt(x: float) -> float:
		'''
			
		< \brief Round float to specific Type
		
		'''
		pass # cpp source

	@staticmethod
	def Sqrt(x: float) -> float:
		'''
			
		< \brief Square root (float)
		
		'''
		pass # cpp source

	@staticmethod
	def FastInvSqrt(x: float) -> float:
		'''
			
		< \brief Square root (double)
		
		'''
		pass # cpp source

	@staticmethod
	def FastSqrt(x: float) -> float:
		'''
			
		< \brief Fast Inverse Square Root (Quake III algorithm)
		
		'''
		pass # cpp source

	@staticmethod
	def Sin(a: float) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Cos(a: float) -> float:
		'''
			
		< \brief Sine (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Sin(a: float) -> float:
		'''
			
		< \brief Cosine (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Cos(a: float) -> float:
		'''
			
		< \brief Sine (double)
		
		'''
		pass # cpp source

	@staticmethod
	def SinCos(Angle: float, S: float, C: float):
		'''
			
		< \brief Cosine (double)
		
		'''
		pass # cpp source

	@staticmethod
	def SinCos(Angle: float, S: float, C: float):
		'''
			
		< \brief Simultaneous Sine and Cosine (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Tan(a: float) -> float:
		'''
			
		< \brief Simultaneous Sine and Cosine (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Tan(a: float) -> float:
		'''
			
		< \brief Tangent (float)
		
		'''
		pass # cpp source

	@staticmethod
	def ASin(x: float) -> float:
		'''
			
		< \brief Tangent (double)
		
		'''
		pass # cpp source

	@staticmethod
	def ASin(x: float) -> float:
		'''
			
		< \brief ArcSine (float)
		
		'''
		pass # cpp source

	@staticmethod
	def ACos(x: float) -> float:
		'''
			
		< \brief ArcSine (double)
		
		'''
		pass # cpp source

	@staticmethod
	def ACos(x: float) -> float:
		'''
			
		< \brief ArcCosine (float)
		
		'''
		pass # cpp source

	@staticmethod
	def ATan(x: float) -> float:
		'''
			
		< \brief ArcCosine (double)
		
		'''
		pass # cpp source

	@staticmethod
	def ATan(x: float) -> float:
		'''
			
		< \brief ArcTangent (float)
		
		'''
		pass # cpp source

	@staticmethod
	def ATan(y: float, x: float) -> float:
		'''
			
		< \brief ArcTangent (double)
		
		'''
		pass # cpp source

	@staticmethod
	def ATan(y: float, x: float) -> float:
		'''
			
		< \brief ArcTangent2 (y, x) float
		
		'''
		pass # cpp source

	@staticmethod
	def Pow(x: float, y: float) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Pow(x: float, y: float) -> float:
		'''
			
		< \brief Power x^y (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Exp(x: float) -> float:
		'''
			
		< \brief Power x^y (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Exp(x: float) -> float:
		'''
			
		< \brief Exponential e^x (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Ldexp(x: float, exp: int) -> float:
		'''
			
		< \brief Exponential e^x (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Ldexp(x: float, exp: int) -> float:
		'''
			
		< \brief Multiply x by 2^exp (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Frexp(x: float, exp: int) -> float:
		'''
			
		< \brief Multiply x by 2^exp (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Frexp(x: float, exp: int) -> float:
		'''
			
		< \brief Split x into mantissa and exponent (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Log(x: float) -> float:
		'''
			
		< \brief Split x into mantissa and exponent (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Log(x: float) -> float:
		'''
			
		< \brief Natural logarithm (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Floor(f: float) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Ceil(f: float) -> float:
		'''
			
		< \brief Floor value (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Frac(f: float) -> float:
		'''
			
		< \brief Ceiling value (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Floor(d: float) -> float:
		'''
			
		< \brief Fractional part (float)
		
		'''
		pass # cpp source

	@staticmethod
	def Ceil(d: float) -> float:
		'''
			
		< \brief Floor value (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Frac(d: float) -> float:
		'''
			
		< \brief Ceiling value (double)
		
		'''
		pass # cpp source

	@staticmethod
	def Periodic(f: float, Lo: float, Hi: float, nPeriods: int = None) -> float:
		'''
			
		< \brief Fractional part (double)
		
		'''
		pass # cpp source

	@staticmethod
	def IndexForInsert(f: float, Array: float, nCount: int, Stride: int = 0) -> int:
		'''
			
		< \brief Normalizes value to a periodic range
		
		'''
		pass # cpp source

	@staticmethod
	def AngleNormalizeTwoPi(Angle: float) -> float:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def AngleNormalizeTwoPi(Angle: float) -> float:
		'''
			
		< \brief Normalizes angle to [0, 2Pi) (float)
		
		'''
		pass # cpp source

	@staticmethod
	def AngleNormalizePi(Angle: float) -> float:
		'''
			
		< \brief Normalizes angle to [0, 2Pi) (double)
		
		'''
		pass # cpp source

	@staticmethod
	def AngleNormalize360(Angle: float) -> float:
		'''
			
		< \brief Normalizes angle to (-Pi, Pi]
		
		'''
		pass # cpp source

	@staticmethod
	def AngleNormalize180(Angle: float) -> float:
		'''
			
		< \brief Normalizes angle to [0, 360)
		
		'''
		pass # cpp source

	@staticmethod
	def AngleEnsureShortestPath180(Alpha: float, Beta: float):
		'''
			
		< \brief Normalizes angle to (-180, 180]
		
		'''
		pass # cpp source

	@staticmethod
	def AngleDeltaRad(Alpha: float, Beta: float) -> float:
		'''
			
		< \brief Adjusts Beta so transition from Alpha is shortest
		
		'''
		pass # cpp source

	@staticmethod
	def AngleLerpRad(Alpha: float, Beta: float, s: float) -> float:
		'''
			
		< \brief Smallest difference between two angles in radians
		
		'''
		pass # cpp source

	@staticmethod
	def AngleDeltaDeg(Alpha: float, Beta: float) -> float:
		'''
			
		< \brief Interpolates between angles in radians correctly
		
		'''
		pass # cpp source

	@staticmethod
	def AngleLerpDeg(Alpha: float, Beta: float, s: float) -> float:
		'''
			
		< \brief Smallest difference between two angles in degrees
		
		'''
		pass # cpp source

	@staticmethod
	def ClosestPowerOfTwo(X: int) -> int:
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def UpperPowerOfTwo(X: int) -> int:
		'''
			
		< \brief Finds closest power of two
		
		'''
		pass # cpp source

	@staticmethod
	def LowerPowerOfTwo(X: int) -> int:
		'''
			
		< \brief Finds next higher power of two
		
		'''
		pass # cpp source

	@staticmethod
	def IsPowerOfTwo(X: int) -> bool:
		'''
			
		< \brief Finds next lower power of two
		
		'''
		pass # cpp source

	@staticmethod
	def Randomize(Seed: int):
		'''
			
		-
		
		'''
		pass # cpp source

	@staticmethod
	def Rand01() -> float:
		'''
			
		< \brief Seeds the random generator
		
		'''
		pass # cpp source

	@staticmethod
	def RandBool() -> bool:
		'''
			
		< \brief Returns random float in [0, 1]
		
		'''
		pass # cpp source

	@staticmethod
	def RandRange1() -> float:
		'''
			
		< \brief Returns random boolean
		
		'''
		pass # cpp source

	@staticmethod
	def dRand(Lo: float, Hi: float) -> float:
		'''
			
		< \brief Returns random float in [-1, 1]
		
		'''
		pass # cpp source

	@staticmethod
	def Rand(Lo: float, Hi: float) -> float:
		'''
			
		< \brief Returns random double in [Lo, Hi]
		
		'''
		pass # cpp source

	@staticmethod
	def Rand(Lo: int, Hi: int) -> int:
		'''
			
		< \brief Returns random float in [Lo, Hi]
		
		'''
		pass # cpp source

	@staticmethod
	def SignBitSet(i: int) -> int:
		pass # cpp source

	@staticmethod
	def SignBitNotSet(i: int) -> int:
		'''
			
		< \brief Returns non-zero if sign bit is set
		
		'''
		pass # cpp source

	@staticmethod
	def TCBAdjInCoeff(tPrev: float, tCur: float, tNext: float) -> float:
		pass # cpp source

	@staticmethod
	def TCBAdjOutCoeff(tPrev: float, tCur: float, tNext: float) -> float:
		pass # cpp source

	@staticmethod
	def AlignToDword(i: int) -> int:
		pass # cpp source

	@staticmethod
	def Checksum(Src: any, Size: int) -> int:
		'''
			
		< \brief Aligns integer to 4-byte boundary
		
		'''
		pass # cpp source

	@staticmethod
	def Float2Half(Float: float) -> int:
		'''
			
		< \brief Calculates simple checksum
		
		'''
		pass # cpp source

	@staticmethod
	def Half2Float(Half: int) -> float:
		'''
			
		< \brief Convert Float32 to Float16 (Half)
		
		'''
		pass # cpp source

	@staticmethod
	def EndianSwap2(Src: any, Count: int = 1) -> any:
		'''
			
		 b (byte, char)
		
		'''
		pass # cpp source

	@staticmethod
	def EndianSwap4(Src: any, Count: int = 1) -> any:
		'''
			
		< \brief Swap bytes for 16-bit values (Word)
		
		'''
		pass # cpp source

	@staticmethod
	def EndianSwap8(Src: any, Count: int = 1) -> any:
		'''
			
		< \brief Swap bytes for 32-bit values (Dword/Float)
		
		'''
		pass # cpp source

	@staticmethod
	def EndianSwap(Src: any, Format: str, Count: int = 1) -> any:
		'''
			
		< \brief Swap bytes for 64-bit values (Qword/Double)
		
		'''
		pass # cpp source


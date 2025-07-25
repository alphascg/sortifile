# Sortifile

Sortifile is a simple yet powerful command-line tool to automatically sort files in a directory into categorized subfolders based on customizable rules. It supports undo functionality to restore the original file structure, making file organization effortless and reversible.

---

## Features

- Automatically sort files by extension or custom rules  
- Supports recursive scanning of directories  
- Undo the last sorting operation to restore file locations  
- Dry-run mode to preview changes without moving files  
- Customizable rules via JSON configuration  
- Minimal dependencies, easy to install and use

---

## Installation

Install via pip:

```bash
pip install sortifile
```

Or install from source:

```bash
git clone https://github.com/alphascg/sortifile.git
cd sortifile
pip install .
```

## Usage

### Basic usage:
```bash
sortifile /path/to/your/folder
```

### Options
--dry-run, -d
Show what would be moved without actually moving files

--silent, -s
Suppress output messages during the operation

--config, -c
Specify a custom JSON rules file (optional)

### Undo last operation:

If you want to revert the last sorting operation:
```bash
sortifile undo
```

### Configuration Rules

The rules file should be a JSON mapping of file extensions to target folders. This is what the default ruleset looks like:

```json
{
  ".jpg": "Pictures",
  ".jpeg": "Pictures",
  ".png": "Pictures",
  ".gif": "Pictures",
  ".webp": "Pictures",
  ".bmp": "Pictures",
  ".tiff": "Pictures",
  ".svg": "Pictures",

  ".pdf": "Documents",
  ".doc": "Documents",
  ".docx": "Documents",
  ".odt": "Documents",
  ".rtf": "Documents",
  ".txt": "Documents",
  ".md": "Documents",

  ".xls": "Spreadsheets",
  ".xlsx": "Spreadsheets",
  ".ods": "Spreadsheets",
  ".csv": "Spreadsheets",

  ".ppt": "Presentations",
  ".pptx": "Presentations",
  ".odp": "Presentations",

  ".mp3": "Audio",
  ".wav": "Audio",
  ".flac": "Audio",
  ".aac": "Audio",
  ".ogg": "Audio",
  ".m4a": "Audio",

  ".mp4": "Video",
  ".avi": "Video",
  ".mkv": "Video",
  ".mov": "Video",
  ".wmv": "Video",
  ".flv": "Video",
  ".webm": "Video",

  ".zip": "Archives",
  ".rar": "Archives",
  ".7z": "Archives",
  ".tar": "Archives",
  ".gz": "Archives",
  ".bz2": "Archives",
  ".xz": "Archives",

  ".exe": "Programs",
  ".msi": "Programs",
  ".apk": "Programs",
  ".bat": "Programs",
  ".sh": "Programs",
  ".jar": "Programs",

  ".html": "Code",
  ".htm": "Code",
  ".css": "Code",
  ".js": "Code",
  ".ts": "Code",
  ".php": "Code",
  ".py": "Code",
  ".java": "Code",
  ".c": "Code",
  ".cpp": "Code",
  ".cs": "Code",
  ".rb": "Code",
  ".go": "Code",
  ".rs": "Code",
  ".json": "Code",
  ".xml": "Code",
  ".yml": "Code",
  ".yaml": "Code",

  ".iso": "Disk Images",
  ".img": "Disk Images",

  ".log": "Logs",
  
  ".properties": "Configuration",
  ".ini": "Configuration",
  ".cfg": "Configuration",
  ".conf": "Configuration"
}
```

If a file's extension is not found in the rules, it will be moved to an Others folder.

## License

MIT License - see the LICENSE file for details.

## Author
alphascg - [GitHub](https://github.com/alphascg)

## Contribute

Contributions, issues, and feature requests are welcome!
Feel free to check [issues page](https://github.com/alphascg/sortifile/issues).

## Disclaimer
This tool is provided “as is” without warranty of any kind. Use at your own risk.
##

If you read the whole README, you are are breathtaking!
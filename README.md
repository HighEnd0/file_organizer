# 📂 File Organizer

**A powerful and simple Python script to automatically organize your messy folders (like Downloads or Desktop) by grouping files into categories based on their extensions.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## ✨ Features

- **Automatic Sorting:** Groups files into 19+ predefined categories (Images, Videos, Documents, Code, etc.).
- **Dry Run Mode:** Preview what the script will do *before* actually moving any files. Safe and reliable.
- **Error Handling:** Gracefully handles permission errors, missing files, and file conflicts without crashing.
- **Statistics Report:** Displays a detailed summary of how many files were moved to each category.
- **Highly Customizable:** Easily add or remove categories and file extensions in the `categories` dictionary.

## 🚀 Quick Start

**1. Clone the repository**
```bash
git clone https://github.com/HighEnd0/file_organizer.git
cd file_organizer
```

**2. Run the script**
```bash
python file_organizer.py
```

**3. Follow the prompt**
The script will ask:
`do you want to actually move your files? (y/n):`

- Type `y` to **actually move** the files.
- Type `n` to run in **Dry Run mode** (simulate the process).

## 📊 Example Output

```text
--- Example with Dry Run (n) ---
do you want to actually move your files? (y/n): n
[DRY RUN] would move: test.jpg -> Images
[DRY RUN] would move: test.pdf -> Documents
[DRY RUN] would move: song.mp3 -> Music
[DRY RUN] would move: unknown.xyz -> Others

--- Example with Real Move (y) ---
do you want to actually move your files? (y/n): y
Moved: test.jpg -> Images
Moved: test.pdf -> Documents
Moved: song.mp3 -> Music
Moved: unknown.xyz -> Others

--- Report ---
Images: 1 files
Documents: 1 files
Music: 1 files
Others: 1 files
```

## ⚙️ Customization

You can easily add new categories or extensions by modifying the `categories` dictionary at the top of the script:

```python
categories = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    # Add your own categories here!
}
```

## 📋 Supported Categories

The script comes pre-configured with **19+ categories**, including:

| Category | Example Extensions |
| :--- | :--- |
| Images | `.jpg`, `.png`, `.gif`, `.bmp`, `.svg` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm` |
| Music | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg` |
| Documents | `.pdf`, `.docx`, `.txt`, `.odt`, `.rtf` |
| Spreadsheets | `.xls`, `.xlsx`, `.csv`, `.ods` |
| Presentations | `.ppt`, `.pptx`, `.odp`, `.key` |
| eBooks | `.epub`, `.mobi`, `.azw`, `.djvu` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Programs | `.exe`, `.msi`, `.apk`, `.deb`, `.dmg` |
| Code | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp` |
| Fonts | `.ttf`, `.otf`, `.woff`, `.woff2` |
| Databases | `.db`, `.sqlite`, `.mdb`, `.accdb` |
| 3D Models | `.obj`, `.fbx`, `.stl`, `.blend`, `.3ds` |
| Disk Images | `.iso`, `.img`, `.vhd`, `.vmdk` |
| Torrents | `.torrent`, `.magnet` |
| Subtitles | `.srt`, `.sub`, `.ass`, `.vtt` |
| System & Config | `.log`, `.cfg`, `.conf`, `.reg`, `.dll` |
| Java | `.jar`, `.war`, `.ear` |
| Plugins | `.crx`, `.xpi`, `.vsix`, `.whl` |
| Others | *(any unknown extension)* |

## 🛠️ Requirements

- Python 3.10 or higher
- No external libraries required! (Uses built-in `pathlib` and `shutil`)

## 📖 Usage

1. Open the script and modify the `downloads` path to point to the folder you want to organize:
   ```python
   downloads = Path.home() / "Desktop" / "your_target_folder"
   ```
2. Run the script:
   ```bash
   python file_organizer.py
   ```
3. The script will ask if you want to actually move the files. Follow the prompt.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👤 Author

- **HighEnd0** - [https://github.com/HighEnd0](https://github.com/HighEnd0)

## 📄 License

This project is open-source and available under the **

MIT License**. See the `LICENSE` file for more details.
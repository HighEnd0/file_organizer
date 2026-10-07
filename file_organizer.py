from pathlib import Path
import shutil

categories = {
    # تصاویر (Image)
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
        ".webp", ".svg", ".ico", ".heic", ".heif", ".raw", ".cr2",
        ".nef", ".arw", ".dng", ".psd", ".ai", ".eps", ".indd"
    ],

    # فیلم و ویدیو (Video)
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
        ".m4v", ".mpg", ".mpeg", ".3gp", ".ts", ".vob", ".ogv",
        ".rm", ".rmvb", ".asf", ".divx"
    ],

    # صدا و موسیقی (Audio)
    "Music": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a",
        ".opus", ".aiff", ".alac", ".ape", ".mid", ".midi", ".amr"
    ],

    # اسناد متنی (Documents)
    "Documents": [
        ".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".tex",
        ".md", ".pages", ".wpd", ".wps", ".abw"
    ],

    # صفحه‌گسترده (Spreadsheets)
    "Spreadsheets": [
        ".xls", ".xlsx", ".xlsm", ".xlsb", ".ods", ".csv", ".tsv",
        ".numbers", ".dif", ".sxc"
    ],

    # ارائه‌ها (Presentations)
    "Presentations": [
        ".ppt", ".pptx", ".pptm", ".odp", ".key", ".sxi"
    ],

    # کتاب الکترونیکی (eBooks)
    "eBooks": [
        ".epub", ".mobi", ".azw", ".azw3", ".fb2", ".lit", ".prc",
        ".djvu", ".cbz", ".cbr"
    ],

    # فایل‌های فشرده (Archives)
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso",
        ".cab", ".tgz", ".lz", ".lzma", ".z", ".zipx", ".jar"
    ],

    # برنامه‌ها و نصب‌کننده‌ها (Programs)
    "Programs": [
        ".exe", ".msi", ".bat", ".cmd", ".com", ".app", ".apk",
        ".appx", ".deb", ".rpm", ".dmg", ".pkg", ".sh"
    ],

    # کدهای برنامه‌نویسی (Code)
    "Code": [
        ".py", ".pyw", ".js", ".jsx", ".ts", ".tsx", ".html", ".htm",
        ".css", ".scss", ".sass", ".less", ".php", ".java", ".class",
        ".c", ".cpp", ".h", ".hpp", ".cs", ".go", ".rs", ".rb",
        ".swift", ".kt", ".kts", ".lua", ".pl", ".r", ".m",
        ".sql", ".json", ".xml", ".yaml", ".yml", ".toml", ".ini",
        ".ipynb", ".vue", ".svelte"
    ],

    # فونت‌ها (Fonts)
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon", ".fnt"
    ],

    # پایگاه داده (Databases)
    "Databases": [
        ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".dbf",
        ".frm", ".myd", ".myi", ".sql", ".bak"
    ],

    # فایل‌های سه‌بعدی و طراحی (3D & Design)
    "3D_Models": [
        ".obj", ".fbx", ".stl", ".blend", ".3ds", ".dae", ".ply",
        ".max", ".ma", ".mb", ".c4d", ".skp", ".step", ".stp",
        ".iges", ".igs"
    ],

    # فایل‌های دیسک ایمیج (Disk Images)
    "Disk_Images": [
        ".iso", ".img", ".vhd", ".vhdx", ".vmdk", ".dmg", ".bin",
        ".cue", ".nrg", ".mdf", ".mds"
    ],

    # فایل‌های تورنت (Torrents)
    "Torrents": [
        ".torrent", ".magnet"
    ],

    # زیرنویس‌ها (Subtitles)
    "Subtitles": [
        ".srt", ".sub", ".ass", ".ssa", ".vtt", ".sbv", ".smi"
    ],

    # فایل‌های سیستمی و تنظیمات (System & Config)
    "System_Config": [
        ".log", ".cfg", ".conf", ".config", ".reg", ".sys", ".dll",
        ".dat", ".tmp", ".cache", ".pid", ".lock"
    ],

    # فایل‌های اجرایی جاوا (Java)
    "Java": [
        ".jar", ".war", ".ear"
    ],

    # پلاگین‌ها و افزونه‌ها (Plugins)
    "Plugins": [
        ".crx", ".xpi", ".vsix", ".whl", ".egg"
    ],

    # دسته ناشناخته (Others)
    "Others": []
}

stat = {}
downloads = Path.home() / "Desktop" / "test_organizer"

answer = input("do you want to actually move your files? (y/n): ")
if answer == "y":
    dry_run = False
else:
    dry_run = True

for file in downloads.iterdir():
    try:
        if file.is_file():
            for folder, extentions in categories.items():
                if file.suffix.lower() in extentions:
                    target_folder = downloads / folder
                    target_folder.mkdir(exist_ok=True)
                    if dry_run:
                        print(f"[DRY RUN] would move: {file.name} -> {folder}")
                    else:
                        shutil.move(str(file), str(target_folder / file.name))
                    stat[folder] = stat.get(folder, 0) + 1
                    break
            else:
                target_folder = downloads / "Others"
                target_folder.mkdir(exist_ok=True)
                if dry_run:
                    print(f"unkown extension: {file.name} -> {folder}")
                else:
                    shutil.move(str(file), str(target_folder / file.name))
                stat["Others"] = stat.get("Others", 0) + 1
    except PermissionError:
        print(f" دسترسی به {file.name} وجود ندارد")
        continue
    except FileNotFoundError:
        print(f"فایل {file.name} پیدا نشد")
        continue
    except FileExistsError:
        print(f"فایل {file.name} از قبل در مسیر وجود دارد")
        continue

print("\n--- Report ---")
for folder, count in stat.items():
    print(f"{folder}: {count} files")

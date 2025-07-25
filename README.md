# 🐸 FrogsFantomeConverter

A simple drag-and-drop tool to convert League of Legends custom skin folders into .fantome files for easy installation with cslol-manager.

## 🎯 What it does

FrogsFantomeConverter takes folders containing custom League of Legends skins and converts them into .fantome files (which are just renamed zip files) that can be easily installed using cslol-manager.

## ✨ Features

- **🖱️ Drag & Drop**: Simply drag your skin folders onto the executable
- **📁 Batch Processing**: Converts all subfolders in a directory at once
- **🔄 Non-destructive**: Keeps your original folders intact
- **⚡ Fast**: Quick zip compression with progress feedback
- **🎨 Custom Icon**: Features a festive cat mascot
- **🚀 Standalone**: No Python installation required

## 🚀 How to Use

### Method 1: Drag & Drop (Recommended)
1. Download `FrogsFantomeConverter.exe` from the releases
2. Drag your main skin folder (containing multiple skin subfolders) onto the executable
3. Watch the magic happen! Each subfolder becomes a .fantome file
4. Install the .fantome files using cslol-manager

### Method 2: Manual Mode
1. Run `FrogsFantomeConverter.exe` directly
2. Enter the path to your folder containing skin subfolders
3. The tool will convert all subfolders to .fantome files

## 📂 Example Usage

**Before:**
```
MyCustomSkins/
├── ArcaneJinx/
│   ├── assets/
│   └── META/
├── ProjectYasuo/
│   ├── assets/
│   └── META/
└── StarGuardianLux/
    ├── assets/
    └── META/
```

**After:**
```
MyCustomSkins/
├── ArcaneJinx/
├── ArcaneJinx.fantome          ← New!
├── ProjectYasuo/
├── ProjectYasuo.fantome        ← New!
├── StarGuardianLux/
└── StarGuardianLux.fantome     ← New!
```

## 🛠️ Technical Details

- **Language**: Python 3.13
- **Compression**: ZIP with DEFLATED compression
- **File Format**: .fantome (renamed .zip files)
- **Platform**: Windows (built with PyInstaller)
- **Dependencies**: None (standalone executable)

## 📋 Requirements

- Windows 10/11
- No additional software required (standalone executable)

## 🔧 Building from Source

If you want to build the executable yourself:

1. **Clone the repository**
   ```bash
   git clone https://github.com/FrogCsLoL/FrogsFantomeConverter.git
   cd FrogsFantomeConverter
   ```

2. **Install dependencies**
   ```bash
   pip install pyinstaller
   ```

3. **Build the executable**
   ```bash
   python build_exe.py
   ```

4. **Find your executable**
   The built executable will be in the `dist/` folder as `FrogsFantomeConverter.exe`

## 📁 Project Structure

```
FrogsFantomeConverter/
├── folder_to_fantome_converter.py  # Main script
├── build_exe.py                    # Build script for creating executable
├── stricker.ico                    # Custom icon file
├── dist/                          # Built executable location
│   └── FrogsFantomeConverter.exe
└── README.md                      # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This tool is for educational purposes and personal use. Make sure you have the right to use any custom skins you're converting. Always respect the intellectual property rights of skin creators and Riot Games.

## 🎮 Related Projects

- [cslol-manager](https://github.com/LeagueToolkit/cslol-manager) - The League of Legends skin manager this tool is designed to work with
- [LeagueToolkit](https://github.com/LeagueToolkit) - Collection of tools for League of Legends modding

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/FrogsFantomeConverter/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide as much detail as possible about your setup and the error

---

Made with ❤️ for the League of Legends modding community

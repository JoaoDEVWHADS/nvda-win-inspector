import zipfile
import os

OUTPUT_FILE = "WindowInspector.nvda-addon"
SOURCE_DIR = "addon"

def create_addon():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        
    with zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, SOURCE_DIR)
                zf.write(abs_path, rel_path)
                print(f"Adding {rel_path}")

    print(f"Created {OUTPUT_FILE}")

if __name__ == "__main__":
    create_addon()

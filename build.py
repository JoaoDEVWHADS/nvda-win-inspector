import zipfile
import os
import subprocess

OUTPUT_FILE = "WindowInspector.nvda-addon"
SOURCE_DIR = "addon"

def compile_translations():
    locale_dir = os.path.join(SOURCE_DIR, "locale")
    if not os.path.exists(locale_dir):
        return
    print("Compiling translations...")
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith(".po"):
                po_path = os.path.join(root, file)
                mo_path = po_path[:-3] + ".mo"
                try:
                    subprocess.run(["msgfmt", "-o", mo_path, po_path], check=True)
                    print(f"  ✓ Compiled {po_path} -> {mo_path}")
                except Exception as e:
                    print(f"  ✗ Failed to compile {po_path}: {e}")

def create_addon():
    compile_translations()
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        
    with zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                if file.endswith(".po"):
                    continue
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, SOURCE_DIR)
                zf.write(abs_path, rel_path)
                print(f"Adding {rel_path}")

    print(f"Created {OUTPUT_FILE}")

if __name__ == "__main__":
    create_addon()

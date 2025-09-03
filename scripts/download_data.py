"""
Downloads the Kaggle dataset 'wosaku/crime-in-vancouver' to data/raw/crime.csv.
If you already placed crime.csv there, this script will skip downloading.
"""
import zipfile, os, subprocess, shutil
from scripts.utils import get_logger, load_config, ensure_dirs, file_exists

logger = get_logger("download")

def main():
    cfg = load_config()
    raw_csv = cfg["paths"]["raw"]
    raw_dir = cfg["paths"]["raw_dir"]
    ensure_dirs(raw_csv)

    if file_exists(raw_csv):
        logger.info(f"Found existing raw CSV at {raw_csv}. Skipping download.")
        return

    # Try Kaggle API
    try:
        logger.info("Downloading via Kaggle API...")
        subprocess.check_call([
            "kaggle", "datasets", "download",
            "-d", "wosaku/crime-in-vancouver",
            "-p", raw_dir, "--force"
        ])
        # Unzip whatever was downloaded
        for f in os.listdir(raw_dir):
            if f.endswith(".zip"):
                with zipfile.ZipFile(os.path.join(raw_dir, f)) as zf:
                    zf.extractall(raw_dir)
                os.remove(os.path.join(raw_dir, f))
        # Find a CSV (some zips contain a named CSV)
        candidates = [f for f in os.listdir(raw_dir) if f.lower().endswith(".csv")]
        if not candidates:
            raise FileNotFoundError("No CSV found in downloaded files.")
        # Standardize name
        src = os.path.join(raw_dir, candidates[0])
        shutil.move(src, raw_csv)
        logger.info(f"Saved raw CSV to {raw_csv}")
    except Exception as e:
        logger.warning(
            "Kaggle download failed. "
            "Manually download CSV from Kaggle and place it at data/raw/crime.csv. "
            f"Reason: {e}"
        )

if __name__ == "__main__":
    main()

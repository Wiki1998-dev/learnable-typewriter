import argparse
from pathlib import Path

from learnable_typewriter.utils.rocft import ROCFTScorer


def main():
    parser = argparse.ArgumentParser(description="Score ROCFT drawings")
    parser.add_argument("reference", help="Path to reference ROCFT figure")
    parser.add_argument("drawing", help="Path to drawing image or folder")
    args = parser.parse_args()

    scorer = ROCFTScorer(args.reference)
    drawing_path = Path(args.drawing)

    if drawing_path.is_dir():
        for img_path in drawing_path.glob("*.png"):
            print(f"{img_path.name}\t{scorer(str(img_path)):.2f}")
    else:
        score = scorer(str(drawing_path))
        print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()

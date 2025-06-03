import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

class ROCFTScorer:
    """Utility class to compute an automatic similarity score for the
    Rey-Osterrieth Complex Figure Test.

    This implementation is a lightweight approximation of the manual
    scoring procedure. It compares a drawing against a reference image
    using structural similarity (SSIM). The score is scaled to the
    traditional 0-36 range.
    """

    def __init__(self, reference_path, size=(512, 512)):
        self.reference = self._load_image(reference_path, size)
        self.size = size

    def _load_image(self, path, size):
        img = Image.open(path).convert("L")
        img = img.resize(size, Image.BILINEAR)
        return np.array(img, dtype=np.float32) / 255.0

    def score_image(self, drawing_path):
        drawing = self._load_image(drawing_path, self.size)
        value, _ = ssim(self.reference, drawing, full=True)
        return float(value * 36)

    def __call__(self, drawing_path):
        return self.score_image(drawing_path)

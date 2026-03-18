import tempfile
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image_file(image_file) -> str:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
            image_file.save(temp_image.name)
            image = Image.open(temp_image.name)
            text = pytesseract.image_to_string(image)

        return text.strip()

    except Exception as e:
        return f"OCR error: {str(e)}"
import easyocr
import base64

class OCRService:
    def __init__(self):
        print("-"*20, "\nLoading EasyOCR model...")
        self.reader = easyocr.Reader(['ar', 'en'], gpu=False)
        print("EasyOCR Loaded Successfully\n", "-"*20)
    
    def extract_text(self, base64_string: str) -> str:
        try: 
            # data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...
            if "," in base64_string:
                base64_string = base64_string.split(",")[1]
            
            image_data = base64.b64decode(base64_string)
            result_list = self.reader.readtext(image_data, detail=0)
            return "\n".join(result_list)
        except Exception as e:
            print(f"OCR Error: {e}")
            return ""

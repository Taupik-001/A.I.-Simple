import pytesseract
from PIL import Image
from docx import Document


def ocr_image(image_path):
    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.open(image_path))

    # Preprocess the text (optional)
    # For example, you can remove unnecessary white spaces and newline characters
    text = " ".join(text.split())
    text = text.replace("\n", " ")

    return text


def save_text_to_word(text, output_file):
    # Create a new Word document
    doc = Document()

    # Add the OCR text to the Word document
    doc.add_paragraph(text)

    # Save the Word document
    doc.save(output_file)


if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your input image
    input_image_path = "1.png"

    # Replace 'output_document.docx' with the desired output Word document name
    output_document_path = "1.docx"

    # Perform OCR on the image and get the extracted text
    extracted_text = ocr_image(input_image_path)

    # Save the extracted text to a Word document
    save_text_to_word(extracted_text, output_document_path)

    print(f"OCR completed. Extracted text saved to {output_document_path}.")

import pytest
import json
from io import BytesIO
from fastapi.testclient import TestClient
from unittest import mock
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the extract info pdf API"}

@pytest.fixture
def mock_pdf():
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    pdf_file = BytesIO()
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, "This is a test PDF file with some text.")
    c.save()
    pdf_file.seek(0)
    return pdf_file

def test_upload_pdf_success(mock_pdf):
    patterns = {
        "patterns": {
            "test": ["test PDF file", ""]
        }
    }
    response = client.post(
        "/process/pdf/regex",
        files={"file": ("test.pdf", mock_pdf, "application/pdf")},
        data={"patterns": json.dumps(patterns)},
    )
    assert response.status_code == 200
    assert response.json() == {"matches": {"test": ["test PDF file"]}}

def test_upload_pdf_invalid_file():
    invalid_file = b"This is not a PDF file."
    patterns = {
        "patterns": {
            "test": ["test PDF file", ""]
        }
    }
    response = client.post(
        "/process/pdf/regex",
        files={"file": ("test.pdf", invalid_file, "application/pdf")},
        data={"patterns": json.dumps(patterns)},
    )
    assert response.status_code == 400
    assert "An error occurred" in response.json()["detail"]

def test_upload_pdf_invalid_json():
    mock_pdf = BytesIO(b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\n")
    response = client.post(
        "/process/pdf/regex",
        files={"file": ("test.pdf", mock_pdf, "application/pdf")},
        data={"patterns": "invalid json"},
    )
    assert response.status_code == 400
    assert "An error occurred" in response.json()["detail"]

def test_upload_pdf_general_exception(mocker):
    # Mock the fitz.open method to raise an exception
    mocker.patch("app.main.fitz.open", side_effect=Exception("Unexpected error"))

    mock_pdf = BytesIO(b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\n")
    patterns = {
        "patterns": {
            "test": ["test PDF file", ""]
        }
    }
    response = client.post(
        "/process/pdf/regex",
        files={"file": ("test.pdf", mock_pdf, "application/pdf")},
        data={"patterns": json.dumps(patterns)},
    )
    assert response.status_code == 400
    assert "An error occurred" in response.json()["detail"]

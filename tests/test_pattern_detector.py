# tests/test_pattern_detector.py
import unittest
import pathlib
import tempfile
from src.pattern_detector import analyze_text, load_flagged_list, generate_report

class TestPatternDetector(unittest.TestCase):
    def test_analyze_text_finds_ipv4_strict(self):
        text = "Una IP válida es 192.168.1.1 y otra es 10.0.0.1."
        results = analyze_text(text)
        self.assertIn("ipv4_strict", results)
        self.assertEqual(len(results["ipv4_strict"]), 2)
        self.assertIn("192.168.1.1", results["ipv4_strict"])
        self.assertIn("10.0.0.1", results["ipv4_strict"])

    def test_analyze_text_finds_email(self):
        text = "El correo es test@example.com."
        results = analyze_text(text)
        self.assertIn("email", results)
        self.assertEqual(len(results["email"]), 1)
        self.assertIn("test@example.com", results["email"])

    def test_analyze_text_finds_url(self):
        text = "Visita https://my-secure-site.com para más info."
        results = analyze_text(text)
        self.assertIn("url", results)
        self.assertIn("https://my-secure-site.com", results["url"])

    def test_analyze_text_finds_sha256(self):
        full_hash = "a2c5d99b86d0b8f4d3b3c3b4b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3b3"
        text = f"El hash es {full_hash}"
        results = analyze_text(text)
        self.assertIn("sha256", results)
        self.assertIn(full_hash, results["sha256"])

    def test_analyze_text_identifies_invalid_ipv4(self):
        text = "IPs: 192.168.1.1, 999.168.1.1, 1.2.3.400"
        results = analyze_text(text)
        self.assertIn("ipv4_invalid_format", results)
        self.assertEqual(len(results["ipv4_invalid_format"]), 2)
        self.assertIn("999.168.1.1", results["ipv4_invalid_format"])
        self.assertIn("1.2.3.400", results["ipv4_invalid_format"])
        self.assertIn("192.168.1.1", results["ipv4_strict"])

    def test_load_flagged_list(self):
        content = "1.1.1.1\n2.2.2.2\n # Comentario\n\n3.3.3.3"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp_file:
            tmp_file.write(content)
            tmp_file_path = pathlib.Path(tmp_file.name)
        try:
            flagged_list = load_flagged_list(tmp_file_path)
            self.assertEqual(len(flagged_list), 3)
            self.assertIn("1.1.1.1", flagged_list)
        finally:
            import os
            os.remove(tmp_file_path)

    def test_generate_report_with_flagged_ips(self):
        results = {"ipv4_strict": ["1.1.1.1", "2.2.2.2"]}
        flagged = ["1.1.1.1"]
        report = generate_report(results, flagged=flagged)
        self.assertIn("1.1.1.1  <-- FLAGGED", report)
        self.assertNotIn("2.2.2.2  <-- FLAGGED", report)

if __name__ == '__main__':
    unittest.main()

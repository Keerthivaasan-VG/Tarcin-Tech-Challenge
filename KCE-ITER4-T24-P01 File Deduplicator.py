import csv
import unittest
from io import StringIO
def deduplicate_files(file_path):
    seen, result = set(), []
    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["hash"] not in seen:
                seen.add(row["hash"])
                result.append(row)
    return result
class TestDeduplicateFiles(unittest.TestCase):
    def test_remove_duplicates(self):
        csv_content = """id,hash1,abc2,def3,abc4,ghi"""
        f = StringIO(csv_content)
        reader = csv.DictReader(f)
        rows = list(reader)
        seen, result = set(), []
        for row in rows:
            if row["hash"] not in seen:
                seen.add(row["hash"])
                result.append(row)
        self.assertEqual(len(result), 3)  # unique hashes
        self.assertEqual(result[0]["id"], "1")
        self.assertEqual(result[1]["id"], "2")
        self.assertEqual(result[2]["id"], "4")
if __name__ == "__main__":
    unittest.main()

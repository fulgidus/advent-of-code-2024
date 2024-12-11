import unittest
from day5 import parse_input, is_update_valid, reorder_update

class TestDay5(unittest.TestCase):
    def setUp(self):
        # Dati di esempio
        self.rules_text = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13'''

        self.updates_text = '''75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

        # Parsing delle regole e degli aggiornamenti
        self.rules = []
        for line in self.rules_text.strip().split('\n'):
            x, y = map(int, line.strip().split('|'))
            self.rules.append((x, y))

        self.updates = []
        for line in self.updates_text.strip().split('\n'):
            update = list(map(int, line.strip().split(',')))
            self.updates.append(update)

    def test_is_update_valid(self):
        # Indici degli aggiornamenti validi e non validi
        valid_updates_indices = [0, 1, 2]
        invalid_updates_indices = [3, 4, 5]

        for idx in valid_updates_indices:
            update = self.updates[idx]
            self.assertTrue(is_update_valid(update, self.rules), f"Update {update} should be valid.")

        for idx in invalid_updates_indices:
            update = self.updates[idx]
            self.assertFalse(is_update_valid(update, self.rules), f"Update {update} should be invalid.")

    def test_reorder_update(self):
        # Aggiornamenti non validi e loro ordini corretti
        invalid_updates_indices = [3, 4, 5]
        expected_reorders = [
            [97, 75, 47, 61, 53],
            [61, 29, 13],
            [97, 75, 47, 29, 13]
        ]

        for idx, expected in zip(invalid_updates_indices, expected_reorders):
            update = self.updates[idx]
            reordered = reorder_update(update, self.rules)
            self.assertEqual(reordered, expected, f"Update {update} should reorder to {expected}.")

    def test_parse_input(self):
        # Test della funzione parse_input con un file temporaneo
        import tempfile

        with tempfile.NamedTemporaryFile('w+', delete=False) as tmpfile:
            tmpfile.write(self.rules_text + '\n\n' + self.updates_text)
            tmpfile_name = tmpfile.name

        parsed_rules, parsed_updates = parse_input(tmpfile_name)
        self.assertEqual(parsed_rules, self.rules)
        self.assertEqual(parsed_updates, self.updates)

    def tearDown(self):
        # Rimozione del file temporaneo
        import os
        if hasattr(self, 'tmpfile_name') and os.path.exists(self.tmpfile_name):
            os.remove(self.tmpfile_name)

if __name__ == '__main__':
    unittest.main()
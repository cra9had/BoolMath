from truth_table import TruthTable, VariableDoesNotExist
import unittest


class TruthTableTest(unittest.TestCase):
    def test_invalid_variable(self):
        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(r"A\/B")
        with self.assertRaises(VariableDoesNotExist):
            self.truth_table.solve_instance("INV(D)")
        with self.assertRaises(VariableDoesNotExist):
            self.truth_table.solve_instance(r"INV(A\/B/\C)\/A->B=B")

    def test_instance_inversion(self):
        instance = "INV(INV(A))"

        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(instance)
        self.truth_table.solve_instance(instance)
        self.assertEqual(self.truth_table.table[1], list("10"))
        self.assertEqual(self.truth_table.table[2], list("01"))

    def test_instance_conjunction(self):
        instance = "A/\\B/\\A"

        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(instance)
        self.truth_table.solve_instance(instance)
        self.assertEqual(self.truth_table.table[2], list("0001"))
        self.assertEqual(self.truth_table.table[3], list("0001"))

    def test_instance_disjunction(self):
        instance = "A\\/B\\/A"

        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(instance)
        self.truth_table.solve_instance(instance)
        self.assertEqual(self.truth_table.table[2], list("0111"))
        self.assertEqual(self.truth_table.table[3], list("0111"))

    def test_implication(self):
        instance = "A->B->A"

        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(instance)
        self.truth_table.solve_instance(instance)
        self.assertEqual(self.truth_table.table[2], list("1101"))
        self.assertEqual(self.truth_table.table[3], list("0011"))

    def test_equation(self):
        instance = "A=B=A"

        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(instance)
        self.truth_table.solve_instance(instance)
        self.assertEqual(self.truth_table.table[2], list("1001"))
        self.assertEqual(self.truth_table.table[3], list("0101"))

    def test_hard_instance(self):
        instance = r"INV(A\/B/\C)\/A->B=B"

        self.truth_table = TruthTable()
        self.truth_table.set_start_columns(instance)
        self.truth_table.solve_instance(instance)
        self.assertEqual(self.truth_table.table[3:], [list("00010001"),
                                                      list("00011111"),
                                                      list("11100000"),
                                                      list("11101111"),
                                                      list("00110011"),
                                                      list("11111111")])

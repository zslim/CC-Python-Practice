import reports
import unittest


def get_date_ordered():
    return ['Diablo III',
            'Terraria',
            'StarCraft II: Wings of Liberty',
            'Minecraft',
            'The Sims 3',
            'Crysis',
            "Garry's Mod",
            'Guild Wars',
            'Counter-Strike: Condition Zero',
            'Doom 3',
            'Half-Life 2',
            'The Sims 2',
            'Warhammer 40,000: Dawn of War (including expansions)',
            'World of Warcraft',
            'Warcraft III: Reign of Chaos',
            'Diablo II',
            'The Sims',
            'Counter-Strike',
            'EverQuest',
            'Half-Life',
            'StarCraft',
            'Age of Empires',
            'Command & Conquer',
            'Populous']


def get_grouped_dic():
    return {"Action-adventure": 1,
            "First-person shooter": 6,
            "Real-time strategy": 7,
            "RPG": 5,
            "Sandbox": 1,
            "Simulation": 3,
            "Survival game": 1}


class Tester(unittest.TestCase):
    input_file = "game_stat.txt"

    def test_1_get_most_played(self):
        result = reports.get_most_played(self.input_file)
        self.assertEqual(result, "Minecraft")
        if result == "Minecraft":
            print("Function 'get_most_played' is passed.")

    def test_2_sum_sold(self):
        result = reports.sum_sold(self.input_file)
        self.assertEqual(result, 187.16)
        if result == 187.16:
            print("Function 'sum_sold' is passed.")

    def test_3_get_selling_avg(self):
        result = reports.get_selling_avg(self.input_file)
        self.assertEqual(result, 7.798333333333333)
        if result == 7.798333333333333:
            print("Function 'get_selling_avg' is passed.")

    def test_4_count_longest_title(self):
        result = reports.count_longest_title(self.input_file)
        self.assertEqual(result, 52)
        if result == 52:
            print("Function 'count_longest_title' is passed.")

    def test_5_get_date_avg(self):
        result = reports.get_date_avg(self.input_file)
        self.assertEqual(result, 2003)
        if result == 2003:
            print("Function 'get_date_avg' is passed.")

    def test_6_get_game(self):
        result = reports.get_game(self.input_file, "Counter-Strike")
        expected = ["Counter-Strike", 12.5, 1999,
                    "First-person shooter", "Valve Corporation"]

        self.assertEqual(result, expected)
        if result == expected:
            print("Function 'get_game' is passed.")

    def test_bonus_1_count_grouped_by_genre(self):
        result = reports.count_grouped_by_genre(self.input_file)
        expected_result = get_grouped_dic()
        self.assertEqual(result, expected_result)

        if result == expected_result:
            print("Bonus function 'count_grouped_by_genre' is passed.")

    def test_bonus_2_get_date_ordered(self):
        result = reports.get_date_ordered(self.input_file)
        expected_result = get_date_ordered()
        self.assertEqual(result, expected_result)

        if result == expected_result:
            print("Bonus function 'get_date_ordered' is passed.")


def main():
    unittest.main()

if __name__ == '__main__':
    main()

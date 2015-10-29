# Define the key for `grouping`
# It will receive the raw row from CSV file.
def key(row):
    return row["ORDER_ID"]

# Defint the csv format

# Assumes the destination format requires `id`,`name`,`items`

# Define all required fields, all field method will receive the grouped raw data
def id_(rows):
    return rows[0]['ORDER_ID']


def name(rows):
    return rows[0]['Name']


def items(rows):
    def f(row):
        return {
                "name": row["item_name"],
                "quantity": int(row["Quantity"]),
                }

    return map(f, rows)

if __name__ == "__main__":
    import unittest
    class Tests(unittest.TestCase):
        def test_0(self):
            import pkgutil
            import csv
            import StringIO
            import importer
            from importer.test import test

            order_csv = pkgutil.get_data(__package__, "/fixtures/order.csv")
            f = StringIO.StringIO(order_csv)

            # Assumes the CSV has header
            csv_reader = csv.DictReader(f)

            # for row in csv_reader:
            #     print row

            orders = importer.process(test, csv_reader)

            # print orders
            expected = {
                    "1": {"id": "1", "name":"andy", "items": [{"name":"foo", "quantity": 3}, {"name":"bar", "quantity": 2}]},
                    "2": {"id": "2", "name":"judy", "items": [{"name":"foo", "quantity": 1},]},
                    }

            self.assertEqual(orders, expected)

    unittest.main()


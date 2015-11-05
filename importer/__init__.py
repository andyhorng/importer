
def process(module, reader):

    from collections import defaultdict

    grouped_rows = defaultdict(list)
    for row in reader:
        k = module.key(row)
        grouped_rows[k].append(row)

    orders = defaultdict(dict)

    for key, rows in list(grouped_rows.items()):
        orders[module.id_(rows)] = {
                "id": module.id_(rows),
                "name": module.name(rows),
                "items": module.items(rows),
                }

    return dict(orders)

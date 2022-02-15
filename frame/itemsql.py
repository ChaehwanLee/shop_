# itemsql.py

MAKE_TABLE = """
    CREATE TABLE IF NOT EXISTS tb_item(
        id int PRIMARY KEY,
        name CHAR(20),
        price INT,
        rate REAL
    )
""";
ITEM_INSERT = """
    INSERT INTO tb_item VALUES (%d,"%s",%d,%f)
""";
ITEM_UPDATE = """
    UPDATE tb_item SET name="%s", price=%d, rate=%f WHERE id=%d
""";
ITEM_DELETE = """
    DELETE FROM tb_item WHERE id=%d
""";
ITEM_SELECT_ONE = """
    SELECT * FROM tb_item WHERE id=%d
""";
ITEM_SELECT = """
    SELECT * FROM tb_item
""";





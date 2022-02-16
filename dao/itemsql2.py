MAKE_TABLE = """
    CREATE TABLE IF NOT EXISTS tb_shop(
        id CHAR(20) PRIMARY KEY,
        name CHAR(20),
        money INT,
        rate REAL
    )
""";# 테이블이 존재하지 않으면 tb_item 생성
SHOP_INSERT = """
    INSERT INTO tb_shop VALUES ("%s","%s",%d,%f)
""";
SHOP_UPDATE = """
    UPDATE tb_shop SET name="%s",money=%d,rate=%f WHERE id="%s"
""";
SHOP_DELETE = """
    DELETE FROM tb_shop WHERE id="%s"    
""";
SHOP_SELECT_ONE = """
    SELECT * FROM tb_shop WHERE id="%s"
""";
SHOP_SELECT = """
    SELECT * FROM tb_shop
""";
import sqlite3

conn = sqlite3.connect("pedidos.pb")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        telefono INTEGER NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio FLOAT NOT NULL
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS pedidos (
        id_pedido INTEGER PRIMARY KEY,
        id_cliente INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
    )
    """
)

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS detalle_pedidos (
        id_detalle INTEGER PRIMARY KEY,
        id_pedido INTEGER NOT NULL,
        id_producto INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
        FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
    )
    """
)


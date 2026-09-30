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
    INSERT INTO clientes (nombre, email, telefono) 
    VALUES ("maria jimenez", "maria.jimenez@email.com", 453975641)
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
    INSERT INTO productos (nombre, precio) 
    VALUES ("pan", 0.70)
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
    INSERT INTO pedidos (id_cliente, fecha) 
    VALUES (3, "2025-10-23")
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
conn.execute(
    """
    INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad) 
    VALUES (3, 3, 70)
    """
)

conn.commit()
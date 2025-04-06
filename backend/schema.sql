CREATE TABLE items (
    id TEXT PRIMARY KEY,
    name TEXT,
    width REAL,
    depth REAL,
    height REAL,
    priority INTEGER,
    expiryDate TEXT,
    usageLimit INTEGER,
    usageCount INTEGER,
    preferredZone TEXT,
    isWaste INTEGER,
    containerId TEXT,
    x REAL,
    y REAL,
    z REAL,
    FOREIGN KEY (containerId) REFERENCES containers(id)
);

CREATE TABLE containers (
    id TEXT PRIMARY KEY,
    zone TEXT,
    width REAL,
    depth REAL,
    height REAL,
    spaceUtilization REAL
);

CREATE TABLE logs (
    id TEXT PRIMARY KEY,
    timestamp TEXT,
    userId TEXT,
    actionType TEXT,
    itemId TEXT,
    details TEXT
);

from typing import List, Optional
from models import Item, Container, Log
from database import query_db, execute_db

def create_item(item: Item):
    execute_db('INSERT INTO items (id, name, width, depth, height, priority, expiryDate, usageLimit, usageCount, preferredZone, isWaste, containerId, x, y, z) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
               (item.itemId, item.name, item.width, item.depth, item.height, item.priority, item.expiryDate, item.usageLimit, item.usageCount, item.preferredZone, int(item.isWaste), item.containerId, item.x, item.y, item.z))

def get_item_by_id(item_id: str) -> Optional[Item]:
    row = query_db('SELECT * FROM items WHERE id = ?', [item_id], one=True)
    return Item(**row) if row else None

def update_item(item_id: str, updated_item: Item):
    execute_db('UPDATE items SET name=?, width=?, depth=?, height=?, priority=?, expiryDate=?, usageLimit=?, usageCount=?, preferredZone=?, isWaste=?, containerId=?, x=?, y=?, z=? WHERE id=?',
               (updated_item.name, updated_item.width, updated_item.depth, updated_item.height, updated_item.priority, updated_item.expiryDate, updated_item.usageLimit, updated_item.usageCount, updated_item.preferredZone, int(updated_item.isWaste), updated_item.containerId, updated_item.x, updated_item.y, updated_item.z, item_id))

def delete_item(item_id: str):
    execute_db('DELETE FROM items WHERE id = ?', [item_id])

def create_container(container: Container):
    execute_db('INSERT INTO containers (id, zone, width, depth, height, spaceUtilization) VALUES (?, ?, ?, ?, ?, ?)',
               (container.containerId, container.zone, container.width, container.depth, container.height, container.spaceUtilization))

def get_container_by_id(container_id: str) -> Optional[Container]:
    row = query_db('SELECT * FROM containers WHERE id = ?', [container_id], one=True)
    return Container(**row) if row else None

def update_container(container_id: str, updated_container: Container):
    execute_db('UPDATE containers SET zone=?, width=?, depth=?, height=?, spaceUtilization=? WHERE id=?',
               (updated_container.zone, updated_container.width, updated_container.depth, updated_container.height, updated_container.spaceUtilization, container_id))

def delete_container(container_id: str):
    execute_db('DELETE FROM containers WHERE id = ?', [container_id])

def create_log(log: Log):
    execute_db('INSERT INTO logs (id, timestamp, userId, actionType, itemId, details) VALUES (?, ?, ?, ?, ?, ?)',
               (log.id, log.timestamp, log.userId, log.actionType, log.itemId, log.details))

def get_logs() -> List[Log]:
    rows = query_db('SELECT * FROM logs')
    return [Log(**row) for row in rows]

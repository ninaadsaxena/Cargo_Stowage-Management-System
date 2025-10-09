import unittest
from typing import List, Optional
from api.placement import find_optimal_container
from models import Item, Container

class TestPlacement(unittest.TestCase):
    def test_find_optimal_container_prioritizes_preferred_zone(self):
        """
        Tests that find_optimal_container correctly prioritizes the preferred zone
        even if a container in another zone has lower space utilization.
        """
        item = Item(
            itemId="test_item",
            name="Test Item",
            width=10,
            depth=10,
            height=10,
            priority=1,
            expiryDate=None,
            usageLimit=10,
            preferredZone="A"
        )

        container_A = Container(
            containerId="container_a",
            zone="A",
            width=20,
            height=20,
            depth=20,
            spaceUtilization=70.0
        )

        container_B = Container(
            containerId="container_b",
            zone="B",
            width=20,
            height=20,
            depth=20,
            spaceUtilization=10.0
        )

        containers = [container_A, container_B]

        # The buggy function will choose container_b due to lower utilization
        # The correct function should choose container_a as it is in the preferred zone
        optimal_container = find_optimal_container(item, containers)

        self.assertIsNotNone(optimal_container)
        self.assertEqual(optimal_container.containerId, "container_a")

if __name__ == '__main__':
    unittest.main()
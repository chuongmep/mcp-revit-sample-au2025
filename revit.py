import os 
import json
import csv
from typing import Any
import httpx
import matplotlib.pyplot as plt
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("revit")


# Constants
BASE_PATH = "./models"
MODEL_NAME = "ARC Model.csv"


async def read_csv_data():
    """Read CSV data from a file."""
    csv_file_path = os.path.join(BASE_PATH, MODEL_NAME)
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file for {MODEL_NAME} not found.")

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
    
@mcp.tool()
async def count_elements() -> int:
    """Count elements in a Revit model."""
    data = await read_csv_data()
    return len(data)

@mcp.tool()
async def count_categories() -> dict[str, Any]:
    """Count categories of elements in a Revit model, 
    return a dictionary with category names as 
    keys and counts as values."""
    data = await read_csv_data()
    categories = {}
    for row in data:
        category = row["Category"]
        categories[category] = categories.get(category, 0) + 1
    return categories

@mcp.tool()
async def get_elements_by_category(category: str) -> list[dict[str, Any]]:
    """Get elements by category from the Revit model."""
    data = await read_csv_data()
    return [row for row in data if row["Category"] == category]

@mcp.tool()
async def get_families_by_category(category: str) -> list[str]:
    """Get a list of families in the Revit model."""
    data = await read_csv_data()
    families = set(row["Family"] for row in data if row["Category"] == category)
    return list(families)

@mcp.tool()
async def get_family_types(family: str) -> list[str]:
    """Get a list of family types for a given family in the Revit model."""
    data = await read_csv_data()
    family_types = set(row["Type"] for row in data if row["Family"] == family)
    return list(family_types)

@mcp.tool()
async def get_family_types_by_category(category: str) -> list[str]:
    """Get a list of family types for a given category in the Revit model."""
    data = await read_csv_data()
    family_types = set(row["Type"] for row in data if row["Category"] == category)
    return list(family_types)

@mcp.tool()
async def get_element_by_id(element_id: str) -> dict[str, Any]:
    """Get element details by its ID."""
    data = await read_csv_data()
    for row in data:
        if row["ElementId"] == element_id:
            return row
    raise ValueError(f"Element with ID {element_id} not found.")


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
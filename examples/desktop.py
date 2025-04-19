"""
FastMCP Desktop Example

A simple example that exposes the desktop directory as a resource.
"""

from pathlib import Path

from fastmcp.server import FastMCP

import io

import cv2
from fastmcp import FastMCP, Image
from PIL import Image as PILImage

# Create server
mcp = FastMCP("Demo")


@mcp.resource("dir://desktop")
def desktop() -> list[str]:
    """List the files in the user's desktop"""
    desktop = Path.home() / "Desktop"
    return [str(f) for f in desktop.iterdir()]



@mcp.tool()
def get_image() -> list[Image]:
    # these works
    img1 = Image(path="/Users/jakesimonds/Documents/fastmcp/examples/photo/latest_photo.jpg")


    # buffer = io.BytesIO()
    # PILImage.open("photo/test.jpg").save(buffer, format="PNG")
    # img4 = Image(data=buffer.getvalue(), format="png")


    # success
    return img1


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 100

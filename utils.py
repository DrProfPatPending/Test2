"""Utility functions for the project."""
import math
from typing import Tuple


def cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
    """
    Convert Cartesian coordinates (x, y) to polar coordinates (r, theta).
    r: distance from origin
    theta: angle in radians from the positive x-axis
    Returns:
        (r, theta) where r >= 0 and theta is in radians
    """
    r = math.hypot(x, y)
    theta = math.atan2(y, x)
    print(f"Debug: Calculated {r=:<7.3f}, {theta=:<7.3f}")
    return r, theta

def radians_to_degrees(theta_rad: float) -> float:
    """
    Convert angle from radians to degrees.
    """
    return math.degrees(theta_rad)

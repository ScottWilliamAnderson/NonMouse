"""Utility functions used by NonMouse."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import cv2
import numpy as np


def draw_circle(
    image: np.ndarray,
    x: float,
    y: float,
    roudness: int,
    color: tuple[int, int, int],
) -> None:
    """Draw a circle on ``image``."""
    cv2.circle(
        image,
        (int(x), int(y)),
        roudness,
        color,
        thickness=5,
        lineType=cv2.LINE_8,
        shift=0,
    )


def calculate_distance(
    landmark1: Sequence[float],
    landmark2: Sequence[float],
) -> float:
    """Return the Euclidean distance between two 2D landmarks."""
    v = np.array([landmark1[0], landmark1[1]]) - np.array(
        [landmark2[0], landmark2[1]],
    )
    return np.linalg.norm(v)


def calculate_moving_average(landmark: float, ran: int, lit: list[float]) -> float:
    """Return the moving average of ``landmark`` over ``ran`` samples."""
    while len(lit) < ran:
        lit.append(landmark)
    lit.append(landmark)
    if len(lit) > ran:
        lit.pop(0)
    return sum(lit) / ran

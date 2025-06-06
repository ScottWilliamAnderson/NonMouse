"""Unit tests for :mod:`nonmouse.utils`."""

import numpy as np
from hypothesis import given
from hypothesis import strategies as st

from nonmouse.utils import calculate_distance, calculate_moving_average, draw_circle


def test_calculate_distance() -> None:
    """Distance between (0,0) and (3,4) should be 5."""
    assert calculate_distance((0, 0), (3, 4)) == 5


@given(
    st.tuples(st.floats(-100, 100), st.floats(-100, 100)),
    st.tuples(st.floats(-100, 100), st.floats(-100, 100)),
)
def test_calculate_distance_symmetric(
    p1: tuple[float, float],
    p2: tuple[float, float],
) -> None:
    """Distance symmetry property."""
    assert calculate_distance(p1, p2) == calculate_distance(p2, p1)


def test_calculate_moving_average() -> None:
    """Verify moving average for a small sequence."""
    seq = []
    assert calculate_moving_average(1.0, 3, seq) == 1.0
    assert calculate_moving_average(2.0, 3, seq) == 4 / 3
    assert calculate_moving_average(3.0, 3, seq) == 2.0


@given(st.floats(-10, 10), st.integers(min_value=1, max_value=10))
def test_moving_average_range(value: float, ran: int) -> None:
    """Result stays within expected range."""
    seq = []
    result = calculate_moving_average(value, ran, seq)
    assert -10 <= result <= 10


def test_draw_circle() -> None:
    """Ensure drawing modifies the image."""
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    draw_circle(img, 5, 5, 2, (255, 0, 0))
    assert img.sum() > 0

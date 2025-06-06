"""Package metadata for ``nonmouse``."""

from pathlib import Path

__copyright__ = "Copyright (C) 2023 Yuki TAKEYAMA"
__version__ = "2.7.0"
__license__ = "Apache-2.0"
__author__ = "Yuki TAKEYAMA"
__author_email__ = "namiki.takeyama@gmail.com"
__url__ = "http://github.com/takeyamayuki/NonMouse"

__all__ = [path.stem for path in Path(__file__).parent.glob("[a-zA-Z0-9]*.py")]

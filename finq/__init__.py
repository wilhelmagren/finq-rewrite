"""
MIT License

Copyright (c) 2024 Wilhelm Ågren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

File created: 2024-05-17
Last updated: 2024-05-20
"""

import logging
from finq import datautil

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


# Create the default `finq` home directory if it does not already exist. If it exists 
# but is a file, then raise a `FileExistsError` and ask user to remove the file.
# This will be executed at each import of the library. It should only have to create
# directory once, else, the user has created something else with the same name already..
_default_finq_path = datautil.paths.default_finq_path()
if _default_finq_path.exists():
    try:
        _default_finq_path.mkdir(parents=False, exist_ok=True)
    except FileExistsError as err:
        log.error(
            f"The default home path (located at '{_default_finq_path}') already exists "
            "but as a file!\nThis needs to be a directory. Please remove the file!"
        )
        raise err
else:
    log.info(f"Setting up the default `finq` directory at: '{_default_finq_path}'.")
    _default_finq_path.mkdir(parents=True, exist_ok=False)


def set_log_level(level: int) -> logging.Logger:
    """ Set the threshold for the global log handler to the specified level. 

    Parameters
    ----------
    level : int
        The level to assign to the globa log handler.

    Returns
    -------
    logging.Logger
        The global log handler that has the new threshold level.

    """
    log.setLevel(level)
    return log


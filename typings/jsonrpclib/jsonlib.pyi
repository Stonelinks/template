"""
This type stub file was generated by pyright.
"""

"""
Loads the "best" Python library available for the current interpreter and
provides a single interface for all

:authors: Thomas Calmant
:copyright: Copyright 2025, Thomas Calmant
:license: Apache License 2.0
:version: 0.4.3.4

..

    Copyright 2025 Thomas Calmant

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__version_info__ = ...
__version__ = ...
__docformat__ = ...
PYTHON_2 = ...
class JsonHandler:
    """
    Parent class for JSON handlers
    """
    def get_methods(self): # -> tuple[Callable[..., Any], Callable[..., str]]:
        """
        Returns the loads and dumps methods
        """
        ...
    


class CJsonHandler(JsonHandler):
    """
    Handler based on cjson
    """
    def get_methods(self): # -> tuple[Any, Callable[..., Any]]:
        ...
    


class SimpleJsonHandler(JsonHandler):
    """
    Handler based on simplejson
    """
    def get_methods(self): # -> tuple[Callable[..., Any], Callable[..., Any]]:
        ...
    


class UJsonHandler(JsonHandler):
    """
    Handler based on ujson
    """
    def get_methods(self): # -> tuple[Callable[..., Any], Callable[..., str]]:
        ...
    


class OrJsonHandler(JsonHandler):
    """
    Handler based on orjson
    """
    def get_methods(self): # -> tuple[Any, Callable[..., Any]]:
        ...
    


def get_handler() -> JsonHandler:
    """
    Returns the best available Json parser
    """
    ...

def get_handler_methods(): # -> tuple[Callable[..., Any], Callable[..., str]]:
    """
    Returns the load and dump methods of the best Json handler
    """
    ...


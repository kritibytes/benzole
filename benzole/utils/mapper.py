from cgitb import handler
import os
from typing import Any, List
from .types import Route
import importlib.util

slash: str = os.path.join('a', '')[1:]


def files_mapper(src_dir: str) -> List[str]:
    files: List[str] = []

    for item in os.listdir(src_dir):
        full_path: str = os.path.join(src_dir, item)

        if os.path.isdir(full_path):
            files += files_mapper(full_path)
        elif full_path.endswith(".py"):
            files.append(full_path)

    return files


def routes_mapper(files_map: List[str]) -> List[Route]:
    routes: List[Route] = []

    for file in files_map:
        if file.startswith(f"src{slash}"):
            route: List[str] = file[3:].split(slash)
            route_name = route[-1].split('.')[0]
            route_name = "" if route_name == "index" else route_name
            route[-1] = route_name

            url = "/".join(route)

            spec: Any = importlib.util.spec_from_file_location("route__"+url.replace("/", "_"), file)
            handler: Any = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(handler)

            if "Default" in dir(handler):
                routes.append({"url": url, "handler": handler.Default()})

    return routes

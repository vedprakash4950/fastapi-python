from fastapi import Request


def build_file_url(
    request: Request,
    path: str | None,
) -> str | None:
    if not path:
        return None

    base_url = str(request.base_url).rstrip("/")
    path = path.lstrip("/")

    return f"{base_url}/{path}"
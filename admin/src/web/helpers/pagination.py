from flask import url_for
from typing import Dict
from flask import Request
from flask_sqlalchemy import Pagination


def pagination_generator(
    paginator: Pagination, request: Request, paginator_name: str = "paginator"
) -> Dict:
    """Generates pagination data for a given paginator, the output of this function is meant to go directly to the render_template function.
    Args:
        paginator (flask_sqlalchemy.pagination.Pagination): A Pagination object, contains the paginated data.
        request (flask.Request): A Request object, used to pass the args to the next page and to get current route.
        paginator_name (str, optional): The name of the pagination object to be passed to the template. Defaults to "paginator".
    Returns:
        dict: A dictionary containing the next page url, the previous page url, a list with all the pages with their numbers and the paginator object.
    """
    args = dict(request.args)
    try:
        args.pop("page")
    except KeyError:
        pass
    pages_urls = [
        (url_for(request.endpoint, page=page_num, **args), page_num)
        for page_num in paginator.iter_pages(100, 100, 100, 100)
    ]
    next_url = (
        url_for(request.endpoint, page=paginator.next_num, **args)
        if paginator.has_next
        else None
    )
    prev_url = (
        url_for(request.endpoint, page=paginator.prev_num, **args)
        if paginator.has_prev
        else None
    )
    return {
        "next_url": next_url,
        "pages_urls": pages_urls,
        "prev_url": prev_url,
        f"{paginator_name}": paginator,
        "higlighted_page": paginator.page,
        "args": args,
    }

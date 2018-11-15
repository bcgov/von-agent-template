
import logging.config

from aiohttp import web
import aiohttp_jinja2

from vonx.web.view_helpers import (
    IndyRequestError,
    get_handle_id,
    get_manager,
    get_request_json,
    indy_client,
    perform_issue_credential,
    perform_store_credential,
    service_request,
)

LOGGER = logging.getLogger(__name__)


def get_agent_routes(_app) -> list:
    """
    Get the standard list of routes for the von-x agent
    """
    return [
        web.get('/chooser', render_chooser),
        web.post('/chooser', process_chooser),
    ]


async def render_chooser(request: web.Request) -> web.Response:
    """
    Respond with HTTP code 200 if services are ready to accept new credentials, 451 otherwise
    """

    tpl_name = "my_chooser.html"

    tpl_vars = {
        "inputs": {},
        "request": {},
    }
    tpl_vars["inputs"].update(request.query)
    tpl_vars["request"].update(request.query)

    result = await get_manager(request).get_service_status('manager')
    ok = result and result.get("services", {}).get("indy", {}).get("synced")

    tpl_vars["result_text"] = 'ok get chooser' if ok else ''
    tpl_vars["ok_text"] = '200' if ok else '451'

    return aiohttp_jinja2.render_template(tpl_name, request, tpl_vars)


async def process_chooser(request: web.Request) -> web.Response:
    """
    Respond with HTTP code 200 if services are ready to accept new credentials, 451 otherwise
    """

    inputs = await request.json()
    if isinstance(inputs, dict):
        inputs = inputs.get("attributes") or {}
    else:
        inputs = await request.post()

    corp_num = inputs.get("corp_num")
    cred_schema = inputs.get("credential_type")

    print("corp_num", corp_num)
    print("cred_schema", cred_schema)

    if corp_num is not None and corp_num == "goto":
        print("Redirecting :-D")
        return web.Response(status=307, headers={'location': "/myorg/myorg-credential",},) 
    else:
        print("Stay on same page :-(")
        return await render_chooser(request)


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
        web.post('/chooser2', process_chooser),
        web.post('/chooser3', process_chooser),
    ]


async def render_chooser(request: web.Request) -> web.Response:
    """
    Respond with HTTP code 200 if services are ready to accept new credentials, 451 otherwise
    """

    tpl_name = "my_chooser.html"
    tpl_vars = {}

    result = await get_manager(request).get_service_status('manager')
    ok = result and result.get("services", {}).get("indy", {}).get("synced")

    tpl_vars["result_text"] = 'ok get chooser' if ok else ''
    tpl_vars["ok_text"] = '200' if ok else '451'

    print("tpl_vars", tpl_vars)

    response = aiohttp_jinja2.render_template(tpl_name, request, tpl_vars)
    print(response)
    return response


async def process_chooser(request: web.Request) -> web.Response:
    """
    Respond with HTTP code 200 if services are ready to accept new credentials, 451 otherwise
    """

    tpl_name = "my_chooser.html"
    tpl_vars = {}

    inputs = await request.post()

    corp_num = inputs.get("corp_num")
    if corp_num is not None and corp_num != '':
        tpl_vars["corp_num"] = corp_num
        tpl_name = "my_chooser2.html"
    cred_schema = inputs.get("credential_type")
    if cred_schema is not None and cred_schema != '':
        tpl_vars["cred_schema"] = cred_schema
    credential_id = inputs.get("credential_id")
    if credential_id is not None and credential_id != '':
        tpl_vars["credential_id"] = credential_id
        tpl_name = "my_chooser3.html"

    print("corp_num", corp_num)
    print("cred_schema", cred_schema)
    print("credential_id", credential_id)

    if corp_num is not None and corp_num == "goto":
        print("Redirecting :-D")
        location = request.app.router['myorg-issue'].url_for()
        raise web.HTTPFound(location=location)
        #return web.Response(status=307, headers={'location': "/myorg/myorg-credential",},) 
    else:
        print("Go to page ", tpl_name)
        response = aiohttp_jinja2.render_template(tpl_name, request, tpl_vars)
        print(response)
        return response

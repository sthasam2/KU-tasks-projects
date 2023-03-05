from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from slr.grammar import Grammar
from slr.slr_parser import SLRParser

#########################
# CONFIG
#########################

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#########################
# ROUTES
#########################


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def parse_grammar(request: Request):
    form = await request.form()

    # form inputs
    raw_grammar = form.get("grammar")
    to_check = form.get("to_check")

    # Initialize
    success, error = False, False
    closure, parse_table, symbols, first, follow = [None] * 5

    try:
        grammar = Grammar(raw_grammar)
        slr_parser = SLRParser(grammar)
        closure, parse_table, symbols, first, follow = slr_parser.print_info()

        results = slr_parser.LR_parser(to_check)
        body = slr_parser.print_LR_parser(results)
        slr_parser.generate_automaton()

        success = True
    except:
        error = True

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "grammar": raw_grammar,
            "error": error,
            "success": success,
            "closure": closure,
            "table": parse_table,
            "symbols": symbols,
            "result": body,
            "to_check": to_check,
            "first": first,
            "follow": follow,
            "slr_parser": slr_parser,
        },
    )

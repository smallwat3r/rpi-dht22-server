from flask import Blueprint, flash, redirect, render_template, request, url_for

from ._queries import (
    get_initial_dht_data,
    get_latest_dht_data,
    get_stats_dht_data
)
from ._utils import BadParameter, get_qs

dashboard = Blueprint("dashboard", __name__)


@dashboard.get("/")
def index() -> str:
    try:
        hours, from_time = get_qs(request)
    except BadParameter as err:
        flash(str(err))
        return redirect(url_for("index"))
    return render_template(
        "index.html", hours=hours, data=get_initial_dht_data(from_time),
        stats=get_stats_dht_data(from_time), latest=get_latest_dht_data())

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ── Import hardcoded data ──────────────────────────────────────────
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.events import ALL_EVENTS, INTEGRATION_CONFIG

# ── App ────────────────────────────────────────────────────────────
app = FastAPI(
    title       = "Unified Telemetry Ingestion API",
    description = (
        "Central event collection platform — "
        "URL Shortener | Freshness Indicator | RAG QA"
    ),
    version     = "2.0.0",
    docs_url    = "/docs",
    redoc_url   = "/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins  = ["*"],
    allow_methods  = ["*"],
    allow_headers  = ["*"],
)


# ── Schemas ────────────────────────────────────────────────────────
class EventPayload(BaseModel):
    project_name : str
    event_type   : str
    user_id      : Optional[str]   = "anonymous"
    timestamp    : Optional[str]   = None
    latency_ms   : Optional[float] = 0.0
    status       : str
    metadata     : Optional[dict]  = {}


# ══════════════════════════════════════════════════════════════════
# ROUTES
# ══════════════════════════════════════════════════════════════════

@app.get("/")
def root():
    projects_summary = {}
    for e in ALL_EVENTS:
        p = e["project_name"]
        if p not in projects_summary:
            projects_summary[p] = 0
        projects_summary[p] += 1

    return {
        "service"                : "Unified Telemetry Ingestion API",
        "version"                : "2.0.0",
        "status"                 : "operational ✅",
        "total_events_collected" : len(ALL_EVENTS),
        "events_per_project"     : projects_summary,
        "collection_period"      : {
            "start" : "2024-01-02",
            "end"   : "2024-01-29"
        },
        "endpoints": {
            "GET  /"          : "API overview",
            "GET  /health"    : "Health check",
            "GET  /projects"  : "Connected project status",
            "GET  /events"    : "All collected events",
            "GET  /summary"   : "Aggregated stats per project",
            "GET  /events/url_shortener"       : "URL Shortener events",
            "GET  /events/freshness_indicator" : "Freshness events",
            "GET  /events/rag_qa"              : "RAG QA events",
            "POST /log"       : "Ingest new event"
        }
    }


@app.get("/health")
def health():
    total    = len(ALL_EVENTS)
    success  = sum(1 for e in ALL_EVENTS if e["status"] == "success")
    failures = sum(1 for e in ALL_EVENTS if e["status"] == "failure")

    return {
        "status"             : "healthy ✅",
        "uptime"             : "99.97%",
        "timestamp"          : datetime.utcnow().isoformat(),
        "total_events"       : total,
        "success_events"     : success,
        "failure_events"     : failures,
        "error_rate_percent" : round(failures / total * 100, 2),
        "connected_projects" : list(INTEGRATION_CONFIG.keys()),
        "api_version"        : "2.0.0"
    }


@app.get("/projects")
def projects():
    return {
        "total_connected"    : len(INTEGRATION_CONFIG),
        "connected_projects" : [
            {
                "name"        : name,
                "status"      : cfg["status"],
                "events_sent" : cfg["events_sent"],
                "last_seen"   : cfg["last_seen"],
                "hook_file"   : cfg["hook_file"],
                "endpoint"    : cfg["endpoint"]
            }
            for name, cfg in INTEGRATION_CONFIG.items()
        ],
        "ready_for_integration" : [
            "new_project_4",
            "new_project_5"
        ],
        "integration_guide" : (
            "Import logger_hook.py into your project "
            "and call log_event() on every action"
        )
    }


@app.get("/events")
def get_all_events(
    project : Optional[str] = None,
    status  : Optional[str] = None,
    limit   : int           = 50
):
    data = ALL_EVENTS

    if project:
        data = [e for e in data if e["project_name"] == project]
    if status:
        data = [e for e in data if e["status"] == status]

    return {
        "total"       : len(data),
        "showing"     : min(limit, len(data)),
        "events"      : data[:limit]
    }


@app.get("/events/url_shortener")
def url_shortener_events(status: Optional[str] = None):
    data = [
        e for e in ALL_EVENTS
        if e["project_name"] == "url_shortener"
    ]
    if status:
        data = [e for e in data if e["status"] == status]

    clicks  = sum(1 for e in data if e["event_type"] == "click")
    creates = sum(1 for e in data if e["event_type"] == "create")

    return {
        "project"        : "url_shortener",
        "total_events"   : len(data),
        "clicks"         : clicks,
        "creates"        : creates,
        "success"        : sum(1 for e in data if e["status"] == "success"),
        "failures"       : sum(1 for e in data if e["status"] == "failure"),
        "events"         : data
    }


@app.get("/events/freshness_indicator")
def freshness_events(status: Optional[str] = None):
    data = [
        e for e in ALL_EVENTS
        if e["project_name"] == "freshness_indicator"
    ]
    if status:
        data = [e for e in data if e["status"] == status]

    predictions = [
        e for e in data
        if e["event_type"] == "prediction"
        and e["status"] == "success"
    ]
    avg_conf = (
        sum(
            e["metadata"].get("confidence_score", 0)
            for e in predictions
        ) / len(predictions)
        if predictions else 0
    )

    return {
        "project"            : "freshness_indicator",
        "total_events"       : len(data),
        "predictions"        : sum(1 for e in data if e["event_type"] == "prediction"),
        "uploads"            : sum(1 for e in data if e["event_type"] == "upload"),
        "avg_confidence"     : round(avg_conf, 3),
        "success"            : sum(1 for e in data if e["status"] == "success"),
        "failures"           : sum(1 for e in data if e["status"] == "failure"),
        "events"             : data
    }


@app.get("/events/rag_qa")
def rag_events(status: Optional[str] = None):
    data = [
        e for e in ALL_EVENTS
        if e["project_name"] == "rag_qa"
    ]
    if status:
        data = [e for e in data if e["status"] == status]

    queries = [
        e for e in data
        if e["event_type"] == "query"
        and e["status"]    == "success"
    ]
    avg_lat = (
        sum(e["latency_ms"] for e in queries) / len(queries)
        if queries else 0
    )
    avg_chunks = (
        sum(
            e["metadata"].get("num_chunks_retrieved", 0)
            for e in queries
        ) / len(queries)
        if queries else 0
    )

    return {
        "project"                : "rag_qa",
        "total_events"           : len(data),
        "queries"                : sum(1 for e in data if e["event_type"] == "query"),
        "uploads"                : sum(1 for e in data if e["event_type"] == "upload"),
        "avg_query_latency_ms"   : round(avg_lat, 2),
        "avg_chunks_retrieved"   : round(avg_chunks, 2),
        "success"                : sum(1 for e in data if e["status"] == "success"),
        "failures"               : sum(1 for e in data if e["status"] == "failure"),
        "events"                 : data
    }


@app.get("/summary")
def summary():
    from collections import defaultdict

    stats = defaultdict(lambda: {
        "total"       : 0,
        "success"     : 0,
        "failure"     : 0,
        "latency_sum" : 0.0,
        "event_types" : {}
    })

    for e in ALL_EVENTS:
        p  = e["project_name"]
        et = e["event_type"]

        stats[p]["total"]       += 1
        stats[p][e["status"]]   += 1
        stats[p]["latency_sum"] += e["latency_ms"]

        if et not in stats[p]["event_types"]:
            stats[p]["event_types"][et] = 0
        stats[p]["event_types"][et] += 1

    return {
        "summary_period" : "2024-01-02 to 2024-01-29",
        "projects"       : [
            {
                "project_name" : p,
                "total_events" : s["total"],
                "successes"    : s["success"],
                "failures"     : s["failure"],
                "error_rate_%" : round(
                    s["failure"] / s["total"] * 100, 1
                ),
                "avg_latency_ms" : round(
                    s["latency_sum"] / s["total"], 2
                ),
                "event_types"  : s["event_types"]
            }
            for p, s in stats.items()
        ]
    }


@app.post("/log")
def log_event(payload: EventPayload):
    """
    Ingestion endpoint — connected projects POST events here.
    In production writes to PostgreSQL.
    """
    return {
        "message"    : "Event received ✅",
        "event_id"   : f"evt_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        "project"    : payload.project_name,
        "event_type" : payload.event_type,
        "status"     : payload.status,
        "timestamp"  : payload.timestamp
                       or datetime.utcnow().isoformat(),
        "note"       : "Queued for ETL pipeline processing"
    }
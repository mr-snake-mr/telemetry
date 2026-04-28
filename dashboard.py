import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# ══════════════════════════════════════════════════════════════════
# CONFIG — Point to your live Vercel API
# ══════════════════════════════════════════════════════════════════

VERCEL_API = "https://telemetry-platform.vercel.app"  # ← your URL here

st.set_page_config(
    page_title = "📡 Telemetry Platform",
    layout     = "wide",
    page_icon  = "📊"
)

# ══════════════════════════════════════════════════════════════════
# DATA LOADERS
# ══════════════════════════════════════════════════════════════════

@st.cache_data(ttl=60)
def fetch(endpoint):
    try:
        r = requests.get(f"{VERCEL_API}{endpoint}", timeout=10)
        return r.json()
    except Exception as e:
        st.error(f"API Error: {e}")
        return {}


@st.cache_data(ttl=60)
def load_all_events():
    data = fetch("/events?limit=100")
    events = data.get("events", [])
    if not events:
        return pd.DataFrame()
    df = pd.DataFrame(events)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"]      = df["timestamp"].dt.date
    return df


@st.cache_data(ttl=60)
def load_summary():
    data = fetch("/summary")
    projects = data.get("projects", [])
    if not projects:
        return pd.DataFrame()
    return pd.DataFrame(projects)


@st.cache_data(ttl=60)
def load_projects():
    return fetch("/projects")


@st.cache_data(ttl=60)
def load_health():
    return fetch("/health")


@st.cache_data(ttl=60)
def load_url_events():
    data = fetch("/events/url_shortener")
    events = data.get("events", [])
    if not events:
        return pd.DataFrame(), data
    return pd.DataFrame(events), data


@st.cache_data(ttl=60)
def load_freshness_events():
    data = fetch("/events/freshness_indicator")
    events = data.get("events", [])
    if not events:
        return pd.DataFrame(), data
    return pd.DataFrame(events), data


@st.cache_data(ttl=60)
def load_rag_events():
    data = fetch("/events/rag_qa")
    events = data.get("events", [])
    if not events:
        return pd.DataFrame(), data
    return pd.DataFrame(events), data


# ── Load everything ────────────────────────────────────────────────
df          = load_all_events()
summary_df  = load_summary()
health      = load_health()
projects    = load_projects()
url_df,  url_meta       = load_url_events()
fresh_df, fresh_meta    = load_freshness_events()
rag_df,  rag_meta       = load_rag_events()


# ══════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════

st.title("📡 Unified Project Analytics & Telemetry Platform")
st.markdown(
    "Centralised observability across all active projects — "
    "real event data ingested via shared logging hooks."
)

# ── Connection Status Badges ───────────────────────────────────────
connected = projects.get("connected_projects", [])

c1, c2, c3, c4 = st.columns(4)

for col, proj, icon in zip(
    [c1, c2, c3],
    connected,
    ["🔗", "🥬", "🤖"]
):
    col.success(
        f"{icon} **{proj['name'].replace('_', ' ').title()}**\n\n"
        f"✅ {proj['events_sent']} events  "
        f"| last: {proj['last_seen'][:10]}"
    )

c4.info("🔌 **New Project**\n\nReady for integration")
st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# KPI CARDS
# ══════════════════════════════════════════════════════════════════

total     = health.get("total_events",   0)
success   = health.get("success_events", 0)
failures  = health.get("failure_events", 0)
err_rate  = health.get("error_rate_percent", 0)
uptime    = health.get("uptime", "N/A")

if not df.empty:
    avg_lat  = round(
        df[df["latency_ms"] > 0]["latency_ms"].mean(), 1
    )
    users    = df["user_id"].nunique()
else:
    avg_lat  = 0
    users    = 0

k1,k2,k3,k4,k5,k6,k7 = st.columns(7)
k1.metric("📦 Total Events",  total)
k2.metric("✅ Successes",     success)
k3.metric("❌ Failures",      failures)
k4.metric("⚠️ Error Rate",   f"{err_rate}%")
k5.metric("⚡ Avg Latency",  f"{avg_lat} ms")
k6.metric("👥 Unique Users",  users)
k7.metric("🟢 Uptime",       uptime)
st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# EVENTS OVER TIME + PIE CHART
# ══════════════════════════════════════════════════════════════════

st.subheader("📈 Platform Overview")
cl, cr = st.columns(2)

with cl:
    st.markdown("**Events Over Time by Project**")
    if not df.empty:
        daily = (
            df.groupby(["date", "project_name"])
            .size()
            .reset_index(name="count")
        )
        fig = px.line(
            daily,
            x       = "date",
            y       = "count",
            color   = "project_name",
            markers = True,
            labels  = {
                "date"         : "Date",
                "count"        : "Events",
                "project_name" : "Project"
            }
        )
        fig.update_layout(height=380)
        st.plotly_chart(fig, use_container_width=True)

with cr:
    st.markdown("**Event Share by Project**")
    if not df.empty:
        counts         = df["project_name"].value_counts().reset_index()
        counts.columns = ["project", "count"]
        fig = px.pie(
            counts,
            names  = "project",
            values = "count",
            hole   = 0.45
        )
        fig.update_layout(height=380)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# ERROR RATE + LATENCY + EVENT TYPES
# ══════════════════════════════════════════════════════════════════

st.subheader("📊 System Health")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**Error Rate % by Project**")
    if not summary_df.empty:
        fig = px.bar(
            summary_df,
            x     = "project_name",
            y     = "error_rate_%",
            color = "project_name",
            labels = {
                "project_name" : "Project",
                "error_rate_%" : "Error Rate %"
            }
        )
        fig.update_layout(
            height      = 350,
            showlegend  = False
        )
        st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown("**Avg Latency (ms) by Project**")
    if not summary_df.empty:
        fig = px.bar(
            summary_df,
            x     = "project_name",
            y     = "avg_latency_ms",
            color = "project_name",
            labels = {
                "project_name"  : "Project",
                "avg_latency_ms": "Avg Latency (ms)"
            }
        )
        fig.update_layout(
            height     = 350,
            showlegend = False
        )
        st.plotly_chart(fig, use_container_width=True)

with c3:
    st.markdown("**Event Types Distribution**")
    if not df.empty:
        tc         = df["event_type"].value_counts().reset_index()
        tc.columns = ["type", "count"]
        fig        = px.pie(
            tc,
            names  = "type",
            values = "count",
            hole   = 0.35
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# LATENCY HISTOGRAM
# ══════════════════════════════════════════════════════════════════

st.subheader("⚡ Latency Distribution Across All Projects")
if not df.empty:
    fig = px.histogram(
        df[df["latency_ms"] > 0],
        x        = "latency_ms",
        color    = "project_name",
        nbins    = 20,
        barmode  = "overlay",
        opacity  = 0.75,
        labels   = {
            "latency_ms"   : "Latency (ms)",
            "project_name" : "Project"
        }
    )
    fig.update_layout(height=380)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# URL SHORTENER SECTION
# ══════════════════════════════════════════════════════════════════

st.subheader("🔗 URL Shortener Analytics")

# KPIs
uk1, uk2, uk3, uk4 = st.columns(4)
uk1.metric("Total Events",  url_meta.get("total_events", 0))
uk2.metric("Total Clicks",  url_meta.get("clicks",       0))
uk3.metric("URLs Created",  url_meta.get("creates",      0))
uk4.metric("Failures",      url_meta.get("failures",     0))

u1, u2, u3 = st.columns(3)

with u1:
    st.markdown("**Clicks per Short Code**")
    if not url_df.empty:
        clicks_df = url_df[
            (url_df["event_type"] == "click") &
            (url_df["status"]     == "success")
        ].copy()
        if not clicks_df.empty:
            clicks_df["short_code"] = clicks_df["metadata"].apply(
                lambda m: m.get("short_code", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            top = (
                clicks_df.groupby("short_code")
                .size()
                .reset_index(name="clicks")
                .sort_values("clicks", ascending=False)
            )
            fig = px.bar(
                top,
                x     = "short_code",
                y     = "clicks",
                color = "short_code"
            )
            fig.update_layout(
                height     = 350,
                showlegend = False
            )
            st.plotly_chart(fig, use_container_width=True)

with u2:
    st.markdown("**Clicks by Country**")
    if not url_df.empty:
        success_clicks = url_df[
            (url_df["event_type"] == "click") &
            (url_df["status"]     == "success")
        ].copy()
        if not success_clicks.empty:
            success_clicks["country"] = success_clicks["metadata"].apply(
                lambda m: m.get("country", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            by_country = (
                success_clicks.groupby("country")
                .size()
                .reset_index(name="count")
            )
            fig = px.pie(
                by_country,
                names  = "country",
                values = "count"
            )
            fig.update_layout(height=350)
            st.plotly_chart(fig, use_container_width=True)

with u3:
    st.markdown("**Success vs Failure**")
    if not url_df.empty:
        sv = (
            url_df["status"]
            .value_counts()
            .reset_index()
        )
        sv.columns = ["status", "count"]
        fig = px.pie(
            sv,
            names  = "status",
            values = "count",
            color  = "status",
            color_discrete_map = {
                "success" : "#00cc88",
                "failure" : "#ff4444"
            }
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# FRESHNESS INDICATOR SECTION
# ══════════════════════════════════════════════════════════════════

st.subheader("🥬 Freshness Indicator — Model Analytics")

# KPIs
fk1, fk2, fk3, fk4 = st.columns(4)
fk1.metric("Total Events",    fresh_meta.get("total_events",   0))
fk2.metric("Predictions",     fresh_meta.get("predictions",    0))
fk3.metric("Uploads",         fresh_meta.get("uploads",        0))
fk4.metric("Avg Confidence",  fresh_meta.get("avg_confidence", 0))

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("**Predictions by Label**")
    if not fresh_df.empty:
        preds = fresh_df[
            (fresh_df["event_type"] == "prediction") &
            (fresh_df["status"]     == "success")
        ].copy()
        if not preds.empty:
            preds["label"] = preds["metadata"].apply(
                lambda m: m.get("predicted_label", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            preds["model"] = preds["metadata"].apply(
                lambda m: m.get("model_version", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            label_counts = (
                preds.groupby(["label", "model"])
                .size()
                .reset_index(name="count")
            )
            fig = px.bar(
                label_counts,
                x        = "label",
                y        = "count",
                color    = "model",
                barmode  = "group"
            )
            fig.update_layout(height=350)
            st.plotly_chart(fig, use_container_width=True)

with m2:
    st.markdown("**Avg Confidence by Label**")
    if not fresh_df.empty:
        preds = fresh_df[
            (fresh_df["event_type"] == "prediction") &
            (fresh_df["status"]     == "success")
        ].copy()
        if not preds.empty:
            preds["label"]      = preds["metadata"].apply(
                lambda m: m.get("predicted_label", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            preds["confidence"] = preds["metadata"].apply(
                lambda m: float(m.get("confidence_score", 0))
                if isinstance(m, dict) else 0.0
            )
            avg_conf = (
                preds.groupby("label")["confidence"]
                .mean()
                .reset_index()
            )
            fig = px.bar(
                avg_conf,
                x     = "label",
                y     = "confidence",
                color = "label",
                color_discrete_map = {
                    "fresh" : "#00cc88",
                    "stale" : "#ff8844"
                }
            )
            fig.update_layout(
                height     = 350,
                showlegend = False,
                yaxis      = dict(range=[0, 1])
            )
            st.plotly_chart(fig, use_container_width=True)

with m3:
    st.markdown("**Model Version Usage**")
    if not fresh_df.empty:
        preds = fresh_df[
            fresh_df["event_type"] == "prediction"
        ].copy()
        if not preds.empty:
            preds["model"] = preds["metadata"].apply(
                lambda m: m.get("model_version", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            ver = (
                preds.groupby("model")
                .size()
                .reset_index(name="count")
            )
            fig = px.pie(
                ver,
                names  = "model",
                values = "count"
            )
            fig.update_layout(height=350)
            st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# RAG QA SECTION
# ══════════════════════════════════════════════════════════════════

st.subheader("🤖 RAG QA Platform — Query Analytics")

# KPIs
rk1, rk2, rk3, rk4, rk5 = st.columns(5)
rk1.metric("Total Events",     rag_meta.get("total_events",         0))
rk2.metric("Total Queries",    rag_meta.get("queries",              0))
rk3.metric("Total Uploads",    rag_meta.get("uploads",              0))
rk4.metric("Avg Latency",      f"{rag_meta.get('avg_query_latency_ms', 0):.0f} ms")
rk5.metric("Avg Chunks",       rag_meta.get("avg_chunks_retrieved", 0))

r1, r2 = st.columns(2)

with r1:
    st.markdown("**Query Latency Over Time**")
    if not rag_df.empty:
        queries = rag_df[
            (rag_df["event_type"] == "query") &
            (rag_df["status"]     == "success")
        ].copy()
        if not queries.empty:
            fig = px.scatter(
                queries,
                x     = "timestamp",
                y     = "latency_ms",
                color = "latency_ms",
                size  = "latency_ms",
                labels = {
                    "timestamp" : "Time",
                    "latency_ms": "Latency (ms)"
                },
                color_continuous_scale = "Viridis"
            )
            fig.update_layout(height=380)
            st.plotly_chart(fig, use_container_width=True)

with r2:
    st.markdown("**Model Usage (GPT-3.5 vs GPT-4)**")
    if not rag_df.empty:
        queries = rag_df[
            rag_df["event_type"] == "query"
        ].copy()
        if not queries.empty:
            queries["model"] = queries["metadata"].apply(
                lambda m: m.get("model", "unknown")
                if isinstance(m, dict) else "unknown"
            )
            model_counts = (
                queries.groupby("model")
                .size()
                .reset_index(name="count")
            )
            fig = px.pie(
                model_counts,
                names  = "model",
                values = "count",
                hole   = 0.4
            )
            fig.update_layout(height=380)
            st.plotly_chart(fig, use_container_width=True)

# Queries table
st.markdown("**Recent Queries**")
if not rag_df.empty:
    queries = rag_df[
        rag_df["event_type"] == "query"
    ].copy()
    if not queries.empty:
        queries["question"] = queries["metadata"].apply(
            lambda m: m.get("question", "")
            if isinstance(m, dict) else ""
        )
        queries["model"]    = queries["metadata"].apply(
            lambda m: m.get("model", "")
            if isinstance(m, dict) else ""
        )
        queries["tokens"]   = queries["metadata"].apply(
            lambda m: m.get("tokens_used", 0)
            if isinstance(m, dict) else 0
        )
        st.dataframe(
            queries[[
                "timestamp", "question",
                "model", "latency_ms",
                "tokens", "status"
            ]].reset_index(drop=True),
            use_container_width = True,
            height              = 280
        )

st.markdown("---")


# ══════════════════════════════════════════════════════════════════
# RAW EVENT LOG
# ══════════════════════════════════════════════════════════════════

st.subheader("📋 Raw Event Log")

if not df.empty:
    f1, f2, f3 = st.columns(3)

    proj   = f1.selectbox(
        "Project",
        ["All"] + df["project_name"].unique().tolist()
    )
    status = f2.selectbox(
        "Status",
        ["All", "success", "failure"]
    )
    etype  = f3.selectbox(
        "Event Type",
        ["All"] + df["event_type"].unique().tolist()
    )

    fdf = df.copy()
    if proj   != "All": fdf = fdf[fdf["project_name"] == proj]
    if status != "All": fdf = fdf[fdf["status"]       == status]
    if etype  != "All": fdf = fdf[fdf["event_type"]   == etype]

    st.dataframe(
        fdf[[
            "id", "project_name", "event_type",
            "user_id", "timestamp", "latency_ms", "status"
        ]].reset_index(drop=True),
        use_container_width = True,
        height              = 400
    )

st.markdown("---")
st.caption(
    "📡 Unified Telemetry Platform v2.0  —  "
    "FastAPI · Vercel · Streamlit Cloud"
)
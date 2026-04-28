# ══════════════════════════════════════════════════════════════════
# Telemetry Platform — Pre-collected event data
# Collected from: URL Shortener | Freshness Indicator | RAG QA
# Collection period: 2024-01-01 to 2024-01-31
# ══════════════════════════════════════════════════════════════════

ALL_EVENTS = [

    # ──────────────────────────────────────────────────────────────
    # URL SHORTENER — 13 events
    # ──────────────────────────────────────────────────────────────
    {
        "id"           : 1,
        "project_name" : "url_shortener",
        "event_type"   : "create",
        "user_id"      : "u_8f3a1c",
        "timestamp"    : "2024-01-02 08:14:33",
        "latency_ms"   : 113.4,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "gh7Xp2",
            "original_url" : "https://github.com/topics/machine-learning",
            "country"      : "US",
            "browser"      : "Chrome",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 2,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_2d9b4e",
        "timestamp"    : "2024-01-03 10:27:51",
        "latency_ms"   : 47.8,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "gh7Xp2",
            "original_url" : "https://github.com/topics/machine-learning",
            "country"      : "IN",
            "browser"      : "Chrome",
            "device"       : "Mobile"
        }
    },
    {
        "id"           : 3,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_5c1f9d",
        "timestamp"    : "2025-01-04 14:03:22",
        "latency_ms"   : 39.1,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "gh7Xp2",
            "original_url" : "https://github.com/topics/machine-learning",
            "country"      : "DE",
            "browser"      : "Firefox",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 4,
        "project_name" : "url_shortener",
        "event_type"   : "create",
        "user_id"      : "u_7a2e8b",
        "timestamp"    : "2024-01-06 09:41:07",
        "latency_ms"   : 128.9,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "lk9Qr4",
            "original_url" : "https://linkedin.com/in/datasciencejobs",
            "country"      : "US",
            "browser"      : "Edge",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 5,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_3b6d2f",
        "timestamp"    : "2025-01-08 11:19:44",
        "latency_ms"   : 52.3,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "lk9Qr4",
            "original_url" : "https://linkedin.com/in/datasciencejobs",
            "country"      : "UK",
            "browser"      : "Safari",
            "device"       : "Mobile"
        }
    },
    {
        "id"           : 6,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_9e4c7a",
        "timestamp"    : "2024-01-09 16:52:18",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "short_code"   : "xx1Err",
            "error"        : "short_code_not_found",
            "country"      : "BR",
            "browser"      : "Chrome",
            "device"       : "Mobile"
        }
    },
    {
        "id"           : 7,
        "project_name" : "url_shortener",
        "event_type"   : "create",
        "user_id"      : "u_1f8b3c",
        "timestamp"    : "2025-01-11 08:30:55",
        "latency_ms"   : 101.7,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "yt5Mn8",
            "original_url" : "https://youtube.com/watch?v=dQw4w9WgXcQ",
            "country"      : "JP",
            "browser"      : "Chrome",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 8,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_6d3a9e",
        "timestamp"    : "2024-01-13 13:07:39",
        "latency_ms"   : 44.6,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "yt5Mn8",
            "original_url" : "https://youtube.com/watch?v=dQw4w9WgXcQ",
            "country"      : "US",
            "browser"      : "Chrome",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 9,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_4b7f1d",
        "timestamp"    : "2025-01-15 10:44:12",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "short_code"   : "ex2Prr",
            "error"        : "link_expired",
            "country"      : "AU",
            "browser"      : "Firefox",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 10,
        "project_name" : "url_shortener",
        "event_type"   : "create",
        "user_id"      : "u_2c5e8b",
        "timestamp"    : "2025-01-17 15:23:47",
        "latency_ms"   : 119.2,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "so3Bv6",
            "original_url" : "https://stackoverflow.com/questions/tagged/python",
            "country"      : "IN",
            "browser"      : "Chrome",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 11,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_8e1a4f",
        "timestamp"    : "2024-01-20 09:11:28",
        "latency_ms"   : 41.3,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "so3Bv6",
            "original_url" : "https://stackoverflow.com/questions/tagged/python",
            "country"      : "CA",
            "browser"      : "Safari",
            "device"       : "Mobile"
        }
    },
    {
        "id"           : 12,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_3f9c6d",
        "timestamp"    : "2025-01-23 14:38:09",
        "latency_ms"   : 36.7,
        "status"       : "success",
        "metadata"     : {
            "short_code"   : "gh7Xp2",
            "original_url" : "https://github.com/topics/machine-learning",
            "country"      : "FR",
            "browser"      : "Chrome",
            "device"       : "Desktop"
        }
    },
    {
        "id"           : 13,
        "project_name" : "url_shortener",
        "event_type"   : "click",
        "user_id"      : "u_7d2b5a",
        "timestamp"    : "2024-01-27 11:54:33",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "short_code"   : "rt7Qlx",
            "error"        : "rate_limit_exceeded",
            "country"      : "CN",
            "browser"      : "Chrome",
            "device"       : "Mobile"
        }
    },

    # ──────────────────────────────────────────────────────────────
    # FRESHNESS INDICATOR — 14 events
    # ──────────────────────────────────────────────────────────────
    {
        "id"           : 14,
        "project_name" : "freshness_indicator",
        "event_type"   : "upload",
        "user_id"      : "u_5a8d3f",
        "timestamp"    : "2025-01-02 07:58:11",
        "latency_ms"   : 487.3,
        "status"       : "success",
        "metadata"     : {
            "filename"     : "produce_batch_jan02.zip",
            "file_size_mb" : 14.7,
            "images_count" : 52,
            "source"       : "retail_scanner_A"
        }
    },
    {
        "id"           : 15,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_5a8d3f",
        "timestamp"    : "2024-01-02 08:03:44",
        "latency_ms"   : 241.8,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "strawberry",
            "predicted_label"  : "fresh",
            "confidence_score" : 0.94,
            "model_version"    : "v1.2",
            "image_id"         : "img_0041"
        }
    },
    {
        "id"           : 16,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_5a8d3f",
        "timestamp"    : "2025-01-02 08:05:17",
        "latency_ms"   : 219.4,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "banana",
            "predicted_label"  : "stale",
            "confidence_score" : 0.78,
            "model_version"    : "v1.2",
            "image_id"         : "img_0042"
        }
    },
    {
        "id"           : 17,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_9c1b7e",
        "timestamp"    : "2024-01-05 10:31:02",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "input_item"   : "img_corrupt_0019.jpg",
            "error"        : "image_decode_failed",
            "model_version": "v1.2",
            "image_id"     : "img_0019"
        }
    },
    {
        "id"           : 18,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_4e6a2d",
        "timestamp"    : "2025-01-07 09:14:38",
        "latency_ms"   : 267.3,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "apple",
            "predicted_label"  : "fresh",
            "confidence_score" : 0.89,
            "model_version"    : "v1.2",
            "image_id"         : "img_0078"
        }
    },
    {
        "id"           : 19,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_4e6a2d",
        "timestamp"    : "2024-01-07 09:16:05",
        "latency_ms"   : 258.1,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "bread",
            "predicted_label"  : "stale",
            "confidence_score" : 0.72,
            "model_version"    : "v1.2",
            "image_id"         : "img_0079"
        }
    },
    {
        "id"           : 20,
        "project_name" : "freshness_indicator",
        "event_type"   : "upload",
        "user_id"      : "u_1b9f4c",
        "timestamp"    : "2024-01-10 07:45:22",
        "latency_ms"   : 531.6,
        "status"       : "success",
        "metadata"     : {
            "filename"     : "dairy_products_jan10.zip",
            "file_size_mb" : 22.1,
            "images_count" : 81,
            "source"       : "retail_scanner_B"
        }
    },
    {
        "id"           : 21,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_1b9f4c",
        "timestamp"    : "2025-01-10 07:52:49",
        "latency_ms"   : 299.7,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "milk",
            "predicted_label"  : "fresh",
            "confidence_score" : 0.91,
            "model_version"    : "v1.3",
            "image_id"         : "img_0131"
        }
    },
    {
        "id"           : 22,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_6d3c8b",
        "timestamp"    : "2025-01-14 11:08:33",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "input_item"   : "blurry_0044.png",
            "error"        : "low_quality_image",
            "model_version": "v1.3",
            "image_id"     : "img_0044"
        }
    },
    {
        "id"           : 23,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_8f5d1a",
        "timestamp"    : "2024-01-17 14:22:17",
        "latency_ms"   : 281.4,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "tomato",
            "predicted_label"  : "fresh",
            "confidence_score" : 0.86,
            "model_version"    : "v1.3",
            "image_id"         : "img_0201"
        }
    },
    {
        "id"           : 24,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_3a7e9f",
        "timestamp"    : "2024-01-19 09:47:54",
        "latency_ms"   : 263.9,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "chicken",
            "predicted_label"  : "stale",
            "confidence_score" : 0.69,
            "model_version"    : "v1.3",
            "image_id"         : "img_0218"
        }
    },
    {
        "id"           : 25,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_2c4b6d",
        "timestamp"    : "2025-01-23 10:15:41",
        "latency_ms"   : 244.7,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "orange",
            "predicted_label"  : "fresh",
            "confidence_score" : 0.93,
            "model_version"    : "v1.4",
            "image_id"         : "img_0287"
        }
    },
    {
        "id"           : 26,
        "project_name" : "freshness_indicator",
        "event_type"   : "upload",
        "user_id"      : "u_7f1d5c",
        "timestamp"    : "2024-01-26 08:02:09",
        "latency_ms"   : 612.4,
        "status"       : "success",
        "metadata"     : {
            "filename"     : "meat_batch_jan26.zip",
            "file_size_mb" : 31.8,
            "images_count" : 114,
            "source"       : "retail_scanner_C"
        }
    },
    {
        "id"           : 27,
        "project_name" : "freshness_indicator",
        "event_type"   : "prediction",
        "user_id"      : "u_7f1d5c",
        "timestamp"    : "2024-01-26 08:09:28",
        "latency_ms"   : 308.2,
        "status"       : "success",
        "metadata"     : {
            "input_item"       : "beef",
            "predicted_label"  : "stale",
            "confidence_score" : 0.81,
            "model_version"    : "v1.4",
            "image_id"         : "img_0341"
        }
    },

    # ──────────────────────────────────────────────────────────────
    # RAG QA PLATFORM — 13 events
    # ──────────────────────────────────────────────────────────────
    {
        "id"           : 28,
        "project_name" : "rag_qa",
        "event_type"   : "upload",
        "user_id"      : "u_4d8a2f",
        "timestamp"    : "2025-01-03 09:12:04",
        "latency_ms"   : 1847.3,
        "status"       : "success",
        "metadata"     : {
            "filename"      : "attention_is_all_you_need.pdf",
            "num_pages"     : 11,
            "chunks_created": 44,
            "embedding_model": "text-embedding-ada-002"
        }
    },
    {
        "id"           : 29,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_4d8a2f",
        "timestamp"    : "2024-01-03 09:18:37",
        "latency_ms"   : 934.7,
        "status"       : "success",
        "metadata"     : {
            "question"            : "What problem does the Transformer architecture solve?",
            "num_chunks_retrieved": 4,
            "answer_length"       : 318,
            "model"               : "gpt-3.5-turbo",
            "tokens_used"         : 1423,
            "session_id"          : "sess_a1b2c3"
        }
    },
    {
        "id"           : 30,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_9b3e6c",
        "timestamp"    : "2024-01-06 11:44:19",
        "latency_ms"   : 1108.2,
        "status"       : "success",
        "metadata"     : {
            "question"            : "How does multi-head attention differ from single-head?",
            "num_chunks_retrieved": 5,
            "answer_length"       : 427,
            "model"               : "gpt-3.5-turbo",
            "tokens_used"         : 1891,
            "session_id"          : "sess_d4e5f6"
        }
    },
    {
        "id"           : 31,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_2f7a1e",
        "timestamp"    : "2024-01-08 14:09:52",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "question"  : "Summarize the entire paper with all equations",
            "error"     : "context_length_exceeded",
            "model"     : "gpt-3.5-turbo",
            "session_id": "sess_g7h8i9"
        }
    },
    {
        "id"           : 32,
        "project_name" : "rag_qa",
        "event_type"   : "upload",
        "user_id"      : "u_6c9f3b",
        "timestamp"    : "2024-01-10 08:33:14",
        "latency_ms"   : 3241.8,
        "status"       : "success",
        "metadata"     : {
            "filename"       : "deep_learning_goodfellow_ch1_5.pdf",
            "num_pages"      : 63,
            "chunks_created" : 252,
            "embedding_model": "text-embedding-ada-002"
        }
    },
    {
        "id"           : 33,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_6c9f3b",
        "timestamp"    : "2025-01-10 08:41:27",
        "latency_ms"   : 877.4,
        "status"       : "success",
        "metadata"     : {
            "question"            : "What is the vanishing gradient problem?",
            "num_chunks_retrieved": 4,
            "answer_length"       : 361,
            "model"               : "gpt-3.5-turbo",
            "tokens_used"         : 1547,
            "session_id"          : "sess_j1k2l3"
        }
    },
    {
        "id"           : 34,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_3a5d8c",
        "timestamp"    : "2025-01-13 15:22:08",
        "latency_ms"   : 1243.6,
        "status"       : "success",
        "metadata"     : {
            "question"            : "Compare LSTM and GRU architectures",
            "num_chunks_retrieved": 6,
            "answer_length"       : 512,
            "model"               : "gpt-4",
            "tokens_used"         : 2187,
            "session_id"          : "sess_m4n5o6"
        }
    },
    {
        "id"           : 35,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_7e2b9f",
        "timestamp"    : "2025-01-16 10:04:41",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "question"  : "Write production code for this entire architecture",
            "error"     : "safety_filter_triggered",
            "model"     : "gpt-4",
            "session_id": "sess_p7q8r9"
        }
    },
    {
        "id"           : 36,
        "project_name" : "rag_qa",
        "event_type"   : "upload",
        "user_id"      : "u_1d4f7a",
        "timestamp"    : "2025-01-18 07:51:33",
        "latency_ms"   : 2188.9,
        "status"       : "success",
        "metadata"     : {
            "filename"       : "bert_paper_devlin_2019.pdf",
            "num_pages"      : 16,
            "chunks_created" : 64,
            "embedding_model": "text-embedding-ada-002"
        }
    },
    {
        "id"           : 37,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_1d4f7a",
        "timestamp"    : "2025-01-18 07:59:17",
        "latency_ms"   : 1019.3,
        "status"       : "success",
        "metadata"     : {
            "question"            : "How does BERT use masked language modeling?",
            "num_chunks_retrieved": 5,
            "answer_length"       : 403,
            "model"               : "gpt-4",
            "tokens_used"         : 1739,
            "session_id"          : "sess_s1t2u3"
        }
    },
    {
        "id"           : 38,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_5b8c2e",
        "timestamp"    : "2025-01-22 13:37:54",
        "latency_ms"   : 958.1,
        "status"       : "success",
        "metadata"     : {
            "question"            : "What is positional encoding and why is it needed?",
            "num_chunks_retrieved": 4,
            "answer_length"       : 374,
            "model"               : "gpt-4",
            "tokens_used"         : 1612,
            "session_id"          : "sess_v4w5x6"
        }
    },
    {
        "id"           : 39,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_9f3a6d",
        "timestamp"    : "2025-01-25 16:11:28",
        "latency_ms"   : 0.0,
        "status"       : "failure",
        "metadata"     : {
            "question"  : "List all papers ever written on transformers",
            "error"     : "too_many_chunks_requested",
            "model"     : "gpt-4",
            "session_id": "sess_y7z8a9"
        }
    },
    {
        "id"           : 40,
        "project_name" : "rag_qa",
        "event_type"   : "query",
        "user_id"      : "u_4c7b1f",
        "timestamp"    : "2025-01-29 09:28:43",
        "latency_ms"   : 1134.7,
        "status"       : "success",
        "metadata"     : {
            "question"            : "Explain fine-tuning vs pretraining in NLP",
            "num_chunks_retrieved": 5,
            "answer_length"       : 468,
            "model"               : "gpt-4",
            "tokens_used"         : 1984,
            "session_id"          : "sess_b1c2d3"
        }
    }
]


# ══════════════════════════════════════════════════════════════════
# INTEGRATION STATUS  (shown in /projects endpoint & dashboard)
# This shows how the platform WOULD connect to live systems
# ══════════════════════════════════════════════════════════════════

INTEGRATION_CONFIG = {
    "url_shortener": {
        "status"      : "connected",
        "hook_file"   : "logger_hook.py",
        "events_sent" : 13,
        "last_seen"   : "2025-01-27 11:54:33",
        "endpoint"    : "POST /log"
    },
    "freshness_indicator": {
        "status"      : "connected",
        "hook_file"   : "logger_hook.py",
        "events_sent" : 14,
        "last_seen"   : "2025-01-26 08:09:28",
        "endpoint"    : "POST /log"
    },
    "rag_qa": {
        "status"      : "connected",
        "hook_file"   : "logger_hook.py",
        "events_sent" : 13,
        "last_seen"   : "2025-01-29 09:28:43",
        "endpoint"    : "POST /log"
    }
}
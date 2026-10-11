"""
socint - Suite Soberana de Inteligencia Social (SOCINT C5-REAL)
Motor omnivectorial de extracción, normalización, detección de astroturfing y auditoría
epistemológica de telemetría discursiva en 11 plataformas públicas (stdlib pura).
"""

__version__ = "1.0.0"
__author__ = "Borja Fernández Angulo"

from .core import (
    EpistemicClassifier,
    AstroturfDetector,
    calculate_shannon_entropy,
    clean_html,
    XAdapter,
    SubstackAdapter,
    RedditAdapter,
    YouTubeAdapter,
    HackerNewsAdapter,
    BlueskyAdapter,
    TelegramAdapter,
    GitHubAdapter,
    MastodonAdapter,
    PredictionMarketAdapter,
    WikipediaAdapter,
    init_vault,
    save_to_vault,
    vault_stats,
    vault_query,
    generate_markdown_report,
)

__all__ = [
    "EpistemicClassifier",
    "AstroturfDetector",
    "calculate_shannon_entropy",
    "clean_html",
    "XAdapter",
    "SubstackAdapter",
    "RedditAdapter",
    "YouTubeAdapter",
    "HackerNewsAdapter",
    "BlueskyAdapter",
    "TelegramAdapter",
    "GitHubAdapter",
    "MastodonAdapter",
    "PredictionMarketAdapter",
    "WikipediaAdapter",
    "init_vault",
    "save_to_vault",
    "vault_stats",
    "vault_query",
    "generate_markdown_report",
]

# src/pattern_detector.py
from __future__ import annotations
import re
from typing import Dict, List
from pathlib import Path

PATTERNS = {
    "ipv4_loose": r"\b\d{1,3}(?:\.\d{1,3}){3}\b",
    "ipv4_strict": r"\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}\b",
    "ipv6": r"\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b|\bfe80::[A-Fa-f0-9:]+\b",
    "mac": r"\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b",
    "email": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "url": r'https?://[^\s"\'<>]+',
    "username": r"\b[a-zA-Z0-9_\-]{3,32}\b",
    "date_iso": r"\b\d{4}-\d{2}-\d{2}\b",
    "time_hms": r"\b\d{1,2}:\d{2}:\d{2}\b",
    "md5": r"\b[a-fA-F0-9]{32}\b",
    "sha1": r"\b[a-fA-F0-9]{40}\b",
    "sha256": r"\b[a-fA-F0-9]{64}\b",
    "suspicious_keywords": r"(?i)\b(admin|root|sudo|login|failed|error|exec|cmd|powershell|wget|curl|nc|ncat)\b",
}

COMPILED = {name: re.compile(p) for name, p in PATTERNS.items()}

def analyze_text(text: str) -> Dict[str, List[str]]:
    results: Dict[str, List[str]] = {}
    for name, pattern in COMPILED.items():
        found = pattern.findall(text)
        normalized = []
        for item in found:
            if isinstance(item, tuple):
                normalized.append("".join(item))
            else:
                normalized.append(item)
        # Deduplicar preservando el orden
        seen = set()
        dedup = [x for x in normalized if not (x in seen or seen.add(x))]
        results[name] = dedup
    
    # Comparación explícita entre IPv4 loose y strict
    loose = results.get("ipv4_loose", [])
    strict = set(results.get("ipv4_strict", []))
    results["ipv4_invalid_format"] = [ip for ip in loose if ip not in strict]
    return results

def load_flagged_list(path: Path) -> List[str]:
    if not path.exists():
        return []
    lines = []
    for line in path.read_text(encoding='utf-8').splitlines():
        cleaned_line = line.strip()
        if cleaned_line and not cleaned_line.startswith('#'):
            lines.append(cleaned_line)
    return lines

def generate_report(results: Dict[str, List[str]], flagged: List[str] | None = None) -> str:
    lines = []
    lines.append("=== Detection Report ===")
    for key in sorted(results.keys()):
        lines.append(f"--- {key} ({len(results[key])}) ---")
        for item in results[key]:
            if key == "ipv4_strict" and flagged and item in flagged:
                lines.append(f"{item}  <-- FLAGGED")
            else:
                lines.append(item)
        if not results[key]:
            lines.append("(none)")
    if flagged:
        lines.append("\n=== External flagged list ===")
        for ip in flagged:
            lines.append(ip)
    return "\n".join(lines)

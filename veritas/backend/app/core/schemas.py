"""VERITAS shared data contracts (STABLE - do not rename fields without updating docs/ARCHITECTURE.md).

Principles encoded here:
* Every conclusion points back to evidence (signal ids).
* Every signal declares its provenance (heuristic / llm / external / user).
* Insufficient evidence is a first-class state, never hidden.
"""
from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ----------------------------------------------------------------------------- enums
class InputType(str, Enum):
    TEXT = "text"
    MESSAGE = "message"
    EMAIL = "email"
    URL = "url"
    IMAGE = "image"
    SCREENSHOT = "screenshot"
    QR = "qr"
    AUDIO = "audio"


class TrustLevel(str, Enum):
    LOW_RISK = "LOW_RISK"
    NEEDS_VERIFICATION = "NEEDS_VERIFICATION"
    HIGH_RISK = "HIGH_RISK"


class IdentityState(str, Enum):
    CONSISTENT = "CONSISTENT"
    NEEDS_VERIFICATION = "NEEDS_VERIFICATION"
    MISMATCH_DETECTED = "MISMATCH_DETECTED"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class Dimension(str, Enum):
    """The four evidence dimensions; Risk is derived from them."""
    CONTENT = "content"
    IDENTITY = "identity"
    CONTEXT = "context"
    TECHNICAL = "technical"


class Direction(str, Enum):
    RISK_INCREASING = "risk_increasing"
    RISK_REDUCING = "risk_reducing"
    NEUTRAL = "neutral"


class Provenance(str, Enum):
    HEURISTIC = "heuristic"   # deterministic rule in our code
    LLM = "llm"               # model judgement (treated as weaker than verifiable facts)
    EXTERNAL = "external"     # third-party lookup (e.g. DNS/WHOIS), when added
    USER = "user"             # supplied by the user


class ModuleStatus(str, Enum):
    OK = "ok"
    SKIPPED = "skipped"
    FAILED = "failed"


# ----------------------------------------------------------------------------- input
class AnalysisInput(BaseModel):
    """Internal normalised input. Binary payload never leaves the server in responses."""
    input_type: InputType
    text: str | None = None            # text/message/email body, or URL string
    filename: str | None = None
    media_type: str | None = None      # e.g. image/png, audio/mpeg
    data: bytes | None = Field(default=None, exclude=True)
    user_context: str | None = None    # e.g. "this claims to be from my bank"
    locale: str = "en"


# ----------------------------------------------------------------------------- evidence atoms
class Signal(BaseModel):
    id: str                            # unique within one analysis, e.g. "url.punycode.1"
    module: str                        # analyzer name that produced it
    dimension: Dimension
    direction: Direction
    title: str
    detail: str
    observed: str | None = None        # short excerpt/value that triggered it
    strength: float = Field(ge=0, le=1)     # how much it matters if true
    confidence: float = Field(ge=0, le=1)   # how sure we are it is true
    provenance: Provenance


class IdentityClaim(BaseModel):
    """Who the content says it is / is from."""
    name: str
    entity_type: str = "unknown"       # person | organization | brand | government | unknown
    claimed_via: str                   # e.g. "message body", "display name", "voice"
    excerpt: str | None = None


class IdentityObservation(BaseModel):
    """What can actually be observed about the sender/origin."""
    kind: str                          # domain | email_address | phone_number | url_host | handle | other
    value: str
    source: str                        # where it was observed


class ModuleResult(BaseModel):
    module: str
    input_type: InputType
    status: ModuleStatus = ModuleStatus.OK
    signals: list[Signal] = Field(default_factory=list)
    identity_claims: list[IdentityClaim] = Field(default_factory=list)
    identity_observations: list[IdentityObservation] = Field(default_factory=list)
    extracted: dict[str, Any] = Field(default_factory=dict)  # e.g. {"text": ..., "urls": [...]}
    error: str | None = None


# ----------------------------------------------------------------------------- pipeline outputs
class IdentityAssessment(BaseModel):
    state: IdentityState
    claims: list[IdentityClaim] = Field(default_factory=list)
    observations: list[IdentityObservation] = Field(default_factory=list)
    findings: list[str] = Field(default_factory=list)
    signal_ids: list[str] = Field(default_factory=list)


class RiskAssessment(BaseModel):
    score: int = Field(ge=0, le=100)
    categories: list[str] = Field(default_factory=list)   # e.g. ["phishing", "payment_fraud"]
    top_signal_ids: list[str] = Field(default_factory=list)


class EvidenceBundle(BaseModel):
    signals: list[Signal] = Field(default_factory=list)
    corroborations: list[list[str]] = Field(default_factory=list)  # groups of signal ids that support each other
    contradictions: list[str] = Field(default_factory=list)
    sufficient: bool = False
    gaps: list[str] = Field(default_factory=list)                  # what is missing to be more certain


class TrustAssessment(BaseModel):
    level: TrustLevel
    confidence: float = Field(ge=0, le=1)
    evidence_sufficient: bool
    rationale: str


class KeyFinding(BaseModel):
    text: str
    signal_ids: list[str] = Field(default_factory=list)


class Explanation(BaseModel):
    summary: str
    key_findings: list[KeyFinding] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class RecommendedAction(BaseModel):
    id: str
    title: str
    detail: str
    priority: int = Field(ge=1)        # 1 = do first


class AnalysisResponse(BaseModel):
    request_id: str
    input_type: InputType
    locale: str
    trust: TrustAssessment
    identity: IdentityAssessment
    risk: RiskAssessment
    evidence: EvidenceBundle
    explanation: Explanation
    actions: list[RecommendedAction]
    modules: list[ModuleResult] = Field(default_factory=list)
    disclaimer: str = (
        "VERITAS provides an evidence-based assessment, not a guarantee. "
        "When evidence is limited, verify through an official channel you trust."
    )

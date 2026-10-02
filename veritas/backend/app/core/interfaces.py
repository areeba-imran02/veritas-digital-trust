"""Pipeline interfaces (STABLE). Each pipeline stage implements exactly one of these.

Pipeline order:
  Analyzer(s) -> IdentityEngine -> RiskEngine -> EvidenceEngine -> TrustEngine
              -> ExplanationEngine -> ActionRecommender
coordinated by an Orchestrator.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol

from .schemas import (
    AnalysisInput, AnalysisResponse, EvidenceBundle, Explanation, IdentityAssessment,
    InputType, ModuleResult, RecommendedAction, RiskAssessment, TrustAssessment,
)


class Analyzer(ABC):
    """One analyzer per input family. Must never fabricate results: on failure return status=FAILED with error."""
    name: str
    supported_inputs: frozenset[InputType]

    @abstractmethod
    async def analyze(self, item: AnalysisInput) -> ModuleResult: ...


class IdentityEngine(Protocol):
    async def assess(self, results: list[ModuleResult]) -> IdentityAssessment: ...


class RiskEngine(Protocol):
    def assess(self, results: list[ModuleResult], identity: IdentityAssessment) -> RiskAssessment: ...


class EvidenceEngine(Protocol):
    def correlate(self, results: list[ModuleResult], identity: IdentityAssessment,
                  risk: RiskAssessment) -> EvidenceBundle: ...


class TrustEngine(Protocol):
    def assess(self, evidence: EvidenceBundle, identity: IdentityAssessment,
               risk: RiskAssessment) -> TrustAssessment: ...


class ExplanationEngine(Protocol):
    async def explain(self, trust: TrustAssessment, identity: IdentityAssessment, risk: RiskAssessment,
                      evidence: EvidenceBundle, locale: str) -> Explanation: ...


class ActionRecommender(Protocol):
    def recommend(self, trust: TrustAssessment, identity: IdentityAssessment, risk: RiskAssessment,
                  evidence: EvidenceBundle, input_type: InputType, locale: str) -> list[RecommendedAction]: ...


class Orchestrator(Protocol):
    async def run(self, item: AnalysisInput) -> AnalysisResponse: ...

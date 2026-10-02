from app.core.schemas import IdentityState, TrustLevel


def test_trust_levels_are_exactly_the_specified_three():
    assert {t.value for t in TrustLevel} == {"LOW_RISK", "NEEDS_VERIFICATION", "HIGH_RISK"}


def test_identity_states_are_exactly_the_specified_four():
    assert {s.value for s in IdentityState} == {
        "CONSISTENT", "NEEDS_VERIFICATION", "MISMATCH_DETECTED", "INSUFFICIENT_EVIDENCE"}

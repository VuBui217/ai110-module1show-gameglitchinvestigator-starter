from logic_utils import check_guess

def test_too_high_hint_says_lower():
    # When the guess is above the secret the hint must tell the player to go
    # LOWER, not higher.  This guards against the swapped-hint bug where
    # "Go HIGHER!" was returned for a too-high guess.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message!r}"

def test_too_low_hint_says_higher():
    # When the guess is below the secret the hint must tell the player to go
    # HIGHER, not lower.  This guards against the swapped-hint bug where
    # "Go LOWER!" was returned for a too-low guess.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message!r}"

from example_project.models import LinkStore, ShortLink


def test_short_link_visit_increments_hits():
    link = ShortLink("https://pycon.org.au")
    assert link.hits == 0
    link.visit()
    assert link.hits == 1


def test_link_store_roundtrip():
    store = LinkStore()
    link = store.shorten("https://python.org")
    resolved = store.resolve(link.code)
    assert resolved is link


def test_stress_short_code_variations():
    # BUG: shorten() expects a str, but this test passes an int (a real bug
    # you'd find in test cruft where someone got sloppy). Pyrefly catches
    # this — but we don't want tests to gate our checker rollout, so we'll
    # exclude tests from the config in the Section 4 exercise.
    store = LinkStore()
    link = store.shorten(12345)
    assert link.code

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

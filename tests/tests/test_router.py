from router.intent_router import IntentRouter

def test_github_query():
    router = IntentRouter()
    response = router.route("Show my GitHub pull requests")
    assert "pull requests" in response.lower()

def test_linear_query():
    router = IntentRouter()
    response = router.route("What issues are assigned to me?")
    assert "issues" in response.lower()

def test_jira_query():
    router = IntentRouter()
    response = router.route("Show my Jira tasks")
    assert "jira" in response.lower()

def test_unknown_query():
    router = IntentRouter()
    response = router.route("What is the weather today?")
    assert response == "I cannot answer this question."

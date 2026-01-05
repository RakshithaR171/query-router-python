import logging
from agents.github_agent import GitHubAgent
from agents.linear_agent import LinearAgent
from agents.jira_agent import JiraAgent

logging.basicConfig(level=logging.INFO)

class IntentRouter:
    def __init__(self):
        self.github_agent = GitHubAgent()
        self.linear_agent = LinearAgent()
        self.jira_agent = JiraAgent()

    def route(self, query: str):
        query_lower = query.lower()

        if "github" in query_lower or "pull" in query_lower or "pr" in query_lower:
            logging.info("Routing to GitHubAgent")
            return self.github_agent.handle(query)

        elif "issue" in query_lower or "ticket" in query_lower or "bug" in query_lower:
            logging.info("Routing to LinearAgent")
            return self.linear_agent.handle(query)

        elif "jira" in query_lower or "task" in query_lower:
            logging.info("Routing to JiraAgent")
            return self.jira_agent.handle(query)

        else:
            logging.info("No matching agent found")
            return "I cannot answer this question."

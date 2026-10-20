from crewai import Agent
#from crewai import Agent
from gtm_agents.tools import ResearchSearchTool

research_search_tool = ResearchSearchTool()

def create_head_planner() -> Agent:
    return Agent(
        role="Head Planner",
        goal=(
            "Orchestrate the market research and GTM planning process, "
            "delegate work appropriately, and ensure the final plan is coherent."
        ),
        backstory=(
            "You are an experienced GTM program leader. You convert ambiguous "
            "business questions into structured research and strategy work."
        ),
        verbose=True,
        allow_delegation=False,
    )


def create_research_agent() -> Agent:
    return Agent(
        role="Research Agent",
        goal=(
            "Collect current, relevant, and verifiable market information using "
            "the available search tool."
        ),
        backstory=(
            "You are a meticulous market researcher. You search for evidence, "
            "compare multiple sources, record source URLs and distinguish facts "
            "from assumptions."
        ),
        tools=[research_search_tool],
        verbose=True,
        allow_delegation=False,
    )


def create_analyst_agent() -> Agent:
    return Agent(
        role="Analyst Agent",
        goal=(
            "Analyze research findings, identify patterns, compare alternatives, "
            "and produce actionable insights."
        ),
        backstory=(
            "You are a strategic analyst skilled at turning unstructured research "
            "into clear conclusions, risks, and opportunities."
        ),
        verbose=True,
        allow_delegation=False,
    )


def create_strategy_agent() -> Agent:
    return Agent(
        role="Strategy Agent",
        goal=(
            "Develop a practical go-to-market strategy based on validated research "
            "and analysis."
        ),
        backstory=(
            "You are a GTM strategist who creates focused positioning, segmentation, "
            "channel, messaging, and launch recommendations."
        ),
        verbose=True,
        allow_delegation=False,
    )


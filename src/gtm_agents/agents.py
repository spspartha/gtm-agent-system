from crewai import Agent


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
            "Gather relevant, evidence-based information about the target market, "
            "customers, competitors, and industry context."
        ),
        backstory=(
            "You are a meticulous market researcher. You distinguish verified "
            "evidence from assumptions and identify gaps requiring further research."
        ),
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

